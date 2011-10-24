# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/rob/src/opensesame/OpenSesame/ui/authentry.ui'
#
# Created: Sun Oct 23 17:17:49 2011
#      by: pyside-uic 0.2.11 running on PySide 1.0.6
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AuthEntry(object):
    def setupUi(self, AuthEntry):
        AuthEntry.setObjectName("AuthEntry")
        AuthEntry.resize(400, 203)
        self.buttonBox = QtGui.QDialogButtonBox(AuthEntry)
        self.buttonBox.setGeometry(QtCore.QRect(40, 160, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtGui.QWidget(AuthEntry)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 142))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(20, 10, 20, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelUsername = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelUsername.setFont(font)
        self.labelUsername.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelUsername.setObjectName("labelUsername")
        self.verticalLayout.addWidget(self.labelUsername)
        self.lineEditUsername = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEditUsername.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.verticalLayout.addWidget(self.lineEditUsername)
        self.labelPassword = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.labelPassword.setFont(font)
        self.labelPassword.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelPassword.setObjectName("labelPassword")
        self.verticalLayout.addWidget(self.labelPassword)
        self.lineEditPassword = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEditPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.verticalLayout.addWidget(self.lineEditPassword)
        self.checkBoxRemember = QtGui.QCheckBox(AuthEntry)
        self.checkBoxRemember.setGeometry(QtCore.QRect(10, 150, 361, 18))
        self.checkBoxRemember.setObjectName("checkBoxRemember")

        self.retranslateUi(AuthEntry)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), AuthEntry.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), AuthEntry.reject)
        QtCore.QMetaObject.connectSlotsByName(AuthEntry)
        AuthEntry.setTabOrder(self.lineEditUsername, self.lineEditPassword)
        AuthEntry.setTabOrder(self.lineEditPassword, self.checkBoxRemember)
        AuthEntry.setTabOrder(self.checkBoxRemember, self.buttonBox)

    def retranslateUi(self, AuthEntry):
        AuthEntry.setWindowTitle(QtGui.QApplication.translate("AuthEntry", "Enter Authorization Info", None, QtGui.QApplication.UnicodeUTF8))
        self.labelUsername.setText(QtGui.QApplication.translate("AuthEntry", "Username", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPassword.setText(QtGui.QApplication.translate("AuthEntry", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxRemember.setText(QtGui.QApplication.translate("AuthEntry", "Remember for rest of session", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AuthEntry = QtGui.QDialog()
    ui = Ui_AuthEntry()
    ui.setupUi(AuthEntry)
    AuthEntry.show()
    sys.exit(app.exec_())

