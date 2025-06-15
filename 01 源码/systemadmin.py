# 系统管理员界面模块
import sys
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from connect import *
from PyQt5 import QtCore, QtWidgets

cursor, conn = connect()

# 管理员界面设计模块
class Ui_systemadmin(object):

    def setupUi(self, systemadmin):
        self.mainwindow = systemadmin
        systemadmin.setObjectName("systemadmin")
        systemadmin.resize(1200, 900)
        systemadmin.setWindowTitle("系统管理员系统")
        systemadmin.setStyleSheet("""
            QWidget {
                font-family: "Microsoft YaHei";
                font-size: 18px;
                background-color: #f9f9f9;
            }
            QPushButton {
                font-size: 18px;
                padding: 6px 15px;
                border-radius: 5px;
            }
            QPushButton:hover {
                opacity: 0.85;
            }
            QTableWidget {
                background-color: #ffffff;
                border: 1px solid #ccc;
            }
            QScrollBar:vertical {
                width: 12px;
                background: #f0f0f0;
            }
            QScrollBar::handle:vertical {
                background: #888;
                border-radius: 6px;
            }
        """)

        self.tabWidget = QtWidgets.QTabWidget(systemadmin)
        self.tabWidget.setGeometry(QtCore.QRect(20, 20, 1160, 860))
        self.tabWidget.setStyleSheet("background-color: white;")
        self.tabWidget.setObjectName("tabWidget")

        # ========== Tab 1: 读者信息录入 ==========
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.tabLayout = QtWidgets.QVBoxLayout(self.tab)
        self.tabLayout.setContentsMargins(20, 20, 20, 20)
        self.tabLayout.setSpacing(20)

        # 输入区域布局（拆分上下）
        self.inputLayoutTop = QtWidgets.QHBoxLayout()
        self.inputLayoutTop.setSpacing(20)

        self.label = QtWidgets.QLabel("读者ID")
        self.readerid = QtWidgets.QLineEdit()
        self.inputLayoutTop.addWidget(self.label)
        self.inputLayoutTop.addWidget(self.readerid)
        self.searchReaderBtn = QtWidgets.QPushButton("查询")
        self.searchReaderBtn.setStyleSheet("background-color: #007bff; color: white;")
        self.inputLayoutTop.addWidget(self.searchReaderBtn)

        self.label_2 = QtWidgets.QLabel("姓名")
        self.readname = QtWidgets.QLineEdit()
        self.inputLayoutTop.addWidget(self.label_2)
        self.inputLayoutTop.addWidget(self.readname)

        self.label_4 = QtWidgets.QLabel("单位")
        self.unit = QtWidgets.QComboBox()
        self.unit.addItems([
            "航空学院", "能源与动力学院", "自动化学院", "电子学院", "机电学院",
            "材料学院", "民航学院", "数学学院", "经管学院", "人文学院",
            "艺术学院", "外国语学院", "航天学院", "计算机学院", "马克思主义学院",
            "通飞学院", "物理学院"
        ])
        self.inputLayoutTop.addWidget(self.label_4)
        self.inputLayoutTop.addWidget(self.unit)

        self.label_3 = QtWidgets.QLabel("性别")
        self.sex = QtWidgets.QComboBox()
        self.sex.addItems(["男", "女"])
        self.inputLayoutTop.addWidget(self.label_3)
        self.inputLayoutTop.addWidget(self.sex)

        self.tabLayout.addLayout(self.inputLayoutTop)

        self.inputLayoutBottom = QtWidgets.QHBoxLayout()
        self.inputLayoutBottom.setSpacing(20)

        self.label_6 = QtWidgets.QLabel("读者类型")
        self.readtype = QtWidgets.QComboBox()
        self.readtype.addItems(["本科生", "研究生", "教师"])
        self.inputLayoutBottom.addWidget(self.label_6)
        self.inputLayoutBottom.addWidget(self.readtype)

        self.label_7 = QtWidgets.QLabel("可借册数")
        self.totalnumber = QtWidgets.QLineEdit()
        self.inputLayoutBottom.addWidget(self.label_7)
        self.inputLayoutBottom.addWidget(self.totalnumber)

        self.label_8 = QtWidgets.QLabel("在借册数")
        self.number = QtWidgets.QLineEdit()
        self.inputLayoutBottom.addWidget(self.label_8)
        self.inputLayoutBottom.addWidget(self.number)

        self.label_9 = QtWidgets.QLabel("欠款")
        self.money = QtWidgets.QLineEdit()
        self.inputLayoutBottom.addWidget(self.label_9)
        self.inputLayoutBottom.addWidget(self.money)

        self.label_10 = QtWidgets.QLabel("密码")
        self.readerpassword = QtWidgets.QLineEdit()
        self.readerpassword.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.inputLayoutBottom.addWidget(self.label_10)
        self.inputLayoutBottom.addWidget(self.readerpassword)

        self.tabLayout.addLayout(self.inputLayoutBottom)

        # 按钮区域
        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.addr = QtWidgets.QPushButton("添加")
        self.addr.setStyleSheet("background-color: #28a745; color: white;")
        self.alterr = QtWidgets.QPushButton("修改")
        self.alterr.setStyleSheet("background-color: #007bff; color: white;")
        self.deleter = QtWidgets.QPushButton("删除")
        self.deleter.setStyleSheet("background-color: #dc3545; color: white;")
        self.buttonLayout.addWidget(self.addr)
        self.buttonLayout.addWidget(self.alterr)
        self.buttonLayout.addWidget(self.deleter)
        self.tabLayout.addLayout(self.buttonLayout)

        # 表格
        self.readerinfos = QtWidgets.QTableWidget()
        self.readerinfos.setColumnCount(9)
        self.readerinfos.setHorizontalHeaderLabels([
            "读者ID", "姓名", "性别", "单位", "读者类型",
            "可借册数", "在借册数", "密码", "欠款"])
        self.readerinfos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.readerinfos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.readerinfos.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tabLayout.addWidget(self.readerinfos)

        self.tabWidget.addTab(self.tab, "读者信息录入")

        # ========== Tab 2: 图书管理员信息录入 ==========
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tab2Layout = QtWidgets.QVBoxLayout(self.tab_2)
        self.tab2Layout.setContentsMargins(20, 20, 20, 20)
        self.tab2Layout.setSpacing(20)

        self.adminFormLayout = QtWidgets.QFormLayout()
        self.adminname = QtWidgets.QLineEdit()
        self.adminID = QtWidgets.QLineEdit()
        self.adminpassword = QtWidgets.QLineEdit()
        self.adminFormLayout.addRow("姓名", self.adminname)
        self.adminFormLayout.addRow("ID", self.adminID)
        self.adminFormLayout.addRow("密码", self.adminpassword)
        self.admintype = QtWidgets.QComboBox()
        self.admintype.addItems(["图书管理员", "系统管理员"])
        self.adminFormLayout.addRow("身份", self.admintype)

        self.tab2Layout.addLayout(self.adminFormLayout)

        self.adminButtonLayout = QtWidgets.QHBoxLayout()
        self.adda = QtWidgets.QPushButton("添加")
        self.adda.setStyleSheet("background-color: #28a745; color: white;")
        self.altera = QtWidgets.QPushButton("修改")
        self.altera.setStyleSheet("background-color: #007bff; color: white;")
        self.deletea = QtWidgets.QPushButton("删除")
        self.deletea.setStyleSheet("background-color: #dc3545; color: white;")
        self.adminButtonLayout.addWidget(self.adda)
        self.adminButtonLayout.addWidget(self.altera)
        self.adminButtonLayout.addWidget(self.deletea)
        self.tab2Layout.addLayout(self.adminButtonLayout)

        self.admininfos = QtWidgets.QTableWidget()
        self.admininfos.setColumnCount(4)
        self.admininfos.setHorizontalHeaderLabels(["ID", "姓名", "类型", "密码"])
        self.admininfos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.admininfos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.admininfos.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tab2Layout.addWidget(self.admininfos)

        self.tabWidget.addTab(self.tab_2, "图书管理员信息录入")

        # ========== Tab 3: 登录记录查看 ==========
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tab3Layout = QtWidgets.QVBoxLayout(self.tab_3)

        # 查询框
        self.searchLayout = QtWidgets.QHBoxLayout()
        self.searchLabel = QtWidgets.QLabel("按读者ID查询：")
        self.searchID = QtWidgets.QLineEdit()
        self.searchBtn = QtWidgets.QPushButton("查询")
        self.searchBtn.setStyleSheet("background-color: #007bff; color: white;")
        self.searchLayout.addWidget(self.searchLabel)
        self.searchLayout.addWidget(self.searchID)
        self.searchLayout.addWidget(self.searchBtn)
        self.tab3Layout.addLayout(self.searchLayout)

        # 登录记录表格
        self.loginrecordTable = QtWidgets.QTableWidget()
        self.loginrecordTable.setColumnCount(5)
        self.loginrecordTable.setHorizontalHeaderLabels(["读者ID", "姓名", "单位", "登录时间", "序号"])
        self.loginrecordTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.loginrecordTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.loginrecordTable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tab3Layout.addWidget(self.loginrecordTable)

        self.tabWidget.addTab(self.tab_3, "登录记录查看")

        # 数据加载和信号连接
        self.getreadersinfo()
        self.getadmininfo()
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(systemadmin)

        self.readerinfos.activated.connect(self.displayinfo)
        self.admininfos.activated.connect(self.displayadmininfo)
        self.addr.clicked.connect(self.addreader)
        self.readtype.activated.connect(self.auto)
        self.alterr.clicked.connect(self.alterreader)
        self.deleter.clicked.connect(self.deletereader)
        self.adda.clicked.connect(self.addadmin)
        self.altera.clicked.connect(self.alteradmin)
        self.deletea.clicked.connect(self.deleteadmin)
        self.searchBtn.clicked.connect(self.onSearchLoginRecord)
        self.loadLoginRecords()
        self.searchReaderBtn.clicked.connect(self.searchReaderByID)

    # 清空输入框
    def clearReaderInputs(self):
        self.readerid.clear()
        self.readname.clear()
        self.totalnumber.clear()
        self.number.clear()
        self.money.clear()
        self.unit.setCurrentIndex(0)
        self.sex.setCurrentIndex(0)
        self.readtype.setCurrentIndex(0)
        self.readerpassword.clear()

    def clearAdminInputs(self):
        self.adminID.clear()
        self.adminname.clear()
        self.adminpassword.clear()

    # 获取所有读者的信息
    def getreadersinfo(self):
        sql = 'SELECT * FROM readers order by ID'
        res = cursor.execute(sql)
        readers = cursor.fetchall()
        self.readerinfos.setRowCount(res)
        for i in range(res):
            reader = readers[i]
            for j in range(9):
                self.readerinfos.setItem(i, j, QTableWidgetItem(str(reader[j])))

    # 刷新
    def displayinfo(self):
        s = self.readerinfos.currentRow()
        self.readerid.setText(self.readerinfos.item(s, 0).text())
        self.readname.setText(self.readerinfos.item(s, 1).text())
        self.totalnumber.setText(self.readerinfos.item(s, 5).text())
        self.number.setText(self.readerinfos.item(s, 6).text())
        self.readerpassword.setText(self.readerinfos.item(s, 7).text())
        self.money.setText(self.readerinfos.item(s, 8).text())

    # 添加读者
    def addreader(self):
        id = self.readerid.text()
        name = self.readname.text()
        runit = self.unit.currentText()
        rsex = self.sex.currentText()
        rtype = self.readtype.currentText()
        num = int(self.number.text())
        rpassword = self.readerpassword.text()
        sql = 'SELECT * FROM readers WHERE ID="%s"' % id
        res = cursor.execute(sql)
        if res:
            QMessageBox.warning(self.mainwindow, "警告", "该读者ID已被占用！", QMessageBox.Yes)
        else:
            value = (id, name, rsex, runit, rtype, num, rpassword)
            sql = 'INSERT INTO readers' \
                  '(ID, 姓名, 性别, 单位, 读者类型, 在借册数, password) ' \
                  'VALUES ("%s","%s","%s","%s","%s",%d, "%s");' % value
            cursor.execute(sql)
            conn.commit()
            QMessageBox.warning(self.mainwindow, "提示", "添加成功！", QMessageBox.Yes)
            self.getreadersinfo()
            self.clearReaderInputs()
            self.readerinfos.clearSelection()

    # 添加读者设置角色
    def auto(self):
        if self.readtype.currentText() == '本科生':
            self.totalnumber.setText('10')
        elif self.readtype.currentText() == '研究生':
            self.totalnumber.setText('20')
        elif self.readtype.currentText() == '教师':
            self.totalnumber.setText('30')

    # 读者ID查询
    def searchReaderByID(self):
        id = self.readerid.text().strip()
        if not id:
            QMessageBox.warning(self.mainwindow, "提示", "请输入读者ID进行查询", QMessageBox.Yes)
            return

        sql = 'SELECT * FROM readers ' \
              'WHERE ID="%s"' % id
        cursor.execute(sql)
        reader = cursor.fetchone()
        if reader:
            self.readname.setText(reader[1])
            self.sex.setCurrentText(reader[2])
            self.unit.setCurrentText(reader[3])
            self.readtype.setCurrentText(reader[4])
            self.totalnumber.setText(str(reader[5]))
            self.number.setText(str(reader[6]))
            self.readerpassword.setText(reader[7])
            self.money.setText(str(reader[8]))
            # 定位表格选中行
            for i in range(self.readerinfos.rowCount()):
                if self.readerinfos.item(i, 0).text() == id:
                    self.readerinfos.selectRow(i)
                    break
        else:
            QMessageBox.information(self.mainwindow, "提示", "未找到该读者信息", QMessageBox.Yes)
            self.clearReaderInputs()
            self.readerinfos.clearSelection()

    # 修改读者信息
    def alterreader(self):
        id = self.readerid.text()
        name = self.readname.text()
        runit = self.unit.currentText()
        rsex = self.sex.currentText()
        rtype = self.readtype.currentText()
        total = int(self.totalnumber.text())
        num = int(self.number.text())
        rmoney = float(self.money.text())
        rpassword = self.readerpassword.text()
        sql = 'SELECT * FROM readers ' \
              'WHERE ID="%s"' % id
        res = cursor.execute(sql)
        if res == 0:
            QMessageBox.warning(self.mainwindow, "提示", "该读者不存在，无法修改！", QMessageBox.Yes)
            return
        value = (name, rsex, runit, rtype, total, num, rmoney, rpassword, id)
        sql = 'UPDATE readers ' \
              'SET 姓名="%s",性别="%s",单位="%s",读者类型="%s",可借册数=%d,在借册数=%d,欠款=%.2f,password="%s" ' \
              'WHERE ID="%s"' % value
        cursor.execute(sql)
        conn.commit()
        QMessageBox.warning(self.mainwindow, "提示", "修改成功！", QMessageBox.Yes)
        self.getreadersinfo()
        self.clearReaderInputs()
        self.readerinfos.clearSelection()

    # 删除读者信息
    def deletereader(self):
        res = QMessageBox.warning(self.mainwindow, "警告", "即将删除, 确定？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if res == QMessageBox.Yes:
            id = self.readerid.text()

            # 外键依赖检查
            check_sqls = [
                ('borrow', 'SELECT * FROM borrow WHERE ID="%s" LIMIT 1' % id),
                ('item', 'SELECT * FROM item WHERE ID="%s" LIMIT 1' % id),
            ]
            for name, sql in check_sqls:
                cursor.execute(sql)
                if cursor.fetchone():
                    QMessageBox.warning(self.mainwindow, "删除失败", "该读者在 %s 表中存在关联记录，无法删除。" % name, QMessageBox.Yes)
                    return

            try:
                sql = 'DELETE FROM readers ' \
                      'WHERE ID="%s"' % id
                cursor.execute(sql)
                conn.commit()
                QMessageBox.information(self.mainwindow, "提示", "删除成功！", QMessageBox.Yes)
                self.getreadersinfo()
                self.clearReaderInputs()
                self.readerinfos.clearSelection()
            except Exception as e:
                QMessageBox.critical(None, "错误", "删除失败：%s" % str(e), QMessageBox.Yes)

    # 获取图书管理员的信息
    def getadmininfo(self):
        sql = 'SELECT * FROM workers ' \
              'order by ID'
        res = cursor.execute(sql)
        admins = cursor.fetchall()
        self.admininfos.setRowCount(res)
        for i in range(res):
            admin = admins[i]
            for j in range(4):
                self.admininfos.setItem(i, j, QTableWidgetItem(str(admin[j])))

    # 增加管理员
    def addadmin(self):
        id = self.adminID.text()
        name = self.adminname.text()
        password = self.adminpassword.text()
        rtype = self.admintype.currentText()
        sql = 'SELECT * FROM workers WHERE ID="%s"' % id
        res = cursor.execute(sql)
        if res:
            QMessageBox.warning(self.mainwindow, "警告", "该ID已被占用！", QMessageBox.Yes)
        else:
            value = (id, name, rtype, password)
            sql = 'INSERT INTO workers(ID, 姓名, type, password) ' \
                  'VALUES ("%s","%s","%s","%s");' % value
            print(sql)
            cursor.execute(sql)
            conn.commit()
            QMessageBox.warning(self.mainwindow, "提示", "添加成功！", QMessageBox.Yes)
            self.getadmininfo()
            self.clearReaderInputs()
            self.readerinfos.clearSelection()

    def displayadmininfo(self):
        s = self.admininfos.currentRow()
        self.adminname.setText(self.admininfos.item(s, 1).text())
        self.adminID.setText(self.admininfos.item(s, 0).text())
        self.adminpassword.setText(self.admininfos.item(s, 3).text())
        self.admintype.setCurrentText(self.admininfos.item(s, 2).text())

    # 修改管理员
    def alteradmin(self):
        id = self.adminID.text()
        name = self.adminname.text()
        password = self.adminpassword.text()
        rtype = self.admintype.currentText()
        value = (name, rtype, password, id)
        sql = 'UPDATE workers SET 姓名="%s",type="%s",password="%s" ' \
              'WHERE ID="%s"' % value
        cursor.execute(sql)
        conn.commit()
        self.getadmininfo()
        QMessageBox.warning(self.mainwindow, "提示", "修改成功！", QMessageBox.Yes)
        self.getadmininfo()
        self.clearAdminInputs()
        self.admininfos.clearSelection()

    def deleteadmin(self):
        res = QMessageBox.warning(self.mainwindow, "警告", "即将删除, 确定？", QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if res == QMessageBox.Yes:
            id = self.adminID.text()
            sql = 'DELETE FROM workers WHERE ID="%s"' % id
            cursor.execute(sql)
            conn.commit()
            QMessageBox.warning(self.mainwindow, "提示", "删除成功！", QMessageBox.Yes)
            self.getadmininfo()
            self.clearReaderInputs()
            self.readerinfos.clearSelection()

    # 登陆记录查看
    def loadLoginRecords(self, filter_id=None):
        if filter_id:
            sql = 'SELECT L.ID, R.姓名, R.单位, L.time, L.number ' \
                  'FROM loginrecord L, readers R ' \
                  'WHERE L.ID = R.ID AND L.ID = "%s" ' \
                  'ORDER BY L.time DESC, L.number DESC' % filter_id
        else:
            sql = 'SELECT L.ID, R.姓名, R.单位, L.time, L.number ' \
                  'FROM loginrecord L, readers R ' \
                  'WHERE L.ID = R.ID ' \
                  'ORDER BY L.time DESC, L.number DESC'

        cursor.execute(sql)
        records = cursor.fetchall()
        self.loginrecordTable.setRowCount(len(records))

        for i, row in enumerate(records):
            for j in range(5):
                self.loginrecordTable.setItem(i, j, QTableWidgetItem(str(row[j])))

    # 查询登陆记录
    def onSearchLoginRecord(self):
        id = self.searchID.text().strip()
        self.loadLoginRecords(filter_id=id if id else None)

# 调试 UI
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QWidget()
    ui = Ui_systemadmin()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())