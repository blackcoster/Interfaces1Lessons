from PyQt5 import QtCore,QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowFlag(QtCore.Qt.Dialog)
window.setWindowTitle('закрытие окна')
window.resize(300,70)
window.move(300,260)

window1 = QtWidgets.QWidget()
window1.setWindowFlag(QtCore.Qt.Dialog)
window1.setWindowTitle('закрытие окна')
window1.resize(300,70)

button = QtWidgets.QPushButton('закрыть окно',window)
button.setFixedSize(150,30)
button.move(75,20)

# button.clicked.connect(app.quit) # для закрытия всех окон приложения
button.clicked.connect(window.close) # для закрытия одного окна

window.show()
window1.show()
sys.exit(app.exec_())