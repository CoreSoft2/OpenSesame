# OVPN/exception.py
# OpenSesame

# This file is part of OpenSesame. 
# Copyright (C) 2009 by Rob Lemley.
# See the README.TXT file for important information about this project.

# Exceptions


import sys
import os.path
import traceback

from PySide.QtGui import QMessageBox

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


def handle_exception( exc_type, exc_value, exc_traceback ):
  filename, line, dummy, dummy = traceback.extract_tb( exc_traceback ).pop()
  filename = os.path.basename( filename )
  error    = "%s: %s" % ( exc_type.__name__, exc_value )

  CriticalError("<center>Whoops. A critical error has occured. This is most likely a bug "
  + "in iOpenSesame. The error is:<br/><br/>"
  + "<b><i>%s</i></b><br/><br/>" % error
  + "It occured at <b>line %d</b> of file <b>%s</b>.<br/><br/>"
      % ( line, filename )
  + "iOpenSesame will now close.</center>" )

  sys.exit( 1 )
    
