# setWindowModality(NonModal)
# setWindowModality(WindowModal)
# setWindowModality(ApplicationModal)

from PyQt5 import QtCore, QtWidgets
import sys

def show_modal_window():
    global modalwindow
    modalwindow = QtWidgets.QWidget(window1,QtCore.Qt.Window)
    modalwindow.setWindowTitle('модальное окно')
    modalwindow.resize(200,50)
    modalwindow.setWindowModality(QtCore.Qt.WindowModal)
    modalwindow.setAttribute(QtCore.Qt.WA_DeleteOnClose,True) # удаляем окно при закрытии
    modalwindow.move(window1.geometry().center() - modalwindow.rect().center() - QtCore.QPoint(4,30))
    modalwindow.show()

app = QtWidgets.QApplication(sys.argv)

window1 = QtWidgets.QWidget()
window1.setWindowTitle('Обычное окно')
window1.resize(300,100)


button = QtWidgets.QPushButton('открыть модальное окно')
button.clicked.connect(show_modal_window)
box = QtWidgets.QVBoxLayout()
box.addWidget(button)
window1.setLayout(box)
window1.show()

window2 = QtWidgets.QWidget()
window2.setWindowTitle('окно не блокируется')
window2.resize(500,100)
window2.show()


sys.exit(app.exec_())


