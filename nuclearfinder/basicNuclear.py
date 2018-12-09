# -*- coding: utf-8 -*-
from basicSql import BasicSql
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(QtWidgets.QWidget):
    # def setupUi(self, Form):
    #     Form.setObjectName("Form")
    #     Form.resize(1003, 652)
    def __init__(self):
        super(Ui_Form, self).__init__()
        # self.resize(600,300)
        # self.setStyleSheet("background:#FFC1C1;")
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(100, 200, 600, 300))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 3, 7, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 5)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 9, 3, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 6, 1, 1, 5)
        self.Atomic_name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.Atomic_name.setObjectName("Atomic_name")
        self.gridLayout.addWidget(self.Atomic_name, 0, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 6, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 5)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 0, 1, 1, 5)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 9, 7, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 7, 7, 1, 4)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 7, 11, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 0, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_6.setObjectName("boiling_point")
        self.gridLayout.addWidget(self.lineEdit_6, 7, 1, 1, 5)
        self.lineEdit_6.setReadOnly(True)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 9, 0, 1, 3)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 3, 8, 1, 4)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 9, 8, 1, 4)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 7, 1, 2)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 5, 7, 1, 2)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 5, 9, 1, 2)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 2, 7, 1, 3)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 6, 9, 1, 3)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 9, 4, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout.addWidget(self.lineEdit_13, 2, 10, 1, 2)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 5, 1, 1, 5)
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(100, 80, 81, 81))
        self.label_4.setObjectName("label_4")
        self.gridLayout.setSpacing(0)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "基本元素"))
        self.label_12.setText(_translate("Form", "Ionic radius"))
        self.label_8.setText(_translate("Form", "Atomic number"))
        self.label_10.setText(_translate("Form", "Melting point"))
        self.lineEdit_2.setText(_translate("Form", ""))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_5.setText(_translate("Form", ""))
        self.lineEdit_5.setReadOnly(True)
        self.Atomic_name.setText(_translate("Form", "Atomic name"))
        self.label_9.setText(_translate("Form", "Density"))
        self.lineEdit.setText(_translate("Form", ""))
        self.lineEdit.setReadOnly(True)
        self.label_3.setText(_translate("Form", "Atomic mass"))
        self.lineEdit_3.setText(_translate("Form", ""))
        self.lineEdit_3.setReadOnly(True)
        self.label_14.setText(_translate("Form", "Discovered by"))
        self.label_5.setText(_translate("Form", "Electronegativity according to Pauling"))
        self.lineEdit_7.setText(_translate("Form", ""))
        self.lineEdit_7.setReadOnly(True)
        self.label_6.setText(_translate("Form", "Boiling point"))
        self.lineEdit_6.setText(_translate("Form", ""))
        self.lineEdit_6.setReadOnly(True)
        self.label_7.setText(_translate("Form", "Vanderwaals radius"))
        self.lineEdit_9.setText(_translate("Form", ""))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_11.setText(_translate("Form", ""))
        self.lineEdit_11.setReadOnly(True)
        self.label_13.setText(_translate("Form", "Electronic shell"))
        self.label_16.setText(_translate("Form", "Isotopes"))
        self.lineEdit_8.setText(_translate("Form", ""))
        self.lineEdit_8.setReadOnly(True)
        self.label_17.setText(_translate("Form", "Energy of first ionisation"))
        self.lineEdit_10.setText(_translate("Form", ""))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_12.setText(_translate("Form", ""))
        self.lineEdit_12.setReadOnly(True)
        self.lineEdit_13.setText(_translate("Form", ""))
        self.lineEdit_13.setReadOnly(True)
        self.lineEdit_4.setText(_translate("Form", ""))
        self.lineEdit_4.setReadOnly(True)
        self.label_4.setText(_translate("Form", ""))
        self.label_4.setStyleSheet("""background:#CAFF70;font-size:50px;font-weight:1500;font-family:"Helvetica Neue",Helvetica, Arial, sans-serif;color:#FCFCFC""")
        self.setStyleSheet("""
        QWidget{
            background:#FFFFFF;
        }
         QLabel{
            background:#836FFF;
            font-family:"Helvetica Neue",Helvetica, Arial, sans-serif;
            color:#ffffff;
            }
        QLineEdit{
            background:#FFF0F5;
            border:0px;
            font-family:"Helvetica Neue",Helvetica, Arial, sans-serif;
        }
        """)
    def setmessage(self,name):
        self.label_4.setText(name)
        db = BasicSql()
        result = db.Search(name)
        print(result)
        self.lineEdit.setText(result[2])
        self.lineEdit_2.setText(result[1])#number
        self.lineEdit_3.setText(result[0])
        self.lineEdit_4.setText(result[4])
        self.lineEdit_5.setText(result[5])
        self.lineEdit_6.setText(result[6])
        self.lineEdit_7.setText(result[3])
        self.lineEdit_8.setText(result[9])
        self.lineEdit_9.setText(result[8])
        self.lineEdit_10.setText(result[10])
        self.lineEdit_11.setText(result[12])
        self.lineEdit_12.setText(result[7])
        self.lineEdit_13.setText(result[11])
    def SetInfo(self,result):
        a = result["Atomic name"]
        name = a.split()[2]
        self.label_4.setText(name)
        self.lineEdit.setText(result['Atomic mass'])
        self.lineEdit_2.setText(result['Atomic number'])#number
        self.lineEdit_3.setText(result['Atomic name'])
        self.lineEdit_4.setText(result['Density'])
        self.lineEdit_5.setText(result['Melting point'])
        self.lineEdit_6.setText(result['Boiling point'])
        self.lineEdit_7.setText(result['Electronegativity according to Pauling'])
        self.lineEdit_8.setText(result['Isotopes'])
        self.lineEdit_9.setText(result['Ionic radius'])
        self.lineEdit_10.setText(result['Electronic shell '])
        self.lineEdit_11.setText(result['Discovered by'])
        self.lineEdit_12.setText(result['Vanderwaals radius '])
        self.lineEdit_13.setText(result['Energy of first ionisation'])



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Form()
    ui.show()
    sys.exit(app.exec_())