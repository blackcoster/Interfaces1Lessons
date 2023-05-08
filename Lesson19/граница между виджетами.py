from PyQt5 import QtWidgets, QtCore
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('QSplitter')
window.resize(200,200)

splitter = QtWidgets.QSplitter(QtCore.Qt.Vertical)

label1 = QtWidgets.QLabel('Содержимое компонента 1')
label2 = QtWidgets.QLabel('Содержимое компонента 2')

label1.setFrameStyle(QtWidgets.QFrame.Box| QtWidgets.QFrame.Plain)
label2.setFrameStyle(QtWidgets.QFrame.Box| QtWidgets.QFrame.Plain)

box = QtWidgets.QVBoxLayout(window)
splitter.addWidget(label1)
splitter.addWidget(label2)
box.addWidget(splitter)


window.show()
sys.exit(app.exec_())