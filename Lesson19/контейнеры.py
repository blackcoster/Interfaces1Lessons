import PyQt5
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Box Layout')
window.resize(300,120)
label = QtWidgets.QLabel('Текст надписи')
button = QtWidgets.QPushButton('Кнопка')

#1 способ привзять коробку к окну
# box = QtWidgets.QHBoxLayout(window)

#2 способ
# box = QtWidgets.QVBoxLayout() #- вертикальная коробка
box = QtWidgets.QHBoxLayout() #- горизонтальная коробка
window.setLayout(box)

box.addWidget(label)
box.addWidget(button)

window.show()
sys.exit(app.exec_())