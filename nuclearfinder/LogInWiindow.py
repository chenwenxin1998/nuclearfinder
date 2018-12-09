# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LogInWiindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from UserAcount import UserAcount
class Ui_LogIn(QtWidgets.QWidget):


    def __init__(self):
        super(Ui_LogIn, self).__init__()
        self.log_flag = False
        self.setObjectName("LogIn")
        self.resize(345, 600)
        self.setMaximumHeight(600)
        self.setMinimumHeight(600)
        self.setMaximumWidth(345)
        self.setMinimumWidth(345)
        self.setStyleSheet("border-radius:10px;background-color:#6e6e6e;border: 0px solid #255,0,0;")
        self._w = "window.png"
        self.w = QtGui.QIcon(self._w)
        self.setWindowIcon(self.w)

        self.imagelPath = "icon.png"
        self.image = QtGui.QImage(self.imagelPath)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(60, 80, 221, 211))
        self.label.setObjectName("label")
        self.label.setPixmap(QtGui.QPixmap.fromImage(self.image))
        self.label.setScaledContents(True)

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(70, 380, 211, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("username")
        self.lineEdit.setStyleSheet("background-color:#ffffff;color:6e6e6e;font-size:15px;border-radius:10px;")

        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 460, 211, 41))
        self.lineEdit_2.setPlaceholderText("password")

        self.lineEdit_2.setStyleSheet("background-color:#ffffff;border-radius:10px;")
        self.lineEdit_2.setObjectName("lineEdit")
        self.lineEdit_2.setEchoMode(self.lineEdit_2.Password)

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(70, 540, 211, 41))
        self.pushButton.setStyleSheet("color:#000000;font: 14pt \"黑体\";background-color:#4e4e4e;color:white;border-radius:10px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.userLog)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("LogIn", "登录"))
        self.label.setText(_translate("LogIn", ""))
        self.lineEdit.setText(_translate("LogIn", ""))
        self.lineEdit_2.setText(_translate("LogIn", ""))
        self.pushButton.setText(_translate("LogIn", "Log In"))

        # QtCore.QMetaObject.connectSlotsByName(self)
    def userLog(self):
        if(self.log_flag==False):
            username = self.lineEdit.text()
            password = self.lineEdit_2.text()
            username = str(username)
            print(username)
            password = str(password)
            print(password)
            user_acount = UserAcount()
            if user_acount.Judge(username,password):
                self.log_flag = True
                self.hide()
                return True

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_LogIn()
    ui.show()
    sys.exit(app.exec_())
