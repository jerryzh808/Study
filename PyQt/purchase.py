from Ui_purchase import *
from PyQt5.QtWidgets import *



class purchase(QMainWindow,Ui_Purchase):
    def __init__(self):
        super(purchase,self).__init__();
        self.setupUi(self);

    def closeEvent(self,event):
        event.accept();
        from fuction import fuction
        self.Fuctionwin=fuction();
        self.Fuctionwin.show();


