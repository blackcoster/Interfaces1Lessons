from PyQt5 import QtCore, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)

window = QtWidgets.QWidget(flags = QtCore.Qt.Dialog)
window.setWindowTitle('подсказки')
window.resize(300,70)

button = QtWidgets.QPushButton('закрыть окно',window)
button.setFixedSize(150,30)
button.move(75,20)

button.setToolTip('Кнопка')
button.setToolTipDuration(3000) # задаем время отображения

window.setToolTip('Окно')
button.setToolTipDuration(-1) # автоматически

button.setWhatsThis('Справка для кнопки')
window.setWhatsThis('Справка для окна')


button.clicked.connect(app.quit)
window.show()

sys.exit(app.exec_())