import sys
from PyQt5.QtCore import Qt
from PyQt5.QtTextToSpeech import QTextToSpeech,QVoice
from PyQt5.QtWidgets import qApp, QApplication, QComboBox, QFormLayout, QHBoxLayout, QLineEdit, QPushButton, QSlider, \
    QWidget, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super(QWidget,self).__init__()



        layout = QFormLayout(self)

        hbox = QVBoxLayout(self)
        self.text = QLineEdit('Type...')
        self.text.setClearButtonEnabled(True)
        hbox.addWidget(self.text)
        self.btn = QPushButton('Play')
        hbox.addWidget(self.btn)
        self.text.returnPressed.connect(self.btn.animateClick)
        self.btn.clicked.connect(self.say)
        layout.addRow('Text: ',hbox)
        self.voice = QComboBox()
        layout.addRow('Voice: ',self.voice)

        self.volume = QSlider(Qt.Horizontal)
        self.volume.setMinimum(0)
        self.volume.setMaximum(100)
        self.volume.setValue(100)
        layout.addRow('Volume: ',self.volume)

        engine = QTextToSpeech.availableEngines()[0]
        self.text_to_speech = QTextToSpeech(engine)
        self.text_to_speech.stateChanged.connect(self.stateChanged)
        self.voices = []
        for voice in self.text_to_speech.availableVoices():
            self.voices.append(voice)
            self.voice.addItem(voice.name())

    def say(self):
        self.btn.setEnabled(False)
        self.text_to_speech.setVoice(self.voices[self.voice.currentIndex()])
        self.text_to_speech.setVolume(float(self.volume.value())/100)
        self.text_to_speech.say(self.text.text())

    def stateChanged(self,state):
        if state==QTextToSpeech.State.Ready:
            self.btn.setEnabled(True)

app = QApplication([])
window = Window()
window.show()
sys.exit(app.exec_())


