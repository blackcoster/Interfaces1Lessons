# QWidget - QFrame - QAbstractScrollArea - QTextEdit
#
# a = QTextEdit(parent)
# a = QTextEdit(text,parent)

# setText
# setPlaintext
# setHtml
# insertPlainText
# append(text)
# toPlainText()
# toHtml
# clear()
# selectAll()
# zoomIn zoomOut
# cut() copy() paste() canPaste() undo() redo()
#
# cursorPositionChanged
# tectChanged
# copyAvailable


import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTextEdit, QPushButton, QVBoxLayout


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.resize(300,270)
        self.setWindowTitle('QTextEdit')

        self.textEdit = QTextEdit()

        self.button1 = QPushButton('Показать текст')
        self.button2 = QPushButton('Показать другой текст')

        box = QVBoxLayout()
        box.addWidget(self.textEdit)
        box.addWidget(self.button1)
        box.addWidget(self.button2)

        self.button1.clicked.connect(self.btn1)
        self.button2.clicked.connect(self.btn2)
        self.setLayout(box)
    def btn1(self):
        self.textEdit.insertPlainText('Показываю текст') # вставляем текст туда где курсор

    def btn2(self): # удаляем что было и вставляем текст
        self.textEdit.setHtml("<font color = 'red' size = '6'> <red> Показываю другой текст </ font>")



app = QApplication(sys.argv)
win = Window()
win.show()
sys.exit(app.exec_())