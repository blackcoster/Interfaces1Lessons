import PyQt5
from PyQt5 import QtWidgets,QtGui

# QLabel
#
# QWidget - QFrame - QLabel
#
# label = QLabel(parent=,flag=)
# label = QLabel(text,parent=,flag=)

import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
labelA = QtWidgets.QLabel(window)
labelA.setText('Label Пример')
window.setWindowTitle('example')
window.setGeometry(100,100,300,200)
labelA.move(100,40)

window.show()
sys.exit(app.exec_())
