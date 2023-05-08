import PyQt5
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Абсолютное позиционирование')
window.resize(300,120)
label = QtWidgets.QLabel('Текст надписи',window)
button = QtWidgets.QPushButton('Кнопка',window)

label.setGeometry(10,10,280,60) #1 способ двигать и меняь размер виджета

#2 способ
button.move(10,80)
button.resize(280,30)

window.show()
sys.exit(app.exec_())
