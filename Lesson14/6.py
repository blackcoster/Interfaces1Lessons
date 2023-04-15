from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('zagolovok')
window.resize(300,100)
window.show()
print(window.width(),window.height()) # размеры без заголовка
print(window.frameSize().width(),window.frameSize().height()) #размеры с заголовком вместе


sys.exit(app.exec_())