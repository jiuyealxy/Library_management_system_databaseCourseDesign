# 登录界面设计模块

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

# 登录界面设计
class Ui_Login(object):
    def setupUi(self, Login):
        Login.setStyleSheet("""
            QWidget {
                font-family: '微软雅黑';
                font-size: 12pt;
                background-color: #f4f4f4;
            }
            QLabel {
                color: #333333;
            }
            QLineEdit, QComboBox {
                padding: 4px;
                border: 1px solid #ccc;
                border-radius: 4px;
                background-color: #ffffff;
            }
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                border-radius: 5px;
                padding: 6px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
        """)

        # ===== 标题标签 =====
        Login.setObjectName("Login")
        Login.setWindowModality(QtCore.Qt.ApplicationModal)
        Login.resize(800, 494)
        self.label = QtWidgets.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(325, 20, 150, 80))
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName("label")

        # ===== 用户 ID 、密码、身份标签 =====
        self.user = QtWidgets.QLabel(Login)
        self.user.setGeometry(QtCore.QRect(215, 90, 80, 61))
        self.user.setObjectName("user")
        self.password = QtWidgets.QLabel(Login)
        self.password.setGeometry(QtCore.QRect(225, 155, 80, 61))
        self.password.setObjectName("password")
        self.identify = QtWidgets.QLabel(Login)
        self.identify.setGeometry(QtCore.QRect(200, 220, 110, 59))
        self.identify.setObjectName("identify")

        # ===== 用户输入框 =====
        self.userline = QtWidgets.QLineEdit(Login)
        self.userline.setGeometry(QtCore.QRect(320, 105, 230, 41))
        self.userline.setObjectName("userline")
        self.pwline = QtWidgets.QLineEdit(Login)
        self.pwline.setGeometry(QtCore.QRect(320, 165, 230, 41))
        self.pwline.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pwline.setObjectName("pwline")
        self.idbox = QtWidgets.QComboBox(Login)
        self.idbox.setGeometry(QtCore.QRect(350, 230, 170, 41))
        self.idbox.setObjectName("idbox")
        self.idbox.addItem("")
        self.idbox.addItem("")
        self.idbox.addItem("")

        # ===== 按钮 =====
        self.loginbt = QtWidgets.QPushButton(Login)
        self.loginbt.setGeometry(QtCore.QRect(280, 320, 93, 40))
        self.loginbt.setObjectName("loginbt")
        self.exitbt = QtWidgets.QPushButton(Login)
        self.exitbt.setGeometry(QtCore.QRect(450, 320, 93, 40))
        self.exitbt.setObjectName("exitbt")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "图书馆管理系统"))

        self.label.setText("用户登录")
        self.label.setFont(QtGui.QFont("微软雅黑", 25, QtGui.QFont.Bold))

        self.user.setText("用户ID：")
        self.user.setFont(QtGui.QFont("微软雅黑", 12))

        self.password.setText("密码：")
        self.password.setFont(QtGui.QFont("微软雅黑", 12))

        self.identify.setText("身份类型：")
        self.identify.setFont(QtGui.QFont("微软雅黑", 12))

        # 设置下拉框选项
        self.idbox.setItemText(0, _translate("Login", "读者"))
        self.idbox.setItemText(1, _translate("Login", "图书管理员"))
        self.idbox.setItemText(2, _translate("Login", "系统管理员"))

        self.loginbt.setText(_translate("Login", "登录"))
        self.exitbt.setText(_translate("Login", "退出"))

# 调试 UI
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    LoginWindow = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(LoginWindow)
    LoginWindow.show()
    sys.exit(app.exec_())