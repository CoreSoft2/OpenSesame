# ui/openvpnclient.py
# OpenSesame

# This file is part of OpenSesame. 
# Copyright (C) 2009 by Rob Lemley.
# See the README.TXT file for important information about this project.

"""
Module implementing MainWindow.
"""

from PyQt4 import QtGui
from PyQt4 import QtCore

from Ui_openvpnclient import Ui_MainWindow

from appsettings import AppSettings
from properties import Properties
from logging import LogMapper
from privkeyentry import PrivKeyEntry, PrivKeyMapper
from authentry import AuthEntry, AuthMapper

import sys, os.path

from OVPN import config, clientmgr, exception
 
class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """
    closeconnection = QtCore.pyqtSignal(str)
    startconnection = QtCore.pyqtSignal(str, int)
    prepconnection = QtCore.pyqtSignal(str)
    sendPrivKey = QtCore.pyqtSignal(str, str)   # name, passphrase
    sendUserPass = QtCore.pyqtSignal(str, str, str) # name, username, password
    doExitCleanup = QtCore.pyqtSignal()
    def __init__(self, parent = None):
        """
        Constructor
        """
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        
        self.settings = config.settings
        
        self.createTrayIcon()
        showTrayWarning = self.settings.value('showTrayWarning', QtCore.QVariant(config.DEFAULTS['showTrayWarning'])).toBool()
        self.showTrayWarning = showTrayWarning
        
        self.logmaps = {}
        self.config = config
        self.loadconnections()
        self.manager = None
        self.rememberedPrivKeys = {}
        self.rememberedAuths = {}
        self.connstate = {}
        
        self._exiting = False
        
    def closeEvent(self, event):
        if not self._exiting:
            if self.showTrayWarning:
                rv = exception.TrayBox("The program will keep running in the system "
                                "tray. To terminate the program, choose "
                                "<b>Exit</b> in the context menu of the system "
                                "tray entry.")
                if rv:
                    self.showTrayWarning = False
                    tw = QtCore.QVariant(self.showTrayWarning)
                    self.settings.setValue('showTrayWarning', tw)
            self.hide()
            event.ignore()   
        else:
            self.trayIcon.hide()
            event.accept()
    
    def createTrayIcon(self):
        self.minimizeAction = QtGui.QAction("Minimize", self)
        self.minimizeAction.triggered.connect(self.hide)
        self.restoreAction = QtGui.QAction("Restore", self)
        self.restoreAction.triggered.connect(self.showNormal)
        
        self.trayIconMenu = QtGui.QMenu(self)
        self.trayIconMenu.addAction(self.minimizeAction)
        self.trayIconMenu.addAction(self.restoreAction)
        self.trayIconMenu.addSeparator()
        self.trayIconMenu.addAction(self.actionExit)

        self.trayIcon = QtGui.QSystemTrayIcon(self)
        self.trayIcon.setContextMenu(self.trayIconMenu)
        
        self.disconnectedIcon = QtGui.QIcon()
        self.disconnectedIcon.addPixmap(QtGui.QPixmap(":/resources/disconnect.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.connectedIcon = QtGui.QIcon()
        self.connectedIcon.addPixmap(QtGui.QPixmap(":/resources/connect.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        
        self.trayIcon.setIcon(self.disconnectedIcon)
        self.trayIcon.show()

    def startmanager(self):
        self.manager = clientmgr.ClientManager()
        self.manager.logqueueready.connect(self.finishconnection)
        self.manager.posterror.connect(self.criticalError)
        self.manager.changeConnState.connect(self.updateState)
        self.manager.getPrivKeyPass.connect(self.getPrivKeyPass)
        self.manager.getUserPass.connect(self.getUserPass)
        self.manager.clientlog.connect(self.getClientLog)
        self.manager.managerfinished.connect(self.managerfinished)
        self.startconnection.connect(self.manager.startconnection)
        self.closeconnection.connect(self.manager.closeconnection)
        self.prepconnection.connect(self.manager.prepconnection)
        self.sendPrivKey.connect(self.manager.recvPrivKey)
        self.sendUserPass.connect(self.manager.recvUserPass)
        self.doExitCleanup.connect(self.manager.shutdown)
        
        self.manager.start()

    @QtCore.pyqtSlot()
    def criticalError(self, msg):
        exception.CriticalError(msg)
    
    @QtCore.pyqtSlot()
    def updateState(self, name, state):
        name = str(name)
        state = str(state).capitalize()
        
        if self.connstate.has_key(name):
            oldstate = self.connstate[name]
        else:
            oldstate = None
        if self.rememberedPrivKeys.has_key(name):
            savedkey = self.rememberedPrivKeys[name]
        else:
            savedkey = None
        if self.rememberedAuths.has_key(name):
            savedauth = self.rememberedAuths[name]
        else:
            savedauth = None
            
        if oldstate == 'Auth' and state == 'Get_config':
            if savedkey and savedkey.needsCheck():
                savedkey.setVerified()
            if savedauth and savedauth.needsCheck():
                savedauth.setVerified()
            
        
        self.connstate[name] = state
        if state == 'Connected':
            self.trayIcon.setIcon(self.connectedIcon)
        elif state == 'Disconnected':
            self.trayIcon.setIcon(self.disconnectedIcon)
        self.tableConnections.setState(name, state)
    
    @QtCore.pyqtSlot()
    def getPrivKeyPass(self, name):
        name = str(name)
        if self.rememberedPrivKeys.has_key(name) and self.rememberedPrivKeys[name].isVerified():
            self.sendPrivKey.emit(name, self.rememberedPrivKeys[name].passphrase)
        else:
            privKeyPass = PrivKeyEntry(parent=self)
            rv = privKeyPass.exec_()
            if rv == QtGui.QDialog.Accepted:
                privkey = str(privKeyPass.lineEditPrivKey.text())
                if privKeyPass.checkBoxRemember.isChecked():
                    self.rememberedPrivKeys[name] = PrivKeyMapper(privkey)
                self.sendPrivKey.emit(name, privkey)
            elif rv == QtGui.QDialog.Rejected:
                self.closeconnection.emit(name)
    
    @QtCore.pyqtSlot()
    def getUserPass(self, name):
        name = str(name)
        if self.rememberedAuths.has_key(name) and self.rememberedAuths[name].isVerified():
            self.sendUserPass.emit(name, self.rememberedAuths[name].username, self.rememberedAuths[name].password)
        else:
            UserPass = AuthEntry(parent=self)
            rv = UserPass.exec_()
            if rv == QtGui.QDialog.Accepted:
                username = str(UserPass.lineEditUsername.text())
                password = str(UserPass.lineEditPassword.text())
                if UserPass.checkBoxRemember.isChecked():
                    self.rememberedAuths[name] = AuthMapper(username, password)
                self.sendUserPass.emit(name, username, password)
            elif rv == QtGui.QDialog.Rejected:
                self.closeconnection.emit(name)
        
    def loadconnections(self):
        self.settings.beginGroup("connections")
        connames = self.settings.allKeys()
        for conn in connames:
            ovconfig = self.config.OVConfig(name=conn)
            self.addconnection(ovconfig)
        self.settings.endGroup()
            
    
    def addconnection(self, ovconfig):
        self.tableConnections.appendRow(ovconfig)
    
    def editconnection(self, ovconfig, key):
        self.tableConnections.editRow(key, ovconfig)
        
    
    @QtCore.pyqtSignature("")
    def on_actionExit_triggered(self):
        """
        Slot documentation goes here.
        """
        self._exiting = True
        if self.manager and self.manager.numConnections() > 0:
            rv = exception.QuestionMsgBox("Do you want to exit OpenSesame? This will close all open connections.")
        else:
            rv = True
        if rv:
            if not self.manager:
                self.close()
            else:
                self.doExitCleanup.emit()


    @QtCore.pyqtSlot()
    def managerfinished(self):
        if self.manager:
            self.manager.wait()
        self.manager = None
        self.close()
    
    @QtCore.pyqtSignature("")
    def on_actionNew_triggered(self):
        """
        Create a new config
        """
        propDialog = Properties(self.config, parent=self)
        if propDialog.exec_():
            ovconfig = propDialog.getconfig()
            self.addconnection(ovconfig)
            ovconfig.copycerts()
            filename = ovconfig.writeconfig()
            settingkey = 'connections/%s' % ovconfig.getname()
            self.settings.setValue(settingkey, QtCore.QVariant(filename))
    
    @QtCore.pyqtSignature("")
    def on_actionProperties_triggered(self):
        """
        Slot documentation goes here.
        """
        row = self.tableConnections.currentRow()
        self.doProperties(row)

    def doProperties(self, row):
        if row >= 0:
            ovconfig = self.tableConnections.configs[row]
            propDialog = Properties(self.config, ovconfig, self)
        
            if propDialog.exec_():
                ovconfig = propDialog.getconfig()
                self.editconnection(ovconfig, row)
                ovconfig.copycerts()
                filename = ovconfig.writeconfig()
                settingkey = 'connections/%s' % ovconfig.getname()
                self.settings.setValue(settingkey, QtCore.QVariant(filename))

    @QtCore.pyqtSignature("")
    def on_actionDelete_triggered(self):
        """
        Slot documentation goes here.
        """
        key = self.tableConnections.currentRow()
        if key >= 0:
            ovconfig = self.tableConnections.configs[key]
            if ovconfig.remove():
                self.tableConnections.removeRow(key)
            
        
    @QtCore.pyqtSignature("")
    def on_actionConnect_triggered(self):
        """
        Slot documentation goes here.
        """
        if not self.manager:
            self.startmanager()
            
        key = self.tableConnections.currentRow()
        if key >= 0:
            ovconfig = self.tableConnections.configs[key]
            name = ovconfig.getname()
            
            self.prepconnection.emit(name)

    @QtCore.pyqtSlot()
    def finishconnection(self, name, logq):
        name=str(name)
        if self.logmaps.has_key(name):
            self.logmaps[name].reset()
            self.logmaps[name].newQ(logq)
        else:
            self.logmaps[name] = LogMapper(logq, name, self)
        
        mgmtPortBaseTmp = config.settings.value('ManagementBasePort', QtCore.QVariant(config.DEFAULTS['defMgmtBasePort'])).toInt()
        if mgmtPortBaseTmp[1]:
            port = mgmtPortBaseTmp[0]
            self.startconnection.emit(name, port)
        else:
            exception.ConfigErrorMsg("There is an application settings error. Please correct the Management Base Port value.")
            self.closeconnection.emit(name)
            return
        
        self.tableConnections.setState(name, "Connecting")
    
    @QtCore.pyqtSignature("")
    def on_actionDisconnect_triggered(self):
        """
        Slot documentation goes here.
        """
        key = self.tableConnections.currentRow()
        if key >= 0:
            ovconfig = self.tableConnections.configs[key]
            name = ovconfig.getname()
            self.closeconnection.emit(name)
    
    @QtCore.pyqtSignature("")
    def on_actionLogging_triggered(self):
        """
        Slot documentation goes here.
        """
        key = self.tableConnections.currentRow()
        if key >= 0:
            ovconfig = self.tableConnections.configs[key]
            name = ovconfig.getname()
           
            if self.logmaps.has_key(name):
                self.logmaps[name].createWindow()
                self.logmaps[name].showWindow()
            else:
                exception.CriticalError('No log available for connection %s.' % name)

    @QtCore.pyqtSlot()
    def getClientLog(self, name):
        name = str(name)
        self.logmaps[name].getLog()
    
    @QtCore.pyqtSignature("")
    def on_actionAbout_triggered(self):
        """
        Call about dialog
        """
        QtGui.QMessageBox.about(None,
            self.trUtf8("About OpenSesame - Version %s" % config.VERSION),
            self.trUtf8("""Copyright (C) 2009 by Rob Lemley

OpenSesame is distributed under the terms of the GPL license version 3. See license.txt for the full license.

For license terms for OpenVPN and its components, see openvpn-license.txt."""))

    
    @QtCore.pyqtSignature("")
    def on_actionSettings_triggered(self):
        """
        Open the app settings dialog.
        """
        defaultexelocation = QtCore.QVariant(config.defPlatformEXE)
        exelocation = self.settings.value("EXELocation", defaultexelocation).toString()
        defaultMgmtPortBase = QtCore.QVariant(self.config.DEFAULTS['defMgmtBasePort'])
        mgmtPortBase = self.settings.value("ManagementBasePort", defaultMgmtPortBase).toString()
        appsettingsDialog = AppSettings(exelocation, self.showTrayWarning, mgmtPortBase, self)
        
        
        
        if appsettingsDialog.exec_():
            exelocation = appsettingsDialog.exelocation()
            self.settings.setValue("EXELocation", QtCore.QVariant(exelocation))
            trayIconWarning = appsettingsDialog.trayIconWarning()
            self.showTrayWarning = trayIconWarning
            tw = QtCore.QVariant(self.showTrayWarning)
            self.settings.setValue('showTrayWarning', tw)
            mgmtPortBase = appsettingsDialog.mgmtPortBase()
            self.settings.setValue('ManagementBasePort', QtCore.QVariant(mgmtPortBase))
            
    
    @QtCore.pyqtSignature("QModelIndex")
    def on_tableConnections_doubleClicked(self, index):
        """
        double-click on a connection row
        """
        row = index.row()
        if row >= 0:
            self.doProperties(row)
    
    @QtCore.pyqtSignature("")
    def on_actionForget_Password_triggered(self):
        """
        Slot documentation goes here.
        """
        del self.rememberedPrivKeys
        self.rememberedPrivKeys = {}
        del self.rememberedAuths
        self.rememberedAuths = {}
        exception.MsgBox("Passwords forgotten.")
    
    @QtCore.pyqtSignature("")
    def on_actionAbout_Qt_triggered(self):
        """
        Slot documentation goes here.
        """
        QtGui.QMessageBox.aboutQt(None, 
            self.trUtf8("About Qt..."))
    
    @QtCore.pyqtSignature("")
    def on_actionImport_triggered(self):
        """
        Import a config.
        """
        options = QtGui.QFileDialog.Options()
        selectedFilter = QtCore.QString()
        homeDir = QtCore.QDir.homePath()
        fileName = QtGui.QFileDialog.getOpenFileName(self,
                self.tr("Import VPN Configuration"),
                homeDir,
                self.tr("VPN Config Exports (*.ovpnz);;All Files (*)"), selectedFilter,
                options)
        if not fileName.isEmpty():
            fileName = str(fileName)
            ovconfig = config.OVConfig()
            rv = ovconfig.importconf(fileName)
            if rv[0]:
                name = ovconfig.getname()
                if name not in self.tableConnections.getConfigNames():
                    self.addconnection(ovconfig)
                settingkey = 'connections/%s' % name
                dirname, filename = ovconfig.getdir_file()
                self.settings.setValue(settingkey, QtCore.QVariant(filename))
            else:
                exception.CriticalError("Import Error: %s" % rv[1])
                
        
        
    
    @QtCore.pyqtSignature("")
    def on_actionExport_triggered(self):
        """
        Export a config file for transfer to another computer.
        """
        key = self.tableConnections.currentRow()
        if key >= 0:
            ovconfig = self.tableConnections.configs[key]
            
            options = QtGui.QFileDialog.Options()
            selectedFilter = QtCore.QString()
            homeDir = QtCore.QDir.homePath()
            fileName = QtGui.QFileDialog.getSaveFileName(self,
                self.tr("Export VPN Configuration"),
                homeDir,
                self.tr("VPN Config Exports (*.ovpnz);;All Files (*)"), selectedFilter,
                options)
            if not fileName.isEmpty():
                ovconfig.export(fileName)
            
