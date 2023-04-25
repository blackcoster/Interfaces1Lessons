import sys

from PyQt5 import QtCore, QtWidgets

class MyWindow(QtWidgets.QWidget):

    mysignal = QtCore.pyqtSignal(int,int)

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setWindowTitle('Генерация сигнала из программы')
        self.resize(300,100)
        self.button1 = QtWidgets.QPushButton('Нажми меня')
        self.button2 = QtWidgets.QPushButton('кнопка 2')

        box = QtWidgets.QVBoxLayout()
        box.addWidget(self.button1)
        box.addWidget(self.button2)

        self.setLayout(box)
        self.button1.clicked.connect(self.on_clicked_button1)
        self.button2.clicked.connect(self.on_clicked_button2)
        self.mysignal.connect(self.on_mysignal)

    def on_clicked_button1(self):
        print('нажата кнопка button1')

        self.button2.clicked[bool].emit(False)
        # self.button2.click()
        self.mysignal.emit(10,20)


    def on_clicked_button2(self):
        print('нажата кнопка 2')

    def on_mysignal(self,x,y):
        print('обработан mysignal')
        print(f'x = {x}, y = {y}')


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())