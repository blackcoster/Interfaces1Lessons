# QWidget - QAbstractButton - QPushButton
#
# btn = QPushPutton(parent=)
# btn = QPushButton(text,parent = )
# btn = QPushButton(icon,text,parent = )

import sys
from PyQt5.QtWidgets import QApplication,QWidget,QPushButton,QLabel

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.btn = QPushButton('Нажми меня',self)
        self.btn.setToolTip('кнопка')
        self.btn.setGeometry(100,20,100,30)
        self.btn.clicked.connect(self.onClicked)

        self.label = QLabel('',self)
        self.label.setGeometry(90,60,290,60)

        self.move(850,300)
        self.show()



    def onClicked(self):
        self.label.setText('Кнопка нажата')

app = QApplication(sys.argv)
window = Window()
sys.exit(app.exec_())

# setText(text)
# text()
# setShortcut()
# setIcon(QIcon)
# seticonSize(QSize)
# setAutoRepeat(True)
# animateClick(interval)
# click()
# setCheckable(True)
# isChecked()
# setDown(True)

