import sys

from PyQt5 import QtCore,QtGui,QtWidgets
import time

class MyWindow(QtWidgets.QPushButton):
    def __init__(self):
        QtWidgets.QPushButton.__init__(self)
        self.setText('закрыть окно')
        self.clicked.connect(QtWidgets.qApp.quit)

    def load_data(self,ekran_zagruzki):
        for i in range(1,11):
            time.sleep(1)
            ekran_zagruzki.showMessage(f'Загрузка данных {i*10}%',QtCore.Qt.AlignHCenter| QtCore.Qt.AlignBottom,QtCore.Qt.black)
            QtWidgets.qApp.processEvents()

app = QtWidgets.QApplication(sys.argv)
kartinka = QtGui.QPixmap('logo.png')
splash = QtWidgets.QSplashScreen(kartinka)
splash.show()
QtWidgets.qApp.processEvents()
window = MyWindow()
window.setWindowTitle('Использование экрана загрузки')
window.resize(300,30)
window.load_data(splash)
window.show()
sys.exit(app.exec_())
