# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'privkeyentry.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PrivKeyEntry(object):
    def setupUi(self, PrivKeyEntry):
        PrivKeyEntry.setObjectName("PrivKeyEntry")
        PrivKeyEntry.resize(400, 152)
        self.buttonBox = QtWidgets.QDialogButtonBox(PrivKeyEntry)
        self.buttonBox.setGeometry(QtCore.QRect(30, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(PrivKeyEntry)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(20, 10, 20, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelPrivKeyPrompt = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelPrivKeyPrompt.setFont(font)
        self.labelPrivKeyPrompt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelPrivKeyPrompt.setObjectName("labelPrivKeyPrompt")
        self.verticalLayout.addWidget(self.labelPrivKeyPrompt)
        self.lineEditPrivKey = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditPrivKey.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPrivKey.setObjectName("lineEditPrivKey")
        self.verticalLayout.addWidget(self.lineEditPrivKey)
        self.checkBoxRemember = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxRemember.setObjectName("checkBoxRemember")
        self.verticalLayout.addWidget(self.checkBoxRemember)

        self.retranslateUi(PrivKeyEntry)
        self.buttonBox.accepted.connect(PrivKeyEntry.accept)
        self.buttonBox.rejected.connect(PrivKeyEntry.reject)
        QtCore.QMetaObject.connectSlotsByName(PrivKeyEntry)
        PrivKeyEntry.setTabOrder(self.lineEditPrivKey, self.checkBoxRemember)
        PrivKeyEntry.setTabOrder(self.checkBoxRemember, self.buttonBox)

    def retranslateUi(self, PrivKeyEntry):
        _translate = QtCore.QCoreApplication.translate
        PrivKeyEntry.setWindowTitle(_translate("PrivKeyEntry", "Enter Private Key"))
        self.labelPrivKeyPrompt.setText(_translate("PrivKeyEntry", "Enter Private Key"))
        self.checkBoxRemember.setText(_translate("PrivKeyEntry", "Remember for rest of session"))

