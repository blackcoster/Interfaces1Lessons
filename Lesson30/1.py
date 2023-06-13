from PyQt5 import QtCore,QtWidgets,QtMultimedia
import sys,os

class Window(QtWidgets.QWidget):
    def __init__(self,parent = None):
        QtWidgets.QWidget.__init__(self,parent)

        self.setWindowTitle('Диктофон')
        self.dictofon = QtMultimedia.QAudioRecorder()
        self.dictofon.setVolume(100)
        path = QtCore.QUrl.fromLocalFile(os.path.abspath('record.wav'))
        self.dictofon.setOutputLocation(path)
        self.dictofon.setAudioInput(self.dictofon.defaultAudioInput())

        self.dictofon.setContainerFormat('audio/x-wav')

        settings = QtMultimedia.QAudioEncoderSettings()
        settings.setCodec('audio/pcm')# настройка кодеков
        settings.setSampleRate(8000) #частота дискретизации
        settings.setChannelCount(1) # одноканальная запись
        settings.setEncodingMode(QtMultimedia.QMultimedia.ConstantQualityEncoding)
        settings.setQuality(QtMultimedia.QMultimedia.VeryLowQuality)

        self.dictofon.setAudioSettings(settings)

        self.dictofon.statusChanged.connect(self.initRecorder)
        self.dictofon.durationChanged.connect(self.showDuration)

        vbox = QtWidgets.QVBoxLayout()
        hbox = QtWidgets.QHBoxLayout()

        self.btnRecord = QtWidgets.QPushButton('Запись')
        self.btnRecord.clicked.connect(self.dictofon.record)
        hbox.addWidget(self.btnRecord)

        self.btnPause = QtWidgets.QPushButton('Пауза')
        self.btnPause.clicked.connect(self.dictofon.pause)
        hbox.addWidget(self.btnPause)

        self.btnStop = QtWidgets.QPushButton('Стоп')
        self.btnStop.clicked.connect(self.dictofon.stop)
        hbox.addWidget(self.btnStop)

        vbox.addLayout(hbox)
        hbox = QtWidgets.QHBoxLayout()
        lblVolume = QtWidgets.QLabel ('Звук')
        hbox.addWidget(lblVolume)
        sldVolume = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        sldVolume.setRange(0,100)
        sldVolume.setTickPosition(QtWidgets.QSlider.TicksAbove)
        sldVolume.setTickInterval(10)
        sldVolume.setValue(100)
        sldVolume.valueChanged.connect(self.dictofon.setVolume)
        hbox.addWidget(sldVolume)
        vbox.addLayout(hbox)

        self.lblStatus = QtWidgets.QLabel('Готово')
        vbox.addWidget(self.lblStatus)

        self.setLayout(vbox)
        self.resize(300,100)

    def initRecorder(self,status):
        if status == QtMultimedia.QMediaRecorder.RecordingStatus:
            self.btnRecord.setEnabled(False)
            self.btnPause.setEnabled(True)
            self.btnStop.setEnabled(True)
            self.lblStatus.setText('Запись')
        elif status == QtMultimedia.QMediaRecorder.PausedStatus:
            self.btnRecord.setEnabled(True)
            self.btnPause.setEnabled(False)
            self.btnStop.setEnabled(True)
            self.lblStatus.setText('Пауза')
        elif status == QtMultimedia.QMediaRecorder.FinalizingStatus:
            self.btnRecord.setEnabled(True)
            self.btnPause.setEnabled(False)
            self.btnStop.setEnabled(False)
            self.lblStatus.setText('Готово')
    def showDuration(self,duration):
        self.lblStatus.setText(f'Записано {duration//1000} секунд')

app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())