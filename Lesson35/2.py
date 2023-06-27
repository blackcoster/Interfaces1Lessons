import sys

from PyQt5 import QtWidgets,QtTextToSpeech

class Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TextToSpeech')
        self.resize(300,150)
        self.vbox = QtWidgets.QVBoxLayout()
        self.line = QtWidgets.QLineEdit()
        self.line.setPlaceholderText('Введите текст')
        self.btn = QtWidgets.QPushButton('Преобразовать')
        self.vbox.addWidget(self.line)
        self.vbox.addWidget(self.btn)
        self.setLayout(self.vbox)
        engine = QtTextToSpeech.QTextToSpeech.availableEngines()[0]
        self.text_to_speech=QtTextToSpeech.QTextToSpeech(engine)

        self.btn.clicked.connect(self.say_text)

    def say_text(self):
        text = self.line.text()
        self.text_to_speech.say(text)

app = QtWidgets.QApplication([])
window = Window()
window.show()
sys.exit(app.exec_())
