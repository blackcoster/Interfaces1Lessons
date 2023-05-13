# QDateTimeEdit
# QDateEdit
# QTimeEdit
#
# QWidget - QAbstarctSpinBox - QDateTimeEdit - QDateEdit
#
# data = QDateTimeEdit(QTime,parent=)
# data = QDateTimeEdit(parent=)

# setData
# setTime
# dateTime()
# date()
# time()
# setDateTimeRange(min,max)
# setMaximundateTime(datetime)
# setdateRange setTimeRange
# setDisplayFormal    dd.mm.yyyy   mm.dd.yyyy
# setTimeSpex(UTC)
# setCaledarPopup(True)
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QDateTimeEdit, QHBoxLayout, QApplication, QDateEdit, QTimeEdit


class Window(QWidget):
    def __init__(self):
        super().__init__()

        hbox = QHBoxLayout(self)
        time_edit = QDateTimeEdit(self)
        hbox.addWidget(time_edit)
        self.setLayout(hbox)

        self.setGeometry(300,300,350,250)
        self.setWindowTitle('QdateTimeEdit')

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())