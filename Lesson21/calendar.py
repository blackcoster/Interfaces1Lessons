# QWidget - QCalendarWidget
#
# QCalendarWidget(parent)
# setSelecteddate(date)
# selectedDate()
# setDateRange(QDate,QDate)
# monthShown()
# showToday()
# showNextMonth()
# setFirstDayOfWeek('monday')
# selctionchanged
# currentPageChanged
# clicked

import sys

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QWidget,QCalendarWidget,QLabel,QApplication
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('calendar')
        self.setGeometry(300,300,350,350)

        calendar = QCalendarWidget(self)
        # calendar.setGridVisible(True)
        calendar.move(20,20)

        self.label = QLabel(self)

        calendar.clicked[QDate].connect(self.showDate)

        date = calendar.selectedDate()
        self.label.setText(date.toString())

    def showDate(self,date):
        self.label.setText(date.toString())

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
