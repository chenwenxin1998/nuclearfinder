from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication,Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from nuclearsql import NuclearSql
from ResultWidget import ResultWidget
from sss import Result
from get_class import DATA
import sys
from basicNuclear import Ui_Form
import json
import threading
import time


def _update(TempArray,listwidget):  # 更新函数

    for i in range(1, 3):
        temp = []
        data = (DATA(i).data)
        a = data["Atomic name"]
        temp1 = a.split()[2]
        temp.append(temp1 + str(data["Atomic number"]))
        TempArray.append(data)
        listwidget.addItems(temp)
        with open("data//basicnuclear.json", "w", newline='', encoding='utf-8') as f_obj:
            json.dump(data, f_obj)
            print(data)

class UpThread(threading.Thread):
    def __init__(self,TempArray,listwidget):
        super(UpThread, self).__init__()
        self.TempArray = TempArray
        self.listwidget = listwidget
    def run(self):
        try:
            for i in range(1, 2):
                self.temp = []
                data = (DATA(i).data)
                a = data["Atomic name"]
                temp1 = a.split()[2]
                self.temp.append(temp1 + str(data["Atomic number"]))
                self.TempArray.append(data)
                self.listwidget.addItems(self.temp)
            print(TempArray)
            with open("data//basicnuclear.json", "w", newline='', encoding='utf-8') as f_obj:
                json.dump(self.TempArray, f_obj)
            time.sleep(1)

        except:  # 网络异常时弹出提示框提示网络异常。
            reply = QtWidgets.QMessageBox.question(self,
                                                   'NuclearFinder',
                                                   "网络不稳定请等会再试！",
                                                   QtWidgets.QMessageBox.Yes)
            if reply == QtWidgets.QMessageBox.Yes:
                pass
            else:
                pass


class Update(QMainWindow):
    def __init__(self):
        super(Update, self).__init__()
        # db = NuclearSql()
        # 设置大小
        # self.setMaximumWidth(800)
        # self.setMinimumWidth(800)
        # self.setMinimumHeight(700)
        # self.setMaximumHeight(700)
        self.TempArray = []#暂时储存更新信息的数组
        self.dock1 = QDockWidget('核素')
        self.dock1.setMaximumWidth(85)
        self.dock1.setFeatures(QDockWidget.DockWidgetFloatable)
        self.dock1.setAllowedAreas(Qt.LeftDockWidgetArea)
        self.listwidget = QListWidget()
        # self.listwidget.currentRowChanged.connect(self.onDockListIndexChanged)
        self.dock1.setWidget(self.listwidget)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.dock1)

        self.UpButton = QtWidgets.QPushButton(self)
        self.UpButton.setObjectName("UpButton")
        self.UpButton.setText("点击此处进行数据更新！")
        # self.UpButton.setObjectName("UpButton")
        self.UpButton.setStyleSheet("color:white;background:pink;UpButton:hover:{background:yellow;}")
        self.UpButton.setGeometry(400,100,80,20)
        self.UpButton.clicked.connect(self.Update)
        self.setMenuWidget(self.UpButton)
        self.text = Ui_Form()
        self.text.gridLayoutWidget.setGeometry(QtCore.QRect(50, 200, 600, 300))
        self.setCentralWidget(self.text)
        self.listwidget.currentRowChanged.connect(self.onDockListIndexChanged)
        self.setStyleSheet("""
            QMainWindow{
                background:#EEEED1;
            }
            QPushButton#UpButton{
                font: 14pt \"华文彩云\";
                background:pink;
                border:0px;
                color:white
            }
            QPushButton#UpButton:hover{
                background:yellow;
            }

        """)

    def onDockListIndexChanged(self, index):
        item = self.TempArray[index]
        self.text.SetInfo(item)

    # def Update(self):
    #     try:
    #         up_ = UpThread(self.TempArray,self.listwidge)
    #         up_.start()
    #         up_.join()
    #     except:
    #         print("hahhaha")
    # def _update(self):#更新函数
    #     try:
    #         for i in range(1,3):
    #             self.temp = []
    #             data  = (DATA(i).data)
    #             a = data["Atomic name"]
    #             temp1 = a.split()[2]
    #             self.temp.append(temp1+str(data["Atomic number"]))
    #             self.TempArray.append(data)
    #             self.listwidget.addItems(self.temp)
    #             with open("data//basicnuclear.json", "a", newline='', encoding='utf-8') as f_obj:
    #                 json.dump(data, f_obj)


        #
        # except:#网络异常时弹出提示框提示网络异常。
        #
        #     reply = QtWidgets.QMessageBox.question(self,
        #                                            'NuclearFinder',
        #                                            "网络不稳定请等会再试！",
        #                                            QtWidgets.QMessageBox.Yes )
        #     if reply == QtWidgets.QMessageBox.Yes:
        #         pass
        #     else:
        #         pass

    def Update(self):
        try:
            thread1 = threading.Thread(target=_update,args=(self.TempArray,self.listwidget,))
            thread1.start()
            thread1.join()
            time.sleep(1)
        except:
            print("something worry")

def main():
    app = QApplication(sys.argv)
    window = Update()
    window.show()
    sys.exit(app.exec_())
# 入口
if __name__ == '__main__':
    main()
