import os
import sys

from PyQt5 import QtWidgets, QtCore, QtGui 
from PyQt5.Qt import QApplication

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
        #self.wordslist.insertRow(0)
        #item1 = QtWidgets.QTableWidgetItem("a")
        #self.wordslist.setItem(0,0, item1)
        #item2 = QtWidgets.QTableWidgetItem("b")
        #self.wordslist.setItem(0,1, item2)

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
        self.exit_action =menubar.addAction("Exit")
        self.add_action = menubar.addAction("Add")
        self.about_action = menubar.addAction("About")



if  __name__ == "__main__":
    print ("start zidian")
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = Zidian()
    mainwindow.show()
    sys.exit(app.exec_())
    