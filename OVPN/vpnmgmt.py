# OVPN/vpnmgmt.py
# OpenSesame

# This file is part of OpenSesame. 
# Copyright (C) 2009 by Rob Lemley.
# See the README.TXT file for important information about this project.


from PyQt4 import QtCore, QtNetwork
import time

STATE_NONE = 0
STATE_HOLD =1
STATE_PASSWORD = 2
STATE_SUCCESS = 3
STATE_ERROR = 4

PASSWORD_PRIVKEY = 0
PASSWORD_AUTH = 1

class MgrClient(QtCore.QObject):
    holdState = QtCore.pyqtSignal()
    errState = QtCore.pyqtSignal(str, str)
    successState = QtCore.pyqtSignal(str, )
    passwordState = QtCore.pyqtSignal(str, int)
    vpnState = QtCore.pyqtSignal(str, int, str, str)
    vpnInfo = QtCore.pyqtSignal(str, str)
    mgrConnected = QtCore.pyqtSignal()
    def __init__(self, name, parent=None):
        super(MgrClient, self).__init__(parent)
        
        self._name = name
        
        self.tcpSocket = QtNetwork.QTcpSocket(self)
        
        self.tcpSocket.connected.connect(self.connReady)
        self.tcpSocket.readyRead.connect(self.readConn)
        self.tcpSocket.error.connect(self.getError)
        
        self.mgrConnected.connect(self.sendInit)
        self.holdState.connect(self.releaseHold)

        self.state = STATE_NONE
        self.vpnstate = 'CONNECTING' # Initial vpn state
        
        self._closing = False

    @QtCore.pyqtSlot()
    def getError(self, error):
        if error == QtNetwork.QAbstractSocket.RemoteHostClosedError and self._closing:
            return
        error = self.tcpSocket.errorString()
        self.errState.emit(self._name, error)
        
    def connectToServer(self, host, port):
        self.tcpSocket.abort()
        self.tcpSocket.connectToHost(host, port)
    
    @QtCore.pyqtSlot()
    def sendInit(self):
        self.tcpSocket.writeData('state on all\n')
        self.tcpSocket.writeData('auth-retry interact\n')
    
    @QtCore.pyqtSlot()
    def releaseHold(self):
        if self.state == STATE_HOLD:
            self.tcpSocket.writeData('hold release\n')
        
    def processLine(self, line):
        line = str(line)
        line  = line.strip()
        if line[0:6] == '>HOLD:':
            self.state = STATE_HOLD
            self.holdState.emit()
        elif line[0:6] == 'ERROR:':
            self.state = STATE_ERROR
            err, msg = line.split(':',1)
            self.errState.emit(self._name, msg)
        elif line[0:8] == 'SUCCESS:':
            self.state = STATE_SUCCESS
            self.successState.emit(self._name)
        elif line[0:10] == '>PASSWORD:':
            self.state = STATE_PASSWORD
            passwd, msg = line.split(':',1)
            if msg[0:4] == 'Need':
                bogus1, type, bogus2 = msg.split("'",2)
                if type == 'Private Key':
                    self.passwordState.emit(self._name, PASSWORD_PRIVKEY)
                elif type == 'Auth':
                    self.passwordState.emit(self._name, PASSWORD_AUTH)
                else:
                    self.errState.emit(self._name, 'Unable to figure out password auth')
            elif msg[0:20] == 'Verification Failed:':
                self.errState.emit(self._name, 'Password verification failed')
            else:
                self.errState.emit(self._name, 'Some weird password error')
        elif line[0:7] == '>STATE:':
            stt, statedata = line.split(':', 1)
            time, state, info = statedata.split(',', 2)
            self.vpnstate = state
            self.vpnState.emit(self._name, int(time), state, info)
        elif line[0:6] == '>INFO:':
            stt, info = line.split(':', 1)
            self.vpnInfo.emit(self._name, info)
        else:
            pass        # ignore everything else for now?
    
    @QtCore.pyqtSlot()
    def connReady(self):
        now = int(time.time())
        self.mgrConnected.emit()
        self.vpnState.emit(self._name, now, self.vpnstate, '')
    
    @QtCore.pyqtSlot()
    def readConn(self):
        while self.tcpSocket.canReadLine():
            line = self.tcpSocket.readLine()
            self.processLine(line)
            
    @QtCore.pyqtSlot()
    def recvPrivKey(self, privkey):
        self.tcpSocket.writeData('password \'Private Key\' %s\n' % privkey)
    
    @QtCore.pyqtSlot()
    def closeconnection(self):
        self._closing = True
        self.tcpSocket.writeData('signal SIGTERM\n')
            

    
    
