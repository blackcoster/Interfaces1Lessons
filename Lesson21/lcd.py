# checkOverflow
# intValue()
# value()
# setSegmentStyle()
# setMode(Hex,Dec,Oct,Bin)

from PyQt5.QtWidgets import QWidget, QCalendarWidget, QLabel, QApplication, QVBoxLayout, QLCDNumber
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('calendar')
        self.resize(600,600)

        self.box = QVBoxLayout()

        self.lcd1 = QLCDNumber(self)
        self.lcd1.setDigitCount(10)
        self.lcd1.display(1234567890)

        self.lcd2 = QLCDNumber(self)
        self.lcd2.setSegmentStyle(QLCDNumber.Flat)
        self.lcd2.setSmallDecimalPoint(True)
        self.lcd2.setDigitCount(10)
        self.lcd2.display(0.123456789)

        self.lcd3 = QLCDNumber(self)
        self.lcd3.setSegmentStyle(QLCDNumber.Filled)
        self.lcd3.display('HELLO')

        self.lcd4 = QLCDNumber(self)
        self.lcd4.setSegmentStyle(QLCDNumber.Outline)
        self.lcd4.setMode(QLCDNumber.Hex)
        self.lcd4.setDigitCount(6)
        self.lcd4.display(666)

        self.setLayout(self.box)
        self.box.addWidget(self.lcd1)
        self.box.addWidget(self.lcd2)
        self.box.addWidget(self.lcd3)
        self.box.addWidget(self.lcd4)




app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
