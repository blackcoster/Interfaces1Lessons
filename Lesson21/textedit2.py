import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout, QLineEdit, QTextBrowser


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(300,270)
        self.setWindowTitle('QTextEdit')

        self.le = QLineEdit()
        self.te = QTextBrowser()

        self.te.setAcceptRichText(True)
        self.te.setOpenExternalLinks(True)

        self.button = QPushButton('Clear')
        box = QVBoxLayout()
        box.addWidget(self.le)
        box.addWidget(self.te)
        box.addWidget(self.button)
        self.setLayout(box)

        self.le.returnPressed.connect(self.func)
        self.button.clicked.connect(self.clean)
    def func(self):
        text = self.le.text()
        self.te.append(text)
        self.le.clear()

    def clean(self):
        self.te.clear()

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
