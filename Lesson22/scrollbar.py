# QWidget - QAbstractSlider - QScrollbar

# a = QSlider(parent=)
# a = QSlider(orientation,parent=)
# QScrollArea

from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,300,500,400)
        self.setWindowTitle('QSlider')

        self.scroll = QScrollBar(self)
        self.scroll.setGeometry(100,50,30,200)

        self.label = QLabel('пример',self)
        self.label.setGeometry(200,100,300,80)

        self.scroll.valueChanged.connect(lambda :self.metod())

    def metod(self):
        value = self.scroll.value()
        self.label.setText(f'Значение {value}')



app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())

