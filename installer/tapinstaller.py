# Windows TAP-32 installer
# OpenSesame

# This file is part of OpenSesame. 
# Copyright (C) 2009 by Rob Lemley.
# See the README.TXT file for important information about this project.

from platform import architecture
import sys, os
from PyQt4.QtCore import QProcess
from optparse import OptionParser

if os.name != 'nt':
    print "Sorry, I only work on Windows"
    sys.exit(1)

arch=architecture()[0]
if arch not in ['32bit', '64bit']:
    print "WTF? Arch is screwy."
    sys.exit(1)
if arch == '32bit':
    ARCH='i386'
else:
    ARCH='amd64'

NEED_REBOOT = False

OLDTAP = "tap0801"
TAP = "tap0901"
TAPDRV = "%s.sys" % TAP
TAPCAT = "%s.cat" %TAP
OEMINF = "OemWin2k.inf"
TAPINSTALL='tapinstall.exe'

parser = OptionParser("usage: %prog [--installdir=] install|update|remove|list")
parser.set_defaults(installdir="C:/Program Files/JFX/OpenSesame")
parser.add_option("--installdir", type="string",
                        help="where the OpenSesame is installed")

(options, args) = parser.parse_args()
if len(args) != 1:
    parser.error("need an action")

# Check what we're sposed to do...
action = args[0]
if action not in ['install',  'remove', 'list']:
    parser.error("invalid action %s" % action)

TAPDIR = '%s/tapinstall/%s' % (options.installdir, ARCH)
OVPNCLIENT = '%s/OpenSesame.exe' % options.installdir

if os.path.isfile(OVPNCLIENT):
    FOUNDCLIENT = True
else:
    print "Error: Installdir doesn't look right. No 'OpenSesame.exe'"
    sys.exit(1)
    
if os.path.isdir(TAPDIR):
    os.chdir(TAPDIR)
else:
    print """Error: Installdir seems correct (ie I found OpenSesame.exe),
but I can't find the tapinstall directory"""
    sys.exit(1)

for file in [ TAPINSTALL, TAPDRV, TAPCAT, OEMINF ]:
    if not os.path.isfile(file):
        print """Error: Installdir seems correct (ie I found OpenSesame.exe),
but I can't find %s""" % file
        sys.exit(1)

##################################################################

def runtapinstall(args, errorok=False):
    EXE = '%s/%s' % (TAPDIR, TAPINSTALL)
#    args.insert(0, EXE)
#    cmd = ' '.join(args)
    process = QProcess()
    process.start(EXE, args)
    if not process.waitForFinished():
        print "tapinstall failed. waitForFinished()"
        sys.exit(1)
    output = process.readAll();
    rv = process.exitStatus()
    output=str(output).strip()
    if rv != 0 and not errorok:
        print """tapinstall failed.
command was: %s
output was: %s
returnvalue was: %d""" % (cmd, output, rv)
        sys.exit(1)
    else:
        return (rv, output)

def list_oldtap():
    (rv, output) = runtapinstall(['hwids', OLDTAP])
    return output

def list_tap():
    (rv, output) = runtapinstall(['hwids', TAP])
    return output

def list_drvs():
    output = list_tap()
    if output.find(TAP) >= 0:
        return output
    else:
        print output
        sys.exit(1)
    
def remove_oldtap():
    (rv, output) = runtapinstall(['remove', OLDTAP])
    return output

def update_tap():
    (rv, output) = runtapinstall(['update', OEMINF, TAP])
    if rv==1:
        NEED_REBOOT = True
    return output

def install_tap():
    (rv, output) = runtapinstall(['install', OEMINF, TAP])
    if rv == 1:
        NEED_REBOOT = True
    return output

def remove_drv():
    (rv, output) = runtapinstall(['remove', TAP])
    if rv == 1:
        NEED_REBOOT = True
    print output    

def install_drv():
    # First check to see if we have an old version installed.
    print "Checking for old version of TAP driver..."
    existing = list_oldtap()
    print existing
    if existing.find(OLDTAP) >= 0:
        print "Found old TAP driver (%s), removing..." % OLDTAP
        output = remove_oldtap()
        print output
        print "Removed old TAP driver."
    print "Checking for current version of driver..."
    existing = list_tap()
    print existing
    if existing.find(TAP) >= 0:
        print "Found old TAP drive (%s), updating..." % OLDTAP
        output = update_tap()
        print output
        print "Updated TAP driver."
        return True
    else:
        print "No existing TAP driver found, installing..."
        output = install_tap()
        print output
        print "Installed TAP driver."
        return True


##################################################################
def main():
    if action == 'list':
        print list_drvs()
        sys.exit(0)
    elif action =='install':
        if install_drv():
            if NEED_REBOOT:
                print "Reboot needed."
                sys.exit(42)
            else:
                sys.exit(0)
    elif action == 'remove':
        if remove_drv():
            if NEED_REBOOT:
                print "Reboot needed."
                sys.exit(42)
            else:
                sys.exit(0)


if __name__=='__main__':
    main()




