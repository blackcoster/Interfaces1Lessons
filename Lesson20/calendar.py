
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QDateTimeEdit, QHBoxLayout, QApplication, QDateEdit, QTimeEdit


class Window(QWidget):
    def __init__(self):
        super().__init__()

        hbox = QHBoxLayout(self)
        time_edit = QDateTimeEdit(self)
        time_edit.setCalendarPopup(True)
        hbox.addWidget(time_edit)
        self.setLayout(hbox)

        self.setGeometry(300,300,350,250)
        self.setWindowTitle('QdateTimeEdit')

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())