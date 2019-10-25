from Ui_supplies import *
from PyQt5.QtWidgets import *


class supply(QMainWindow,Ui_Supplies):
    def __init__(self):
        super(supply,self).__init__();
        self.setupUi(self);

    def closeEvent(self,event):
        event.accept();
        from fuction import fuction
        self.Fuctionwin=fuction();
        self.Fuctionwin.show();