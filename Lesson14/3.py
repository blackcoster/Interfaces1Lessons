from PyQt5 import QtWidgets
import sys,time

def on_clicked():
    button.setDisabled(True)
    for i in range(1,11):
        QtWidgets.qApp.processEvents()
        time.sleep(1)
        print(f'step-{i}')
    button.setDisabled(False)

app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton('Запустить процесс')
button.resize(200,40)
button.clicked.connect(on_clicked)
button.show()
sys.exit(app.exec_())