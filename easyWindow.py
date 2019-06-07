# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_easy.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

import sys
#from time import gmtime, strftime
#from datetime import datetime

# ---------- GUI libraries -----------
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer

# EASY-MODE GUI WINDOW
class Ui_easyWindow(object):
    
    # Call a varible EASY_PLAYER which uses all methods of client.py
    # through home.py (HOMEPAGE) in method __init__
    def __init__(self, EASY_PLAYER):
        self.EASY_PLAYER = EASY_PLAYER
        
      
        # def update():
        #     is_number = self.EASY_PLAYER.get_lastest_number()
        #     print("is_number: ")
        #     if (is_number != None):
        #         self.EASY_PLAYER.updated_message = is_number
        #         self.current_number()

        # self.timer = QTimer()
        # self.timer.timeout.connect(update)
        # self.timer.start(10000)
        
# ---------- end of ___init___ -----------

    # +1 button call
    # purpose: everytime a player click +1 button,
    #         it will run all methods call in this function
    #         which belongs to Client.py

    def pressedOneButton(self):
        self.EASY_PLAYER.game_logic(1) #Game loop 1
        self.current_number()
        self.EASY_PLAYER.game_logic2(1) #Game loop 2
        self.current_number()

    # +2 button call
    # same purpose with +1 button

    def pressedTwoButton(self):
        self.EASY_PLAYER.game_logic(2) #Game loop 1
        self.current_number()
        self.EASY_PLAYER.game_logic2(2) #Game loop 2
        self.current_number()

    def display_message(self):
        self.turnLabel.setText(self.EASY_PLAYER.updated_message)

    # QUIT button call (line 186)
    # purpose: when we click "Quit" on GUI, it will exit the game
    def close_application(self):
        sys.exit()

    # QLCD generated number call "winNumber" (line 158)
    # purpose: display generated number on QLCD bar "winNumber"
    def generated_number(self):
        self.winNumber.display(self.EASY_PLAYER.gen_number()) #call gen_number method from Client.py
        self.winNumber.repaint()

    # QLCD current number call "currNumber" (line 155)
    # purpose: update the current number everytime server send repsonse
    def current_number(self):

        if (self.EASY_PLAYER.updated_message == "YOU WIN" or self.EASY_PLAYER.updated_message == "YOU LOSE"):
            self.turnLabel.setText(self.EASY_PLAYER.updated_message)

        else:
            print("A string is being returned from the server: ", str(self.EASY_PLAYER.updated_message))
            self.currNumber.display(int(self.EASY_PLAYER.updated_message))

            #in case we need to check
            self.EASY_PLAYER.updated_number = int(self.EASY_PLAYER.updated_message)
        
        self.currNumber.repaint()
        
    # GUI frame using PyQT5 libraries
    # convert ui_easy.ui (designed by QT Designer) to easyWindow.py using
    # "pyuic5 -x ui_easy.ui -o easyWindow.py"
    def setupUi(self, MainWindow):

        # OUTSIDE FRAME OF UI WINDOW
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(387, 292)
        MainWindow.setStyleSheet("background: #151515;\n"
                                "\n"
                                "")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # ONE BUTTON
        self.oneButton = QtWidgets.QPushButton(self.centralwidget)
        self.oneButton.setGeometry(QtCore.QRect(60, 110, 91, 81))
        self.oneButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
                                    "font-weight: bold;\n"
                                    "font-size: 30px;\n"
                                    "text-align: center;\n"
                                    "color: #e7e7e7;")
        self.oneButton.setObjectName("oneButton")
        # a call back to method "pressedOneButton" (line 43)
        self.oneButton.clicked.connect(self.pressedOneButton)


        # TWO BUTTON
        self.twoButton = QtWidgets.QPushButton(self.centralwidget)
        self.twoButton.setGeometry(QtCore.QRect(170, 110, 91, 81))
        self.twoButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
                                    "font-weight: bold;\n"
                                    "font-size: 30px;\n"
                                    "text-align: center;\n"
                                    "color: #e7e7e7;")
        self.twoButton.setObjectName("twoButton")
        # a call back to method "pressedTwoButton" (line 52)
        self.twoButton.clicked.connect(self.pressedTwoButton)


        # WIN NUMBER LABEL
        self.winNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.winNumLabel.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.winNumLabel.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
                                    "font-weight: bold;\n"
                                    "font-size: 15px;\n"
                                    "text-align: center;\n"
                                    "color: #e7e7e7;")
        self.winNumLabel.setObjectName("winNumLabel")


        # CURRENT NUMBER LABEL
        self.currNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.currNumLabel.setGeometry(QtCore.QRect(10, 50, 121, 31))
        self.currNumLabel.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
                                        "font-weight: bold;\n"
                                        "font-size: 15px;\n"
                                        "text-align: center;\n"
                                        "color: #e7e7e7;")
        self.currNumLabel.setObjectName("currNumLabel")


        # CURRENT NUMBER DISPLAY
        # purpose: let the users to keep track 
        #         which number is at the moment after other player's turn. 
        self.currNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.currNumber.setGeometry(QtCore.QRect(150, 50, 111, 31))
        self.currNumber.setObjectName("currNumber")


        # WIN NUMBER DISPLAY
        # purpose: let the users know what number to be reached in order to win.
        self.winNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.winNumber.setGeometry(QtCore.QRect(150, 10, 111, 31))
        self.winNumber.setObjectName("winNumber")


        # WHOSE TURN TEXT LABEL
        # purpose: user will know whose turn is next and who is the winner/loser at the end.
        self.turnLabel = QtWidgets.QLabel(self.centralwidget)
        self.turnLabel.setGeometry(QtCore.QRect(70, 200, 181, 31))
        self.turnLabel.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 30px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.turnLabel.setObjectName("turnLabel")


        # GENERATE BUTTON
        # purpose: to let users play the generated number - more excited!
        self.genButton = QtWidgets.QPushButton(self.centralwidget)
        self.genButton.setGeometry(QtCore.QRect(270, 30, 91, 41))
        self.genButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.genButton.setObjectName("genButton")
        # Display random number when it is clicked
        self.genButton.clicked.connect(self.generated_number)
        

        #QUIT BUTTON
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(330, 210, 51, 32))
        self.quitButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: red;")
        self.quitButton.setObjectName("quitButton")
        # Quit the app when it is clicked
        self.quitButton.clicked.connect(self.close_application)
        
        #function of the frame
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 387, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "EASY MODE"))
        self.oneButton.setText(_translate("MainWindow", "+1"))
        self.twoButton.setText(_translate("MainWindow", "+2"))
        self.winNumLabel.setText(_translate("MainWindow", "Win Number:"))
        self.currNumLabel.setText(_translate("MainWindow", "Current Number:"))
        self.turnLabel.setText(_translate("MainWindow", " "))
        self.genButton.setText(_translate("MainWindow", "GENERATE"))
        self.quitButton.setText(_translate("MainWindow", "QUIT"))



# this will show up as GUI when call easyWindow.py
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_easyWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
