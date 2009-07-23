# ui/privkeyentry.py
# JFX OpenVPN Client

# This file is part of the JFX OpenVPN Client GUI. 
# Copyright (C) 2009 by Rob Lemley.
# See the README.TXT file for important information about this project.

"""
Module implementing PrivKeyEntry.
"""

from PyQt4.QtGui import QDialog
from PyQt4.QtCore import pyqtSignature, QObject

from Ui_privkeyentry import Ui_PrivKeyEntry

class PrivKeyMapper(QObject):
    def __init__(self, passphrase, parent = None):
        QObject.__init__(self, parent)
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
        QDialog.__init__(self, parent)
        self.setupUi(self)
