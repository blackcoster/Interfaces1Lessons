from PyQt5 import QtWidgets
import sys

def do_action():
    global label
    value = scroll.value()
    label.setText(f'value - {value}')

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('Scrolling')
window.setGeometry(100,100,500,400)

scroll = QtWidgets.QScrollBar(window)
scroll.setGeometry(100,50,30,200)
label = QtWidgets.QLabel('надпись',window)
label.setGeometry(200,100,300,80)
scroll.valueChanged.connect(do_action)

window.show()
sys.exit(app.exec_())