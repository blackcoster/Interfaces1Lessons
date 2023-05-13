# # QWidget - QAbstractButton -QRadioButton
# btn = QRadioButton(parent=)
# btn = QRadioButton(text,parent=)
#
# QRadiobutton('polina')
# setChecked(True)
# toggled(True)


from PyQt5.QtWidgets import QWidget, QRadioButton, QHBoxLayout, QVBoxLayout, QApplication, QLabel
import sys



class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setGeometry(400,300,350,250)
        self.setWindowTitle('RADIO BUTTON')

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()

        rb1 = QRadioButton('Large',self)
        rb1.toggled.connect(self.updateLabel)

        rb2 = QRadioButton('Medium',self)
        rb2.toggled.connect(self.updateLabel)

        rb3 = QRadioButton('Small',self)
        rb3.toggled.connect(self.updateLabel)

        self.label = QLabel('',self)

        hbox.addWidget(rb1)
        hbox.addWidget(rb2)
        hbox.addWidget(rb3)

        vbox.addSpacing(15)

        vbox.addLayout(hbox)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

    def updateLabel(self):
        btn = self.sender()

        if btn.isChecked()==True:
            self.label.setText(btn.text())

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
