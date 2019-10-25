# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'scrapwin.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Scrap(object):
    def setupUi(self, Scrap):
        Scrap.setObjectName("Scrap")
        Scrap.resize(800, 600)
        Scrap.setWindowIcon(QtGui.QIcon("./icon/windowsicon.ico"))
        self.centralwidget = QtWidgets.QWidget(Scrap)
        self.centralwidget.setObjectName("centralwidget")
        Scrap.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Scrap)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        Scrap.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Scrap)
        self.statusbar.setObjectName("statusbar")
        Scrap.setStatusBar(self.statusbar)

        self.retranslateUi(Scrap)
        QtCore.QMetaObject.connectSlotsByName(Scrap)

    def retranslateUi(self, Scrap):
        _translate = QtCore.QCoreApplication.translate
        Scrap.setWindowTitle(_translate("Scrap", "报废管理"))

