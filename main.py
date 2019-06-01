import sys
from client import client
import home
from PyQt5 import QtCore, uic, QtWidgets

UIClass, QtBaseClass = uic.loadUiType("ui_home.ui")

class MyApp(UIClass, QtBaseClass):
    def __init__(self):
        UIClass.__init__(self)
        QtBaseClass.__init__(self)
        self.setupUi(self)

if __name__ == "__main__":
    #app = QtWidgets.QApplication(sys.argv)
    # window = MyApp()
    # window.show()
    
    # player = client()

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = home.Ui_MainWindow()
    ui.setupUi(MainWindow)

    sys.exit(app.exec_())


    