# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rob/src/opensesame/OpenSesame/ui/logging.ui'
#
# Created: Sun Oct 23 17:17:47 2011
#      by: pyside-uic 0.2.11 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Log(object):
    def setupUi(self, Log):
        Log.setObjectName("Log")
        Log.resize(578, 384)
        self.buttonBox = QtGui.QDialogButtonBox(Log)
        self.buttonBox.setGeometry(QtCore.QRect(210, 330, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtGui.QWidget(Log)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 571, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 5, 10, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelConnectionName = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelConnectionName.setFont(font)
        self.labelConnectionName.setObjectName("labelConnectionName")
        self.verticalLayout.addWidget(self.labelConnectionName)
        self.plainTextEditLog = QtGui.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEditLog.setObjectName("plainTextEditLog")
        self.verticalLayout.addWidget(self.plainTextEditLog)

        self.retranslateUi(Log)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), Log.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), Log.reject)
        QtCore.QMetaObject.connectSlotsByName(Log)

    def retranslateUi(self, Log):
        Log.setWindowTitle(QtGui.QApplication.translate("Log", "Log Window", None, QtGui.QApplication.UnicodeUTF8))
        self.labelConnectionName.setText(QtGui.QApplication.translate("Log", "Connection", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Log = QtGui.QDialog()
    ui = Ui_Log()
    ui.setupUi(Log)
    Log.show()
    sys.exit(app.exec_())

