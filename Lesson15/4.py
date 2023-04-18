from PyQt5 import QtGui,QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('иконка')
window.resize(300,100)

window1 = QtWidgets.QWidget()
window1.setWindowTitle('иконка')
window1.resize(300,100)


ikonka = QtGui.QIcon('icon.png')
window.setWindowIcon(ikonka) # для конкретного окна
app.setWindowIcon(ikonka) # для всех окон

window.show()
window1.show()
sys.exit(app.exec_())