import sys

from PyQt5 import QtCore, QtWidgets

# все то же самое но в стиле ООП

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.label = QtWidgets.QLabel('Привет мир')
        #другой способ выравнивания по центру
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.button = QtWidgets.QPushButton('кнопка')
        # self.button1 = QtWidgets.QPushButton('кнопка')
        # self.button2 = QtWidgets.QPushButton('кнопка')

        self.box = QtWidgets.QVBoxLayout()

        self.box.addWidget(self.label)
        self.box.addWidget(self.button)
        # self.box.addWidget(self.button1)
        # self.box.addWidget(self.button2)

        self.setLayout(self.box)

        self.button.clicked.connect(QtWidgets.qApp.quit)


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle('OOP style')
window.resize(300, 100)
window.show()
sys.exit(app.exec_())
