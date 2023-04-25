
from PyQt5 import QtCore, QtWidgets
import time
import sys

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setWindowTitle('часики')
        self.resize(200,100)
        self.timer_id = 0
        self.label = QtWidgets.QLabel('')
        self.label.setAlignment(QtCore.Qt.AlignHCenter)

        self.button1 = QtWidgets.QPushButton('запустить')
        self.button2 = QtWidgets.QPushButton('остановить')

        self.button2.setEnabled(False)

        box = QtWidgets.QVBoxLayout()
        box.addWidget(self.label)
        box.addWidget(self.button1)
        box.addWidget(self.button2)

        self.setLayout(box)
        self.button1.clicked.connect(self.on_clicked_button1)
        self.button2.clicked.connect(self.on_clicked_button2)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.on_timeout)

    def on_clicked_button1(self):
        self.timer.start(1000)
        self.button1.setEnabled(False)
        self.button2.setEnabled(True)

    def on_clicked_button2(self):
        self.timer.stop()
        self.button2.setEnabled(False)
        self.button1.setEnabled(True)

    def on_timeout(self) :
        self.label.setText(time.strftime('%H:%M:%S'))
    #
    # def on_clicked_button1(self):
    #     self.timer_id = self.startTimer(1000, timerType=QtCore.Qt.VeryCoarseTimer)
    #     self.button1.setEnabled(False)
    #     self.button2.setEnabled(True)

    # def on_clicked_button2(self):
    #     if self.timer_id:
    #         self.killTimer(self.timer_id)
    #         self.timer_id = 0
    #         self.button2.setEnabled(False)
    #         self.button1.setEnabled(True)

    # def timerEvent(self, event) :
    #     self.label.setText(time.strftime('%H:%M:%S'))

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())













# <id> = <объект.starttimer(интвервал,type)
# timerEvent(self,)
# killTimer(id)
#
# PreciseTimer - точный
# CoarseTimer
# VeryCoarseTimer