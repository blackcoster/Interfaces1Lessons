from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Group Box')
window.resize(200,80)

main_box = QtWidgets.QVBoxLayout(window)

radio1 = QtWidgets.QRadioButton('да')
radio2 = QtWidgets.QRadioButton('нет')

group = QtWidgets.QGroupBox('Вы знаете язык Python?')
smol_box = QtWidgets.QHBoxLayout()
smol_box.addWidget(radio1)
smol_box.addWidget(radio2)

group.setLayout(smol_box)

main_box.addWidget(group)

window.show()
sys.exit(app.exec_())