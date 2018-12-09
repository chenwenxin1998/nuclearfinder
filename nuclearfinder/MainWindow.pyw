from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication,Qt
from PyQt5.QtGui import QIcon
import sys
import qtawesome
from TopWidget import TopWidget
from LeftWidget import LeftWidget
from SearchWidget import SearchWidget
from ResultWidget import ResultWidget
from nuclearsql import NuclearSql
from motherNuclear import MainWindow
from LogInWiindow import Ui_LogIn
from sss import Result
from untitled import Related
from UPDATE import Update
import re
from SingleNuclear import SingleNuclear
class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NuclearFinder")
        self.setFixedSize(960, 700)#设置主界面大小
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        #self.setWindowOpacity(0.9)  # 设置窗口透明度

        self.setCentralWidget(self.main_widget)
        self.left_window = LeftWidget()#左侧部件
        self.left_window.left_label_2.clicked.connect(self.addAdmin)
        # self.login = Ui_LogIn()#登陆部件
        # self.left_window.left_visit.clicked.connect(self.login.show)#登录按钮连接函数
        self.left_window.setAttribute(QtCore.Qt.WA_StyledBackground)

        self.top_window = TopWidget()#顶部部件
        self.top_window.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.main_layout.addWidget(self.top_window,0,0,1,12)#添加顶部a部件
        self.main_layout.addWidget(self.left_window,2, 0, 11, 2)#添加左侧菜单
        self.top_window.close_button.clicked.connect(self.close)#顶部关闭部件
        self.left_window.left_label_1.clicked.connect(self.search)  # 左侧查询操作按钮
        self.left_window.left_label_4.clicked.connect(self.related) #左侧关于按钮
        self.left_window.left_label_3.clicked.connect(self.addUpdate)#左侧升级按钮
        self._w = "icon//window.png"
        self.w = QtGui.QIcon(self._w)
        self.setWindowIcon(self.w)

        self.main_layout.setSpacing(0)
        self.init_ui()
        self.LogFlag = False

    def init_ui(self):
        self.right_widget = SearchWidget()
        self.right_widget.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.result_window = ResultWidget()
        self.a = Result()
        self.a.setAttribute(QtCore.Qt.WA_StyledBackground)
        # self.setWindowFlags(Qt.FramelessWindowHint|Qt.Tool)
        self.main_layout.addWidget(self.right_widget,2,2, 11, 10)#添加搜索部件
        self.main_layout.setSpacing(0)
        self.right_widget.SearchButton.clicked.connect(self.result)#查询按钮操作

#定义左侧查询按钮槽函数
    def related(self):
        self.right_widget = Related()
        self.right_widget.setAttribute(QtCore.Qt.WA_StyledBackground)
        self.main_layout.addWidget(self.right_widget, 2, 2, 11, 10)
    def addAdmin(self):
        if(self.left_window.ui.log_flag == True):
            self.right_widget = MainWindow()
            self.right_widget.setAttribute(QtCore.Qt.WA_StyledBackground)
            self.main_layout.addWidget(self.right_widget, 2, 2, 11, 10)
        else:
            self.left_window.ui.show()
    def addUpdate(self):
        if (self.left_window.ui.log_flag == True):
            self.right_widget = Update()
            self.right_widget.setAttribute(QtCore.Qt.WA_StyledBackground)
            self.main_layout.addWidget(self.right_widget, 2, 2, 11, 10)
        else:
            self.left_window.ui.show()
    def search(self):
        self.init_ui()


    def result(self):#定义点击查询后执行的函数
        Snuclear = str(self.right_widget.lineEdit.text())
        temp = re.split('(\d+)' , Snuclear)
        print(len(temp))
        db = NuclearSql()
        if len(temp)!=1:
            try:
                if db.Search(temp[0],(temp[1])) == False:
                     pass
                if db.Search(temp[0],(temp[1])) != False:
                     # self.search_widget.close()
                     self.right_widget = Result()
                     self.right_widget.setAttribute(QtCore.Qt.WA_StyledBackground)
                     self.main_layout.addWidget(self.right_widget,2,2,11,10)
                     self.right_widget.setmessage(db.Search(temp[0],(temp[1])))
                    #
                    #  self.right_widget.NuclearName.setText(str(db.Search(temp[0],int(temp[1]))[2]))
                    #  self.right_widget.AtomicMass.setText(str(db.Search(temp[0],int(temp[1]))[0]))
                    #  self.right_widget.proton.setText(str(db.Search(temp[0],int(temp[1]))[1]))
                    #  #self.result_window.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
                    #
                    #  self.right_widget.setStyleSheet("background:#ffffff")
                    # # self.right_widget.NuclearName.clicked.connect()
            except:
                pass
        else:
            self.right_widget = SingleNuclear(temp[0])
            self.right_widget.setAttribute(QtCore.Qt.WA_StyledBackground)
            self.main_layout.addWidget(self.right_widget, 2, 2, 11, 10)

    def closeEvent(self, event):

        reply = QtWidgets.QMessageBox.question(self,
                                               'NuclearFinder',
                                               "是否要退出程序？",
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()