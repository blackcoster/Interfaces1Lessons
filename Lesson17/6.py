from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Pole(QtWidgets.QLineEdit):
    def __init__(self):
        QtWidgets.QLineEdit.__init__(self)
        self.id = None

    def event(self, e):
        if e.type() == QtCore.QEvent.Shortcut:
            if self.id == e.shortcutId():
                self.setFocus()
                return True
        return QtWidgets.QLineEdit.event(self,e)


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.resize(300,100)

        self.text = QtWidgets.QLabel('Установить фокус на поле &1')
        self.pole1 = QtWidgets.QLineEdit()
        self.text.setBuddy(self.pole1)

        self.pole2 = Pole()
        self.pole2.id = self.pole2.grabShortcut(QtGui.QKeySequence.mnemonic('&2'))

        self.button  = QtWidgets.QPushButton('&Убрать фокус с поля 1')
        self.box = QtWidgets.QVBoxLayout()
        self.box.addWidget(self.text)
        self.box.addWidget(self.pole1)
        self.box.addWidget(self.pole2)
        self.box.addWidget(self.button)
        self.setLayout(self.box)

        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.pole1.clearFocus()

app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())