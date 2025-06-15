# 图书管理员界面模块

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from connect import *
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
import time

cursor, conn = connect()

# 图书管理员界面
class Ui_bookadmin(object):

    def setupUi(self, bookadmin):
        self.mainwindow = bookadmin
        bookadmin.setObjectName("bookadmin")
        bookadmin.resize(1200, 900)
        bookadmin.setStyleSheet("background-color: #f0f0f0;")

        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(12)
        bookadmin.setFont(font)

        _translate = QtCore.QCoreApplication.translate
        bookadmin.setWindowTitle(_translate("bookadmin", "图书管理员系统"))

        self.tabWidget = QtWidgets.QTabWidget(bookadmin)
        self.tabWidget.setGeometry(QtCore.QRect(30, 30, 1140, 840))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.setStyleSheet("""
            QTabWidget::pane {
                border: 1px solid #ccc;
                background-color: #ffffff;
            }
            QTabBar::tab {
                background-color: #e0e0e0;
                padding: 5px 10px;
                border: 1px solid #ccc;
                border-bottom: none;
            }
            QTabBar::tab:selected {
                background-color: #ffffff;
            }
        """)

        # ===== Tab 1: 查询读者信息 =====
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(15)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(15)
        self.label_2 = QtWidgets.QLabel(_translate("bookadmin", "读者ID"), self.tab)
        self.label_2.setStyleSheet("font-size: 12pt;")
        self.horizontalLayout.addWidget(self.label_2)
        self.readerid = QtWidgets.QLineEdit(self.tab)
        self.readerid.setMinimumHeight(30)
        self.readerid.setStyleSheet("font-size: 12pt;")
        self.horizontalLayout.addWidget(self.readerid)

        self.label = QtWidgets.QLabel(_translate("bookadmin", "姓名"), self.tab)
        self.label.setStyleSheet("font-size: 12pt;")
        self.horizontalLayout.addWidget(self.label)
        self.readername = QtWidgets.QLineEdit(self.tab)
        self.readername.setMinimumHeight(30)
        self.readername.setStyleSheet("font-size: 12pt;")
        self.horizontalLayout.addWidget(self.readername)

        self.label_3 = QtWidgets.QLabel(_translate("bookadmin", "单位"), self.tab)
        self.label_3.setStyleSheet("font-size: 12pt;")
        self.horizontalLayout.addWidget(self.label_3)
        self.unit = QtWidgets.QLineEdit(self.tab)
        self.unit.setMinimumHeight(30)
        self.unit.setStyleSheet("font-size: 12pt;")
        self.horizontalLayout.addWidget(self.unit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(20)
        self.select = QtWidgets.QPushButton(_translate("bookadmin", "查询"), self.tab)
        self.select.setMinimumHeight(35)
        self.select.setMinimumWidth(100)
        self.select.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 5px 10px;
                border: none;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.horizontalLayout_2.addWidget(self.select)

        self.selectall = QtWidgets.QPushButton(_translate("bookadmin", "显示所有"), self.tab)
        self.selectall.setMinimumHeight(35)
        self.selectall.setMinimumWidth(100)
        self.selectall.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 5px 10px;
                border: none;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.horizontalLayout_2.addWidget(self.selectall)
        self.refreshreader = QtWidgets.QPushButton("刷新", self.tab)
        self.refreshreader.setMinimumHeight(35)
        self.refreshreader.setMinimumWidth(100)
        self.refreshreader.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                padding: 5px 10px;
                border: none;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        self.horizontalLayout_2.addWidget(self.refreshreader)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.readerinfors = QtWidgets.QTableWidget(self.tab)
        self.readerinfors.setMinimumHeight(500)
        self.readerinfors.setColumnCount(8)
        self.readerinfors.setRowCount(0)
        headers = ["读者ID", "姓名", "性别", "单位", "读者类型", "可借册数", "在借册数", "欠款"]
        for i, header in enumerate(headers):
            item = QtWidgets.QTableWidgetItem(_translate("bookadmin", header))
            self.readerinfors.setHorizontalHeaderItem(i, item)
        self.readerinfors.setStyleSheet("""
            QTableWidget {
                border: 1px solid #ccc;
                background-color: #ffffff;
            }
            QHeaderView::section {
                background-color: #e0e0e0;
                padding: 5px;
                border: 1px solid #ccc;
            }
            QTableWidget::item:alternate {
                background-color: #f9f9f9;
            }
        """)
        self.verticalLayout.addWidget(self.readerinfors)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.tabWidget.addTab(self.tab, _translate("bookadmin", "查询读者信息"))

        # ===== Tab 2: 管理书籍信息 =====
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_books = QtWidgets.QVBoxLayout()
        self.verticalLayout_books.setSpacing(15)

        # 输入区域：书籍属性字段（书号、书名、作者、类型）
        input_fields = [
            ("书号", "bookid"),
            ("书名", "bookname"),
            ("作者", "author"),
            ("类型", "type")
        ]
        row1 = QtWidgets.QHBoxLayout()
        for label_text, obj_name in input_fields:
            label = QtWidgets.QLabel(_translate("bookadmin", label_text), self.tab_2)
            label.setStyleSheet("font-size: 11pt;")
            row1.addWidget(label)
            line_edit = QtWidgets.QLineEdit(self.tab_2)
            line_edit.setObjectName(obj_name)
            line_edit.setMinimumHeight(30)
            line_edit.setStyleSheet("font-size: 11pt;")
            setattr(self, obj_name, line_edit)
            row1.addWidget(line_edit)
        self.verticalLayout_books.addLayout(row1)

        # 输入区域：价格、出版社、馆藏册数、在馆册数
        input_fields2 = [
            ("价格", "prize"),
            ("出版社", "press"),
            ("馆藏册数", "num"),
            ("在馆册数", "totalnum")
        ]
        row2 = QtWidgets.QHBoxLayout()
        for label_text, obj_name in input_fields2:
            label = QtWidgets.QLabel(_translate("bookadmin", label_text), self.tab_2)
            label.setStyleSheet("font-size: 11pt;")
            row2.addWidget(label)
            line_edit = QtWidgets.QLineEdit(self.tab_2)
            line_edit.setObjectName(obj_name)
            line_edit.setMinimumHeight(30)
            line_edit.setStyleSheet("font-size: 11pt;")
            setattr(self, obj_name, line_edit)
            row2.addWidget(line_edit)
        self.verticalLayout_books.addLayout(row2)

        # 输入区域：摘要、书架号
        row3 = QtWidgets.QHBoxLayout()
        for label_text, obj_name in [("摘要", "abstract_2"), ("书架号", "bookshelf")]:
            label = QtWidgets.QLabel(_translate("bookadmin", label_text), self.tab_2)
            label.setStyleSheet("font-size: 11pt;")
            row3.addWidget(label)
            line_edit = QtWidgets.QLineEdit(self.tab_2)
            line_edit.setObjectName(obj_name)
            line_edit.setMinimumHeight(30)
            line_edit.setStyleSheet("font-size: 11pt;")
            setattr(self, obj_name, line_edit)
            row3.addWidget(line_edit)
        self.verticalLayout_books.addLayout(row3)

        # 按钮区域：添加、删除、修改书籍
        btn_layout = QtWidgets.QHBoxLayout()
        self.addbook = QtWidgets.QPushButton(_translate("bookadmin", "添加"), self.tab_2)
        self.deletebook = QtWidgets.QPushButton(_translate("bookadmin", "删除"), self.tab_2)
        self.alterbook = QtWidgets.QPushButton(_translate("bookadmin", "修改"), self.tab_2)
        self.refreshbook = QtWidgets.QPushButton("刷新", self.tab_2)
        self.refreshbook.setMinimumHeight(35)
        self.refreshbook.setMinimumWidth(100)
        self.refreshbook.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                padding: 5px 10px;
                border: none;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        btn_layout.addWidget(self.refreshbook)
        for btn in [self.addbook, self.deletebook, self.alterbook]:
            btn.setMinimumHeight(35)
            btn.setMinimumWidth(100)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #4CAF50;
                    color: white;
                    padding: 5px 10px;
                    border: none;
                    border-radius: 3px;
                }
                QPushButton:hover {
                    background-color: #45a049;
                }
            """)
            btn_layout.addWidget(btn)
        self.verticalLayout_books.addLayout(btn_layout)

        # 表格区域：显示书籍信息
        self.bookinfos = QtWidgets.QTableWidget(self.tab_2)
        self.bookinfos.setMinimumHeight(400)
        self.bookinfos.setColumnCount(11)
        self.bookinfos.setRowCount(0)
        book_headers = [
            "书号", "书名", "作者", "类型", "价格", "出版社", "摘要",
            "馆藏册数", "在馆册数", "书架号", "被借次数"
        ]
        for i, header in enumerate(book_headers):
            item = QtWidgets.QTableWidgetItem(_translate("bookadmin", header))
            self.bookinfos.setHorizontalHeaderItem(i, item)
        self.bookinfos.setStyleSheet("""
            QTableWidget {
                border: 1px solid #ccc;
                background-color: #ffffff;
            }
            QHeaderView::section {
                background-color: #e0e0e0;
                padding: 5px;
                border: 1px solid #ccc;
            }
            QTableWidget::item:alternate {
                background-color: #f9f9f9;
            }
        """)
        self.verticalLayout_books.addWidget(self.bookinfos)

        self.verticalLayout_5.addLayout(self.verticalLayout_books)
        self.tabWidget.addTab(self.tab_2, _translate("bookadmin", "管理书籍信息"))

        # ===== Tab 3: 借阅/归还审批 =====
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")

        # 借阅/归还申请表格
        self.iteminfo = QtWidgets.QTableWidget(self.tab_3)
        self.iteminfo.setGeometry(QtCore.QRect(50, 30, 900, 750))
        self.iteminfo.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.iteminfo.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.iteminfo.setObjectName("iteminfo")
        self.iteminfo.setColumnCount(4)
        self.iteminfo.setRowCount(0)
        item_headers = ["读者ID", "书号", "借/还", "时间"]
        for i, header in enumerate(item_headers):
            item = QtWidgets.QTableWidgetItem(_translate("bookadmin", header))
            self.iteminfo.setHorizontalHeaderItem(i, item)
        self.iteminfo.setStyleSheet("""
            QTableWidget {
                border: 1px solid #ccc;
                background-color: #ffffff;
            }
            QHeaderView::section {
                background-color: #e0e0e0;
                padding: 5px;
                border: 1px solid #ccc;
            }
            QTableWidget::item:alternate {
                background-color: #f9f9f9;
            }
        """)

        # 操作按钮布局（批准/驳回/刷新）
        self.layoutWidget = QtWidgets.QWidget(self.tab_3)
        self.layoutWidget.setGeometry(QtCore.QRect(980, 250, 120, 300))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)

        self.yes = QtWidgets.QPushButton(_translate("bookadmin", "批准"), self.layoutWidget)
        self.yes.setMinimumHeight(40)
        self.yes.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                padding: 5px 10px;
                border: none;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)
        self.verticalLayout_4.addWidget(self.yes)

        self.no = QtWidgets.QPushButton(_translate("bookadmin", "驳回"), self.layoutWidget)
        self.no.setMinimumHeight(40)
        self.no.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                padding: 5px 10px;
                border: none;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)
        self.verticalLayout_4.addWidget(self.no)

        self.refresh = QtWidgets.QPushButton(_translate("bookadmin", "刷新"), self.layoutWidget)
        self.refresh.setMinimumHeight(40)
        self.refresh.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                padding: 5px 10px;
                border: none;
                border-radius: 3px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        self.verticalLayout_4.addWidget(self.refresh)

        self.tabWidget.addTab(self.tab_3, _translate("bookadmin", "借阅/归还审批"))

        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(bookadmin)

        self.readerinfors.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.readerinfors.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.readerinfors.clicked.connect(self.display_readerinfo)
        self.refreshreader.clicked.connect(self.show_all_readers)

        self.bookinfos.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.bookinfos.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.bookinfos.clicked.connect(self.displayinfo)

        self.iteminfo.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.iteminfo.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

        self.selectall.clicked.connect(self.show_all_readers)
        self.show_all_books()
        self.select.clicked.connect(self.readerselect)
        self.addbook.clicked.connect(self.add_book)
        self.deletebook.clicked.connect(self.drop_book)
        self.alterbook.clicked.connect(self.update_book)
        self.refreshbook.clicked.connect(self.show_all_books)
        self.yes.clicked.connect(self.pizhun)
        self.no.clicked.connect(self.bohui)
        self.refresh.clicked.connect(self.show_all_items)
        self.show_all_items()

    # 图书管理员功能
    # 一、读者管理功能
    # 显示所有的读者
    def show_all_readers(self):
        sql = "SELECT * FROM readers"
        res = cursor.execute(sql)
        readerinfo = cursor.fetchall()
        self.readerinfors.setRowCount(res)
        for i in range(res):
            reader = readerinfo[i]
            readerid = QTableWidgetItem(reader[0])
            readername = QTableWidgetItem(reader[1])
            readersex = QTableWidgetItem(reader[2])
            readerunit = QTableWidgetItem(reader[3])
            readertype = QTableWidgetItem(reader[4])
            books_can_borrow = QTableWidgetItem(str(reader[5]))
            books_borrowed = QTableWidgetItem(str(reader[6]))
            charge_to_pay = QTableWidgetItem(str(reader[8]))

            self.readerinfors.setItem(i, 0, readerid)
            self.readerinfors.setItem(i, 1, readername)
            self.readerinfors.setItem(i, 2, readersex)
            self.readerinfors.setItem(i, 3, readerunit)
            self.readerinfors.setItem(i, 4, readertype)
            self.readerinfors.setItem(i, 5, books_can_borrow)
            self.readerinfors.setItem(i, 6, books_borrowed)
            self.readerinfors.setItem(i, 7, charge_to_pay)

    # 显示读者信息
    def display_readerinfo(self):
        row = self.readerinfors.currentRow()
        self.readerid.setText(self.readerinfors.item(row, 0).text())
        self.readername.setText(self.readerinfors.item(row, 1).text())
        self.unit.setText(self.readerinfors.item(row, 3).text())

    # 选择读者
    def readerselect(self):
        readerid = self.readerid.text()
        readername = self.readername.text()
        readerunit = self.unit.text()
        abc = 0
        if readerid:
            readerid = 'ID="%s"' % (readerid)
            abc = 1
        if readername:
            if abc == 1:
                readername = 'and 姓名="%s"' % (readername)
            else:
                readername = '姓名="%s"' % (readername)
                abc = 1
        if readerunit:
            if abc == 1:
                readerunit = 'and 单位="%s"' % (readerunit)
            else:
                readerunit = '单位="%s"' % (readerunit)
        sql0 = 'SELECT * FROM readers WHERE '
        sql1 = readerid + readername + readerunit
        sql = sql0 + sql1
        if sql1:
            res = cursor.execute(sql)
            if res:
                readerinfo = cursor.fetchall()  # 返回一堆元组组成的元组
                self.readerinfors.setRowCount(res)
                for i in range(res):
                    reader = readerinfo[i]
                    readerid = QTableWidgetItem(reader[0])
                    readername = QTableWidgetItem(reader[1])
                    readersex = QTableWidgetItem(reader[2])
                    readerunit = QTableWidgetItem(reader[3])
                    readertype = QTableWidgetItem(reader[4])
                    books_can_borrow = QTableWidgetItem(str(reader[5]))
                    books_borrowed = QTableWidgetItem(str(reader[6]))
                    charge_to_pay = QTableWidgetItem(str(reader[8]))
                    self.readerinfors.setItem(i, 0, readerid)
                    self.readerinfors.setItem(i, 1, readername)
                    self.readerinfors.setItem(i, 2, readersex)
                    self.readerinfors.setItem(i, 3, readerunit)
                    self.readerinfors.setItem(i, 4, readertype)
                    self.readerinfors.setItem(i, 5, books_can_borrow)
                    self.readerinfors.setItem(i, 6, books_borrowed)
                    self.readerinfors.setItem(i, 7, charge_to_pay)
            else:
                QMessageBox.warning(self.mainwindow, "警告", "没有符合条件的读者！", QMessageBox.Yes)
        else:
            QMessageBox.warning(self.mainwindow, "警告", "至少输入一项读者信息！", QMessageBox.Yes)

    # 二、书籍管理界面功能
    # 显示所有图书信息
    def show_all_books(self):
        sql = 'SELECT * FROM books'
        res = cursor.execute(sql)
        books = cursor.fetchall()
        self.bookinfos.setRowCount(res)
        for i in range(res):
            book = books[i]
            self.bookinfos.setItem(i, 0, QTableWidgetItem(book[0]))
            self.bookinfos.setItem(i, 1, QTableWidgetItem(book[1]))
            self.bookinfos.setItem(i, 2, QTableWidgetItem(book[2]))
            self.bookinfos.setItem(i, 3, QTableWidgetItem(book[3]))
            self.bookinfos.setItem(i, 4, QTableWidgetItem(str(book[4])))
            self.bookinfos.setItem(i, 5, QTableWidgetItem(book[5]))
            self.bookinfos.setItem(i, 6, QTableWidgetItem(book[6]))
            self.bookinfos.setItem(i, 7, QTableWidgetItem(str(book[7])))
            self.bookinfos.setItem(i, 8, QTableWidgetItem(str(book[8])))
            self.bookinfos.setItem(i, 9, QTableWidgetItem(book[9]))
            self.bookinfos.setItem(i, 10, QTableWidgetItem(str(book[10])))

    # 添加图书
    def add_book(self):
        bookid = self.bookid.text()
        bookname = self.bookname.text()
        author = self.author.text()
        booktype = self.type.text()
        prize1 = self.prize.text()
        press = self.press.text()

        abstract_2 = self.abstract_2.text()
        bookshelf = self.bookshelf.text()
        try:
            totalnum = int(self.totalnum.text())
            num = int(self.num.text())
            if prize1 != '':
                prize = float(prize1)
                if bookid and bookname and author and booktype and prize and press and totalnum and num and abstract_2 and bookshelf:
                    sql = 'INSERT INTO ' \
                          'books(书号,书名,作者,类型,价格,出版社,摘要,馆藏册数,在馆册数,书架号,被借次数) ' \
                          'VALUES ("%s","%s","%s","%s","%.2f","%s","%s","%d","%d","%s","%d")' % (
                    bookid, bookname, author, booktype, prize, press, abstract_2, num, totalnum, bookshelf, 0)
                    cursor.execute(sql)
                    conn.commit()
                    self.show_all_books()
                else:
                    QMessageBox.warning(self.mainwindow, "警告", "请补全书目信息！", QMessageBox.Yes)
            else:
                QMessageBox.warning(self.mainwindow, "警告", "请补全书目信息！", QMessageBox.Yes)
        except (pymysql.err.IntegrityError, ValueError):
            QMessageBox.warning(self.mainwindow, "警告", "书目信息错误！", QMessageBox.Yes)

    # 删除图书
    def drop_book(self):
        row = self.bookinfos.currentRow()
        if row < 0:
            QMessageBox.warning(self.mainwindow, "提示", "请先选择要删除的图书", QMessageBox.Yes)
            return

        bookid = self.bookinfos.item(row, 0).text()

        # 检查外键依赖项
        cursor.execute("SELECT COUNT(*) FROM item "
                       "WHERE bookid=%s", (bookid,))
        item_count = cursor.fetchone()[0]
        cursor.execute("SELECT COUNT(*) FROM borrow "
                       "WHERE 书号=%s", (bookid,))
        borrow_count = cursor.fetchone()[0]

        if item_count > 0 or borrow_count > 0:
            msg = "无法删除，书号为 [%s] 的图书在以下表中仍有关联记录：\n" % bookid
            if item_count > 0:
                msg += " - item 表中存在 %d 条借阅/还书申请记录\n" % item_count
            if borrow_count > 0:
                msg += " - borrow 表中存在 %d 条借书记录\n" % borrow_count
            QMessageBox.warning(self.mainwindow, "删除失败", msg, QMessageBox.Yes)
            return

        try:
            cursor.execute("DELETE FROM books "
                           "WHERE 书号=%s", (bookid,))
            conn.commit()
            self.show_all_books()
            QMessageBox.information(self.mainwindow, "成功", "图书 [%s] 删除成功！" % bookid, QMessageBox.Yes)
        except Exception as e:
            conn.rollback()
            QMessageBox.warning(self.mainwindow, "错误", "数据库错误：" + str(e), QMessageBox.Yes)

    # 显示修改后的图书信息
    def displayinfo(self):
        s = self.bookinfos.currentRow()
        self.bookid.setText(self.bookinfos.item(s, 0).text())
        self.bookname.setText(self.bookinfos.item(s, 1).text())
        self.author.setText(self.bookinfos.item(s, 2).text())
        self.type.setText(self.bookinfos.item(s, 3).text())
        self.prize.setText(self.bookinfos.item(s, 4).text())
        self.press.setText(self.bookinfos.item(s, 5).text())
        self.abstract_2.setText(self.bookinfos.item(s, 6).text())
        self.num.setText(self.bookinfos.item(s, 7).text())
        self.totalnum.setText(self.bookinfos.item(s, 8).text())
        self.bookshelf.setText(self.bookinfos.item(s, 9).text())

    # 修改图书
    def update_book(self):
        bookid = self.bookid.text()
        bookname = self.bookname.text()
        author = self.author.text()
        booktype = self.type.text()
        prize1 = self.prize.text()
        press = self.press.text()

        abstract_2 = self.abstract_2.text()
        bookshelf = self.bookshelf.text()
        try:
            totalnum = int(self.totalnum.text())
            num = int(self.num.text())
            if prize1 != '':
                prize = float(prize1)
                if bookid and bookname and author and booktype and prize and press and totalnum and num and abstract_2 and bookshelf:
                    sql = 'UPDATE books ' \
                          'SET 书号="%s",书名="%s",作者="%s",类型="%s",价格="%.2f",出版社="%s",' \
                          '摘要="%s",馆藏册数="%d",在馆册数="%d",书架号="%s",被借次数="%d" ' \
                          'WHERE 书号="%s"' % (
                    bookid, bookname, author, booktype, prize, press, abstract_2, num, totalnum, bookshelf, 0, bookid)
                    cursor.execute(sql)
                    conn.commit()
                    self.show_all_books()
                else:
                    QMessageBox.warning(self.mainwindow, "警告", "请补全书目信息！", QMessageBox.Yes)
            else:
                QMessageBox.warning(self.mainwindow, "警告", "请补全书目信息！", QMessageBox.Yes)
        except (pymysql.err.IntegrityError, ValueError):
            QMessageBox.warning(self.mainwindow, "警告", "书目信息错误！", QMessageBox.Yes)

    # 三、借阅归还审批功能
    # 显示所有待审批信息
    def show_all_items(self):
        sql = 'SELECT * FROM item'
        res = cursor.execute(sql)
        items = cursor.fetchall()
        self.iteminfo.setRowCount(res)
        for i in range(res):
            item = items[i]
            self.iteminfo.setItem(i, 1, QTableWidgetItem(item[0]))
            self.iteminfo.setItem(i, 0, QTableWidgetItem(item[1]))
            self.iteminfo.setItem(i, 3, QTableWidgetItem(str(item[2])))
            self.iteminfo.setItem(i, 2, QTableWidgetItem(item[3]))

    # 批准借阅请求
    def pizhun(self):
        s = self.iteminfo.currentRow()
        if s < 0:
            QMessageBox.warning(self.mainwindow, "提示", "请先选择一项申请", QMessageBox.Yes)
            return

        readerid = self.iteminfo.item(s, 0).text()
        bookid = self.iteminfo.item(s, 1).text()
        selecttype = self.iteminfo.item(s, 2).text()
        itemtime_str = self.iteminfo.item(s, 3).text()

        if selecttype == 'return':
            # 检查是否逾期，若逾期则计算欠款
            sql = 'SELECT 借书时间 FROM borrow ' \
                  'WHERE ID=%s AND 书号=%s'
            cursor.execute(sql, (readerid, bookid))
            result = cursor.fetchone()
            if result:
                borrow_date = time.strptime(str(result[0]), "%Y-%m-%d")
                return_date = time.strptime(str(itemtime_str), "%Y-%m-%d")
                days = (time.mktime(return_date) - time.mktime(borrow_date)) // (60 * 60 * 24)

                cursor.execute('SELECT 读者类型 FROM readers '
                               'WHERE ID=%s', (readerid,))
                rtype = cursor.fetchone()[0]
                limits = {'研究生': 60, '本科生': 30, '教师': 90}
                allowed = limits.get(rtype, 30)
                overdue = int(days - allowed)

                if overdue > 0:
                    cursor.execute('UPDATE readers '
                                   'SET 欠款 = 欠款 + %s '
                                   'WHERE ID=%s', (overdue, readerid))
                    conn.commit()
                    QMessageBox.warning(self.mainwindow, "注意", f"超期 {overdue} 天，已计入欠款", QMessageBox.Yes)
                else:
                    QMessageBox.information(self.mainwindow, "提示", "还书成功！", QMessageBox.Yes)

        # 统一删除申请记录（触发器自动处理）
        cursor.execute("DELETE FROM item "
                       "WHERE bookid=%s AND ID=%s AND time=%s AND type=%s",
                       (bookid, readerid, itemtime_str, selecttype))
        conn.commit()
        self.show_all_items()

    # 驳回借阅请求
    def bohui(self):
        s = self.iteminfo.currentRow()
        bookid = self.iteminfo.item(s, 1).text()
        sql = 'DELETE FROM item ' \
              'WHERE bookid="%s"' % (bookid)
        cursor.execute(sql)
        conn.commit()

# 调试 UI
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QWidget()
    ui = Ui_bookadmin()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())