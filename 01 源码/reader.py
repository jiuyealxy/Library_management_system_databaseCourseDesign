# 读者界面模块
import sys
import time
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from connect import *

cursor, conn = connect()  # 连接数据库

# 读者界面设计
class Ui_Reader(object):

    def setupUi(self, Reader):
        self.mainwindow = Reader
        self.loginID = self.getreaderid()
        Reader.setWindowTitle("读者系统")
        Reader.resize(1200, 900)
        Reader.setStyleSheet("""
            background-color: #f0f0f0; 
            font-family: "Microsoft YaHei";
            font-size: 18px;
        """)

        self.readertab = QtWidgets.QTabWidget(Reader)
        self.readertab.setGeometry(QtCore.QRect(50, 50, 1100, 800))
        self.readertab.setStyleSheet("background-color: #fff;")
        self.readertab.setObjectName("readertab")

        # 借书标签页
        self.borrowbook = QtWidgets.QWidget()
        self.borrowbook.setObjectName("borrowbook")
        self.layoutWidget = QtWidgets.QWidget(self.borrowbook)

        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 1060, 760))
        self.layoutWidget.setStyleSheet("background-color: #fff;")
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setText("书号/书名")
        # 设置标签的样式，调整字体和颜色
        self.label.setStyleSheet("font-size: 18px; color: #333;")
        self.horizontalLayout.addWidget(self.label)

        self.borrowbookid = QtWidgets.QLineEdit(self.layoutWidget)
        # 设置输入框的样式，添加边框和背景色
        self.borrowbookid.setStyleSheet("font-size: 18px; padding: 5px; border: 1px solid #ccc; background-color: #fff;")
        self.horizontalLayout.addWidget(self.borrowbookid)

        self.borrowcheckbt = QtWidgets.QPushButton(self.layoutWidget)
        self.borrowcheckbt.setText("查询")
        # 设置按钮的样式，调整字体、颜色和背景色
        self.borrowcheckbt.setStyleSheet("""
            font-size: 18px; 
            padding: 5px 15px; 
            background-color: #007BFF; 
            color: #fff; 
            border: none;
        """)
        self.horizontalLayout.addWidget(self.borrowcheckbt)

        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.borrowtable = QtWidgets.QTableWidget(self.layoutWidget)
        self.borrowtable.setMouseTracking(False)
        self.borrowtable.setEditTriggers(QtWidgets.QAbstractItemView.EditKeyPressed)
        self.borrowtable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.borrowtable.setObjectName("borrowtable")
        self.borrowtable.setColumnCount(5)
        self.borrowtable.setRowCount(0)
        self.borrowtable.setMaximumHeight(600)
        self.borrowtable.setStyleSheet("""
            font-size: 18px; 
            border: 1px solid #ccc; 
            background-color: #fff;
        """)

        self.borrowtable.setHorizontalHeaderLabels(["书号", "书名", "作者", "出版社", "在馆册数"])
        self.borrowtable.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

        self.verticalLayout_2.addWidget(self.borrowtable)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.borrowokbt = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.borrowokbt.sizePolicy().hasHeightForWidth())
        self.borrowokbt.setSizePolicy(sizePolicy)
        self.borrowokbt.setText("提交")
        # 设置按钮的样式，调整字体、颜色和背景色
        self.borrowokbt.setStyleSheet("""
            font-size: 18px; 
            padding: 5px 15px; 
            background-color: #28a745; 
            color: #fff; 
            border: none;
        """)
        self.horizontalLayout_2.addWidget(self.borrowokbt)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.readertab.addTab(self.borrowbook, "借书")

        # 还书标签页
        self.returnbook = QtWidgets.QWidget()
        self.returnbook.setObjectName("returnbook")

        self.return_layout = QtWidgets.QVBoxLayout(self.returnbook)
        self.return_layout.setContentsMargins(20, 20, 20, 20)
        self.return_layout.setSpacing(30)

        # 顶部输入区域
        self.input_layout = QtWidgets.QHBoxLayout()
        self.returnbo = QtWidgets.QLabel("书号")
        self.returnbo.setStyleSheet("font-size: 18px; color: #333;")
        self.input_layout.addWidget(self.returnbo)

        self.returnbookid = QtWidgets.QLineEdit()
        self.returnbookid.setStyleSheet("""
            font-size: 18px;
            padding: 5px;
            border: 1px solid #ccc;
            background-color: #fff;
        """)
        self.input_layout.addWidget(self.returnbookid)

        self.returnallbt = QtWidgets.QPushButton("显示全部")
        self.returnallbt.setStyleSheet("""
            font-size: 18px;
            padding: 6px 20px;
            background-color: #6c757d;
            color: #fff;
            border: none;
        """)
        self.input_layout.addWidget(self.returnallbt)

        # 查询按钮
        self.returnquerybt = QtWidgets.QPushButton("查询")
        self.returnquerybt.setStyleSheet("""
            font-size: 18px;
            padding: 6px 20px;
            background-color: #007BFF;
            color: #fff;
            border: none;
        """)
        self.input_layout.addWidget(self.returnquerybt)

        # 还书按钮
        self.returnbookbt = QtWidgets.QPushButton("还书")
        self.returnbookbt.setStyleSheet("""
            font-size: 18px;
            padding: 6px 20px;
            background-color: #dc3545;
            color: #fff;
            border: none;
        """)
        self.input_layout.addWidget(self.returnbookbt)

        self.return_layout.addLayout(self.input_layout)

        # 表格显示查询结果
        self.return_table = QtWidgets.QTableWidget()
        self.return_table.setRowCount(0)
        self.return_table.setColumnCount(5)
        self.return_table.setHorizontalHeaderLabels(["书号", "书名", "作者", "出版社", "借书时间"])
        self.return_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.return_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.return_table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.return_table.setStyleSheet("""
            font-size: 18px;
            border: 1px solid #ccc;
            background-color: #fff;
        """)
        self.return_layout.addWidget(self.return_table)

        self.readertab.addTab(self.returnbook, "还书")

        # 查询图书信息标签页
        self.checkbook = QtWidgets.QWidget()
        self.checkbook.setObjectName("checkbook")

        # 外层垂直布局
        self.check_layout = QtWidgets.QVBoxLayout(self.checkbook)
        self.check_layout.setContentsMargins(20, 20, 20, 20)
        self.check_layout.setSpacing(30)

        # 顶部输入条件区域（保留原 self.widget）
        self.widget = QtWidgets.QWidget(self.checkbook)
        self.widget.setStyleSheet("background-color: #fff;")
        self.widget.setObjectName("widget")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(15)

        # 左侧：五行输入框
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()

        def make_input_row(label_text):
            layout = QtWidgets.QHBoxLayout()
            label = QtWidgets.QLabel(label_text)
            label.setStyleSheet("font-size: 18px; color: #333;")
            lineedit = QtWidgets.QLineEdit()
            lineedit.setStyleSheet("font-size: 18px; padding: 5px; border: 1px solid #ccc; background-color: #fff;")
            layout.addWidget(label)
            layout.addWidget(lineedit)
            return layout, lineedit

        row1, self.bookid = make_input_row("书名")
        row2, self.bookname = make_input_row("书号")
        row3, self.author = make_input_row("作者")
        row4, self.type = make_input_row("类别")
        row5, self.press = make_input_row("出版社")

        for row in [row1, row2, row3, row4, row5]:
            self.verticalLayout_4.addLayout(row)

        self.horizontalLayout_9.addLayout(self.verticalLayout_4)

        # 右侧：两个按钮垂直布局
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.pushButton = QtWidgets.QPushButton("查询所有")
        self.pushButton.setStyleSheet("""
            font-size: 18px; 
            padding: 6px 20px; 
            background-color: #007BFF; 
            color: #fff; 
            border: none;
        """)
        self.verticalLayout.addWidget(self.pushButton)

        self.checkbt = QtWidgets.QPushButton("查询")
        self.checkbt.setStyleSheet("""
            font-size: 18px; 
            padding: 6px 20px; 
            background-color: #007BFF; 
            color: #fff; 
            border: none;
        """)
        self.verticalLayout.addWidget(self.checkbt)

        self.horizontalLayout_9.addLayout(self.verticalLayout)

        self.check_layout.addWidget(self.widget)

        # 表格
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(0)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.Interactive)
        header.setStretchLastSection(False)
        # 设置各列宽度
        column_widths = [70, 160, 120, 120, 150, 200, 100, 100, 100, 100]
        for i, width in enumerate(column_widths):
            header.resizeSection(i, width)

        self.tableWidget.setHorizontalHeaderLabels([
            "书号", "书名", "作者", "类别", "出版社", "摘要",
            "馆藏册数", "在馆册数", "书架号", "被借次数"
        ])
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.tableWidget.setStyleSheet("""
            font-size: 18px;
            border: 1px solid #ccc;
            background-color: #fff;
            QScrollBar:vertical {
                width: 12px;
                background: #f0f0f0;
            }
            QScrollBar::handle:vertical {
                background: #888;
                min-height: 20px;
                border-radius: 6px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0;
            }
            QScrollBar:horizontal {
                height: 12px;
                background: #f0f0f0;
            }
            QScrollBar::handle:horizontal {
                background: #888;
                min-width: 20px;
                border-radius: 6px;
            }
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                width: 0;
            }
        """)

        self.check_layout.addWidget(self.tableWidget)

        # 添加 tab
        self.readertab.addTab(self.checkbook, "查询图书信息")

        # 用户信息修改标签页
        self.userinfo = QtWidgets.QWidget()
        self.userinfo.setObjectName("userinfo")

        self.userinfo_layout = QtWidgets.QVBoxLayout(self.userinfo)
        self.userinfo_layout.setContentsMargins(20, 20, 20, 20)
        self.userinfo_layout.setSpacing(30)

        # 顶部修改信息区域
        self.edit_layout = QtWidgets.QHBoxLayout()

        # 左边垂直字段输入区域
        self.fields_layout = QtWidgets.QVBoxLayout()

        def make_info_input(label_text):
            layout = QtWidgets.QHBoxLayout()
            label = QtWidgets.QLabel(label_text)
            label.setStyleSheet("font-size: 18px; color: #333;")
            lineedit = QtWidgets.QLineEdit()
            lineedit.setStyleSheet("""
                font-size: 18px;
                padding: 5px;
                border: 1px solid #ccc;
                background-color: #fff;
            """)
            layout.addWidget(label)
            layout.addWidget(lineedit)
            return layout, lineedit

        row1, self.lineEdit_8 = make_info_input("姓名")
        row2, self.lineEdit_9 = make_info_input("性别")
        row3, self.lineEdit_11 = make_info_input("密码")

        for row in [row1, row2, row3]:
            self.fields_layout.addLayout(row)

        self.edit_layout.addLayout(self.fields_layout)

        # 右侧按钮
        self.pushButton_5 = QtWidgets.QPushButton("修改")
        self.pushButton_5.setStyleSheet("""
            font-size: 18px;
            padding: 6px 20px;
            background-color: #28a745;
            color: #fff;
            border: none;
        """)
        self.edit_layout.addWidget(self.pushButton_5)

        self.userinfo_layout.addLayout(self.edit_layout)

        # 中部信息展示框
        self.textBrowser_2 = QtWidgets.QTextBrowser()
        self.textBrowser_2.setAlignment(QtCore.Qt.AlignCenter)
        self.textBrowser_2.setStyleSheet("""
            font-size: 22px;
            color: #333;
            background-color: #fdfdfd;
            border: 1px solid #ddd;
            border-radius: 10px;
            padding: 20px;
            line-height: 28px;
            box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.05);
        """)
        self.userinfo_layout.addWidget(self.textBrowser_2)

        self.readertab.addTab(self.userinfo, "用户信息修改")

        # 逾期罚款标签页
        self.pay_2 = QtWidgets.QWidget()
        self.pay_2.setObjectName("pay_2")

        self.pay_layout = QtWidgets.QVBoxLayout(self.pay_2)
        self.pay_layout.setContentsMargins(50, 50, 50, 50)
        self.pay_layout.setSpacing(30)

        # 欠款金额显示
        self.fine_layout = QtWidgets.QHBoxLayout()
        self.label_12 = QtWidgets.QLabel("需支付罚款")
        self.label_12.setStyleSheet("font-size: 20px; color: #333;")
        self.money = QtWidgets.QLabel("0 元")
        self.money.setStyleSheet("font-size: 20px; font-weight: bold; color: #d9534f;")
        self.fine_layout.addWidget(self.label_12)
        self.fine_layout.addWidget(self.money)
        self.fine_layout.addStretch()

        self.pay_layout.addLayout(self.fine_layout)

        # 支付按钮区域
        self.button_layout = QtWidgets.QHBoxLayout()
        self.button_layout.addStretch()

        self.wepay = QtWidgets.QPushButton("微信支付")
        self.wepay.setStyleSheet("""
            font-size: 18px;
            padding: 6px 20px;
            background-color: #09BB07;
            color: #fff;
            border: none;
        """)
        self.button_layout.addWidget(self.wepay)

        self.alipay = QtWidgets.QPushButton("支付宝支付")
        self.alipay.setStyleSheet("""
            font-size: 18px;
            padding: 6px 20px;
            background-color: #00A1FF;
            color: #fff;
            border: none;
        """)
        self.button_layout.addWidget(self.alipay)

        self.button_layout.addStretch()
        self.pay_layout.addLayout(self.button_layout)

        self.readertab.addTab(self.pay_2, "逾期罚款")

        # 获取读者信息
        self.getreaderinfo()
        # 设置当前显示的标签页为第一个
        self.readertab.setCurrentIndex(0)
        # 连接信号和槽函数
        QtCore.QMetaObject.connectSlotsByName(Reader)
        self.borrowcheckbt.clicked.connect(self.borrowidcheck)
        self.borrowokbt.clicked.connect(self.submit)
        self.returnbookbt.clicked.connect(self.ReturnBook)
        self.returnallbt.clicked.connect(self.show_all_returns)
        self.pushButton.clicked.connect(self.selectallbook)
        self.checkbt.clicked.connect(self.selectbook)
        self.pushButton_5.clicked.connect(self.alterinfo)
        self.wepay.clicked.connect(self.paymoney)
        self.alipay.clicked.connect(self.paymoney)
        self.returnquerybt.clicked.connect(self.returnquery)
        self.return_table.itemDoubleClicked.connect(self.fill_return_bookid)

        self.returnquery()
        self.borrowidcheck()

    # 借书信息查询
    def borrowidcheck(self):
        bookin = self.borrowbookid.text()
        if bookin:
            sql = 'SELECT * FROM books WHERE 书号="%s" OR 书名 LIKE "%%%s%%"' % (bookin, bookin)
        else:
            sql = 'SELECT * FROM books'

        cursor.execute(sql)
        bookinfo = cursor.fetchall()
        n = len(bookinfo)
        self.borrowtable.setRowCount(n)
        for i in range(n):
            book = bookinfo[i]
            bookid = QTableWidgetItem(book[0])
            bookid.setTextAlignment(QtCore.Qt.AlignCenter)
            bookname = QTableWidgetItem(book[1])
            bookname.setTextAlignment(QtCore.Qt.AlignCenter)
            bookauthor = QTableWidgetItem(book[2])
            bookauthor.setTextAlignment(QtCore.Qt.AlignCenter)
            bookpress = QTableWidgetItem(book[5])
            bookpress.setTextAlignment(QtCore.Qt.AlignCenter)
            booknumber = QTableWidgetItem(str(book[8]))
            booknumber.setTextAlignment(QtCore.Qt.AlignCenter)

            self.borrowtable.setItem(i, 0, bookid)
            self.borrowtable.setItem(i, 1, bookname)
            self.borrowtable.setItem(i, 2, bookauthor)
            self.borrowtable.setItem(i, 3, bookpress)
            self.borrowtable.setItem(i, 4, booknumber)

    # 获取当前读者ID
    def getreaderid(self):
        nowtime = time.strftime("%Y-%m-%d", time.localtime())
        sql = 'SELECT * FROM loginrecord ' \
              'WHERE time = "%s" ' \
              'ORDER BY number' % nowtime
        cursor.execute(sql)
        todaylogin = cursor.fetchall()
        readerlogin = todaylogin[-1]
        ID = readerlogin[0]
        print(ID)
        return ID

    # 获取读者信息
    def getreaderinfo(self):
        sql = 'SELECT * FROM readers ' \
              'WHERE ID="%s"' % (self.loginID)
        cursor.execute(sql)
        readerlogined = cursor.fetchall()
        readerlogined = readerlogined[0]
        text = '读者ID：%s\n姓名：%s\n性别：%s\n单位：%s\n读者类型：%s\n可借册数：%d\n在借册数：%d\n密码：%s\n欠款：%.2f' % readerlogined
        self.textBrowser_2.setText(text)
        money = str(readerlogined[-1]) + '元'
        self.money.setText(money)

    # 提交借书申请
    def submit(self):
        s = self.borrowtable.currentRow()
        if s == -1:
            QMessageBox.warning(self.mainwindow, "警告", "请点击想借阅的书！", QMessageBox.Yes)
        else:
            remain = int(self.borrowtable.item(s, 4).text())
            if remain == 0:
                QMessageBox.warning(self.mainwindow, "警告", "这本书已经借光啦！", QMessageBox.Yes)
            else:
                t = self.borrowtable.item(s, 0).text()
                sql = 'SELECT * FROM item ' \
                      'where ID="%s" and bookid="%s" and type="borrow"' % (self.loginID, t)
                res = cursor.execute(sql)
                if res:
                    QMessageBox.warning(self.mainwindow, "警告", "请勿重复提交！", QMessageBox.Yes)
                else:
                    nowtime = time.strftime("%Y-%m-%d", time.localtime())
                    sql = 'INSERT INTO item(bookid,ID,time,type) ' \
                          'VALUES ("%s","%s","%s","borrow")' % (t, self.loginID, nowtime)
                    cursor.execute(sql)
                    conn.commit()
                    QMessageBox.warning(self.mainwindow, "提示", "提交成功！", QMessageBox.Yes)

    def show_all_returns(self):
        self.returnbookid.clear()
        self.returnquery()

    # 还书查询
    def returnquery(self):
        bookid = self.returnbookid.text().strip()

        if bookid:
            sql = 'SELECT br.书号, b.书名, b.作者, b.出版社, br.借书时间 ' \
                  'FROM borrow br, books b ' \
                  'WHERE br.书号 = b.书号 AND br.ID = "%s" AND br.书号 = "%s" ' \
                  'ORDER BY br.借书时间 DESC' % (self.loginID, bookid)
        else:
            sql = 'SELECT br.书号, b.书名, b.作者, b.出版社, br.借书时间 ' \
                  'FROM borrow br, books b ' \
                  'WHERE br.书号 = b.书号 AND br.ID = "%s" ' \
                  'ORDER BY br.借书时间 DESC' % self.loginID
        cursor.execute(sql)
        results = cursor.fetchall()

        self.return_table.setRowCount(len(results))
        for i, row in enumerate(results):
            for j, val in enumerate(row):
                item = QTableWidgetItem(str(val))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                self.return_table.setItem(i, j, item)

    def fill_return_bookid(self, item):
        row = item.row()
        bookid = self.return_table.item(row, 0).text()
        self.returnbookid.setText(bookid)

    # 提交还书申请
    def ReturnBook(self):
        bookid = self.returnbookid.text().strip()
        if not bookid:
            QMessageBox.warning(self.mainwindow, "警告", "请输入书号或从列表中选择！", QMessageBox.Yes)
            return

        nowtime = time.strftime("%Y-%m-%d", time.localtime())
        sql = 'SELECT * FROM item ' \
              'WHERE ID="%s" AND time="%s" AND type="return" AND bookid="%s"' % (
              self.loginID, nowtime, bookid)
        res = cursor.execute(sql)

        if res:
            QMessageBox.warning(self.mainwindow, "警告", "请勿重复提交！", QMessageBox.Yes)
        else:
            sql = 'INSERT INTO item(bookid, ID, time, type) ' \
                  'VALUES ("%s", "%s", "%s", "return")' % (bookid, self.loginID, nowtime)
            cursor.execute(sql)
            conn.commit()
            QMessageBox.information(self.mainwindow, "提示", "提交成功！", QMessageBox.Yes)
            self.returnquery()

    # 查询所有书籍
    def selectallbook(self):
        sql = 'SELECT * FROM books'
        cursor.execute(sql)
        books = cursor.fetchall()
        booknumber = len(books)
        self.tableWidget.setRowCount(booknumber)
        for i in range(booknumber):
            book = books[i]
            self.tableWidget.setItem(i, 0, QTableWidgetItem(book[0]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(book[1]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(book[2]))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(book[3]))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(book[5]))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(book[6]))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(str(book[7])))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(str(book[8])))
            self.tableWidget.setItem(i, 8, QTableWidgetItem(book[9]))
            self.tableWidget.setItem(i, 9, QTableWidgetItem(str(book[10])))

    # 条件查询书籍
    def selectbook(self):
        bookname = self.bookid.text()
        bookid = self.bookname.text()
        bookauthor = self.author.text()
        booktype = self.type.text()
        bookpress = self.press.text()
        an = 0
        if bookname:
            bookname = ' 书名 LIKE "%%%s%%"' % (bookname)
            an = 1
        if bookid:
            if an == 1:
                bookid = ' and 书号="%s"' % (bookid)
            else:
                bookid = ' 书号="%s"' % (bookid)
                an = 1
        if bookauthor:
            if an == 1:
                bookauthor = 'and 作者="%s"' % (bookauthor)
            else:
                bookauthor = '作者="%s"' % (bookauthor)
                an = 1
        if booktype:
            if an == 1:
                booktype = ' and 类型="%s"' % (booktype)
            else:
                booktype = ' 类型="%s"' % (booktype)
                an = 1
        if bookpress:
            if an == 1:
                bookpress = ' and 出版社="%s"' % (bookpress)
            else:
                bookpress = ' 出版社="%s"' % (bookpress)
        sql1 = 'SELECT * FROM books where'
        sql = sql1 + bookname + bookid + bookauthor + booktype + bookpress
        res = cursor.execute(sql)
        books = cursor.fetchall()
        if res:
            booknumber = len(books)
            self.tableWidget.setRowCount(booknumber)
            for i in range(booknumber):
                book = books[i]
                self.tableWidget.setItem(i, 0, QTableWidgetItem(book[0]))
                self.tableWidget.setItem(i, 1, QTableWidgetItem(book[1]))
                self.tableWidget.setItem(i, 2, QTableWidgetItem(book[2]))
                self.tableWidget.setItem(i, 3, QTableWidgetItem(book[3]))
                self.tableWidget.setItem(i, 4, QTableWidgetItem(book[5]))
                self.tableWidget.setItem(i, 5, QTableWidgetItem(book[6]))
                self.tableWidget.setItem(i, 6, QTableWidgetItem(str(book[7])))
                self.tableWidget.setItem(i, 7, QTableWidgetItem(str(book[8])))
                self.tableWidget.setItem(i, 8, QTableWidgetItem(book[9]))
                self.tableWidget.setItem(i, 9, QTableWidgetItem(str(book[10])))
        else:
            QMessageBox.warning(self.mainwindow, "提示", "没有符合条件的书！", QMessageBox.Yes)

    # 读者修改自己的信息
    def alterinfo(self):
        name = self.lineEdit_8.text()
        sex = self.lineEdit_9.text()
        password = self.lineEdit_11.text()
        if name:
            sql = 'UPDATE readers SET 姓名="%s" ' \
                  'WHERE ID="%s"' % (name, self.loginID)
            print(sql)
            cursor.execute(sql)
            conn.commit()
        if sex == '男' or sex == '女':
            sql = 'UPDATE readers SET 性别="%s" ' \
                  'WHERE ID="%s"' % (sex, self.loginID)
            print(sql)
            cursor.execute(sql)
            conn.commit()
        elif sex != '':
            QMessageBox.warning(self.mainwindow, "警告", "性别输入错误，请输入男/女！", QMessageBox.Yes)
        if password:
            sql = 'UPDATE readers SET password="%s" ' \
                  'WHERE ID="%s"' % (password, self.loginID)
            print(sql)
            cursor.execute(sql)
            conn.commit()
        self.getreaderinfo()

    # 支付欠款（链接支付接口）
    def paymoney(self):
        # 获取当前欠款金额
        sql = 'SELECT 欠款 FROM readers ' \
              'WHERE ID="%s"' % self.loginID
        cursor.execute(sql)
        result = cursor.fetchone()

        if result and float(result[0]) == 0.0:
            QMessageBox.information(self.mainwindow, "提示", "当前无欠款，无需支付。", QMessageBox.Yes)
            return

        # 否则清零并提示成功
        money = 0.00
        sql = 'UPDATE readers SET 欠款="%f" ' \
              'WHERE ID="%s"' % (money, self.loginID)
        cursor.execute(sql)
        conn.commit()
        self.getreaderinfo()

        QMessageBox.information(self.mainwindow, "提示", "支付成功，欠款已清零！", QMessageBox.Yes)

# 调试 UI
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QWidget()
    ui = Ui_Reader()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())