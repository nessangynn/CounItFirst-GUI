

'''
    Count-It-First - Client GUI
    CSC/CPE 4750
    Author: Tai Doan, Hung Nguyen, Huyen Nguyen
'''

import sys
import datetime

# ---------- GUI libraries -----------
from PyQt5 import QtCore, QtGui, QtWidgets
#from PyQt5.QtWidgets import (QVBoxLayout, QWidget, QPushButton, QApplication, 
#                           QMainWindow, QLabel, QTextEdit, QProgressBar, QLineEdit)
# from PyQt5.QtCore import QCoreApplication
#from PyQt5.QtCore import QTimer
# ---------- GUI libraries -----------

#Connection between Home Page and Game Page
from easyWindow import Ui_easyWindow #EASY MODE

from hardWindow import Ui_hardWindow #HARD MODE

#Connection between client.py with GUI - home.py
from client import Client


class Ui_MainWindow(object):

    def __init__(self):
        self.EASY_PLAYER = Client()
        self.HARD_PLAYER = Client()

    # EASY button method call (line 94)
    # purpose: player clicks "Easy" then it will translate to easyWindow.py window
    def openEasyGame(self):

        self.EASY_PLAYER.prep_game("1") #call back to Client.py for prep_game() method
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_easyWindow(self.EASY_PLAYER) #connect with easyWindow.py
        self.ui.setupUi(self.window)
        MAINWINDOW.hide()
        self.window.show()

    # HARD button method call (line 107)
    # purpose: player clicks "Hard" then it will translate to hardWindow.py window
    def openHardGame(self):

        self.HARD_PLAYER.prep_game("2")#call back to Client.py for prep_game() method
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_hardWindow(self.HARD_PLAYER) #connect with hardWindow.py
        self.ui.setupUi(self.window)
        MAINWINDOW.hide()
        self.window.show()

    # QUIT button method call (line 120)
    # purpose: close the application when players click "Quit"
    def close_application(self):
        sys.exit()

    # Style sheet for GUI
    def setupUi(self, MainWindow):

        # Outside frame structure
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(416, 327)
        MainWindow.setStyleSheet("background: #151515;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gameLabel = QtWidgets.QLabel(self.centralwidget)
        self.gameLabel.setGeometry(QtCore.QRect(80, 10, 251, 51))

        # Font for the title
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue,sans-serif")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)

        # TITLE OF THE GAME
        self.gameLabel.setFont(font)
        self.gameLabel.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 20px;\n"
"text-align: center;\n"
"color: #e7e7e7;\n"
"letter-spacing: 5px;")
        self.gameLabel.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.gameLabel.setObjectName("gameLabel")


        # EASY MODE BUTTON
        self.easyButton = QtWidgets.QPushButton(self.centralwidget)
        self.easyButton.setGeometry(QtCore.QRect(150, 100, 111, 41))
        self.easyButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.easyButton.setObjectName("easyButton")
        # Connection between Home Page and Easy Game Mode
        self.easyButton.clicked.connect(self.openEasyGame)


        # HARD MODE BUTTON
        self.hardButton = QtWidgets.QPushButton(self.centralwidget)
        self.hardButton.setGeometry(QtCore.QRect(150, 150, 111, 41))
        self.hardButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.hardButton.setObjectName("hardButton")
        # Connection between Home Page and Hard Game Mode
        self.hardButton.clicked.connect(self.openHardGame)


        # QUIT BUTTON
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(340, 250, 51, 32))
        self.quitButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: red;")
        self.quitButton.setObjectName("quitButton")
        # quit game
        self.quitButton.clicked.connect(self.close_application)

        # GAME MODE LABEL
        self.gameModeLabel = QtWidgets.QLabel(self.centralwidget)
        self.gameModeLabel.setGeometry(QtCore.QRect(120, 70, 181, 16))
        self.gameModeLabel.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.gameModeLabel.setObjectName("gameModeLabel")

        # Inside frame structure
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
        MainWindow.setWindowTitle(_translate("MainWindow", "HOME"))
        self.gameLabel.setText(_translate("MainWindow", "Welcome to Count-It-First"))
        self.easyButton.setText(_translate("MainWindow", "EASY"))
        self.hardButton.setText(_translate("MainWindow", "HARD"))
        self.quitButton.setText(_translate("MainWindow", "QUIT"))
        self.gameModeLabel.setText(_translate("MainWindow", "Choose your game mode:"))


# Open the game with GUI frame when method is called
if __name__ == "__main__":
    APP = QtWidgets.QApplication(sys.argv)
    MAINWINDOW = QtWidgets.QMainWindow()
    UI = Ui_MainWindow()
    UI.setupUi(MAINWINDOW)
    MAINWINDOW.show()

    sys.exit(APP.exec_())
