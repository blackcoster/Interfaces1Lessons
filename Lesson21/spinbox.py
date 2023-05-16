# QWidget - QAbstractSpinbox - QSpinBox
# QWidget - QAbstractSpinbox - QDoubleSpinBox

from PyQt5.QtWidgets import QWidget,QSpinBox,QDoubleSpinBox,QHBoxLayout,QLabel,QApplication
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('spinbox')
        self.setGeometry(300,300,350,250)

        box = QHBoxLayout()
        spin = QSpinBox(self)

        self.label = QLabel('0',self)
        box.addSpacing(15)
        box.addWidget(spin)
        box.addWidget(self.label)

        self.setLayout(box)

        spin.valueChanged.connect(self.func)

    def func(self,value):
        self.label.setText(str(value))

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())