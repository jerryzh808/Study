from Ui_fixasset import *
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
#from Ui_fixasset_add import *
import sys

class fixasset(QMainWindow,Ui_FixAsset):
    def __init__(self):
        super(fixasset,self).__init__();
        self.setupUi(self);
        self.InitDB();
        self.Initmodel();
        self.Data_TableView.setSortingEnabled(False)
        self.Data_TableView.setModel(Data_Model);
        self.Data_TableView.setContextMenuPolicy(Qt.CustomContextMenu)
        self.Data_TableView.customContextMenuRequested.connect(self.showContextMenu)
        #self.Data_TableView.horizontalHeader().setStretchLastSection(True);
        self.Data_TableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.QueryBtn.clicked.connect(self.Query);
        self.ClearBtn.clicked.connect(self.Clear);
        self.Sub_ModifyBtn.clicked.connect(self.Fixmodifydata);
        self.setStyleSheet(self.readqss())

    def readqss(self):
        file=open('fixasset_qss.qss');
        stylesheet=file.read();
        return stylesheet;

    def InitDB(self):
        self.DB = QSqlDatabase.addDatabase('QSQLITE');
        self.DB.setDatabaseName('data.db');

    def Initmodel(self):
        global Data_Model;
        Data_Model= QSqlTableModel();
        Data_Model.setEditStrategy(QSqlTableModel.OnManualSubmit);
        Data_Model.setTable('fixasset');
        self.SetHeader();

    def SetHeader(self):

        Data_Model.setHeaderData(0, Qt.Horizontal, '名称');
        Data_Model.setHeaderData(1, Qt.Horizontal, '固定资产编号');
        Data_Model.setHeaderData(2, Qt.Horizontal, '型号');
        Data_Model.setHeaderData(3, Qt.Horizontal, '使用者');
        Data_Model.setHeaderData(4, Qt.Horizontal, '位置');
        Data_Model.setHeaderData(5, Qt.Horizontal, '部门');
        Data_Model.setHeaderData(6, Qt.Horizontal, '配置');
        Data_Model.setHeaderData(7, Qt.Horizontal, '服务编号');
        Data_Model.setHeaderData(8, Qt.Horizontal, '到货日期');
        Data_Model.setHeaderData(9, Qt.Horizontal, '是否报废');
        Data_Model.setHeaderData(10, Qt.Horizontal, '安装日期');

    def Decide(self):
        user = ['user=','"',self.User_LineEdit.text(),'"'];
        name = ['name=', '"', self.Name_LineEdit.text(), '"'];
        fixassetno = ['fixassetno=', '"', self.Fixassetno_LineEdit.text(), '"'];
        model = ['model=', '"', self.Model_LineEdit.text(), '"'];
        location = ['location=', '"', self.Location_LineEdit.text(), '"'];
        dept = ['dept=', '"', self.Dept_LineEdit.text(), '"'];
        config = ['config=', '"', self.Config_LineEdit.text(), '"'];
        servicetag = ['servicetag=', '"', self.Servicetag_LineEdit.text(), '"'];
        getdate = ['getdate=', '"', self.Getdate_LineEdit.text(),'"'];
        isscrap = ['isscrap=', '"', self.Isscra_LineEdit.text(), '"'];
        element = [user,name, fixassetno, model, location, dept, config, servicetag, getdate, isscrap];
        Exec_temp = ''
        for item in element:
            if Exec_temp != '':
                if item[2] != '':
                    Exec_temp += ' or ' + item[0] + item[1] + item[2] + item[3];
                else:
                    continue;
            else:
                if item[2] != '':
                    Exec_temp += item[0] + item[1] + item[2] + item[3];
                else:
                    continue;
        return Exec_temp;

    def Query(self):
        Exec=self.Decide();
        if Exec!='':
            Data_Model.setFilter(Exec);
        else:
            Data_Model.setFilter(None);
        Data_Model.select();
        self.Data_TableView.setSelectionBehavior(QAbstractItemView.SelectItems);
        self.Data_TableView.resizeColumnsToContents();
        self.Data_TableView.resizeRowsToContents();
        self.Data_TableView.sortByColumn(0, QtCore.Qt.AscendingOrder)

    def Delete(self):
        Data_Model.removeRow(self.Data_TableView.currentIndex().row());
        Data_Model.submitAll();
        self.Data_TableView.resizeColumnsToContents();
        self.Data_TableView.resizeRowsToContents();

    def Clear(self):
        self.User_LineEdit.clear();
        self.Name_LineEdit.clear();
        self.Fixassetno_LineEdit.clear();
        self.Model_LineEdit.clear();
        self.Location_LineEdit.clear();
        self.Dept_LineEdit.clear();
        self.Config_LineEdit.clear();
        self.Servicetag_LineEdit.clear();
        self.Getdate_LineEdit.clear();
        self.Isscra_LineEdit.clear();

    def Fixadddata(self):
        Data_Model.insertRow(0);
        #self.AddData=fixadddata();
        #self.AddData.show();

    def Fixmodifydata(self):
        Data_Model.submitAll();
        self.Data_TableView.resizeColumnsToContents();
        self.Data_TableView.resizeRowsToContents();
        self.Data_TableView.sortByColumn(0, QtCore.Qt.AscendingOrder)

    def closeEvent(self,event):
        event.accept();
        from fuction import fuction
        self.Fuctionwin=fuction();
        self.Fuctionwin.show();

    def showContextMenu(self):
        self.Data_TableView.contextMenu = QMenu(self)
        self.Adddata_action = self.Data_TableView.contextMenu.addAction(u'添加数据')
        self.Deldata_action = self.Data_TableView.contextMenu.addAction(u'删除行')
        self.Data_TableView.contextMenu.popup(self.cursor().pos())
        self.Adddata_action.triggered.connect(self.Fixadddata)
        self.Deldata_action.triggered.connect(self.Delete)
        self.Data_TableView.contextMenu.show()

#class fixadddata(QWidget,Ui_Adddata):
    #def __init__(self):
        #super(fixadddata,self).__init__();
        #self.setupUi(self);
        #self.AdddataTable.setModel(Data_Model);
        #self.AdddataTable.horizontalHeader().setStretchLastSection(True);
        #self.InertRow();
        #self.SubmitBtn.clicked.connect(self.Submit);

    #def InertRow(self):
        #Data_Model.insertRow(0);

    #def Submit(self):
        #Data_Model.submitAll();
        #self.close();

if __name__=='__main__':
    GSTAPP=QApplication(sys.argv);
    GSTwin=fixasset();
    GSTwin.show();
    GSTAPP.exec_();
