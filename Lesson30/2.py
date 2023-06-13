from PyQt5 import QtCore,QtWidgets,QtMultimedia
import sys,os

class Window(QtWidgets.QWidget):
    def __init__(self,parent = None):
        QtWidgets.QWidget.__init__(self,parent)

        self.setWindowTitle('Диктофон')

        self.sndEffect = QtMultimedia.QSoundEffect()
        self.sndEffect.setVolume(1)
        path = QtCore.QUrl.fromLocalFile(os.path.abspath('record.wav'))
        self.sndEffect.setSource(path)
        self.sndEffect.loopsRemainingChanged.connect(self.showCount)
        self.sndEffect.playingChanged.connect(self.clearCount)
        vbox = QtWidgets.QVBoxLayout()
        lblPlay = QtWidgets.QLabel('Воспроизвести...')
        vbox.addWidget(lblPlay)
        btnOnce = QtWidgets.QPushButton('один раз')
        btnOnce.clicked.connect(self.playOnce)
        vbox.addWidget(btnOnce)
        btnFour = QtWidgets.QPushButton('четыре раза')
        btnFour.clicked.connect(self.playFour)
        vbox.addWidget(btnFour)
        btnForever = QtWidgets.QPushButton('зациклить')
        btnForever.clicked.connect(self.playForever)
        vbox.addWidget(btnForever)

        stop = QtWidgets.QPushButton('стоп')
        stop.clicked.connect(self.sndEffect.stop)
        vbox.addWidget(stop)

        self.lblStatus = QtWidgets.QLabel('')
        vbox.addWidget(self.lblStatus)
        self.setLayout(vbox)

        self.resize(300,100)

    def playOnce(self):
        self.sndEffect.setLoopCount(1)
        self.sndEffect.play()
    def playFour(self):
        self.sndEffect.setLoopCount(4)
        self.sndEffect.play()
    def playForever(self):
        self.sndEffect.setLoopCount(QtMultimedia.QSoundEffect.Infinite)
        self.sndEffect.play()
        self.lblStatus.setText('Зациклено')

    def showCount(self):
        self.lblStatus.setText(f'Воспроизведено {self.sndEffect.loopCount()-self.sndEffect.loopsRemaining()} раз')

    def clearCount(self):
        if not self.sndEffect.isPlaying():
            self.lblStatus.setText('')

app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())