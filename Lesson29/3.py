from PyQt5 import QtCore, QtWidgets,QtMultimedia, QtMultimediaWidgets
import sys

class Window(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.setWindowTitle('Видео')

        self.mplPlayer = QtMultimedia.QMediaPlayer()
        self.mplPlayer.setVolume(50)

        self.mplPlayer.mediaStatusChanged.connect(self.initPlayer) # запуск плеера
        self.mplPlayer.stateChanged.connect(self.setPlayerState) #блокиратор кнопочек

        vbox = QtWidgets.QVBoxLayout()
        btnOpen = QtWidgets.QPushButton('Открыть файл...')
        btnOpen.clicked.connect(self.openFile)
        vbox.addWidget(btnOpen)


        video = QtMultimediaWidgets.QVideoWidget()
        video.setAspectRatioMode(QtCore.Qt.KeepAspectRatio)
        self.mplPlayer.setVideoOutput(video)
        vbox.addWidget(video)
        self.sldPosition = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        self.sldPosition.setMinimum(0)
        self.sldPosition.valueChanged.connect(self.mplPlayer.setPosition)# куда слайдер - туда и плеер
        self.mplPlayer.positionChanged.connect(self.sldPosition.setValue)# куда плеер- туда и слайдер
        self.sldPosition.setEnabled(False)
        vbox.addWidget(self.sldPosition)
        hbox = QtWidgets.QHBoxLayout()
        self.btnPlay = QtWidgets.QPushButton('Пуск')
        self.btnPlay.clicked.connect(self.mplPlayer.play)
        self.btnPlay.setEnabled(False)
        hbox.addWidget(self.btnPlay)
        self.btnPause = QtWidgets.QPushButton('Пауза')
        self.btnPause.clicked.connect(self.mplPlayer.pause)
        self.btnPause.setEnabled(False)
        hbox.addWidget(self.btnPause)
        self.btnStop = QtWidgets.QPushButton('Стоп')
        self.btnStop.clicked.connect(self.mplPlayer.stop)
        self.btnStop.setEnabled(False)
        hbox.addWidget(self.btnStop)
        vbox.addLayout(hbox)
        hbox = QtWidgets.QHBoxLayout()
        lblVolume = QtWidgets.QLabel('Громкость')
        hbox.addWidget(lblVolume)
        sldVolume = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        sldVolume.setRange(0,100)
        sldVolume.setTickPosition(QtWidgets.QSlider.TicksAbove)
        sldVolume.setTickInterval(10)
        sldVolume.setValue(50)
        sldVolume.valueChanged.connect(self.mplPlayer.setVolume)
        hbox.addWidget(sldVolume)
        btnMute = QtWidgets.QPushButton('Тихо!')
        btnMute.setCheckable(True)
        btnMute.toggled.connect(self.mplPlayer.setMuted)
        hbox.addWidget(btnMute)
        vbox.addLayout(hbox)
        self.setLayout(vbox)
        self.resize(300,300)
    def initPlayer(self,state):
        if state == QtMultimedia.QMediaPlayer.LoadedMedia:
            self.mplPlayer.stop()
            self.btnPlay.setEnabled(True)
            self.btnPause.setEnabled(False)
            self.sldPosition.setEnabled(True)
            self.sldPosition.setMaximum(self.mplPlayer.duration())
        elif state == QtMultimedia.QMediaPlayer.EndOfMedia:
            self.mplPlayer.stop()
            self.btnPlay.setEnabled(False)
            self.btnPause.setEnabled(False)
            self.btnStop.setEnabled(False)
            self.sldPosition.setValue(0)
            self.sldPosition.setEnabled(False)
        elif state == QtMultimedia.QMediaPlayer.NoMedia or state == QtMultimedia.QMediaPlayer.InvalidMedia:
            self.btnPlay.setEnabled(False)
            self.btnPause.setEnabled(False)
            self.btnStop.setEnabled(False)
            self.sldPosition.setValue(0)
            self.sldPosition.setEnabled(False)

    def setPlayerState(self, state):
        if state == QtMultimedia.QMediaPlayer.StoppedState:
            self.sldPosition.setValue(0)
            self.btnPlay.setEnabled(True)
            self.btnPause.setEnabled(False)
            self.btnStop.setEnabled(False)
        elif state == QtMultimedia.QMediaPlayer.PlayingState:
            self.btnPlay.setEnabled(False)
            self.btnPause.setEnabled(True)
            self.btnStop.setEnabled(True)
        elif state == QtMultimedia.QMediaPlayer.PausedState:
            self.btnPlay.setEnabled(True)
            self.btnPause.setEnabled(False)
            self.btnStop.setEnabled(True)

    def openFile(self):
        file = QtWidgets.QFileDialog.getOpenFileUrl(parent = self,caption='Выберите звуковой файл',
                                                    filter ='Видеофайлы (*.avi *.mp4)')
        self.mplPlayer.setMedia(QtMultimedia.QMediaContent(file[0]))

app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())

