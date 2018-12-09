from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
import sys
import qtawesome
from LogInWiindow import Ui_LogIn

class LeftWidget(QtWidgets.QWidget):
    def __init__(self):
        super(LeftWidget, self).__init__()
        self.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.setLayout(self.left_layout)  # 设置左侧部件布局为网格


        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮

        # self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        # self.left_close.clicked.connect(QCoreApplication.instance().quit)
        self.left_visit.setFixedSize(80, 80)# 设置按钮大小
        self.left_visit.setIcon(QIcon("icon//admin.jpg"))
        self.left_visit.setIconSize(QtCore.QSize(80,80))
        # self.left_visit.setIconSize(QSize=)

        self.ui = Ui_LogIn()#定义一个登陆窗口

        self.left_visit.clicked.connect(self.Show)
        # self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_label_1 = QtWidgets.QPushButton("查询")
        self.left_label_1.setObjectName('left_label')
        self.left_label_1.setIcon(QIcon("icon//search.jpg"))

        # self.left_label_1.clicked.connect(self.ShowSearch)
        self.left_label_2 = QtWidgets.QPushButton("核素管理")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("数据更新")
        self.left_label_3.setObjectName('left_label')
        self.left_label_4 = QtWidgets.QPushButton("关于...")
        self.left_label_4.setObjectName('left_label')

        # self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        # self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_4, 4, 0, 1, 3)


        self.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_label:hover{border-left:4px solid grey;font-weight:900;}

            QWidget#left_widget{
                background:#CDC9C9;

                border-bottom:1px solid white;

                border-left:1px solid white;
                border-bottom-left-radius:10px;
            }
        ''')
        # self.left_close.setStyleSheet(
        #     '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        # self.left_mini.setStyleSheet(
        #     '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')
     # def ShowSearch(main_window):
     #     main_window.main_layout.addWidget(self,2,2, 11, 10)
    def Show(self):
            if(self.ui.log_flag == False):
                self.ui.show()
def main():
    app = QtWidgets.QApplication(sys.argv)
    w =LeftWidget()
    w.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()