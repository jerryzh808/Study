# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fix_add.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Adddata(object):
    def setupUi(self, Adddata):
        Adddata.setObjectName("Adddata")
        Adddata.resize(1200, 130)
        Adddata.setWindowIcon(QtGui.QIcon("./icon/windowsicon.ico"))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.SubmitBtn = QtWidgets.QPushButton(Adddata)
        self.SubmitBtn.setGeometry(QtCore.QRect(10, 20, 75, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SubmitBtn.sizePolicy().hasHeightForWidth())
        self.SubmitBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SubmitBtn.setFont(font)
        self.SubmitBtn.setObjectName("SubmitBtn")
        self.AdddataTable = QtWidgets.QTableView(Adddata)
        self.AdddataTable.setGeometry(QtCore.QRect(10, 60, 1180, 58))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AdddataTable.sizePolicy().hasHeightForWidth())
        self.AdddataTable.setSizePolicy(sizePolicy)
        self.AdddataTable.setObjectName("AdddataTable")
        self.retranslateUi(Adddata)
        QtCore.QMetaObject.connectSlotsByName(Adddata)

    def retranslateUi(self, Adddata):
        _translate = QtCore.QCoreApplication.translate
        Adddata.setWindowTitle(_translate("Adddata", "添加数据"))
        self.SubmitBtn.setText(_translate("Adddata", "提交"))


