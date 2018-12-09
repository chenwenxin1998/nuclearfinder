from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
import sys
import qtawesome
from TopWidget import TopWidget
from LeftWidget import LeftWidget
from SearchWidget import SearchWidget
from ResultWidget import ResultWidget
from nuclearsql import NuclearSql
from MainWindow import  MainUi

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())
