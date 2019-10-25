from Ui_scrap import *
from PyQt5.QtWidgets import *


class scrap(QMainWindow,Ui_Scrap):
    def __init__(self):
        super(scrap,self).__init__();
        self.setupUi(self);

    def closeEvent(self,event):
        event.accept();
        from fuction import fuction
        self.Fuctionwin=fuction();
        self.Fuctionwin.show();