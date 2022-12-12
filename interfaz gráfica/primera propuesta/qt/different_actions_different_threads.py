# -*- coding: utf-8 -*-
# __ <("-")> __


from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import random
import threading
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        pg.setConfigOption('background', 'w')
        pg.setConfigOption('foreground', 'k')
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setWindowTitle("asdasd")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.widget = pg.PlotWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 30, 331, 391))
        self.widget.setStyleSheet("border: 1px solid black")
        self.widget.setObjectName("widget")

        
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(410, 40, 151, 111))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setText("asdasdaa")
        self.pushButton.clicked.connect(lambda: threading.Thread(target=self.plot).start())

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(QtCore.QRect(410, 200, 151, 111))
        self.pushButton2.setObjectName("pushButton")
        self.pushButton2.setText("aaaa")
        self.pushButton2.clicked.connect(lambda: threading.Thread(target=self.change_name).start())
        MainWindow.setCentralWidget(self.centralwidget)


    def plot(self):  
        while True:
            hour = [1,2,3,4,5,6,7,8,9,10]
            temperature = [30,32,34,32,33,31,29,32,35,45]
            self.widget.plot([random.choice(hour), random.choice(hour)], 
            [random.choice(temperature), random.choice(temperature)], clear=True)
            time.sleep(0.5)

    def change_name(self):
        lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        self.pushButton2.setText(random.choice(lista))
if __name__ == "__main__":
   
    def run():
        import sys
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    threading.Thread(target=run()).start()
