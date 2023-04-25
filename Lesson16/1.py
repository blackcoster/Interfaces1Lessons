# button.clicked.connect()
#
# <компонент>.<сигнал>.connect(<обработчик>[<тип соединения>])
# button.clicked[bool].connect(func)


from PyQt5 import QtWidgets
import sys


def on_clicked():
    print('кнопка нажата. функция ')

class MyClass():
    def __init__(self,x=0):
        self.x = x
    def __call__(self):
        print('кнопка нажата. call')
        print(f'x = {self.x}')
    def on_clicked(self):
        print('кнопка нажата. метод')
        print(self.x)

obj = MyClass()

app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton('Нажми меня')

button.clicked.connect(on_clicked)
button.clicked.connect(obj.on_clicked)
button.clicked.connect(MyClass(6))
button.clicked.connect(lambda : MyClass(8)())
button.show()
sys.exit(app.exec_())