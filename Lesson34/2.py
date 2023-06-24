# settings.value('ключ1/значени1',123)
# lv1 = setting.value('ключ1/wfwf/wf2ef/2f2f/2f2f/значени1')
#
# settings.beginGroup('ключ1')
# settings.setValue('значение1',4878)
# clear()
# remove('')
# contains('Значение1')
# childkeys()
# allKeys()
# group()
# childGroups()
# settings.endGroup()

from PyQt5 import QtCore,QtWidgets
import sys
class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.setWindowTitle('Настройки')
        self.settings = QtCore.QSettings('Настройки','использование ключей')

        vbox = QtWidgets.QVBoxLayout()
        self.line = QtWidgets.QLineEdit(parent= self)
        vbox.addWidget(self.line)
        btn = QtWidgets.QPushButton('Сохранить')
        btn.clicked.connect(self.saveText)
        vbox.addWidget(btn)
        self.setLayout(vbox)

        if self.settings.contains('Окно/Место'):
            self.setGeometry(self.settings.value('Окно/Место'))
        else:
            self.resize(200,50)

        if self.settings.contains('Данные/Текст'):
            self.line.setText(self.settings.value('Данные/Текст'))
        # self.settings.clear()

    def closeEvent(self, evt):
        self.settings.beginGroup('Окно')
        self.settings.setValue('Место',self.geometry())
        # self.settings.remove('Место')
        self.settings.endGroup()


    def saveText(self):
        self.settings.beginGroup('Данные')
        self.settings.setValue('Текст',self.line.text())
        # self.settings.remove('Текст')
        self.settings.endGroup()

app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
