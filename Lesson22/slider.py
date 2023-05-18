# QWidget - QAbstactSlider - QSlider
#
# a = QSlider(parent=)
# a = QSlider(orientation,parent=)
# setValue(x)
# value()
# setSliderPosition()
# sliderPosition()
# setOrientation()
# setSingleStep()

# actionTrigered
# rangeChanged()
# sliderPressed
# sliderReleased
# valueChanged


import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QProgressBar, QPushButton, QApplication, QSlider


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QSlider')

        sld = QSlider(Qt.Horizontal,self)
        sld.setGeometry(80,40,100,30)
        sld.setSingleStep(5)
        sld.setPageStep(20)
        sld.setTickPosition(QSlider.TicksBothSides)



app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
