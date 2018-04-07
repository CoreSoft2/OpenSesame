# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'authentry.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AuthEntry(object):
    def setupUi(self, AuthEntry):
        AuthEntry.setObjectName("AuthEntry")
        AuthEntry.resize(400, 203)
        self.buttonBox = QtWidgets.QDialogButtonBox(AuthEntry)
        self.buttonBox.setGeometry(QtCore.QRect(40, 160, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(AuthEntry)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 142))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(20, 10, 20, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelUsername = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelUsername.setFont(font)
        self.labelUsername.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelUsername.setObjectName("labelUsername")
        self.verticalLayout.addWidget(self.labelUsername)
        self.lineEditUsername = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditUsername.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.verticalLayout.addWidget(self.lineEditUsername)
        self.labelPassword = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPassword.setFont(font)
        self.labelPassword.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelPassword.setObjectName("labelPassword")
        self.verticalLayout.addWidget(self.labelPassword)
        self.lineEditPassword = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.verticalLayout.addWidget(self.lineEditPassword)
        self.checkBoxRemember = QtWidgets.QCheckBox(AuthEntry)
        self.checkBoxRemember.setGeometry(QtCore.QRect(10, 150, 361, 18))
        self.checkBoxRemember.setObjectName("checkBoxRemember")

        self.retranslateUi(AuthEntry)
        self.buttonBox.accepted.connect(AuthEntry.accept)
        self.buttonBox.rejected.connect(AuthEntry.reject)
        QtCore.QMetaObject.connectSlotsByName(AuthEntry)
        AuthEntry.setTabOrder(self.lineEditUsername, self.lineEditPassword)
        AuthEntry.setTabOrder(self.lineEditPassword, self.checkBoxRemember)
        AuthEntry.setTabOrder(self.checkBoxRemember, self.buttonBox)

    def retranslateUi(self, AuthEntry):
        _translate = QtCore.QCoreApplication.translate
        AuthEntry.setWindowTitle(_translate("AuthEntry", "Enter Authorization Info"))
        self.labelUsername.setText(_translate("AuthEntry", "Username"))
        self.labelPassword.setText(_translate("AuthEntry", "Password"))
        self.checkBoxRemember.setText(_translate("AuthEntry", "Remember for rest of session"))

