from PyQt5 import QtCore, QtWidgets, uic
import sys


# если хотим создать класс для создания окон, вместо одного экземпляра окна

class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        Form, Base = uic.loadUiType('untitled.ui')
        self.ui = Form()
        self.ui.setupUi(self)

        self.ui.button.clicked.connect(QtWidgets.qApp.quit)


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
