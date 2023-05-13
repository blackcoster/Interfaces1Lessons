# drag&drop
#
# # QWidget - QLineEdit
# # # btn = QLineEdit(parent=)
# # # btn =QLineEdit(text,parent=)
# setText(TEXT)
# insert(text)
# text()
# displaytext()
# clear()
# backspace()
# del()
# setSection(index,len)

# setEchoMode(режим)
# normal = 0
# noEcho =1 - не показывать
# password =2 показывает звездочки
# passwordEchoonEdit -3 буквы становятся звездочками

import sys
from PyQt5.QtWidgets import QWidget,QLabel,QLineEdit,QApplication

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel(self)
        self.polevvoda = QLineEdit(self)
        self.polevvoda.setEchoMode(2)#стиль для ввода пароля
        self.polevvoda.move(60,100)
        self.label.move(60,40)

        self.polevvoda.textChanged[str].connect(self.onChanged)

        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QLineEdit')

    def onChanged(self,text):
        self.label.setText(text)
        self.label.adjustSize()

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())