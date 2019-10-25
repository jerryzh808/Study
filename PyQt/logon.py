from fuction import *
from Ui_logon import *
import sqlite3
import time


class logon(QMainWindow,Ui_logon):
    def __init__(self):
        super(logon,self).__init__();
        self.setupUi(self);
        self.LogonBtn.clicked.connect(self.Pushlogin);
    def Pushlogin(self):
        Username=self.Username_LineEdit.text();
        Password=self.Password_LineEdit.text();
        if Username=='':
            self.Logontxt_Label.setText("用户名不能为空，请输入用户名");
        elif Password=='':
            self.Logontxt_Label.setText("密码不能为空");
        else:
            Username_Exec='select * from people where username='+"'"+Username+"'";
            Password_Exec = 'select * from people where username=' + "'" + Username + "'" + ' and ' + 'password= ' + "'" + Password + "'";
            Logon_result=self.DBopen(Username_Exec);
            if Logon_result==None:
                self.Logontxt_Label.setText('Username is not exist');
            else:
                Logon_result=self.DBopen(Password_Exec);
                if Logon_result==None:
                    self.Logontxt_Label.setText('Password is not correct');
                else:
                    time.sleep(1);
                    self.Fuctionshow();

    def Fuctionshow(self):
        self.Fuctionwindow=fuction();
        self.Fuctionwindow.show();
        self.close();

    def DBopen(self,exec):
        Conn = sqlite3.connect('user.db');
        Cursor = Conn.cursor();
        Exec = Cursor.execute(exec);
        Result=Exec.fetchone();
        Cursor.close();
        Conn.close();
        return Result;
