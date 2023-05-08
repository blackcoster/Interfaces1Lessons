import PyQt5
from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Grid Layout')
window.resize(300,120)

button1 = QtWidgets.QPushButton('1')
button2 = QtWidgets.QPushButton('2')
button3 = QtWidgets.QPushButton('3')
button4 = QtWidgets.QPushButton('4')

grid = QtWidgets.QGridLayout()
window.setLayout(grid)

grid.addWidget(button1,0,0) #сначала номер строки, потом столбца
grid.addWidget(button2,0,1)
grid.addWidget(button3,1,0)
grid.addWidget(button4,1,1)

window.show()
sys.exit(app.exec_())