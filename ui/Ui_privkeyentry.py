# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rob\projects\ovpnclient\trunk\ui\privkeyentry.ui'
#
# Created: Mon Jul 20 17:09:03 2009
#      by: PyQt4 UI code generator 4.5.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_PrivKeyEntry(object):
    def setupUi(self, PrivKeyEntry):
        PrivKeyEntry.setObjectName("PrivKeyEntry")
        PrivKeyEntry.resize(400, 152)
        self.buttonBox = QtGui.QDialogButtonBox(PrivKeyEntry)
        self.buttonBox.setGeometry(QtCore.QRect(30, 110, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtGui.QWidget(PrivKeyEntry)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 111))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(20, 10, 20, 10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelPrivKeyPrompt = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.labelPrivKeyPrompt.setFont(font)
        self.labelPrivKeyPrompt.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.labelPrivKeyPrompt.setObjectName("labelPrivKeyPrompt")
        self.verticalLayout.addWidget(self.labelPrivKeyPrompt)
        self.lineEditPrivKey = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEditPrivKey.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPrivKey.setObjectName("lineEditPrivKey")
        self.verticalLayout.addWidget(self.lineEditPrivKey)
        self.checkBoxRemember = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxRemember.setObjectName("checkBoxRemember")
        self.verticalLayout.addWidget(self.checkBoxRemember)

        self.retranslateUi(PrivKeyEntry)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), PrivKeyEntry.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), PrivKeyEntry.reject)
        QtCore.QMetaObject.connectSlotsByName(PrivKeyEntry)
        PrivKeyEntry.setTabOrder(self.lineEditPrivKey, self.checkBoxRemember)
        PrivKeyEntry.setTabOrder(self.checkBoxRemember, self.buttonBox)

    def retranslateUi(self, PrivKeyEntry):
        PrivKeyEntry.setWindowTitle(QtGui.QApplication.translate("PrivKeyEntry", "Enter Private Key", None, QtGui.QApplication.UnicodeUTF8))
        self.labelPrivKeyPrompt.setText(QtGui.QApplication.translate("PrivKeyEntry", "Enter Private Key", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxRemember.setText(QtGui.QApplication.translate("PrivKeyEntry", "Remember for rest of session", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    PrivKeyEntry = QtGui.QDialog()
    ui = Ui_PrivKeyEntry()
    ui.setupUi(PrivKeyEntry)
    PrivKeyEntry.show()
    sys.exit(app.exec_())

