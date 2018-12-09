from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication,Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from nuclearsql import NuclearSql
from ResultWidget import ResultWidget
from sss import Result
import sys

class SingleNuclear(QMainWindow):
    def __init__(self,nuclear):
        super().__init__()

        db = NuclearSql()
        self.items = list(db._search(nuclear))

        self.addDock()
        self.text = Result()
        # self.text.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.text)
        self.setStyleSheet("""
        background:#f0fff0;
        """)
        # self.text.setStyleSheet("""
        #     background:#EEEED1;
        # """)
        self.setGeometry(200, 200, 800, 400)
        self.setWindowTitle('核素')
        # self.show()


    def onDockListIndexChanged(self, index):
        item = self.items[index]
        self.text.setmessage(item)

    def addDock(self):
        dock1 = QDockWidget('核素')
        dock1.setMaximumWidth(85)
        dock1.setFeatures(QDockWidget.DockWidgetFloatable)
        dock1.setAllowedAreas(Qt.LeftDockWidgetArea)
        # dock1.setGeometry(0,0,100,400)
        listwidget = QListWidget()
        self.temp = []
        for each in self.items:
            self.temp.append(str(each[2])+str(each[0]))
        listwidget.addItems(self.temp)
        listwidget.currentRowChanged.connect(self.onDockListIndexChanged)
        dock1.setWidget(listwidget)
        self.addDockWidget(Qt.LeftDockWidgetArea, dock1)
    # def __init__(self,nuclear):
    #     super().__init__()
    #
    #     db = NuclearSql()
    #     self.items = list(db._search(nuclear))
    #
    #     self.addDock()
    #     self.text = Result()
    #     # self.text.setAlignment(Qt.AlignCenter)
    #     self.setCentralWidget(self.text)
    #     self.setStyleSheet("""
    #     background:#f0fff0;
    #     """)
    #     # self.text.setStyleSheet("""
    #     #     background:#EEEED1;
    #     # """)
    #     self.setGeometry(200, 200, 800, 400)
    #     self.setWindowTitle('核素')
    #     self.show()
    #
    #
    # def onDockListIndexChanged(self, index):
    #     item = self.items[index]
    #     self.text.setmessage(item)
    #
    #     pass
    #
    # def addDock(self):
    #     dock1 = QDockWidget('核素')
    #     dock1.setMaximumWidth(85)
    #     dock1.setFeatures(QDockWidget.DockWidgetFloatable)
    #     dock1.setAllowedAreas(Qt.LeftDockWidgetArea)
    #     # dock1.setGeometry(0,0,100,400)
    #     listwidget = QListWidget()
    #     self.temp = []
    #     for each in self.items:
    #         self.temp.append(str(each[2])+str(each[0]))
    #     listwidget.addItems(self.temp)
    #     listwidget.currentRowChanged.connect(self.onDockListIndexChanged)
    #     dock1.setWidget(listwidget)
    #     self.addDockWidget(Qt.LeftDockWidgetArea, dock1)

def main():
    app = QApplication(sys.argv)
    window = SingleNuclear("fe")
    window.show()
    sys.exit(app.exec_())


# 入口
if __name__ == '__main__':
    main()
