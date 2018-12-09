# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sss.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from basicNuclear import Ui_Form

class Result(QtWidgets.QWidget):
    def __init__(self):
        super(Result, self).__init__()
        self.setObjectName("Result")
    # def setupUi(self, Form):
    #     Form.setObjectName("Form")
    #     Form.resize(677, 611)
        self.gridLayoutWidget = QtWidgets.QWidget(self)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 170, 221, 161))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit")

        self.lineEdit_3.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_3, 2, 1, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit")
        # self.lineEdit_4.setText("aaa")
        self.lineEdit_4.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit_4, 3, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit")

        self.lineEdit_2.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_2, 5, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit")

        self.lineEdit_5.setReadOnly(True)
        self.gridLayout.addWidget(self.lineEdit_5, 4, 1, 1, 1)
        self.name = QtWidgets.QLabel(self.gridLayoutWidget)
        self.name.setObjectName("label")
        self.gridLayout.addWidget(self.name, 0, 0, 1, 1)
        self.gridLayout.setSpacing(0)

        self.gridLayoutWidget_2 = QtWidgets.QWidget(self)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(270, 170, 160, 161))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_10.setObjectName("lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit_10, 0, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_9.setObjectName("label")
        self.gridLayout_2.addWidget(self.label_9, 3, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName("label")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_9.setObjectName("lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit_9, 1, 1, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_7.setObjectName("lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit_7, 2, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_8.setObjectName("label")
        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_6.setObjectName("label")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_7.setObjectName("label")
        self.gridLayout_2.addWidget(self.label_7, 1, 0, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_8.setObjectName("lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit_8, 3, 1, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_6.setObjectName("lineEdit")

        self.gridLayout_2.addWidget(self.lineEdit_6, 4, 1, 1, 1)
        self.gridLayout_2.setSpacing(0)


        #第三板块
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(40, 340, 221, 161))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_11.setObjectName("lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit_11, 0, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_10.setObjectName("label")
        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_12.setObjectName("lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit_12, 2, 1, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_13.setObjectName("lineEdit")


        self.gridLayout_3.addWidget(self.lineEdit_13, 3, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_11.setObjectName("label")
        self.gridLayout_3.addWidget(self.label_11, 5, 0, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_14.setObjectName("lineEdit")


        self.gridLayout_3.addWidget(self.lineEdit_14, 5, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_12.setObjectName("label")
        self.gridLayout_3.addWidget(self.label_12, 4, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_13.setObjectName("label")
        self.gridLayout_3.addWidget(self.label_13, 3, 0, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_15.setObjectName("lineEdit")


        self.gridLayout_3.addWidget(self.lineEdit_15, 4, 1, 1, 1)
        self.name_2 = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.name_2.setObjectName("label")
        self.gridLayout_3.addWidget(self.name_2, 0, 0, 1, 1)
        self.gridLayout_3.setSpacing(0)
        # 第四板块
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(440, 170, 221, 161))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.lineEdit_16 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_16.setObjectName("lineEdit")
        self.lineEdit_16.setReadOnly(True)

        self.gridLayout_4.addWidget(self.lineEdit_16, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_14.setObjectName("label")
        self.gridLayout_4.addWidget(self.label_14, 2, 0, 1, 1)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_17.setObjectName("lineEdit")


        self.gridLayout_4.addWidget(self.lineEdit_17, 2, 1, 1, 1)

        self.lineEdit_18 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_18.setObjectName("lineEdit")

        self.lineEdit_18.setReadOnly(True)
        self.gridLayout_4.addWidget(self.lineEdit_18, 3, 1, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_15.setObjectName("label")
        self.gridLayout_4.addWidget(self.label_15, 5, 0, 1, 1)
        self.lineEdit_19 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_19.setObjectName("lineEdit")

        self.lineEdit_19.setReadOnly(True)
        self.gridLayout_4.addWidget(self.lineEdit_19, 5, 1, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_16.setObjectName("label")
        self.gridLayout_4.addWidget(self.label_16, 4, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_17.setObjectName("label")
        self.gridLayout_4.addWidget(self.label_17, 3, 0, 1, 1)

        self.lineEdit_20 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_20.setObjectName("lineEdit")

        self.lineEdit_20.setReadOnly(True)
        self.gridLayout_4.addWidget(self.lineEdit_20, 4, 1, 1, 1)
        self.name_3 = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.name_3.setObjectName("label")
        self.gridLayout_4.addWidget(self.name_3, 0, 0, 1, 1)
        self.gridLayout_4.setSpacing(0)


        # 第五板块
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(270, 340, 221, 161))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.lineEdit_21 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_21.setObjectName("lineEdit")

        self.lineEdit_21.setReadOnly(True)
        self.gridLayout_5.addWidget(self.lineEdit_21, 0, 1, 1, 1)

        self.label_18 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_18.setObjectName("label")
        self.gridLayout_5.addWidget(self.label_18, 2, 0, 1, 1)
        self.lineEdit_22 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_22.setObjectName("lineEdit")

        self.lineEdit_22.setReadOnly(True)
        self.gridLayout_5.addWidget(self.lineEdit_22, 2, 1, 1, 1)

        self.lineEdit_23 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_23.setObjectName("lineEdit")

        self.lineEdit_23.setReadOnly(True)
        self.gridLayout_5.addWidget(self.lineEdit_23, 3, 1, 1, 1)

        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_19.setObjectName("label")
        self.gridLayout_5.addWidget(self.label_19, 5, 0, 1, 1)
        self.lineEdit_24 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_24.setObjectName("lineEdit")

        self.lineEdit_24.setReadOnly(True)
        self.gridLayout_5.addWidget(self.lineEdit_24, 5, 1, 1, 1)

        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_20.setObjectName("label")
        self.gridLayout_5.addWidget(self.label_20, 4, 0, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.label_21.setObjectName("label")
        self.gridLayout_5.addWidget(self.label_21, 3, 0, 1, 1)
        self.lineEdit_25 = QtWidgets.QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_25.setObjectName("lineEdit")

        self.lineEdit_25.setReadOnly(True)
        self.gridLayout_5.addWidget(self.lineEdit_25, 4, 1, 1, 1)

        self.name_4 = QtWidgets.QLabel(self.gridLayoutWidget_5)
        self.name_4.setObjectName("label")
        self.gridLayout_5.addWidget(self.name_4, 0, 0, 1, 1)
        self.gridLayout_5.setSpacing(0)
        # self.retranslateUi()
        # QtCore.QMetaObject.connectSlotsByName(Form)

    # def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        # Form.setWindowTitle(_translate("Form", "Form"))
        self.label_4.setText(_translate("Form", "chinesename"))
        self.label.setText(_translate("Form", "Jπ"))
        self.label_3.setText(_translate("Form", "Half-life"))
        self.label_2.setText(_translate("Form", "E(level)(MeV)"))
        self.name.setText(_translate("Form", "name"))
        self.label_9.setText(_translate("Form", "Sp"))
        self.label_5.setText(_translate("Form", "QEC"))
        self.label_8.setText(_translate("Form", "Sn"))
        self.label_6.setText(_translate("Form", "Qα"))
        self.label_7.setText(_translate("Form", "Qβ+"))
        self.label_10.setText(_translate("Form", "Q2β-"))
        self.label_11.setText(_translate("Form", "Qβ-n"))
        self.label_12.setText(_translate("Form", "QECP"))
        self.label_13.setText(_translate("Form", "Q2EC"))
        self.name_2.setText(_translate("Form", "ΔQα"))
        self.label_14.setText(_translate("Form", "BE/A"))
        self.label_15.setText(_translate("Form", "E2+"))
        self.label_16.setText(_translate("Form", "E1st ex. st"))
        self.label_17.setText(_translate("Form", "(BE-LDM Fit)"))
        self.name_3.setText(_translate("Form", "Qβ-2n(keV)"))
        self.label_18.setText(_translate("Form", "S2p"))
        self.label_19.setText(_translate("Form", "Pair-gap"))
        self.label_20.setText(_translate("Form", "E3-"))
        self.label_21.setText(_translate("Form", "S2n"))
        self.name_4.setText(_translate("Form", "Q-"))
        # self.setStyleSheet("background:#ffffff;")
        self.setStyleSheet("""
        Result{
            background:#ffffff;
            border:1px solid darkgray;
            border-bottom-right-radius:10px;
        }
        QLabel#label{
            background:#836FFF;
            font-family:"Helvetica Neue",Helvetica, Arial, sans-serif;
            color:#ffffff;
            }
        QLineEdit#lineEdit{
            background:#FFF0F5;
            boeder:0px;
            font-family:"Helvetica Neue",Helvetica, Arial, sans-serif;
        }
        """)
        self.NuclearName = QtWidgets.QPushButton(self)
        self.NuclearName.clicked.connect(self.Mother)#定义母体按键事件
        self.NuclearName.setStyleSheet(
            """background:pink;font-size:50px;font-weight:1500;font-family:"Helvetica Neue",Helvetica, Arial, sans-serif;color:#FCFCFC""")
        self.NuclearName.setText("")
        self.NuclearName.setGeometry(QtCore.QRect(100, 75, 80, 80))
        # 左上显示元素的左上的原子质量
        self.AtomicMass = QtWidgets.QLabel(self)
        self.AtomicMass.setStyleSheet(
            """background:#40E0D0;font-size:20px;font-weight:1500;font-family:"Helvetica Neue",Helvetica, Arial, sans-serif;color:#FCFCFC""")
        self.AtomicMass.setObjectName("leabel")
        self.AtomicMass.setText("")
        self.AtomicMass.setGeometry(QtCore.QRect(60, 75, 40, 40))
        # 左上显示元素的左下的质子数
        self.proton = QtWidgets.QLabel(self)
        self.proton.setStyleSheet(
            """background:#CAFF70;font-size:20px;font-weight:1500;font-family:"Helvetica Neue",Helvetica, Arial, sans-serif;color:#FCFCFC""")
        self.proton.setObjectName("label")
        self.proton.setGeometry(QtCore.QRect(60, 115, 40, 40))
        self.ui  = Ui_Form()
        self.Decay_Modes = QtWidgets.QLabel(self)
        self.Decay_Modes.setText("Decay Modes")
        self.Decay_Modes.setStyleSheet("""
            background:#836FFF;
            font-family:"Helvetica Neue",Helvetica, Arial, sans-serif;
            color:#FFFFFF;
        """)
        self.Decay_Modes.setGeometry(40,500,100,20)
        # self.Decay_Modes_value.setReadOnly(True)
        self.Decay_Modes_value = QtWidgets.QLineEdit(self)
        self.Decay_Modes_value.setGeometry(140,500,350,20)
        self.Decay_Modes_value.setStyleSheet("""
            background:#FFF0F5;
            boeder:0px;
            font-family:"Helvetica Neue",Helvetica, Arial, sans-serif;
        """)
    def Mother(self):
        try:
            self.ui.setmessage(str(self.NuclearName.text()))
            self.ui.show()
        except:
            pass

    def setmessage(self,result):
        try:
            self.Decay_Modes_value.setText(result[7])
            self.Decay_Modes_value.setReadOnly(True)
            self.NuclearName.setText(result[2])
            self.AtomicMass.setText(result[0])
            # self.proton.setText(result[1])#中文名
            self.lineEdit.setText(result[2])#名称
            self.lineEdit_2.setText(result[4])#Qbeita-
            self.lineEdit_3.setText(result[1])
            self.lineEdit_4.setText(result[3])#ddd
            self.lineEdit_5.setText(result[6])
            self.lineEdit_6.setText(result[24])#"Qa"
            self.lineEdit_7.setText(result[11])
            self.lineEdit_8.setText(result[19])#"Sp"
            self.lineEdit_9.setText(result[10])
            self.lineEdit_10.setText(result[9])
            self.lineEdit_11.setText(result[23])#"DQa"
            self.lineEdit_12.setText(result[26])#"Q2β-"
            self.lineEdit_13.setText(result[12])
            self.lineEdit_14.setText(result[14])
            self.lineEdit_15.setText(result[13])
            self.lineEdit_16.setText(result[15])#beuta-2N
            self.lineEdit_17.setText(result[16])
            self.lineEdit_18.setText(result[17])
            self.lineEdit_19.setText(result[21])
            self.lineEdit_20.setText(result[20])
            self.lineEdit_21.setText(result[8])#ΔQa
            self.lineEdit_22.setText(result[25])#e4_S2p
            self.lineEdit_23.setText(result[27])#"E4+/E2+"——S2n
            self.lineEdit_24.setText(result[18])#"β2"Pair-gap
            self.lineEdit_25.setText(result[22])
        except:
            pass



if __name__ =="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Result()
    # ui.Qss()
    ui.show()
    sys.exit(app.exec_())
