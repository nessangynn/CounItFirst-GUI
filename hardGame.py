# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_hardGame.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_hardWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(325, 293)
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
        self.twoButton = QtWidgets.QPushButton(self.centralwidget)
        self.twoButton.setGeometry(QtCore.QRect(170, 110, 91, 81))
        self.twoButton.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 30px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.twoButton.setObjectName("twoButton")
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
        self.currNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.currNumber.setGeometry(QtCore.QRect(150, 50, 111, 31))
        self.currNumber.setObjectName("currNumber")
        self.winNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.winNumber.setGeometry(QtCore.QRect(150, 10, 111, 31))
        self.winNumber.setObjectName("winNumber")
        self.turnLabel = QtWidgets.QLabel(self.centralwidget)
        self.turnLabel.setGeometry(QtCore.QRect(60, 200, 201, 31))
        self.turnLabel.setStyleSheet("font-family: \'Helvetica Neue\', sans-serif;\n"
"font-weight: bold;\n"
"font-size: 30px;\n"
"text-align: center;\n"
"color: #e7e7e7;")
        self.turnLabel.setObjectName("turnLabel")
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
    ui = Ui_hardWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
