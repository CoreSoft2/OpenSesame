
# Set some variables to make this easier next time
import os

SOURCEDIR = os.environ['GUIDIR']
QTDIR = 'C:/qt/4.5.2/bin'
PYINSTALLER = 'C:/apps/pyinstaller'



# Process the includes and excludes first

data_files = [
            ('README.TXT', '%s/README.TXT' % SOURCEDIR, 'DATA'),
            ('license.txt', '%s/license.txt' % SOURCEDIR, 'DATA'), 
            ('openvpn-client.ico', '%s/ui/resources/openvpn-client.ico' % SOURCEDIR, 'DATA')
            ]

includes = []
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter']
packages = []
dll_excludes = []
dll_includes = [('QtCore4.dll', '%s/QtCore4.dll' % QTDIR,
                'BINARY'), ('QtGui4.dll', '%s/QtGui4.dll' % QTDIR,
                'BINARY'), ('QtNetwork4.dll', '%s/QtNetwork4.dll' % QTDIR,
                'BINARY')]

# Set up the more obscure PyInstaller runtime options

options = [('O', '', 'OPTION')]


guianalysis = Analysis(['%s/support/_mountzlib.py' % PYINSTALLER,
           '%s/support/useUnicode.py' % PYINSTALLER,
           '%s/opensesame.py' % SOURCEDIR,],
                    pathex=[],
                    hookspath=[],
                    excludes=excludes)
                    
guipyz = PYZ(guianalysis.pure, level=9)

tapanalysis = Analysis(['%s/support/_mountzlib.py' % PYINSTALLER,
           '%s/support/useUnicode.py' % PYINSTALLER,
           '%s/installer/tapinstaller.py' % SOURCEDIR],
                    pathex=[],
                    hookspath=[],
                    excludes=excludes)
                    
tappyz = PYZ(tapanalysis.pure, level=9)


guiexecutable = EXE(guipyz,
                 guianalysis.scripts + includes + packages + options,
                 exclude_binaries=1,
                 name="OpenSesame.exe",
                 debug=False,
                 console=False,
                 strip=False,
                 upx=False,
                 icon='%s/ui/resources/openvpn-client.ico' % SOURCEDIR,
                 version='%s/installer/gui-versioninfo.txt' % SOURCEDIR )

tapexecutable = EXE(tappyz,
                 tapanalysis.scripts + includes + packages + options,
                 exclude_binaries=1,
                 name="tapinstaller.exe",
                 debug=False,
                 console=True,
                 strip=False,
                 upx=False,
                 icon=None,
                 version='%s/installer/tapinstaller-versioninfo.txt' % SOURCEDIR )
          
collect = COLLECT( guiexecutable, tapexecutable,
                  guianalysis.binaries + tapanalysis.binaries - dll_excludes + dll_includes + data_files,
                  name="dist",
                  strip=False,
                  upx=False)


