from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Form Layout')
window.resize(300,120)

lineEdit = QtWidgets.QLineEdit()
textEdit = QtWidgets.QTextEdit()
button1 = QtWidgets.QPushButton('О&тправить')
button2 = QtWidgets.QPushButton('О&чистить')

box = QtWidgets.QHBoxLayout()
box.addWidget(button1)
box.addWidget(button2)

form = QtWidgets.QFormLayout()
form.addRow('&Название',lineEdit)
form.addRow('&Описание',textEdit)
form.addRow(box)

window.setLayout(form)

window.show()
sys.exit(app.exec_())