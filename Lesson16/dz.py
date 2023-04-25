import sys
from PyQt5 import QtWidgets, uic

class Main(QtWidgets.QWidget):
    def __init__(self):
        self.operation = ''
        QtWidgets.QWidget.__init__(self)
        uic.loadUi('calc.ui',self)

        self.Button1.clicked.connect(lambda ch, btn=self.Button1: self.click_button(btn))
        self.Button2.clicked.connect(lambda ch, btn=self.Button2: self.click_button(btn))
        self.Button3.clicked.connect(lambda ch, btn=self.Button3: self.click_button(btn))
        self.Button4.clicked.connect(lambda ch, btn=self.Button4: self.click_button(btn))
        self.ButtonAdd.clicked.connect(lambda ch, btn=self.ButtonAdd: self.click_button(btn))
        self.ButtonEq.clicked.connect(self.get_result)

    def click_button(self,btn):
        self.operation += btn.text()

    def get_result(self):
        print(eval(self.operation))

app = QtWidgets.QApplication(sys.argv)
window = Main()
window.show()
sys.exit(app.exec_())