# -*- coding: utf-8 -*-

"""
Module implementing AuthEntry.
"""

from PySide.QtGui import QDialog
from PySide.QtCore import Slot, QObject

from Ui_authentry import Ui_AuthEntry

class AuthMapper(QObject):
    def __init__(self, username, password, parent = None):
        super(AuthMapper,  self).__init__(parent)
        self.username = username
        self.password = password
        self.verified = False
        self.docheck = True
    
    def setVerified(self):
        self.verified = True
        self.docheck = False
    
    def isVerified(self):
        return self.verified
    
    def needsCheck(self):
        return self.docheck
    
    def setUserPass(self, username, password):
        self.username = username
        self.password = password

class AuthEntry(QDialog, Ui_AuthEntry):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        super(AuthEntry,  self).__init__(parent)
        self.setupUi(self)
        self.lineEditUsername.setFocus()
