# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'purchasewin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Purchase(object):
    def setupUi(self, Purchase):
        Purchase.setObjectName("Purchase")
        Purchase.resize(800, 600)
        Purchase.setWindowIcon(QtGui.QIcon("./icon/windowsicon.ico"))
        self.centralwidget = QtWidgets.QWidget(Purchase)
        self.centralwidget.setObjectName("centralwidget")
        Purchase.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Purchase)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        Purchase.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Purchase)
        self.statusbar.setObjectName("statusbar")
        Purchase.setStatusBar(self.statusbar)

        self.retranslateUi(Purchase)
        QtCore.QMetaObject.connectSlotsByName(Purchase)

    def retranslateUi(self, Purchase):
        _translate = QtCore.QCoreApplication.translate
        Purchase.setWindowTitle(_translate("Purchase", "采购中"))

