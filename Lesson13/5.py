import sys

from PyQt5 import  QtWidgets, uic



class MyWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        uic.loadUi('untitled.ui',self) # добавляем селф чтобы обращаться через self.button/label
        self.button.clicked.connect(QtWidgets.qApp.quit)


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
