import sys
import time
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from login import Ui_Login
from reader import Ui_Reader
from connect import *
from systemadmin import Ui_systemadmin
from BookAdmin import Ui_bookadmin

# 链接数据库
cursor, conn = connect()

class Readerui(QtWidgets.QMainWindow, Ui_Reader):
    def __init__(self, parent=None):
        super(Readerui, self).__init__(parent)
        self.setupUi(self)


class bookadminui(QtWidgets.QMainWindow, Ui_bookadmin):
    def __init__(self, parent=None):
        super(bookadminui, self).__init__(parent)
        self.setupUi(self)


class sysadminui(QtWidgets.QMainWindow, Ui_systemadmin):
    def __init__(self, parent=None):
        super(sysadminui, self).__init__(parent)
        self.setupUi(self)


# 程序首页（登录界面）
class MyMainForm(QMainWindow, Ui_Login):
    def __init__(self, parent=None):
        super(MyMainForm, self).__init__(parent)
        self.setupUi(self)
        self.exitbt.clicked.connect(self.exit)
        self.loginbt.clicked.connect(self.login)

    # 退出
    def exit(self):
        rec_code = QMessageBox.question(self, "确认", "您确认要退出吗？", QMessageBox.Yes | QMessageBox.No)
        if rec_code != 65536:
            self.close()

    # 登陆
    def login(self):
        ID = self.userline.text()
        PW = self.pwline.text()
        if ID == '' or PW == '':
            QMessageBox.warning(self, "警告", "请输入用户名/密码", QMessageBox.Yes)
        else:
            # 读者登录
            if self.idbox.currentText() == '读者':
                sql = 'select * from readers ' \
                      'where ID = "%s" and password="%s"' % (ID, PW)
                res = cursor.execute(sql)
                if res:
                    logintime = time.strftime("%Y-%m-%d", time.localtime())
                    sql = 'select * from loginrecord ' \
                          'where time="%s"' % logintime
                    res = cursor.execute(sql)
                    logined = cursor.fetchall()
                    if res:
                        last = logined[-1]
                        number = last[-1]
                        num = number + 1
                        sql = 'INSERT INTO loginrecord(ID,time,number) ' \
                              'VALUES(%s,"%s",%d)' % (ID, logintime, num)
                        cursor.execute(sql)
                        conn.commit()
                    else:
                        sql = 'INSERT INTO loginrecord(ID,time,number) ' \
                              'VALUES(%s,"%s",%d)' % (ID, logintime, 1)
                        cursor.execute(sql)
                        conn.commit()
                    self.read = Readerui()
                    self.read.show()
                    self.close()
                else:
                    QMessageBox.warning(self, "警告", "用户ID或密码错误，请重新输入！", QMessageBox.Yes)

            # 图书管理员登录
            elif self.idbox.currentText() == '图书管理员':
                type = '图书管理员'
                sql = 'select * from workers ' \
                      'where ID = "%s" and password="%s" and type="%s" ' % (ID, PW, type)
                res = cursor.execute(sql)
                # 进行判断
                if res:
                    self.bookadmin = bookadminui()
                    self.bookadmin.show()
                    self.close()
                    pass
                else:
                    QMessageBox.warning(self, "警告", "用户ID或密码错误，请重新输入！", QMessageBox.Yes)
            # 系统管理员登录
            elif self.idbox.currentText() == '系统管理员':
                type = '系统管理员'
                sql = 'select * from workers ' \
                      'where ID = "%s" and password="%s" and type="%s"' % (ID, PW, type)
                res = cursor.execute(sql)
                # 进行判断
                if res:
                    self.sysadmin = sysadminui()
                    self.sysadmin.show()
                    self.close()
                else:
                    QMessageBox.warning(self, "警告", "用户ID或密码错误，请重新输入！", QMessageBox.Yes)

# 固定的，PyQt5程序都需要QApplication对象。sys.argv为命令行参数列表，确保程序可以双击运行
app = QApplication(sys.argv)
# 初始化
myWin = MyMainForm()
# 将窗口控件显示在屏幕上
myWin.show()
# 程序运行，sys.exit方法确保程序完整退出。
sys.exit(app.exec_())