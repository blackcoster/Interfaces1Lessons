from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *

# ДОМАШКУ НЕОБХОДИМО ДОПОЛНИТЬ САМОСТОЯТЕЛЬНО !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(1000,599)
        self.setWindowTitle('гугл')

        self.hbox = QHBoxLayout()
        self.vbox = QVBoxLayout()

        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText('Введите ссылку на нужный сайт')
        self.btn1 = QPushButton('перейти')
        self.btn2 = QPushButton('Пдфнуть')
        self.browser = QWebEngineView()

        self.btn1.clicked.connect(self.search)
        self.btn2.clicked.connect(self.pdf_maker)

        self.browser.load(QUrl('https://google.com'))

        self.hbox.addWidget(self.line_edit)
        self.hbox.addWidget(self.btn1)
        self.hbox.addWidget(self.btn2)

        self.vbox.addLayout(self.hbox)
        self.vbox.addWidget(self.browser)
        self.setLayout(self.vbox)

    def search(self):
        text = self.line_edit.text()
        self.browser.load(QUrl(text))
    def pdf_maker(self):
        pass # сюда вставьте код самостоятельно из кода webEngineView.py

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
