import sys

from PyQt5 import QtCore,QtWidgets

class MyWindow(QtWidgets.QWidget):
    def __init__(self,parent = None):
        QtWidgets.QWidget.__init__(self,parent)

        self.btnMin = QtWidgets.QPushButton('Свернуть')
        self.btnMax = QtWidgets.QPushButton('Развернуть')
        self.btnFull = QtWidgets.QPushButton('Полный экран')
        self.btnNormal = QtWidgets.QPushButton('Нормальный вид')

        box = QtWidgets.QVBoxLayout()
        box.addWidget(self.btnMin)
        box.addWidget(self.btnMax)
        box.addWidget(self.btnFull)
        box.addWidget(self.btnNormal)

        self.setLayout(box)

        self.btnMin.clicked.connect(self.on_min)
        self.btnMax.clicked.connect(self.on_max)
        self.btnFull.clicked.connect(self.on_full)
        self.btnNormal.clicked.connect(self.on_normal)

    def on_min(self):
        self.showMinimized()

    def on_max(self):
        self.showMaximized()


        # self.activateWindow()
        # self.setWindowFlag()

    def on_full(self):
        self.showFullScreen()

    def on_normal(self):
        self.showNormal()

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.setWindowTitle('Изменение формата')
window.resize(300,100)
window.show()

sys.exit(app.exec_())
