from Ui_device import *
from PyQt5.QtWidgets import *


class device(QMainWindow,Ui_Device):
    def __init__(self):
        super(device,self).__init__();
        self.setupUi(self);

    def closeEvent(self,event):
        event.accept();
        from fuction import fuction
        self.Fuctionwin=fuction();
        self.Fuctionwin.show();