# openvpnclient.py
# JFX OpenVPN Client

# This file is part of the JFX OpenVPN Client GUI. 
# Copyright (C) 2009 by Rob Lemley.
# See the README.TXT file for important information about this project.

if __name__ == '__main__':
    import sys
    from PyQt4.QtGui import QApplication
    from ui.openvpnclient import MainWindow
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

