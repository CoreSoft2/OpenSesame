# OVPN/exception.py
# JFX OpenVPN Client

# This file is part of the JFX OpenVPN Client GUI. 
# Copyright (C) 2009 by Rob Lemley.
# See the README.TXT file for important information about this project.

# Exceptions

from PyQt4.QtGui import QMessageBox

def ConfigErrorMsg(error):
    message = str(error)
    reply = QMessageBox.critical(None,
            "Config Error",
            message,
            QMessageBox.Ok)
            
def MsgBox(msg):
    message = str(msg)
    reply = QMessageBox.information(None,
        "Information",
        msg,
        QMessageBox.Ok)

def TrayBox(msg):
    message = str(msg)
    msgBox = QMessageBox()
    msgBox.setText(msg)
    neverButton = msgBox.addButton("Do not show again",  QMessageBox.ActionRole)
    okButton = msgBox.addButton(QMessageBox.Ok)
    msgBox.exec_()
    
    if msgBox.clickedButton() == neverButton:
        return True
    else:
        return False

def QuestionMsgBox(msg):
    message = str(msg)
    reply = QMessageBox.question(None,
        "Really?",
        message,
        QMessageBox.Ok|QMessageBox.Cancel)
    if reply == QMessageBox.Ok:
        return True
    else:
        return False
        
def YesNoMsgBox(msg):
    message = str(msg)
    reply = QMessageBox.question(None,
        "Question...",
        message,
        QMessageBox.Yes|QMessageBox.No)
    if reply == QMessageBox.Yes:
        return True
    else:
        return False

def CriticalError(error):
    message = str(error)
    reply = QMessageBox.critical(None,
            "Critical Error",
            message,
            QMessageBox.Ok)



    
