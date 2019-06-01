
'''
    Count-It-First - Client
    CSC/CPE 4750
    Author: Tai Doan, Hung Nguyen, Huyen Nguyen
    '''

from socket import *
import re
import sys
import random,time
from time import gmtime, strftime
from datetime import datetime

# --GUI import library--
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QScrollBar,QSplitter,QTableWidgetItem,QTableWidget,QComboBox,QVBoxLayout,QGridLayout,QDialog,QWidget, QPushButton, QApplication, QMainWindow,QAction,QMessageBox,QLabel,QTextEdit,QProgressBar,QLineEdit)
from PyQt5.QtCore import QCoreApplication


#IMPORT client.py as we want to use CLASS client in it
from client import client

class Ui_easyWindow(object):

    def __init__(self, NEW_PLAYER):
        self.NEW_PLAYER = NEW_PLAYER
        
    def pressedOneButton(self):
        self.NEW_PLAYER.game_logic(1)

    def pressedTwoButton(self):
        self.NEW_PLAYER.game_logic(2)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Game Window")
        MainWindow.resize(325, 293)
        MainWindow.setStyleSheet("background: #151515;\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        #ONE BUTTON
        self.oneButton = QtWidgets.QPushButton(self.centralwidget)
        self.oneButton.setGeometry(QtCore.QRect(60, 110, 91, 81))
        self.oneButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 30px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.oneButton.setObjectName("oneButton")

        #Connect +1 button with the def pressedOneButton
        self.oneButton.clicked.connect(self.pressedOneButton)
        self.oneButton.released.connect(self.pressedOneButton)

        #TWO BUTTON
        self.twoButton = QtWidgets.QPushButton(self.centralwidget)
        self.twoButton.setGeometry(QtCore.QRect(170, 110, 91, 81))
        self.twoButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 30px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.twoButton.setObjectName("twoButton")
        #Connect +2 button with the def pressedTwoButton
        self.twoButton.clicked.connect(self.pressedTwoButton)
        self.twoButton.released.connect(self.pressedTwoButton)

        #WIN NUMBER LABEL
        self.winNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.winNumLabel.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.winNumLabel.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.winNumLabel.setObjectName("winNumLabel")

        #CURRENT NUMBER LABEL
        self.currNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.currNumLabel.setGeometry(QtCore.QRect(10, 50, 121, 31))
        self.currNumLabel.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.currNumLabel.setObjectName("currNumLabel")


        #DISPLAY CURRENT NUMBER
        self.currNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.currNumber.setGeometry(QtCore.QRect(150, 50, 111, 31))
        self.currNumber.setObjectName("currNumber")

        #DISPLAY GENERATED NUMBER
        self.winNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.winNumber.setGeometry(QtCore.QRect(150, 10, 111, 31))
        self.winNumber.setObjectName("winNumber")

        #DISPLAY WHOSE TURN IS IT
        self.turnLabel = QtWidgets.QLabel(self.centralwidget)
        self.turnLabel.setGeometry(QtCore.QRect(60, 200, 201, 31))
        self.turnLabel.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 30px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.turnLabel.setObjectName("turnLabel")

        #FRAME OF THE GUI
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 325, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.oneButton.setText(_translate("MainWindow", "+1"))
        self.twoButton.setText(_translate("MainWindow", "+2"))
        self.winNumLabel.setText(_translate("MainWindow", "Win Number:"))
        self.currNumLabel.setText(_translate("MainWindow", "Current Number:"))
        self.turnLabel.setText(_translate("MainWindow", "YOUR TURN"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_easyWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
