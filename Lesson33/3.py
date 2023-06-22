
import sys
from PyQt5 import QtWidgets, QtCore

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('аргументы командной строки')
        self.resize(300,150)
        self.vbox = QtWidgets.QVBoxLayout()

        # для вывода всех аргументов
        # for arg in sys.argv:
        #     lbl = QtWidgets.QLabel(arg)
        #     self.vbox.addWidget(lbl)
        #     print(arg)
        # self.setLayout(self.vbox)

        #для вывода последнего аргумента
        if len(sys.argv) > 1:
            arg = sys.argv[-1]
            lbl = QtWidgets.QLabel(arg)
            self.vbox.addWidget(lbl)
            print(arg)
        self.setLayout(self.vbox)

        # для вывода всех аргументов кроме первого (названия файла)
        if len(sys.argv) > 1:
            args = sys.argv[1:]
            for arg in args:
                lbl = QtWidgets.QLabel(arg)
                self.vbox.addWidget(lbl)
                print(arg)
            self.setLayout(self.vbox)





app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
