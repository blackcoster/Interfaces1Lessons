from PyQt5 import uic,QtWidgets
import sys
#https://build-system.fman.io/qt-designer-download
app = QtWidgets.QApplication(sys.argv)
window = uic.loadUi('untitled.ui') #подгружаем готовый интерфейс. пололжить его в папку где код. имя может быть другим
window.button.clicked.connect(app.quit) #обращаемся через окно

window.show()
sys.exit(app.exec_())
