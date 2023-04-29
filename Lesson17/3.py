from PyQt5 import QtCore,QtWidgets

class MyWidow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.resize(300,100)

    def changeEvent(self, e):
        if e.type() == QtCore.QEvent.WindowStateChange:
            if self.isMinimized():
                print('окно свернуто')
            elif self.isMaximized():
                print('окно раскрыто до максимальных размеров')
            elif self.isFullScreen():
                print('полноэкранный режим')
            elif self.isActiveWindow():
                print('окно в фокусе ввода')
        # QtWidgets.QWidget.changeEvent(self,e)
        return QtWidgets.QWidget.changeEvent(self, e)

    def showEvent(self, e):
        print('окно отображено')
        QtWidgets.QWidget.showEvent(self, e)

    def hideEvent(self, e):
        print('окно скрыто')
        QtWidgets.QWidget.hideEvent(self,e)

    def moveEvent(self, e):
        print(f'окно подвинуто на x = {e.pos().x()} y = {e.pos().y()}')
        QtWidgets.QWidget.moveEvent(self,e)
import sys
app = QtWidgets.QApplication(sys.argv)
window = MyWidow()
window.show()
sys.exit(app.exec_())
