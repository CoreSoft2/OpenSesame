# ui/appsettings.py
# JFX OpenVPN Client

# This file is part of the JFX OpenVPN Client GUI. 
# Copyright (C) 2009 by Rob Lemley.
# See the README.TXT file for important information about this project.

"""
Module implementing Settings.
"""

import os
from PyQt4 import QtGui
from PyQt4 import QtCore

from Ui_appsettings import Ui_AppSettings

class AppSettings(QtGui.QDialog, Ui_AppSettings):
    """
    Class documentation goes here.
    """
    def __init__(self, exelocation, trayIconWarning, parent = None):
        """
        Constructor
        """
        QtGui.QDialog.__init__(self, parent)
        
        self.setupUi(self)
        
        self.setexelocation(exelocation)
        self.setTrayIconWarning(trayIconWarning)
    
    @QtCore.pyqtSignature("")
    def on_toolButtonOpenVPNEXE_clicked(self):
        """
        Slot documentation goes here.
        """
        options = QtGui.QFileDialog.Options()
        selectedFilter = QtCore.QString()
        if self._parent.config.platform == 'win32':
            fileName = QtGui.QFileDialog.getOpenFileName(self,
                    self.tr("Find openvpn.exe ..."),
                    self.lineEditOpenVPNEXE.text(),
                    self.tr("(openvpn.exe);;EXE Files (*.exe)"), selectedFilter,
                    options)
        elif self.parent.config.platform == 'linux2':
            fileName = QtGui.QFileDialog.getOpenFileName(self,
                    self.tr("Find application ..."),
                    self.lineEditOpenVPNEXE.text(),
                    self.tr("(openvpn);;All files(*)"), selectedFilter,
                    options)
        else:
                raise "Unsupported platform %s" % self.parent.config.platform
        if not fileName.isEmpty():
            self.lineEditOpenVPNEXE.setText(fileName)
    
    def setexelocation(self, exelocation):
        self.lineEditOpenVPNEXE.setText(exelocation)
    
    def setTrayIconWarning(self, trayIconWarning):
        self.checkBoxshowTrayWarning.setChecked(trayIconWarning)
    
    def exelocation(self):
        return self.lineEditOpenVPNEXE.text()
    
    def trayIconWarning(self):
        return self.checkBoxshowTrayWarning.isChecked()

