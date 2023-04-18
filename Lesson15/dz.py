from PyQt5 import QtCore, QtWidgets
import sys


def button_clicked():
    text = pole_vvoda.text()
    print(text)


app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget()
window.setWindowTitle('подсказки')
window.resize(300,70)

box = QtWidgets.QVBoxLayout()

pole_vvoda = QtWidgets.QLineEdit()
button = QtWidgets.QPushButton('вывод текста')
button.clicked.connect(button_clicked)

box.addWidget(pole_vvoda)
box.addWidget(button)
window.setLayout(box)



window.show()
sys.exit(app.exec_())
