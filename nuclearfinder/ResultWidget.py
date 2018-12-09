from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
import sys
class ResultWidget(QtWidgets.QWidget):
    def __init__(self):
        super(ResultWidget, self).__init__()
        #创建表一
        self.setObjectName("ResultWidget")
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(100, 200, 561, 121))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        # self.tableWidget.setVerticalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        # self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #self.setAttribute(QAbstractItemView.NoEditTriggers)

        # 创建表二
        self.tableWidget_2 = QtWidgets.QTableWidget(self)
        self.tableWidget_2.setGeometry(QtCore.QRect(100, 350, 561, 150))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(4)
        self.tableWidget_2.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, item)

        # item = self.tableWidget.verticalHeaderItem(0)
        # item.setText("值")
        #item.setStyleSheet("background:#FAEBD7")
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText( "原子质量")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("质子数")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText( "name")
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText("E(level) (MeV)")
        # item = self.tableWidget_2.verticalHeaderItem(0)
        # item.setText("性质")
        # item = self.tableWidget_2.verticalHeaderItem(0)
        # item.setText("值")
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText("Jπ")
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText("Δ(MeV)")
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText("T1/2")
        item = self.tableWidget_2.horizontalHeaderItem(3)
        item.setText("Decay Modes")

        self.tableWidget.setStyleSheet( """
            background:#F5FFFA;
            border:1px solid #E0DDDC;    
        """)
        self.tableWidget_2.setStyleSheet("""
            background:#F5FFFA;
        """)

        self.tableWidget_2.setRowHeight(0,100)
        self.tableWidget.setColumnWidth(3, 175)
        self.tableWidget_2.setColumnWidth(3,175)
        #左上元素名称
        self.NuclearName = QtWidgets.QPushButton(self)
        #self.NuclearName.clicked.connect(self.Mother)#定义母体按键事件
        self.NuclearName.setStyleSheet("""background:pink;font-size:50px;font-weight:1500;font-family:"Helvetica Neue",Helvetica, Arial, sans-serif;color:#FCFCFC""")
        self.NuclearName.setText("C")
        self.NuclearName.setGeometry(QtCore.QRect(100, 75, 80, 80))
        #左上显示元素的左上的原子质量
        self.AtomicMass = QtWidgets.QLabel(self)
        self.AtomicMass.setStyleSheet("""background:#40E0D0;font-size:20px;font-weight:1500;font-family:"Helvetica Neue",Helvetica, Arial, sans-serif;color:#FCFCFC""")
        self.AtomicMass.setObjectName("leabel")
        self.AtomicMass.setText(" ")
        self.AtomicMass.setGeometry(QtCore.QRect(60, 75, 40, 40))
        #左上显示元素的左下的质子数
        self.proton = QtWidgets.QLabel(self)
        self.proton.setStyleSheet("""background:#CAFF70;font-size:20px;font-weight:1500;font-family:"Helvetica Neue",Helvetica, Arial, sans-serif;color:#FCFCFC""")
        self.proton.setObjectName("label")
        self.proton.setGeometry(QtCore.QRect(60, 115, 40, 40))
        self.setStyleSheet("""
            QWidget#ResultWidget{
                background:#FFFFFF;
                border:1px solid darkgray;
                border-bottom-right-radius:10px;
            }
        """)
    # def Mother(self):
    #     self.

    def SetTable(self,Value):#填表
        for i in range (8):
            item = QtWidgets.QTableWidgetItem(str(Value[i]))
            if i<4:
                self.tableWidget.setItem(0,i,item)
            if i>=4:
                self.tableWidget_2.setItem(0,i-4,item)
def main():

    app = QtWidgets.QApplication(sys.argv)
    x = [1,2,3,4,5,6,6,6,6,]
    w = ResultWidget()
    w.SetTable(x)
    w.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()
