import sys
from logon import *
from PyQt5.QtWidgets import QApplication

class gstit_app():
    def __init__(self):
        super(gstit_app,self).__init__();
        self.logonwindow=logon();
        self.logonwindow.show();


if __name__=='__main__':
    GSTAPP=QApplication(sys.argv);
    GSTwin=gstit_app();
    GSTAPP.exec_();

