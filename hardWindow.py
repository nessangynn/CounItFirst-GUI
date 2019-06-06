# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_hard.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import sys

class Ui_hardWindow(object):
    def __init__(self, HARD_PLAYER):
        self.HARD_PLAYER = HARD_PLAYER
        
    def pressedOneButton(self):
        self.HARD_PLAYER.game_logic(1)
        self.current_number()

    def pressedThreeButton(self):
        self.HARD_PLAYER.game_logic(3)
        self.current_number()

    def pressedFiveButton(self):
        self.HARD_PLAYER.game_logic(5)
        self.current_number()

    def on_click(self):
        self.turnLabel.setText('WAITING')
    def off_click(self):
        self.turnLabel.hide()

    def close_application(self):
        sys.exit()

    def generated_number(self):
        self.winNumber.display(self.HARD_PLAYER.gen_number())
        self.winNumber.repaint()

    def current_number(self):
        self.currNumber.display(int(self.HARD_PLAYER.updated_message))
        #print(self.EASY_PLAYER.receive_current_number())
        self.currNumber.repaint()
    
    def print_result(self):
        self.turnLabel.setText(str(self.HARD_PLAYER.updated_message))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(387, 293)
        MainWindow.setStyleSheet("background: #151515;\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.oneButton = QtWidgets.QPushButton(self.centralwidget)
        self.oneButton.setGeometry(QtCore.QRect(20, 110, 91, 81))
        self.oneButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 30px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.oneButton.setObjectName("oneButton")
        #Adding one when it is clicked
        self.oneButton.clicked.connect(self.pressedOneButton)
        self.oneButton.clicked.connect(self.on_click)
        self.oneButton.released.connect(self.off_click)


        self.threeButton = QtWidgets.QPushButton(self.centralwidget)
        self.threeButton.setGeometry(QtCore.QRect(130, 110, 91, 81))
        self.threeButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 30px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.threeButton.setObjectName("threeButton")
        #connection
        self.threeButton.clicked.connect(self.pressedThreeButton)
        self.threeButton.clicked.connect(self.on_click)
        self.threeButton.released.connect(self.off_click)

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
        
        #CURR NUM LCD
        self.currNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.currNumber.setGeometry(QtCore.QRect(150, 50, 111, 31))
        self.currNumber.setObjectName("currNumber")

        #GEN NUMBER LCD
        self.winNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.winNumber.setGeometry(QtCore.QRect(150, 10, 111, 31))
        self.winNumber.setObjectName("winNumber")

        #YOUR TURN LABEL
        self.turnLabel = QtWidgets.QLabel(self.centralwidget)
        self.turnLabel.setGeometry(QtCore.QRect(80, 200, 181, 31))
        self.turnLabel.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 30px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.turnLabel.setObjectName("turnLabel")

        #GENERATE NUMBER BUTTON
        self.genButton = QtWidgets.QPushButton(self.centralwidget)
        self.genButton.setGeometry(QtCore.QRect(270, 30, 91, 41))
        self.genButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.genButton.setObjectName("genButton")
        #generated number display
        self.genButton.clicked.connect(self.generated_number)

        #+5 BUTTON
        self.fiveButton = QtWidgets.QPushButton(self.centralwidget)
        self.fiveButton.setGeometry(QtCore.QRect(240, 110, 91, 81))
        self.fiveButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 30px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.fiveButton.setObjectName("fiveButton")
        #connection
        self.fiveButton.clicked.connect(self.pressedFiveButton)
        self.fiveButton.clicked.connect(self.on_click)
        self.fiveButton.released.connect(self.off_click)

        #QUIT BUTTON
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(330, 210, 51, 32))
        self.quitButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 15px;\n"
"text-align: center;\n"
"color: red;")
        self.quitButton.setObjectName("quitButton")
        #close the game
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
        MainWindow.setWindowTitle(_translate("MainWindow", "HARD MODE"))
        self.oneButton.setText(_translate("MainWindow", "+1"))
        self.threeButton.setText(_translate("MainWindow", "+3"))
        self.winNumLabel.setText(_translate("MainWindow", "Win Number:"))
        self.currNumLabel.setText(_translate("MainWindow", "Current Number:"))
        self.turnLabel.setText(_translate("MainWindow", ""))
        self.genButton.setText(_translate("MainWindow", "GENERATE"))
        self.fiveButton.setText(_translate("MainWindow", "+5"))
        self.quitButton.setText(_translate("MainWindow", "QUIT"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_hardWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
