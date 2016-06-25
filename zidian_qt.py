import os
import sys

from PyQt5 import QtWidgets, QtCore, QtGui 
from PyQt5.Qt import QApplication

class C_AddMenu(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(C_AddMenu, self).__init__(parent)
        self.addItem()
    def addItem(self):
        pass


class Zidian(QtWidgets.QMainWindow):
    def __init__(self,parent=None):
        super(Zidian, self).__init__(parent)
        self.add_Widgets()
        self.windows_resize()
        self.add_QueryBar()
        self.add_Menubar()
        self.add_WordList()
        self.add_Button()
    def windows_resize(self):
        self.resize(200,300)
    def add_Widgets(self):
        self.mainwidgets = QtWidgets.QWidget(self)
        self.setCentralWidget(self.mainwidgets)
    def add_QueryBar(self):
        self.editor = QtWidgets.QLineEdit(self.mainwidgets)
        self.editor.setObjectName("querybar")
        self.editor.setGeometry(0,0,200,20)
    def add_WordList(self):
        self.wordslist = QtWidgets.QTableWidget(0, 2, self.mainwidgets)
        self.wordslist.setObjectName("wordlist")
        self.wordslist.setGeometry(0,25,200,230)
        self.wordslist.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.wordslist.setHorizontalHeaderLabels(["item", "counts"])
        self.wordslist.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        self.wordslist.verticalHeader().hide()
        self.wordslist.setShowGrid(False) 
    def refresh_WordListItem(self):
        pass
    def add_Button(self):
        self.open_button = QtWidgets.QPushButton(self)
        self.open_button.setObjectName("openbutton")
        self.open_button.setGeometry(0,275,100, 25)
        self.open_button.setText("Open")
        
        self.fresh_button = QtWidgets.QPushButton(self)
        self.fresh_button.setObjectName("freshbutton")
        self.fresh_button.setGeometry(100,275,100, 25)
        self.fresh_button.setText("Refresh")
    def add_Menubar(self):
        menubar = self.menuBar()
        self.exit_action = QtWidgets.QAction("Exit", menubar, triggered=self.close)
        menubar.addAction(self.exit_action)

        self.add_action = QtWidgets.QAction("Add", menubar, triggered=self.add)
        menubar.addAction(self.add_action)
        
        self.about_action = QtWidgets.QAction("About", menubar, triggered=self.about)
        menubar.addAction(self.about_action)
    def add(self):
        print("action action is triggered!")
        itemadd_diag = C_AddMenu(self)
        itemadd_diag.show()
    def about(self):
        print("action about is triggered!")
        QtWidgets.QMessageBox.about(self,"About", "Zidian PyQtStyle \nby xufengfeng@2016.06.25")


if  __name__ == "__main__":
    print ("start zidian")
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = Zidian()
    mainwindow.show()
    sys.exit(app.exec_())
    