# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\rob\projects\JFX-OpenVPN-Client\ui\appsettings.ui'
#
# Created: Sat Sep 12 17:29:13 2009
#      by: PySide UI code generator 4.5.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_AppSettings(object):
    def setupUi(self, AppSettings):
        AppSettings.setObjectName("AppSettings")
        AppSettings.resize(408, 118)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AppSettings.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(AppSettings)
        self.buttonBox.setGeometry(QtCore.QRect(50, 80, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtGui.QWidget(AppSettings)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 90))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 5, 10, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtGui.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lineEditOpenVPNEXE = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEditOpenVPNEXE.setEnabled(True)
        self.lineEditOpenVPNEXE.setAutoFillBackground(False)
        self.lineEditOpenVPNEXE.setReadOnly(True)
        self.lineEditOpenVPNEXE.setObjectName("lineEditOpenVPNEXE")
        self.horizontalLayout_2.addWidget(self.lineEditOpenVPNEXE)
        self.toolButtonOpenVPNEXE = QtGui.QToolButton(self.verticalLayoutWidget)
        self.toolButtonOpenVPNEXE.setObjectName("toolButtonOpenVPNEXE")
        self.horizontalLayout_2.addWidget(self.toolButtonOpenVPNEXE)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtGui.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lineEditManagementBasePort = QtGui.QLineEdit(self.verticalLayoutWidget)
        self.lineEditManagementBasePort.setObjectName("lineEditManagementBasePort")
        self.horizontalLayout.addWidget(self.lineEditManagementBasePort)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.checkBoxshowTrayWarning = QtGui.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxshowTrayWarning.setChecked(True)
        self.checkBoxshowTrayWarning.setObjectName("checkBoxshowTrayWarning")
        self.verticalLayout.addWidget(self.checkBoxshowTrayWarning)
        spacerItem2 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(AppSettings)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("rejected()"), AppSettings.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL("accepted()"), AppSettings.accept)
        QtCore.QMetaObject.connectSlotsByName(AppSettings)

    def retranslateUi(self, AppSettings):
        AppSettings.setWindowTitle(QtGui.QApplication.translate("AppSettings", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("AppSettings", "OpenVPN EXE location", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButtonOpenVPNEXE.setText(QtGui.QApplication.translate("AppSettings", "...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("AppSettings", "Management Base Port", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxshowTrayWarning.setText(QtGui.QApplication.translate("AppSettings", "Show Tray Icon Warning", None, QtGui.QApplication.UnicodeUTF8))

import ovpn_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    AppSettings = QtGui.QDialog()
    ui = Ui_AppSettings()
    ui.setupUi(AppSettings)
    AppSettings.show()
    sys.exit(app.exec_())

