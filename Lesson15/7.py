# QWidget {color:red;} #все потомки класса
# .QWidget {font-weight:bold;} # только класс
# QPushButton#knopka1 {} # только объект с этим именем
# QPushButton:pressed {} #класс по услови.

from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
#для всех окон
app.setStyleSheet('QGroupBox QLabel {color:blue;} QPushButton {font-style: italic}')
window = QtWidgets.QWidget()

window.setStyleSheet('QLabel#greentext {color: green;} QLabel:hover {color: red}')
window.setWindowTitle('стили')
window.resize(200,250)

text1 = QtWidgets.QLabel('Зеленый текст')
text1.setObjectName('greentext')

text2 = QtWidgets.QLabel('Полужирный текст')
text2.setStyleSheet('font-weight: bold')

text3 = QtWidgets.QLabel('Синий текст')

button = QtWidgets.QPushButton('Курсивный текст')

gruppa = QtWidgets.QGroupBox('Группа')

box = QtWidgets.QVBoxLayout()
box.addWidget(text3)
gruppa.setLayout(box)

mainbox = QtWidgets.QVBoxLayout()
mainbox.addWidget(text1)
mainbox.addWidget(text2)
mainbox.addWidget(gruppa)
mainbox.addWidget(button)
window.setLayout(mainbox)

window.show()
sys.exit(app.exec_())


