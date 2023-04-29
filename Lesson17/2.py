from PyQt5 import QtCore, QtWidgets
import sys

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.resize(300,100)

    def event(self, e):
        if e.type() == QtCore.QEvent.KeyPress:
            print('нажата клавиша на клавиатуре')
            print(f' код - {e.key()}, текст - {e.text()}')
        elif e.type() == QtCore.QEvent.Close:
            print('окно закрыто')
        elif e.type() == QtCore.QEvent.MouseButtonPress:
            print(f'щелчок мышью в координатах {e.x(),e.y()}')

        return QtWidgets.QWidget.event(self,e)

app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())