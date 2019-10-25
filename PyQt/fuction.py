from Ui_fuction import *
from PyQt5.QtWidgets import *

import sys

class fuction(QWidget,Ui_fuction):
    def __init__(self):
        super(fuction, self).__init__();
        self.setupUi(self);
        self.ScrapBtn.clicked.connect(self.Scrapshow);
        self.DeviceBtn.clicked.connect(self.Deviceshow);
        self.FixAssetBtn.clicked.connect(self.Fixassetshow);
        self.PurchaseBtn.clicked.connect(self.Purchaseshow);
        self.SuppliesBtn.clicked.connect(self.Supplyshow);

    def Scrapshow(self):
        self.close();
        from scrap import scrap
        self.Scrapwindow=scrap();
        self.Scrapwindow.show();

    def Supplyshow(self):
        self.close();
        from supply import supply
        self.Supplywindow=supply();
        self.Supplywindow.show();

    def Purchaseshow(self):
        self.close();
        from purchase import purchase
        self.Purchasewindow=purchase();
        self.Purchasewindow.show();

    def Fixassetshow(self):
        self.close();
        from fixasset import fixasset
        self.Fixassetwindow=fixasset();
        self.Fixassetwindow.show();


    def Deviceshow(self):
        self.close();
        from device import device
        self.Devicewindow=device();
        self.Devicewindow.show();

if __name__=='__main__':
    GSTAPP=QApplication(sys.argv);
    GSTwin=fuction();
    GSTwin.show();
    GSTAPP.exec_();

