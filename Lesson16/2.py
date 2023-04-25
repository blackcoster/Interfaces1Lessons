from PyQt5 import QtWidgets,QtCore
import sys
app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton('завершить рабту')
button.clicked.connect(app.quit)
button.show()
sys.exit(app.exec_())

