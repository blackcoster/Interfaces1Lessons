from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtWebEngineWidgets import *
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(5,30,1355,730)
        self.setWindowTitle('WEB')

        self.browser = QWebEngineView(self)
        self.browser.setGeometry(0,0,1355,730)

        self.browser.load(QUrl('https://www.python.org'))
        self.browser.loadFinished.connect(self.pdf_maker)

    def pdf_maker(self):
        self.browser.page().printToPdf('1.pdf')
        self.browser.page().pdfPrintingFinished.connect(lambda: print('готово'))

app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())
