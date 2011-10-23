# ui/appsettings.py
# OpenSesame

# This file is part of OpenSesame. 
# Copyright (C) 2009 by Rob Lemley.
# See the README.TXT file for important information about this project.

"""
Module implementing Settings.
"""

import os
from PySide import QtGui
from PySide import QtCore

from Ui_appsettings import Ui_AppSettings
from OVPN import exception

class AppSettings(QtGui.QDialog, Ui_AppSettings):
    """
    Class documentation goes here.
    """
    def __init__(self, exelocation, trayIconWarning, mgmtPortBase, parent = None):
        """
        Constructor
        """
        QtGui.QDialog.__init__(self, parent)
        
        self.setupUi(self)
        
        self.setexelocation(exelocation)
        self.setTrayIconWarning(trayIconWarning)
        self.setMgmtPortBase(mgmtPortBase)
    
    @QtCore.pyqtSignature("")
    def on_toolButtonOpenVPNEXE_clicked(self):
        """
        Slot documentation goes here.
        """
        options = QtGui.QFileDialog.Options()
        selectedFilter = QtCore.QString()
        if self.parent().config.platform == 'win32':
            fileName = QtGui.QFileDialog.getOpenFileName(self,
                    self.tr("Find openvpn.exe ..."),
                    self.lineEditOpenVPNEXE.text(),
                    self.tr("(openvpn.exe);;EXE Files (*.exe)"), selectedFilter,
                    options)
        elif self.parent().config.platform == 'linux2':
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
    
    def setMgmtPortBase(self, mgmtPortBase):
        self.lineEditManagementBasePort.setText(mgmtPortBase)
    
    def exelocation(self):
        return self.lineEditOpenVPNEXE.text()
    
    def trayIconWarning(self):
        return self.checkBoxshowTrayWarning.isChecked()
    
    def mgmtPortBase(self):
        return self.lineEditManagementBasePort.text()
    
    @QtCore.pyqtSignature("")
    def on_lineEditManagementBasePort_editingFinished(self):
        mgmtPortBase = self.mgmtPortBase()
        ckval = mgmtPortBase.toInt()
        if not ckval[1]:
            exception.ConfigErrorMsg("Management Base Port must be an integer value between 1025 and 65000")
            self.lineEditManagementBasePort.setFocus()
        else:
            if ckval[0] < 1025 or ckval[0] > 65000:
                exception.ConfigErrorMsg("Management Base Port must be an integer value between 1025 and 65000")
                self.lineEditManagementBasePort.setFocus()

