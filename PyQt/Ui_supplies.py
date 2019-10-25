# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'supplieswin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Supplies(object):
    def setupUi(self, Supplies):
        Supplies.setObjectName("Supplies")
        Supplies.resize(800, 600)
        Supplies.setWindowIcon(QtGui.QIcon("./icon/windowsicon.ico"))
        self.centralwidget = QtWidgets.QWidget(Supplies)
        self.centralwidget.setObjectName("centralwidget")
        Supplies.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Supplies)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        Supplies.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Supplies)
        self.statusbar.setObjectName("statusbar")
        Supplies.setStatusBar(self.statusbar)

        self.retranslateUi(Supplies)
        QtCore.QMetaObject.connectSlotsByName(Supplies)

    def retranslateUi(self, Supplies):
        _translate = QtCore.QCoreApplication.translate
        Supplies.setWindowTitle(_translate("Supplies", "耗材管理"))

