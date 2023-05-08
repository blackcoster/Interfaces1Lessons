from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('QToolBox')
window.resize(200,100)

toolBox = QtWidgets.QToolBox()
toolBox.addItem(QtWidgets.QLabel('Содержимое вкладки 1'),'Вкладка 1')
toolBox.addItem(QtWidgets.QLabel('Содержимое вкладки 2'),'Вкладка 2')
toolBox.addItem(QtWidgets.QLabel('Содержимое вкладки 3'),'Вкладка 3')

toolBox.setCurrentIndex(0)
box = QtWidgets.QVBoxLayout(window)
box.addWidget(toolBox)


window.show()
sys.exit(app.exec_())