import sys
from PyQt5 import QtWidgets, QtCore


class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('аргументы командной строки')
        self.resize(300, 150)
        self.vbox = QtWidgets.QVBoxLayout()
        self.textEdit = QtWidgets.QTextEdit()
        self.vbox.addWidget(self.textEdit)
        self.setLayout(self.vbox)

        if len(sys.argv) > 1:
            try:
                with open(sys.argv[1],encoding='utf-8') as file:
                    text = file.read()
                self.textEdit.setText(text)
            except FileNotFoundError:
                QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Critical,
                                      'Ошибка','данного файла не существует',
                                      QtWidgets.QMessageBox.StandardButton.Ok).exec()



app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())