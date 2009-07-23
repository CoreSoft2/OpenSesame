# OVPN/config.py
# JFX OpenVPN Client

# This file is part of the JFX OpenVPN Client GUI. 
# Copyright (C) 2009 by Rob Lemley.
# See the README.TXT file for important information about this project.

import types
import re
import os
import sys
import time
from hashlib import md5
import shutil

from PyQt4.QtCore import QSettings

from exception import ConfigErrorMsg, QuestionMsgBox

APPNAME = 'OpenVPN Client'
VERSION = 'trunk'

DEFAULTS = { 'exelocation':  "C:/Program Files/JFX/OpenVPN Client/bin/openvpn.exe",
                    'windeffileloc':  "C:/Program Files/OpenVPN/config",
                        'linuxbinary':  "/usr/bin/openvpn", 
                        'linuxdeffileloc': "/home",
                        'showTrayWarning': True,
                        'defaultPort': '1194',
                    }

DEFAULTPORT = '1194'

settings = QSettings(QSettings.IniFormat, QSettings.UserScope, "JFX", APPNAME)
settings.setDefaultFormat(QSettings.IniFormat)
iniPath = os.path.dirname(str(settings.fileName()))

platform=sys.platform

if platform == 'win32':
    defPlatformEXE = DEFAULTS['exelocation']
    defFileLoc = DEFAULTS['windeffileloc']
elif platform == 'linux2':
    defPlatformEXE = DEFAULTS['linuxbinary']
    defFileLoc = DEFAULTS['linuxdeffileloc']
else:
    raise "Unsupported platform: %s" % platform

def md5file(filename):
    """Return the hex digest of a file without loading it all into memory"""
    fh = open(filename)
    digest = md5()
    while 1:
        buf = fh.read(4096)
        if buf == "":
            break
        digest.update(buf)
    fh.close()
    return digest.hexdigest()


def strrange(low, high):
    r = []
    for i in range(low, high):
        r.append(str(i))
    return r

def readfile(filename):
    fp = open(filename, 'r')
    lines = fp.readlines()
    fp.close()
    return lines

def writefile(filename, data):
    fp = open(filename, 'w')
    for line in data:
        fp.write(line + '\n')
    fp.close()

class ConfigDesc:
    def __init__(self, parent=None):
        self._parent=parent
        opts = ConfigDict()

        opts.append('client', None, hidden=True)
        opts.append('dev', ['tap', 'tun'])
        opts.append('proto', ['tcp', 'udp'])
        opts.append('remote', self._hostport, multiple=True)
        opts.append('resolv-retry', 'infinite', hidden=True)
        opts.append('nobind', None, hidden=True)
        opts.append('persist-key', None, hidden=True)
        opts.append('persist-tun', None, hidden=True)
        opts.append('ca', self._file)
        opts.append('cert', self._file)
        opts.append('key', self._file)
        opts.append('ns-cert-type', 'server', hidden=True)
        opts.append('tls-auth', self._tlsauth)
        opts.append('comp-lzo', None)
        opts.append('verb', strrange(0,10), hidden=True, default='3')
    
        self._syntaxes = opts
        #TODO: Fill in the allowed customfields
        self._allowedCFs = []
    
    def _hostport(self, value):
        try:
            host, port = value.split(' ',1)
        except ValueError, AttributeError:
            return False
        
        hostparts = host.split('.')
        for part in hostparts:
            if not re.match("^[a-zA-Z0-9-]+$", part):
                return False
        try:
            int(port)
        except ValueError:
            return False
        
        return True
    
    def _string(self, value):
        if type(value) == types.StringType:
            return True
        else:
            return False

    def _file(self, value):
        value=str(value)
        if os.path.isfile(value):
            return True
        newpath = os.path.normpath(os.path.join(iniPath, value))
        if os.path.isfile(newpath):
            return True
        name = str(self._parent.getname())
        if name is not None:
            newpath = os.path.normpath(os.path.join(iniPath, name, value))
            if os.path.isfile(newpath):
                    return True
        return False
        
    def _tlsauth(self, value):
        try:
            file, direction = value.rsplit(' ', 1)
        except ValueError, AttributeError:
            return False
        if not self._file(file):
            return False
        if direction not in ('0', '1'):
            return False
        return True
        
    def checksyntax(self, key, value):
        if key in self._syntaxes.keys():
            for syntax in self._syntaxes[key]:
                if value == syntax:
                    return True
                elif type(syntax) == types.MethodType:
                    if syntax(value):
                        return True
            return False
        elif key in self._allowedCFs:
            # We don't support this key in the GUI, but we do permit it as 
            # a custom field... deal with it here
            return True
        else:
            return False
    
    def getallowed(self):
        return self._syntaxes.keys()
    
    def getallowedCFs(self):
        return self._allowedCFs
    
    def gethidden(self):
        rv = []
        for key in self._syntaxes.keys():
            if self.isHidden(key):
                value = self._syntaxes[key].getDefault()
                rv.append((key, value))
        return rv
    
    def isMulti(self, key):
        return self._syntaxes[key].isMulti()
    
    def isHidden(self, key):
        return self._syntaxes[key].isHidden()

class MultiDict:
    def __init__(self):
        self.nested_dict = { }
    def append(self, key, value=None):
        if not self.nested_dict.has_key(key):
            self.nested_dict[key] = { }
        if type(value) == types.ListType:
            for i in value:
                self.nested_dict[key][i] = 1
        else:
            self.nested_dict[key][value] = 1
    def __getitem__(self, key):
        return self.nested_dict[key].keys()
    def keys(self):
        return self.nested_dict.keys()
    def clear(self):
        return self.nested_dict.clear()
    def __delitem__(self, key):
        return self.nested_dict.__delitem__(key)

class FlagDict(dict):
    DEFAULTFLAGS = {'hidden': False,
                            'multiple': False,
                            'default': None,
                           }
    def __init__(self):
        dict.__init__(self)
        self._flags = self.DEFAULTFLAGS.copy()
    def Hide(self):
        self._flags['hidden'] = True
    def unHide(self):
        self._flags['hidden'] = False
    def isHidden(self):
        return self._flags['hidden']
        
    def setMulti(self):
        self._flags['multiple'] = True
    def unsetMulti(self):  
        self._flags['multiple'] = False
    def isMulti(self):
        return self._flags['multiple']
    def setDefault(self, default):
        self._flags['default'] = default
    def getDefault(self):
        if self._flags['default'] is not None:
            rv = self._flags['default']
        elif self.keys()[0]:
            rv = self.keys()[0]
        else:
            rv = None
        return rv
        
class ConfigDict:
    def __init__(self):
        self.nested_dict = {}
    def append(self, key, value=None, hidden=False, multiple=False, default=None):
        if not self.nested_dict.has_key(key):
            self.nested_dict[key] = FlagDict()
            if hidden:
                self.nested_dict[key].Hide()
            if multiple:
                self.nested_dict[key].setMulti()
            if default:
                self.nested_dict[key].setDefault(default)
        if type(value) == types.ListType:
            for i in value:
                self.nested_dict[key][i] = 1
        else:
            self.nested_dict[key][value] = 1
    def __getitem__(self, key):
        return self.nested_dict[key]
    def keys(self):
        keys = self.nested_dict.keys()
        return keys
        
class OVConfig:
    def __init__(self, name=None):
        self._dict = None
        self._desc = ConfigDesc(self)
        self._loaded = False
        self._saved = False
        self._description = None
        self._hashes = { 'client': None,
                            'ca': None,
                            'key': None,
                            'ta': None,
                            }
        self._usedCFs = []
        if name is not None:
            self._name = name
            self.loadconfig()
    
    def setname(self, name):
        self._name = name
    
    def getname(self):
        name = str(self._name)
        return name
    
    def setdescription(self, description):
        self._description = description
    
    def getdescription(self):
        return self._description
    
    def getremote(self):
        return self._dict['remote'][0]
    
    def getdir_file(self):
        name = str(self._name)
        configdir = os.path.normpath(os.path.join(iniPath, name))
        configfile = os.path.normpath(os.path.join(configdir, 'config.ovpn'))
        return (configdir, configfile)
    
    def gethidden(self):
        return self._desc.gethidden()
    
    def getUsedCFs(self):
        return self.usedCFs
    
    def loadconfig(self):
        # load a config file and check syntax while we're at it... 
        re_comment = re.compile('^#')

        configdir, configfile = self.getdir_file()
        cdata = readfile(configfile)
        config = MultiDict()
        
        for line in cdata:
            line = line.rstrip()
            if re_comment.match(line):
                try:
                    hash, field, value = line.split(' ', 2)
                    if field == 'name':
                        self.setname(value)
                    elif field == 'description':
                        self.setdescription(value)
                except:
                    pass
                continue
            try:
                key, data = line.split(' ', 1)
            except:
                key = line
                data = None
                
            config.append(key, data)
        
        if self.checkconfigsyntax(config):
            self._dict = MultiDict()
            self._dict.nested_dict = config.nested_dict.copy()
            self._loaded = True
            self._saved = True
            return True
        
    def checkconfigsyntax(self, config):
        allowedCFs = self._desc.getAllowedCFs()
        for key in config.keys():
            # WTF does this do? It looks like its checking for a screwed up
            # multidict?
            if len(config[key]) == 0:
                ConfigErrorMsg('No data')
                return False
            # MultiDict entry with one value...
            elif len(config[key]) == 1:
                    if self._desc.checksyntax(key, config[key][0]):
                        if key in allowedCFs:
                            # Need to keep track of what custom fields we have so
                            # when we load the Properties GUI we don't have to parse
                            # again
                            self.usedCFs.append(key)
                        continue
                    else:
                        ConfigErrorMsg('Bad value %s for key %s' % (config[key][0], key))
                        return False
            # MultiDict entry with multiple values
            elif len(config[key]) > 1:
                # TODO: Fix the laziness here... should really specify somewhere WHAT
                # custom fields are allowed to be used multiple times. Here we are just
                # assuming that they can be. 
                # TODO: What does OpenVPN do when you send it a bad config option?
                # maybe we don't really give a fuck?
                if self._desc.isMulti(key) or key in allowedCFs:
                    for value in config[key]:
                        if self._desc.checksyntax(key, value):
                            if key in allowedCFs:
                                # Again, keep track of custom fields
                                self.usedCFs.append(key)
                            continue
                        else:
                            ConfigErrorMsg('Bad value %s for key %s' % (config[key][0], key))
                            return False
                else:
                    ConfigErrorMsg('Key %s is not allowed multiple times' % key)
                    return False
        return True
        
    def setconfig(self, config):
        if self.checkconfigsyntax(config):
            self._dict = config
            self._loaded = True
            self._saved = False
            return True
        else:
            return False
        
    def getconfig(self):
        return self._dict

    def copycerts(self):
        fndict = {'ca': 'ca.crt',
                    'cert': 'client.crt',
                    'key': 'client.key',
                    'tls-auth': 'ta.key'}
        for key in fndict.keys():
            try:
                newfile = self._dict[key][0]
            except:
                continue
            if key == 'tls-auth':
                newfile, dir = newfile.rsplit(' ',1)
            newfile = os.path.normpath(str(newfile))
            if newfile == os.path.basename(newfile):
                newfile = os.path.join(iniPath, str(self._name), newfile)
            bn = fndict[key]
            dirname, filename = self.getdir_file()
            oldfile = os.path.join(dirname, bn)
            if newfile == oldfile:
                return
            if not os.path.exists(dirname):
                os.makedirs(dirname)
            elif os.path.exists(dirname) and not os.path.isdir(dirname):
                os.remove(dirname)
                os.makedirs(dirname)
            if not os.path.isfile(oldfile):
                shutil.copyfile(newfile, oldfile)
            else:
                oldmd5 = md5file(oldfile)
                newmd5 = md5file(newfile)
                if oldmd5 != newmd5:
                    shutil.copyfile(newfile, oldfile)
            del self._dict[key]
            if key == 'tls-auth':
                bn = '%s %s' % (bn, dir)
            self._dict.append(key, bn)
            print

    def writeconfig(self):
        data = []
        gentime = time.strftime("%a, %d %b %Y %H:%M:%S +0000")
        data.append('# JFX OpenVPN Client Config')
        data.append('# Generated %s' % gentime)
        data.append('# name %s' % self._name)
        data.append('# description %s' % self._description)
        for key in self._dict.keys():
            for value in self._dict[key]:
                if value is None:
                    value = ''
                line = '%s %s' % (key, value)
                data.append(line)
        dirname, filename = self.getdir_file()
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        elif os.path.exists(dirname) and not os.path.isdir(dirname):
            os.remove(dirname)
            os.makedirs(dirname)
        writefile(filename, data)
        self._saved = True
        return filename
    
    def _deleteforreal(self):
        dirname, filename = self.getdir_file()
        if os.path.isdir(dirname):
            shutil.rmtree(dirname)
        
    def remove(self):
        msg = """About to delete all of the config files for connection %s.
Are you sure you want to do this?"""
        reply = QuestionMsgBox(msg % self._name)
        if reply:
            self._deleteforreal()
            settings.remove('connections/%s' % self._name)
        
