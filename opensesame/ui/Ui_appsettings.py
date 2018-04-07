# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'appsettings.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AppSettings(object):
    def setupUi(self, AppSettings):
        AppSettings.setObjectName("AppSettings")
        AppSettings.resize(408, 118)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AppSettings.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(AppSettings)
        self.buttonBox.setGeometry(QtCore.QRect(50, 80, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(AppSettings)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 96))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(10, 5, 10, 5)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.lineEditOpenVPNEXE = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditOpenVPNEXE.setEnabled(True)
        self.lineEditOpenVPNEXE.setAutoFillBackground(False)
        self.lineEditOpenVPNEXE.setReadOnly(True)
        self.lineEditOpenVPNEXE.setObjectName("lineEditOpenVPNEXE")
        self.horizontalLayout_2.addWidget(self.lineEditOpenVPNEXE)
        self.toolButtonOpenVPNEXE = QtWidgets.QToolButton(self.verticalLayoutWidget)
        self.toolButtonOpenVPNEXE.setObjectName("toolButtonOpenVPNEXE")
        self.horizontalLayout_2.addWidget(self.toolButtonOpenVPNEXE)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.lineEditManagementBasePort = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEditManagementBasePort.setObjectName("lineEditManagementBasePort")
        self.horizontalLayout.addWidget(self.lineEditManagementBasePort)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.checkBoxshowTrayWarning = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.checkBoxshowTrayWarning.setChecked(True)
        self.checkBoxshowTrayWarning.setObjectName("checkBoxshowTrayWarning")
        self.verticalLayout.addWidget(self.checkBoxshowTrayWarning)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)

        self.retranslateUi(AppSettings)
        self.buttonBox.rejected.connect(AppSettings.reject)
        self.buttonBox.accepted.connect(AppSettings.accept)
        QtCore.QMetaObject.connectSlotsByName(AppSettings)

    def retranslateUi(self, AppSettings):
        _translate = QtCore.QCoreApplication.translate
        AppSettings.setWindowTitle(_translate("AppSettings", "Settings"))
        self.label.setText(_translate("AppSettings", "OpenVPN EXE location"))
        self.toolButtonOpenVPNEXE.setText(_translate("AppSettings", "..."))
        self.label_2.setText(_translate("AppSettings", "Management Base Port"))
        self.checkBoxshowTrayWarning.setText(_translate("AppSettings", "Show Tray Icon Warning"))

from . import ovpn_rc
