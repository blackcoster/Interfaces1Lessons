# QWidget - QProgressBar
# a = QProgressBar(parent=)
#
# setValue(x)
# value()
# text()
# setRange(min,max)
# reset()
# setOrientation()
# setTextDirection
#
# valueChanged.connect

import sys

from PyQt5.QtCore import QBasicTimer
from PyQt5.QtWidgets import QWidget, QProgressBar,QPushButton,QApplication

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QProgressBar')

        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30,40,200,25)

        self.btn = QPushButton("Start",self)
        self.btn.move(40,80)
        self.btn.clicked.connect(self.clickedAction)

        self.timer = QBasicTimer()
        self.step = 0

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return
        self.step +=5
        self.pbar.setValue(self.step)

    def clickedAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100,self)
            self.btn.setText('Stop')

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())