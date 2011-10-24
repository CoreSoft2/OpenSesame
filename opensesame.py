# openvpnclient.py
# OpenSesame

# This file is part of OpenSesame. 
# Copyright (C) 2009-2012 by Rob Lemley.
# See the README.TXT file for important information about this project.

if __name__ == '__main__':
    import sys
    from PySide.QtGui import QApplication
    from ui.openvpnclient import MainWindow
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())

