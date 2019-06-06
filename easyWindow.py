# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_easy.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_easyWindow(object):
    def __init__(self, EASY_PLAYER):
        self.EASY_PLAYER = EASY_PLAYER
        
    def pressedOneButton(self):
        self.EASY_PLAYER.game_logic(1)
        #print("Returned from game_logic: ", cur_num)
        self.current_number()

    def pressedTwoButton(self):
        self.EASY_PLAYER.game_logic(2)
        #print("Returned from game_logic: ")
        self.current_number()

    def display_message(self):
        self.turnLabel.setText(self.EASY_PLAYER.updated_message)

    #def on_click(self):
    #self.turnLabel.setText(self.display_message)
    #def off_click(self):
    #self.turnLabel.hide()

    def close_application(self):
        sys.exit()

    def generated_number(self):
        self.winNumber.display(self.EASY_PLAYER.gen_number())
        self.winNumber.repaint()

    def current_number(self):
        self.currNumber.display(int(self.EASY_PLAYER.updated_message))
        #print(self.EASY_PLAYER.receive_current_number())
        self.currNumber.repaint()
    
    def print_result(self):
        self.turnLabel.setText(str(self.EASY_PLAYER.updated_message))


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(387, 292)
        MainWindow.setStyleSheet("background: #151515;\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget)
        self.oneButton.setGeometry(QtCore.QRect(60, 110, 91, 81))
        self.oneButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 30px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.oneButton.setObjectName("oneButton")

        self.oneButton.clicked.connect(self.pressedOneButton)
        #self.oneButton.clicked.connect(self.display_message)
        #self.oneButton.released.connect(self.off_click)


        self.twoButton = QtWidgets.QPushButton(self.centralwidget)
        self.twoButton.setGeometry(QtCore.QRect(170, 110, 91, 81))
        self.twoButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 30px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.twoButton.setObjectName("twoButton")

        self.twoButton.clicked.connect(self.pressedTwoButton)
        #self.twoButton.clicked.connect(self.display_message)
        #self.twoButton.released.connect(self.off_click)

        self.winNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.winNumLabel.setGeometry(QtCore.QRect(10, 10, 121, 31))
        self.winNumLabel.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.winNumLabel.setObjectName("winNumLabel")
        self.currNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.currNumLabel.setGeometry(QtCore.QRect(10, 50, 121, 31))
        self.currNumLabel.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.currNumLabel.setObjectName("currNumLabel")

        #CURRENT NUMBER DISPLAY
        self.currNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.currNumber.setGeometry(QtCore.QRect(150, 50, 111, 31))
        self.currNumber.setObjectName("currNumber")

        #WIN NUMBER DISPLAY
        self.winNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.winNumber.setGeometry(QtCore.QRect(150, 10, 111, 31))
        self.winNumber.setObjectName("winNumber")

        #WHOSE TURN TEXT LABEL
        self.turnLabel = QtWidgets.QLabel(self.centralwidget)
        self.turnLabel.setGeometry(QtCore.QRect(70, 200, 181, 31))
        self.turnLabel.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 30px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.turnLabel.setObjectName("turnLabel")

        #GENERATE BUTTON
        self.genButton = QtWidgets.QPushButton(self.centralwidget)
        self.genButton.setGeometry(QtCore.QRect(270, 30, 91, 41))
        self.genButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.genButton.setObjectName("genButton")

        #Display random number when it is clicked
        self.genButton.clicked.connect(self.generated_number)

        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(330, 210, 51, 32))
        self.quitButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: red;")
        self.quitButton.setObjectName("quitButton")
        self.quitButton.clicked.connect(self.close_application)

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




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_easyWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
