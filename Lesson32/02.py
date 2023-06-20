from PyQt5 import QtCore, QtWidgets,QtGui,QtWinExtras
import sys

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('панель управления')
        self.icon1 = QtGui.QIcon('pic1.png')
        self.icon2 = QtGui.QIcon('pic2.png')
        self.taskbarButton = QtWinExtras.QWinTaskbarButton(parent=self)
        hbox = QtWidgets.QHBoxLayout()
        btnIcon1=QtWidgets.QPushButton(self.icon1,'Значок 1')
        btnIcon2 = QtWidgets.QPushButton(self.icon2, 'Значок 2')
        btnIcon1.clicked.connect(self.setIcon1)
        btnIcon2.clicked.connect(self.setIcon2)
        hbox.addWidget(btnIcon1)
        hbox.addWidget(btnIcon2)
        btnClear = QtWidgets.QPushButton('Убрать значок')
        hbox.addWidget(btnClear)
        btnClear.clicked.connect(self.taskbarButton.clearOverlayIcon)
        self.setLayout(hbox)
        self.resize(200,50)

    def showEvent(self,event):
        self.taskbarButton.setWindow(self.windowHandle())
    def setIcon1(self):
        self.taskbarButton.setOverlayIcon(self.icon1)
    def setIcon2(self):
        self.taskbarButton.setOverlayIcon(self.icon2)

app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())

