import time

from PyQt5 import QtCore, QtWidgets,QtGui,QtWinExtras
import sys

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('панель управления')
        self.icon1 = QtGui.QIcon('pic1.png')
        self.icon2 = QtGui.QIcon('pic2.png')
        self.taskbarButton = QtWinExtras.QWinTaskbarButton(parent=self)
        vbox = QtWidgets.QVBoxLayout()
        self.progress = self.taskbarButton.progress()
        self.progress.setRange(0,10)
        self.progress.show()
        btnStart = QtWidgets.QPushButton('Старт')
        vbox.addWidget(btnStart)
        btnStart.clicked.connect(self.start)

        btnPause = QtWidgets.QPushButton('Пауза')
        vbox.addWidget(btnPause)
        btnPause.clicked.connect(self.progress.pause)

        btnStop = QtWidgets.QPushButton('Стоп')
        vbox.addWidget(btnStop)
        btnStop.clicked.connect(self.progress.stop)

        btnResume = QtWidgets.QPushButton('Продолжить')
        vbox.addWidget(btnResume)
        btnResume.clicked.connect(self.progress.resume)
        self.setLayout(vbox)
        self.resize(200,50)
    def showEvent(self,evt):
        self.taskbarButton.setWindow(self.windowHandle())

    def start(self):
        i = 0
        while i <11:
            if not self.progress.isPaused() and not self.progress.isStopped():
                self.progress.setValue(i)
                i+=1
            time.sleep(1)
            QtWidgets.qApp.processEvents()
        self.progress.reset()



app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
