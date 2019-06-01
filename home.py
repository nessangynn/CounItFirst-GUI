# -*- coding: utf-8 -*-

'''
    Count-It-First - Server
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

#Connection between Home Page and Game Page
from easyGame import Ui_easyWindow #EASY MODE
from hardGame import Ui_hardWindow #HARD MODE



from client import client


class Ui_MainWindow(object):

    def __init__(self):
        self.NEW_PLAYER = client()

    def openEasyGame(self, NEW_PLAYER):

        self.NEW_PLAYER.prep_game()
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_easyWindow(self.NEW_PLAYER) #connect with easyGame.py
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()
        
    def openHardGame(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_hardWindow(self.NEW_PLAYER) #connect with hardGame.py
        self.ui.setupUi(self.window)
        MainWindow.hide()
        self.window.show()

    def close_application(self):
        sys.exit()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(416, 327)
        MainWindow.setStyleSheet("background: #151515;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gameLabel = QtWidgets.QLabel(self.centralwidget)
        self.gameLabel.setGeometry(QtCore.QRect(80, 10, 251, 51))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)

        #TITLE OF THE GAME
        self.gameLabel.setFont(font)
        self.gameLabel.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 20px;\n"
"text-align: center;\n"
"color: #e7e7e7;\n"
"letter-spacing: 5px;")
        self.gameLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gameLabel.setObjectName("gameLabel")


        #EASY MODE BUTTON
        self.easyButton = QtWidgets.QPushButton(self.centralwidget)
        self.easyButton.setGeometry(QtCore.QRect(150, 100, 111, 41))
        self.easyButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.easyButton.setObjectName("easyButton")
        #Connection between Home Page and Easy Game Mode
        self.easyButton.clicked.connect(self.openEasyGame)
        #self.easyButton.released.connect(self.openEasyGame)


        #HARD MODE BUTTON
        self.hardButton = QtWidgets.QPushButton(self.centralwidget)
        self.hardButton.setGeometry(QtCore.QRect(150, 150, 111, 41))
        self.hardButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.hardButton.setObjectName("hardButton")
        #Connection between Home Page and Hard Game Mode
        self.hardButton.clicked.connect(self.openHardGame)
        #self.hardButton.released.connect(self.openHardGame)


        #QUIT BUTTON
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(340, 250, 51, 32))
        self.quitButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: red;")
        self.quitButton.setObjectName("quitButton")
        self.quitButton.clicked.connect(self.close_application)

        #GAME MODE LABEL
        self.gameModeLabel = QtWidgets.QLabel(self.centralwidget)
        self.gameModeLabel.setGeometry(QtCore.QRect(120, 70, 181, 16))
        self.gameModeLabel.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.gameModeLabel.setObjectName("gameModeLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 416, 22))
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
        self.gameLabel.setText(_translate("MainWindow", "Welcome to Count-It-First"))
        self.easyButton.setText(_translate("MainWindow", "EASY"))
        self.hardButton.setText(_translate("MainWindow", "HARD"))
        self.quitButton.setText(_translate("MainWindow", "QUIT"))
        self.gameModeLabel.setText(_translate("MainWindow", "Choose your game mode:"))


def start():
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    return ui.NEW_PLAYER



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    MainWindow2 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    # ui.initGame()
    # print("check")
    MainWindow.show()
    sys.exit(app.exec_())
