from PyQt5 import QtWidgets
import sys
app = QtWidgets.QApplication(sys.argv)

#создаем окно, адаем заголовок, меняем размер
window = QtWidgets.QWidget()
window.setWindowTitle('Программа на PyQt')
window.resize(300,100)

#создаем объект надписи
label = QtWidgets.QLabel('<center>Привет, мир!</center>')
#cоздаем объект кнопки
button = QtWidgets.QPushButton('закрыть окно')

#создаем коробку- контейнер
box = QtWidgets.QVBoxLayout()

#кладем кнопку и текст в контейнер
box.addWidget(label)
box.addWidget(button)

#закрепляем коробку на окне
window.setLayout(box)

#обрабатываем нажатие на кнопку
button.clicked.connect(app.quit)

#отрисовка окна
window.show()
#выход
sys.exit(app.exec_())
