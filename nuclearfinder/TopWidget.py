from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
import sys
import qtawesome
class TopWidget(QtWidgets.QWidget):
    def __init__(self):
        super(TopWidget, self).__init__()

        self.setObjectName("TopWidget")
        self.setStyleSheet('''
            QWidget#TopWidget{
                background:#40E0D0;
                border-top-left-radius:10px;
                 border-top-right-radius:10px;
                 border-top:1px solid white;
                 border-right:1px solid darkGray;
                 border-left:1px solid white;

            }
        ''')
        self.close_button = QtWidgets.QPushButton(self)
        self.close_button.setGeometry(QtCore.QRect(900, 20, 25, 25))
        self.close_button.setIcon(QIcon("icon//close.jpg"))

        self.close_button.setStyleSheet("""
            background:#ffffff;
            border-radius:10px;
        """)
        self.sign_pic = QtWidgets.QLabel(self)
        self.sign_pic.setGeometry(QtCore.QRect(15,15,30,30))
        self.sign_pic.setPixmap(QtGui.QPixmap.fromImage(QtGui.QImage("icon//window.png")))
        self.sign_pic.setScaledContents(True)
def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = TopWidget()
    gui.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
