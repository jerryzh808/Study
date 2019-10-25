# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'devicewin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Device(object):
    def setupUi(self, Device):
        Device.setObjectName("Device")
        Device.resize(800, 600)
        Device.setWindowIcon(QtGui.QIcon("./icon/windowsicon.ico"))
        self.centralwidget = QtWidgets.QWidget(Device)
        self.centralwidget.setObjectName("centralwidget")
        Device.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Device)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        Device.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Device)
        self.statusbar.setObjectName("statusbar")
        Device.setStatusBar(self.statusbar)
        self.retranslateUi(Device)
        QtCore.QMetaObject.connectSlotsByName(Device)

    def retranslateUi(self, Device):
        _translate = QtCore.QCoreApplication.translate
        Device.setWindowTitle(_translate("Device", "设备信息管理(IT)"))

