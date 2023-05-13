import sys
from PyQt5.QtWidgets import QWidget, QLabel, QDateTimeEdit, QHBoxLayout, QApplication, QDateEdit, QTimeEdit, \
    QVBoxLayout, QLineEdit, QPushButton


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.polevvoda1 = QLineEdit(self)
        self.polevvoda2 = QLineEdit(self)

        vbox = QVBoxLayout(self)
        hbox = QHBoxLayout(self)
        self.time_edit = QDateTimeEdit(self)
        hbox.addWidget(self.time_edit)
        self.btn = QPushButton('Сохранить', self)

        self.btn.clicked.connect(self.onClicked)

        vbox.addWidget(self.polevvoda1)
        vbox.addWidget(self.polevvoda2)
        vbox.addLayout(hbox)
        vbox.addWidget(self.btn)
        self.setLayout(vbox)

        self.setGeometry(300,300,350,250)
        self.setWindowTitle('QdateTimeEdit')

    def onClicked(self):
        self.name = self.polevvoda1.text()
        self.surname = self.polevvoda2.text()
        self.vremya = str(self.time_edit.dateTime())

        # print(self.name)
        # print(self.surname)
        # print(self.vremya)

        with open('file.txt','a') as file:
            file.write(self.name+'\n')
            file.write(self.surname+'\n')
            file.write(self.vremya+'\n')
            file.write('---------------')
            file.close()


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())

# with open('file.txt','w') as file:
#             file.write(window.name)
#             file.write(window.surname)
#             file.write(window.vremya)