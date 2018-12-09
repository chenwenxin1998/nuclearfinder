# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from WebView import WebView
from WebView2 import WebView2
class Related(QtWidgets.QWidget):
    def __init__(self):
        super(Related, self).__init__()
        self.setObjectName("Form")
        self.resize(739, 711)
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(270, 440, 321, 28))
        self.pushButton.setStyleSheet("font: 10pt \"Bauhaus 93\";background:blue;color:#ffffff;border:0px;hover:{background:yellow};")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(170, 440, 95, 28))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(80, 60, 201, 71))
        self.label_2.setStyleSheet("background:pink;color:#ffffff;"
                                   "\n"
        "font: 28pt \"华文彩云\";\n"
        "")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(170, 510, 95, 28))
        self.label_3.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 510, 321, 28))
        self.pushButton_2.setStyleSheet("font: 10pt \"Bauhaus 93\";background:blue;color:#ffffff;border:0px;hover:{background:yellow};")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(270, 300, 91, 91))
        self.label_4.setObjectName("label_4")
        self.label_8= QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(370, 300, 91, 91))
        self.label_8.setStyleSheet("background:url(icon/zhwiki.png)")

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(190, 190, 311, 28))
        self.label_5.setStyleSheet("font: 11pt \"Copperplate Gothic Bold\";")

        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(190, 250, 191, 28))
        self.label_6.setObjectName("label_6")
        self.label_6.setStyleSheet("font: 11pt \"Copperplate Gothic Bold\";")
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle("Form")
        self.pushButton.setText(_translate("Form", "https://chenwx.cn"))
        self.label.setText( "ChenWenxin")
        self.label.setStyleSheet("font: 10pt \"Bauhaus 93\";background:blue;color:#ffffff;border:0px;")
        self.label_2.setText("数据来源")
        # self.label_2.setStyleSheet("background:pink")
        self.label_3.setText("LiuZongwen")
        self.label_3.setStyleSheet("font: 10pt \"Bauhaus 93\";background:blue;color:#ffffff;border:0px;hover:{background:yellow};")
        self.pushButton_2.setText("https://arthurdax.github.io")
        # self.pushButton_2.setStyleSheet("background:blue;")
        # self.pushButton_2.setStyleSheet()
        # self.label_4.setText("TextLabel")
        self.label_4.setStyleSheet("background:url(icon/nndcblue.gif)")
        self.label_5.setText("https://www.nndc.bnl.gov/")
        self.label_6.setText("https://zh.wikipedia.org/")
        # self.web = WebView()
        self.pushButton_2.clicked.connect(self.Show2)
        self.pushButton.clicked.connect(self.Show)
        self.setStyleSheet("background:#E6E6FA;")
    def Show(self):
        self.web = WebView()
        self.web.show()
    def Show2(self):
        self.web = WebView2()
        self.web.show()
if __name__ =="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Related()
    ui.show()
    sys.exit(app.exec_())