# ui/privkeyentry.py
# OpenSesame

# This file is part of OpenSesame 
# Copyright (C) 2009-2012 by Rob Lemley.
# See the README.TXT file for important information about this project.

"""
Module implementing PrivKeyEntry.
"""

from PySide.QtGui import QDialog
from PySide.QtCore import Slot, QObject

from Ui_privkeyentry import Ui_PrivKeyEntry

class PrivKeyMapper(QObject):
    def __init__(self, passphrase, parent = None):
        super(PrivKeyMapper,  self).__init__(parent)
        self.passphrase = passphrase
        self.verified = False
        self.docheck = True
    
    def setVerified(self):
        self.verified = True
        self.docheck = False
    
    def isVerified(self):
        return self.verified
    
    def needsCheck(self):
        return self.docheck
    
    def setPassphrase(self, passphrase):
        self.passphrase = passphrase

class PrivKeyEntry(QDialog, Ui_PrivKeyEntry):
    """
    Class documentation goes here.
    """
    def __init__(self, parent = None):
        """
        Constructor
        """
        super(PrivKeyEntry,  self).__init__(parent)
        self.setupUi(self)
        self.lineEditPrivKey.setFocus()
