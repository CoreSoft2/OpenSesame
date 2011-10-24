# ui/logging.py
# OpenSesame

# This file is part of the OpenSesame. 
# Copyright (C) 2009-2012 by Rob Lemley.
# See the README.TXT file for important information about this project.


"""
Module implementing Log.
"""

from PySide import QtGui
from PySide import QtCore

from Ui_logging import Ui_Log

class LogMapper(QtCore.QObject):
    def __init__(self, queue, name, parent):
        super(LogMapper,  self).__init__(parent)
        self.Q = queue
        self.name = name
        self.log = ''
        self.window = None
    
    def createWindow(self):
        window = Log()
        self.window = window
    
    def showWindow(self):
        self.window.show()
        self.window.readlog(self.log)
    
    def reset(self):
        self.log = ''
        if self.window and self.window.isVisible():
            self.window.close()
        self.window = None
    
    def getLog(self):
        data = ''
        while not self.Q.empty():
            e = self.Q.get_nowait()
            data += e
        self.log += data
        if self.window:
            self.window.readlog(data)
    
    def newQ(self, queue):
        self.Q = queue
        

class Log(QtGui.QDialog, Ui_Log):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        super(Log,  self).__init__(parent)
        self.setupUi(self)
    
    #@QtCore.Slot()
    def readlog(self, e):
        self.plainTextEditLog.appendPlainText(str(e))
