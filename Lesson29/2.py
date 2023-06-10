from PyQt5 import QtCore, QtWidgets,QtMultimedia
import sys

class Window(QtWidgets.QWidget):
    def __init__(self,parent=None):
        QtWidgets.QWidget.__init__(self,parent)
        self.setWindowTitle('Метаданные')
        self.mplPlayer = QtMultimedia.QMediaPlayer()
        self.mplPlayer.setVolume(50)
        self.mplPlayer.mediaStatusChanged.connect(self.showMetaData)
        vbox = QtWidgets.QVBoxLayout()
        btnOpen = QtWidgets.QPushButton('Открыть файл...')
        btnOpen.clicked.connect(self.openFile)
        vbox.addWidget(btnOpen)
        self.textOutput = QtWidgets.QTextEdit()
        self.textOutput.setReadOnly(True)
        vbox.addWidget(self.textOutput)
        self.setLayout(vbox)
        self.resize(300,250)

    def openFile(self):
        file = QtWidgets.QFileDialog.getOpenFileUrl(parent = self,caption='Выберите звуковой файл',
                                                    filter ='Звуковые файлы (*.mp3)')
        self.mplPlayer.setMedia(QtMultimedia.QMediaContent(file[0]))
    def showMetaData(self,state):
        self.textOutput.clear()
        if state == QtMultimedia.QMediaPlayer.LoadedMedia:
            keys = self.mplPlayer.availableMetaData()
            s = ''
            for k in keys:
                v = self.mplPlayer.metaData(k)
                if v:
                    if v is list:
                        v = ', '.join(v)

                    s += "<strong>"+k+"</strong>:"+str(v)+'<br>'
            self.textOutput.setHtml(s)
app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
