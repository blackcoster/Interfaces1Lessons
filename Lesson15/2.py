from PyQt5 import QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('прозрачность')
window.resize(300,100)
window.setWindowOpacity(0.5)

window.show()
print(window.windowOpacity())
sys.exit(app.exec_())