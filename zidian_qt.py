import os
import sys
import re
from PyQt5 import QtWidgets, QtCore, QtGui 
from PyQt5.Qt import QApplication
from _overlapped import NULL

headname="abcdefghijklmnopqrstuvwxyz"

dir_root="./words"
def CheckFiles():
    def checkfile(file):
        list_tmp=[]
        if not re.match(r'[A-Za-z].txt', file):
            print ("file %s is not match"%file)
            return NULL, NULL
        
        path = os.path.join(dir_root,file)
        with open(path) as fd:
            x = fd.read()
            list_tmp = x.split(";")
            list_tmp.remove('')
            length = len(list_tmp)
        file = file.split('.')[0]
        length = str(length) 
        return file, length
    
    files = os.listdir(dir_root)
    list_tmp=[]
    for file in files:
        x,y = checkfile(file)
        if x != NULL:
            list_tmp.append((x,y))
    return list_tmp


class C_AddMenu(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(C_AddMenu, self).__init__(parent)
        self.resize(200,90)
        self.addItem()
    def addItem(self):
        self.wordlabel = QtWidgets.QLabel(self)
        self.wordlabel.setObjectName("wordlabel")
        self.wordlabel.setGeometry(5,5,40,20)
        self.wordlabel.setText("Word:")

        self.wordEditor = QtWidgets.QLineEdit(self)
        self.wordEditor.setObjectName("wordedit")
        self.wordEditor.setGeometry(55,5,130,20)
        
        self.Explainlabel = QtWidgets.QLabel(self)
        self.Explainlabel.setObjectName("explainlabel")
        self.Explainlabel.setGeometry(5,30,50,20)
        self.Explainlabel.setText("Explain:")
        
        self.ExplainEditor = QtWidgets.QLineEdit(self)
        self.ExplainEditor.setObjectName("word")
        self.ExplainEditor.setGeometry(55,30,130,20)
        
        self.addbutton = QtWidgets.QPushButton(self)
        self.addbutton.clicked.connect(self.add_function)
        self.addbutton.setObjectName("addbutton")
        self.addbutton.setText("Add")
        self.addbutton.setGeometry(125, 55, 60, 20)
    def add_function(self):
        print("add button is clicked")

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
        
        
        self.init_WordListItem()
    def init_WordListItem(self):
        list_tmp = CheckFiles()
        for m in list_tmp:
            row = self.wordslist.rowCount()
            self.wordslist.insertRow(row)
                        
            file = QtWidgets.QTableWidgetItem(m[0])
            count = QtWidgets.QTableWidgetItem(m[1])
            file.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignCenter)
            count.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
            
            self.wordslist.setItem(row, 0, file)
            self.wordslist.setItem(row, 1, count)
    def refresh_WordListItem(self):
        pass
    def add_Button(self):
        self.open_button = QtWidgets.QPushButton(self)
        self.open_button.setObjectName("openbutton")
        self.open_button.setGeometry(0,275,100, 25)
        self.open_button.setText("Open")
        self.open_button.clicked.connect(self.action_open)
        
        self.refresh_button = QtWidgets.QPushButton(self)
        self.refresh_button.setObjectName("freshbutton")
        self.refresh_button.setGeometry(100,275,100, 25)
        self.refresh_button.setText("Refresh")
        self.refresh_button.clicked.connect(self.action_refresh)
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
    def action_open(self):
        print("action open is triggered!")
        CheckFiles()
    def action_refresh(self):
        print("action refresh is triggered!")


if  __name__ == "__main__":
    print ("start zidian")
    app = QtWidgets.QApplication(sys.argv)
    mainwindow = Zidian()
    mainwindow.show()
    sys.exit(app.exec_())
    