# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logging.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Log(object):
    def setupUi(self, Log):
        Log.setObjectName("Log")
        Log.resize(578, 384)
        self.buttonBox = QtWidgets.QDialogButtonBox(Log)
        self.buttonBox.setGeometry(QtCore.QRect(210, 330, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(Log)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 571, 321))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 5, 10, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelConnectionName = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.labelConnectionName.setFont(font)
        self.labelConnectionName.setObjectName("labelConnectionName")
        self.verticalLayout.addWidget(self.labelConnectionName)
        self.plainTextEditLog = QtWidgets.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEditLog.setObjectName("plainTextEditLog")
        self.verticalLayout.addWidget(self.plainTextEditLog)

        self.retranslateUi(Log)
        self.buttonBox.accepted.connect(Log.accept)
        self.buttonBox.rejected.connect(Log.reject)
        QtCore.QMetaObject.connectSlotsByName(Log)

    def retranslateUi(self, Log):
        _translate = QtCore.QCoreApplication.translate
        Log.setWindowTitle(_translate("Log", "Log Window"))
        self.labelConnectionName.setText(_translate("Log", "Connection"))

