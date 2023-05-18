# QWidget - QAbstractSlider - QDial
#
# setNotchesVisible()
# setNotchTarget()
# setWrapping()

from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        grid = QGridLayout()
        self.setLayout(grid)

        self.dial = QDial()
        self.dial.setMinimum(0)
        self.dial.setMaximum(100)
        self.dial.setValue(40)
        self.dial.setNotchesVisible(True)
        self.dial.setWrapping(True)
        self.dial.valueChanged.connect(self.sliderMoved)
        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QSlider')
        grid.addWidget(self.dial)
    def sliderMoved(self):
        print(f'dial value - {self.dial.value()}')
app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
