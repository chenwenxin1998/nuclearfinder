from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
import sys
class SearchWidget(QtWidgets.QWidget):
    def __init__(self):
        super(SearchWidget, self).__init__()

        self.setObjectName("SearchWidget")
        #建立一个查询按钮
        self.SearchButton = QtWidgets.QPushButton(self)
        self.SearchButton.setGeometry(QtCore.QRect(300, 250, 90, 50))
        self.SearchButton.setObjectName("SearchButton")
        self.SearchButton.setText("查询")
        self.SearchButton.setStyleSheet('''
            QPushButton{
                border-radius:10px;
                background:grey;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                color:white;
            }
            QPushButton:hover{background:#CDC9C9;}
            ''')
        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(170, 170, 371, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("输入你要查找的元素或者核素")
        self.lineEdit.setStyleSheet('''
        QLineEdit{
                border:1px solid gray;
                width:300px;
                border-radius:10px;
                padding:2px 4px;
        }
        ''')
        self.setStyleSheet("background:#FFFFFF;border:1px solid darkgray;border-bottom-right-radius:10px;")
        # self.source = QtWidgets.QLabel(self)
        # self.label = QtWidgets.QLabel(self)
        # self.label.setGeometry(QtCore.QRect(500, 400, 100, 15))
        # self.label.setText("DATA FROM")
        # self.source.setGeometry(QtCore.QRect(600, 400, 80, 80))
        # self.imagelPath = "icon\\nndcblue.gif"
        # self.image = QtGui.QImage(self.imagelPath)
        # self.source.setPixmap(QtGui.QPixmap.fromImage(self.image))
        # self.source.setScaledContents(True)
        # self.label.setStyleSheet("""
        #     border:0px;
        #     border-radius:0px;
        # """)