from PyQt5 import QtWidgets
import sys,time

def on_clicked():
    time.sleep(10)

app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton('Запустить процесс')
button.resize(200,40)
button.clicked.connect(on_clicked)
button.show()
sys.exit(app.exec_())