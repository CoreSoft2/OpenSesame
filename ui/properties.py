# ui/properties.py
# OpenSesame

# This file is part of OpenSesame. 
# Copyright (C) 2009 by Rob Lemley.
# See the README.TXT file for important information about this project.

"""
Module implementing Properties.
"""

from PySide import QtGui
from PySide import QtCore

from Ui_properties import Ui_Properties

import os.path

class Properties(QtGui.QDialog, Ui_Properties):
    """
    Class documentation goes here.
    """
    configok = QtCore.Signal()
    def __init__(self, config, ovconfig=None, parent = None):
        """
        Constructor
        """
        super(Properties,  self).__init__(parent)
        self.config = config
        self._defaultfolder = self.config.defFileLoc
        self.setupUi(self)
        self.doconnections()
        if ovconfig is not None:
            self._ovconfig = ovconfig
            self._config = ovconfig.getconfig()
            self._loadformfromconfig()
        else:
            self._ovconfig = self.config.OVConfig()
            self._config = self.config.MultiDict()
            self.lineEditPort.setText(self.config.DEFAULTS['defaultPort'])
        
    def doconnections(self):
        self.configok.connect(self.accept)
        self.buttonBox.accepted.connect(self.checkconfig)
    
    def getconfig(self):
        return self._ovconfig
        
    def _loadformfromconfig(self):
        c=self._config
        checked = QtCore.Qt.Checked
        unchecked = QtCore.Qt.Unchecked
        self.lineEditNickname.setText(self._ovconfig.getname())
        self.lineEditDescription.setText(self._ovconfig.getdescription())
        dev = c['dev'][0]
        if dev == 'tap':
            self.checkBoxUseTap.setCheckState(checked)
        else:
            self.checkBoxUseTap.setCheckState(unchecked)
        proto = c['proto'][0]
        if proto == 'tcp':
            self.checkBoxUseTCP.setCheckState(checked)
        else:
            self.checkBoxUseTCP.setCheckState(unchecked)
        remote = c['remote'][0]
        gateway, port = remote.split(' ', 1)
        if port != self.config.DEFAULTS['defaultPort']:
            self.checkBoxPort.setCheckState(checked)
            self.enableCustomPort()
            self.lineEditPort.setText(port)
        else:
            self.checkBoxPort.setCheckState(unchecked)
            self.disableCustomPort()
            self.lineEditPort.setText(port)
        self.lineEditGateway.setText(gateway)
        ca = c['ca'][0]
        self.lineEditCACert.setText(ca)
        cert = c['cert'][0]
        self.lineEditUserCert.setText(cert)
        key = c['key'][0]
        self.lineEditPrivKey.setText(key)
        try:
            tlsauth = c['tls-auth'][0]
            ta, direction = tlsauth.rsplit(' ', 1)
            self.lineEditTLSAuth.setText(ta)
            index = self.comboBoxKeyDirection.findText(direction, QtCore.Qt.MatchExactly)
            self.comboBoxKeyDirection.setCurrentIndex(index)
            self.checkBoxUseTLSAuth.setChecked(checked)
            self.enableTLSAuth()
        except:
            self.checkBoxUseTLSAuth.setChecked(unchecked)
            self.disableTLSAuth()
        try:
            complzo = c['comp-lzo']
            self.checkBoxUseLZO.setChecked(checked)
        except:
            self.checkBoxUseLZO.setChecked(unchecked)
        try:
            queryauth1 = c['management-query-passwords']
            queryauth2 = c['auth-user-pass']
            self.checkBoxQueryAuth.setChecked(checked)
        except:
            self.checkBoxQueryAuth.setChecked(unchecked)
        for key in self._ovconfig.getUsedCFs():
            for value in c[key]:
                self.tableCustomFields.addCustomField(key, value)
        
    
    def _loadconfigfromform(self):
        self._config.clear()
        for key, value in self._ovconfig.gethidden():
            self._config.append(key, value)
        if self.checkBoxUseTap.isChecked():
            dev = 'tap'
        else:
            dev = 'tun'
        self._config.append('dev', dev)
        if self.checkBoxUseTCP.isChecked():
            proto = 'tcp'
        else:
            proto = 'udp'
        self._config.append('proto', proto)
        port = self.config.DEFAULTS['defaultPort']
        if self.checkBoxPort.isChecked():
            port = self.lineEditPort.text()
        host = self.lineEditGateway.text()
        remote = '%s %s' % (host, port)
        self._config.append('remote', remote)
        ca = self.lineEditCACert.text()
        self._config.append('ca', ca)
        cert = self.lineEditUserCert.text()
        self._config.append('cert', cert)
        key = self.lineEditPrivKey.text()
        self._config.append('key', key)
        if self.checkBoxUseTLSAuth.isChecked():
            takey = self.lineEditTLSAuth.text()
            tadirection = self.comboBoxKeyDirection.currentText()
            tlsauth = '%s %s' % (takey, tadirection)
            self._config.append('tls-auth', tlsauth)
        if self.checkBoxUseLZO.isChecked():
            self._config.append('comp-lzo')
        if self.checkBoxQueryAuth.isChecked():
            self._config.append('management-query-passwords')
            self._config.append('auth-user-pass')
        # Custom field support
        for (field, value) in self.tableCustomFields.getCustomFields():
            if value is None:
                value=''
            self._config.append(str(field), str(value))
    
    @QtCore.Slot()
    def checkconfig(self):
        self._loadconfigfromform()
        name = self.lineEditNickname.text()
        description = self.lineEditDescription.text()
        self._ovconfig.setname(name)
        self._ovconfig.setdescription(description)
        rv = self._ovconfig.setconfig(self._config)
        if rv:
            self.configok.emit()
        
    @QtCore.Slot("bool")
    def on_checkBoxPort_toggled(self, checked):
        """
        Enable/Disable use of a custom port
        """
        if checked:
            self.enableCustomPort()
        else:
            self.disableCustomPort()
    
    def enableCustomPort(self):
        self.lineEditPort.setEnabled(True)
    
    def disableCustomPort(self):
        self.lineEditPort.setDisabled(True)
    
    @QtCore.Slot("")
    def on_toolButtonUserCert_clicked(self):
        """
        Slot documentation goes here.
        """
        options = QtGui.QFileDialog.Options()
        selectedFilter = ''
        file = self.lineEditUserCert.text()
        if file == '':
            file = self._defaultfolder
        fileName = QtGui.QFileDialog.getOpenFileName(self,
                self.tr("Find user certificate ..."),
                file,
                self.tr("CRT Files (*.crt)"), selectedFilter,
                options)
        if not fileName[0] == '':
            self.lineEditUserCert.setText(fileName)
            self._defaultfolder = os.path.dirname(str(fileName))
    
    @QtCore.Slot("")
    def on_toolButtonCACert_clicked(self):
        """
        Slot documentation goes here.
        """
        options = QtGui.QFileDialog.Options()
        selectedFilter = ''
        file = self.lineEditCACert.text()
        if file == '':
            file = self._defaultfolder
        fileName = QtGui.QFileDialog.getOpenFileName(self,
                self.tr("Find CA certificate ..."),
                file,
                self.tr("CRT Files (*.crt)"), selectedFilter,
                options)
        if not fileName.isEmpty():
            self.lineEditCACert.setText(fileName)
            self._defaultfolder = os.path.dirname(str(fileName))
    
    @QtCore.Slot("")
    def on_toolButtonPrivKey_clicked(self):
        """
        Slot documentation goes here.
        """
        options = QtGui.QFileDialog.Options()
        selectedFilter = ''
        file = self.lineEditPrivKey.text()
        if file == '':
            file = self._defaultfolder
        fileName = QtGui.QFileDialog.getOpenFileName(self,
                self.tr("Find private key ..."),
                file,
                self.tr("KEY Files (*.key)"), selectedFilter,
                options)
        if not fileName.isEmpty():
            self.lineEditPrivKey.setText(fileName)
            self._defaultfolder = os.path.dirname(str(fileName))
    
    @QtCore.Slot("bool")
    def on_checkBoxUseTLSAuth_toggled(self, checked):
        """
        Enable/Disable the TLS Auth options
        """
        if checked:
            self.enableTLSAuth()
        else:
            self.disableTLSAuth()
            
    def enableTLSAuth(self):
        self.lineEditTLSAuth.setEnabled(True)
        self.toolButtonTLSAuth.setEnabled(True)
        self.comboBoxKeyDirection.setEnabled(True)
        
    def disableTLSAuth(self):
        self.lineEditTLSAuth.setDisabled(True)
        self.toolButtonTLSAuth.setDisabled(True)
        self.comboBoxKeyDirection.setDisabled(True)
    
    @QtCore.Slot("")
    def on_toolButtonTLSAuth_clicked(self):
        """
        Slot documentation goes here.
        """
        options = QtGui.QFileDialog.Options()
        selectedFilter = ''
        file = self.lineEditTLSAuth.text()
        if file == '':
            file = self._defaultfolder
        fileName = QtGui.QFileDialog.getOpenFileName(self,
                self.tr("Find ta.key ..."),
                file,
                self.tr("(ta.key);;KEY Files (*.key)"), selectedFilter,
                options)
        if not fileName.isEmpty():
            self.lineEditTLSAuth.setText(fileName)
            self._defaultfolder = os.path.dirname(str(fileName))
            
    @QtCore.Slot("")
    def on_toolButtonAddCF_clicked(self):
        """
        Add a custom field.
        """
        self.tableCustomFields.addCustomField()
    
    @QtCore.Slot("")
    def on_toolButtonRemoveCF_clicked(self):
        """
        Remove custom field.
        """
        self.tableCustomFields.removeCustomField()
