from PyQt5 import QtWidgets

class PoleVvoda(QtWidgets.QLineEdit):
    def __init__(self,id):
        QtWidgets.QLineEdit.__init__(self)
        self.id = id

    def focusInEvent(self, e):
        print(f'поле {self.id} получило фокус')
        QtWidgets.QLineEdit.focusInEvent(self,e)

    def focusOutEvent(self, e):
        print(f'поле {self.id} потеряло фокус')
        QtWidgets.QLineEdit.focusOutEvent(self,e)


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.resize(300,100)

        self.button = QtWidgets.QPushButton('Установить фокус на поле 2')
        self.pole1 = PoleVvoda(1)
        self.pole2 = PoleVvoda(2)
        # self.button2 = QtWidgets.QPushButton('кнопка')

        self.box = QtWidgets.QVBoxLayout()
        self.box.addWidget(self.button)
        self.box.addWidget(self.pole1)
        self.box.addWidget(self.pole2)
        # self.box.addWidget(self.button2)

        self.setLayout(self.box)

        self.button.clicked.connect(self.on_clicked)
        # self.button2.clicked.connect(self.y)

        QtWidgets.QWidget.setTabOrder(self.pole1,self.pole2)
        QtWidgets.QWidget.setTabOrder(self.pole2, self.button)
    # def y(self):
    #     print('ого шорткат')
    def on_clicked(self):
        self.pole2.setFocus()

import sys
app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())