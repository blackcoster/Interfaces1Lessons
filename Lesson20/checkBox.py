# # QWidget - QAbstractButton -QCheckBox
# btn = QRadioButton(parent=)
# btn = QRadioButton(text,parent=)
#
# setCheckState( 0 1 2)
# checkState
# setTristate(True)
# isTristate
#
# setChecked
# isChecked
# stateChanged(состояние)

import sys
from PyQt5.QtWidgets import QWidget,QCheckBox,QApplication
from PyQt5.QtCore import Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()

        checkbox = QCheckBox('show title',self)
        checkbox.move(20,20)
        checkbox.toggle() # ставим галочку
        checkbox.stateChanged.connect(self.changeTitle)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Checkbox')

    def changeTitle(self,state):
        if state==Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())