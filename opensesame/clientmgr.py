# opensesame/clientmgr.py
# OpenSesame

# This file is part of the OpenSesame. 
# Copyright (C) 2009 by Rob Lemley.
# See the README.TXT file for important information about this project.

from PyQt5.QtCore import QThread, QProcess, QVariant, pyqtSignal, pyqtSlot
from queue import Queue


from . import config
from . import vpnmgmt


exelocation = config.settings.value('EXELocation', QVariant(config.defPlatformEXE))

class ClientConn(QThread):
    logready = pyqtSignal(str, str)
    processfinished = pyqtSignal(str)
    def __init__(self, name, ip, port, parent = None):
        QThread.__init__(self, parent)
        
        self.mgrip = ip
        self.port = str(port)
        
        self.exiting = False
        self._name = name
        self.ovconfig=config.OVConfig(name)
        
        self.dirname, self.filename = self.ovconfig.getdir_file()
        self.exeopts = {'--cd': self.dirname,
                '--config': self.filename,
                '--management-hold': None,
                '--management':  (self.mgrip, self.port),
                '--management-query-passwords': None}
        
    
    def run(self):
        self.process = QProcess()
        self.process.setWorkingDirectory(self.dirname)
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        
        self.process.readyRead.connect(self.readlog)
        self.process.finished[int].connect(self.processdone)
        
        args = []
        for arg in self.exeopts.keys():
            args.append(arg)
            if type(self.exeopts[arg]) == tuple:
                for a in self.exeopts[arg]:
                    args.append(a)
            elif self.exeopts[arg] is not None:
                args.append(self.exeopts[arg])
        self.process.start(exelocation, args)        
        
        self.exec_()
        if self.exiting:
            self.endProcess()
        
    
    def endProcess(self):
        if self.process is not None and self.process.state():
            self.process.close()
            self.process.terminate()
            QThread.msleep(100)
            if self.process.state():
                self.process.kill()
            self.process = None

    @pyqtSlot()
    def readlog(self):
        log = self.process.readAll()
        log = str(log)
        self.logready.emit(self._name, log)
    
    @pyqtSlot(int)
    def processdone(self, rv):
        self.logready.emit(self._name, 'OpenVPN Finished.')
        self.exiting = True
        if self.isRunning():
            self.quit()
        self.wait()
        self.processfinished.emit(self._name)

class ClientManager(QThread):
    MAXCLIENTS = 1
    clientlog = pyqtSignal(str)
    clientclosed = pyqtSignal(str)
    alldone = pyqtSignal()
    managerfinished = pyqtSignal()
    closeclient = pyqtSignal()
    logqueueready = pyqtSignal()
    posterror = pyqtSignal(str)
    changeConnState = pyqtSignal(str, str)
    getPrivKeyPass = pyqtSignal(str)
    sendPrivKey = pyqtSignal(str)
    getUserPass = pyqtSignal(str)
    sendUserPass = pyqtSignal(str, str)
    def __init__(self, parent = None):
        QThread.__init__(self, parent)
        
        self.clients = {}
        self.logs = {}
        self.clientmgr = {}
        
        self._mgrip = '127.0.0.1'
        
        self.exiting=False
    
    def run(self):
        self.clientclosed.connect(self.watchclientsfinish)
        self.alldone.connect(self.finalcloseout)
        self.exec_()
            
    def startclient(self, name, port):
        if len(self.clients) < self.MAXCLIENTS:
            ip = self._mgrip
            clientthread = ClientConn(name, ip, port)
            
            name=str(name)
            self.clients[name] = clientthread

            clientthread.logready.connect(self.readclientlog)
            clientthread.processfinished.connect(self.clientdone)
            clientthread.start()
            
            clientmanager = vpnmgmt.MgrClient(name)
            clientmanager.vpnState.connect(self.vpnState)
            clientmanager.passwordState.connect(self.passwordState)
            clientmanager.errState.connect(self.errState)
            
            clientmanager.connectToServer(ip, port)
            self.clientmgr[name] = clientmanager
        else:
            self.posterror.emit('Too many connections')
    
    # Manager slots
    @pyqtSlot()
    def errState(self, name, error):
        name = str(name)
        error = str(error)
        self.posterror.emit("Error in client manager for %s.\n%s" % (name, error))
    
    @pyqtSlot()
    def passwordState(self, name, state):
        name = str(name)
        if state == vpnmgmt.PASSWORD_PRIVKEY:
            self.getPrivKeyPass.emit(name)
        elif state == vpnmgmt.PASSWORD_AUTH:
            self.getUserPass.emit(name)
    
    @pyqtSlot()
    def vpnState(self, name, time, state, info):
        self.changeConnState.emit(name, state)
    
    ##
    
    @pyqtSlot()
    def recvPrivKey(self, name, privkey):
        name = str(name)
        clientmgr = self.clientmgr[name]
        self.sendPrivKey.connect(clientmgr.recvPrivKey)
        self.sendPrivKey.emit(privkey)
    
    @pyqtSlot()
    def recvUserPass(self, name, username, password):
        name = str(name)
        clientmgr = self.clientmgr[name]
        self.sendUserPass.connect(clientmgr.recvUserPass)
        self.sendUserPass.emit(username, password)

    def clientprep(self, name):
        name=str(name)
        if len(self.clients) < self.MAXCLIENTS:
            self.logs[name] = Queue()
            self.logqueueready.emit(name, self.logs[name])
        else:
            self.posterror.emit('Too many connections')

    @pyqtSlot()
    def shutdown(self):
        self.exiting = True
        if self.exiting:
            if len(self.clients) == 0:
                self.alldone.emit()
            else:
                for name in self.clients.keys():
                    self.closeclient.connect(self.clientmgr[name].closeconnection)
                    self.closeclient.emit()

    @pyqtSlot()
    def readclientlog(self, name, log):
        name = str(name)
        self.logs[name].put(log)
        self.clientlog.emit(name)
    
    @pyqtSlot()
    def clientdone(self, name):
        name = str(name)
        self.clients[name] = None
        del self.clients[name]
        self.clientmgr[name] = None
        del self.clientmgr[name]
        self.logs[name] = None
        del self.logs[name]
        self.changeConnState.emit(name, "Disconnected")
        self.clientclosed.emit(name)
    
    @pyqtSlot()
    def watchclientsfinish(self, name):
        if self.exiting:
            name = str(name)
            if self.clients.has_key(name):
                self.clients[name] = None
                del self.clients[name]
            if len(self.clients) == 0:
                self.alldone.emit()
    
    @pyqtSlot()
    def finalcloseout(self):
        if self.isRunning():
            self.quit()
        self.wait()
        self.managerfinished.emit()
    
    @pyqtSlot()
    def startconnection(self, name, port):
        self.startclient(name, port)
        
    @pyqtSlot()
    def prepconnection(self, name):
        self.clientprep(name)
    
    @pyqtSlot()
    def closeconnection(self, name):
        name = str(name)
        if self.clientmgr.has_key(name):
            clientmgr = self.clientmgr[name]
            self.closeclient.connect(clientmgr.closeconnection)
            self.closeclient.emit()
    
    def getLogQ(self, name):
        return self.logs[name]
    
    def numConnections(self):
        return len(self.clients)
