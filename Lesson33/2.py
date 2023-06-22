from PyQt5 import QtCore,QtWidgets,QtGui,QtWinExtras
import sys

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('список быстрого доступа')

        icon1 = QtGui.QIcon('pic1.png')
        icon2 = QtGui.QIcon('pic2.png')
        icon3 = QtGui.QIcon('img.jpg')

        self.thumbnailToolBar = QtWinExtras.QWinThumbnailToolBar(self)

        button1 = QtWinExtras.QWinThumbnailToolButton(self)
        button1.setIcon(icon1)
        button1.setToolTip('кнопка 1')
        button1.setDismissOnClick(True) # убираем превью по нажатию
        button1.clicked.connect(self.bt1)
        self.thumbnailToolBar.addButton(button1)

        button2 = QtWinExtras.QWinThumbnailToolButton(self)
        button2.setIcon(icon2)
        button2.setToolTip('кнопка 2')
        button2.clicked.connect(self.bt2)
        self.thumbnailToolBar.addButton(button2)


        button0 = QtWinExtras.QWinThumbnailToolButton(self)
        button0.setInteractive(False)
        button0.setFlat(True)
        self.thumbnailToolBar.addButton(button0)

        button3 = QtWinExtras.QWinThumbnailToolButton(self)
        button3.setIcon(icon3)
        button3.setToolTip('кнопка 3')
        button3.clicked.connect(self.bt3)
        self.thumbnailToolBar.addButton(button3)

        vbox = QtWidgets.QVBoxLayout()
        self.text = QtWidgets.QLabel(self)
        vbox.addWidget(self.text)
        close = QtWidgets.QPushButton('close')
        close.clicked.connect(QtWidgets.qApp.quit)
        vbox.addWidget(close)
        self.setLayout(vbox)
        self.resize(200,100)

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        self.thumbnailToolBar.setWindow(self.windowHandle())

    def bt1(self):
        self.text.setText('нажата кнопка 1')

    def bt2(self):
        self.text.setText('нажата кнопка 2')

    def bt3(self):
        self.text.setText('нажата кнопка 3')

app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())