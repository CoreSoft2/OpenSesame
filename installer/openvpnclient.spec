
# Set some variables to make this easier next time
import os

SOURCEDIR = os.environ['GUIDIR']
CRTHOME = 'C:\\Users\\rob\\projects\\msvcr90_30729.4918'
PYQTHOME = 'C:\\Python26\\Lib\\site-packages\\PyQt4'
PYINSTALLER = 'C:\\Users\\rob\\apps\\pyinstaller'



# Process the includes and excludes first

data_files = [('Microsoft.VC90.CRT.manifest', '%s\\x86_microsoft.vc90.crt_1fc8b3b9a1e18e3b_9.0.30729.4918_none_508da958bcbd2845.manifest' % CRTHOME,
              'DATA'), ('openvpnclient.exe.manifest', '%s\\installer\\installedfiles\\openvpnclient.exe.manifest' % SOURCEDIR,
              'DATA'), ('tapinstaller.exe.manifest', '%s\\installer\\installedfiles\\tapinstaller.exe.manifest' % SOURCEDIR,
              'DATA')]

includes = []
excludes = ['_gtkagg', '_tkagg', 'bsddb', 'curses', 'email', 'pywin.debugger',
            'pywin.debugger.dbgcon', 'pywin.dialogs', 'tcl',
            'Tkconstants', 'Tkinter']
packages = []
dll_excludes = []
dll_includes = [('QtCore4.dll', '%s\\QtCore4.dll' % PYQTHOME,
                'BINARY'), ('QtGui4.dll', '%s\\QtGui4.dll' % PYQTHOME,
                'BINARY'), ('QtNetwork4.dll', '%s\\QtNetwork4.dll' % PYQTHOME,
                'BINARY'), ('msvcp90.dll', '%s\\msvcp90.dll' % CRTHOME,
                'BINARY'), ('msvcr90.dll', '%s\\msvcr90.dll' % CRTHOME,
                'BINARY')]

# Set up the more obscure PyInstaller runtime options

options = [('O', '', 'OPTION')]


guianalysis = Analysis(['%s\\support\\_mountzlib.py' % PYINSTALLER,
           '%s\\support\\useUnicode.py' % PYINSTALLER,
           '%s\\openvpnclient.pyw' % SOURCEDIR,],
                    pathex=[],
                    hookspath=[],
                    excludes=excludes)
                    
guipyz = PYZ(guianalysis.pure, level=9)

tapanalysis = Analysis(['%s\\support\\_mountzlib.py' % PYINSTALLER,
           '%s\\support\\useUnicode.py' % PYINSTALLER,
           '%s\\installer\\tapinstaller.py' % SOURCEDIR],
                    pathex=[],
                    hookspath=[],
                    excludes=excludes)
                    
tappyz = PYZ(tapanalysis.pure, level=9)


guiexecutable = EXE(guipyz,
                 guianalysis.scripts + includes + packages + options,
                 exclude_binaries=1,
                 name="OpenVPNClient.exe",
                 debug=False,
                 console=False,
                 strip=False,
                 upx=False,
                 icon='%s\\ui\\resources\\openvpn-admin-256x256.ico' % SOURCEDIR,
                 version='%s\\installer\\gui-versioninfo.txt' % SOURCEDIR )

tapexecutable = EXE(tappyz,
                 tapanalysis.scripts + includes + packages + options,
                 exclude_binaries=1,
                 name="tapinstaller.exe",
                 debug=False,
                 console=True,
                 strip=False,
                 upx=False,
                 icon=None,
                 version='%s\\installer\\tapinstaller-versioninfo.txt' % SOURCEDIR )
          
collect = COLLECT( guiexecutable, tapexecutable,
                  guianalysis.binaries + tapanalysis.binaries - dll_excludes + dll_includes + data_files,
                  name="dist",
                  strip=False,
                  upx=False)


