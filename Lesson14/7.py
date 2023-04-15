from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle('zagolovok')
window.resize(300,50)
window.show()
rect = window.geometry() # без рамки
print(rect.left(),rect.top())
print(rect.width(),rect.height())

rect = window.frameGeometry() # с рамкой и заголовком
print(rect.left(),rect.top())
print(rect.width(),rect.height())

sys.exit(app.exec_())