from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from functools import partial


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.delenBtn = QPushButton('/')
        self.umnozBtn = QPushButton('*')
        self.celochBtn = QPushButton('//')
        self.ostatBtn = QPushButton('%')

        self.sevenBtn = QPushButton('7')
        self.eightBtn = QPushButton('8')
        self.nineBtn = QPushButton('9')
        self.plustBtn = QPushButton('+')

        self.fourBtn = QPushButton('4')
        self.fiveBtn = QPushButton('5')
        self.sixBtn = QPushButton('6')
        self.minusBtn = QPushButton('-')

        self.oneBtn = QPushButton('1')
        self.twoBtn = QPushButton('2')
        self.threeBtn = QPushButton('3')
        self.stepenBtn = QPushButton('**')

        self.zeroBtn = QPushButton('0')
        self.pointBtn = QPushButton('.')
        self.enterBtn = QPushButton('Enter', clicked=self.enterBtnEvent)
        self.ceBtn = QPushButton('CE', clicked=self.ce)


        h1 = QHBoxLayout()
        h2 = QHBoxLayout()
        h3 = QHBoxLayout()
        h4 = QHBoxLayout()
        h5 = QHBoxLayout()

        self.lineEdit = QLineEdit()

        h1.addWidget(self.delenBtn)
        h1.addWidget(self.umnozBtn)
        h1.addWidget(self.celochBtn)
        h1.addWidget(self.ostatBtn)

        h2.addWidget(self.sevenBtn)
        h2.addWidget(self.eightBtn)
        h2.addWidget(self.nineBtn)
        h2.addWidget(self.plustBtn)

        h3.addWidget(self.fourBtn)
        h3.addWidget(self.fiveBtn)
        h3.addWidget(self.sixBtn)
        h3.addWidget(self.minusBtn)

        h4.addWidget(self.oneBtn)
        h4.addWidget(self.twoBtn)
        h4.addWidget(self.threeBtn)
        h4.addWidget(self.stepenBtn)

        h5.addWidget(self.zeroBtn)
        h5.addWidget(self.pointBtn)
        h5.addWidget(self.enterBtn)
        h5.addWidget(self.ceBtn)


        vbox = QVBoxLayout()
        vbox.addWidget(self.lineEdit)
        vbox.addLayout(h1)
        vbox.addLayout(h2)
        vbox.addLayout(h3)
        vbox.addLayout(h4)
        vbox.addLayout(h5)



        window = QWidget()
        window.setLayout(vbox)

        self.bind()

        self.setWindowTitle('Калькулятор')
        self.setCentralWidget(window)
        self.show()


    def bind(self):
        list = [
            self.umnozBtn,self.stepenBtn, self.umnozBtn, self.celochBtn, self.sevenBtn,
            self.eightBtn,self.nineBtn, self.plustBtn, self.fourBtn, self.fiveBtn,
            self.sixBtn, self.minusBtn, self.oneBtn,self.twoBtn, self.threeBtn,
            self.zeroBtn, self.pointBtn,self.ostatBtn
        ]
        for i in list:
            i.clicked.connect(partial(self.clickButton, i.text()))




    def ce(self):
        self.lineEdit.clear()


    def clickButton(self, btn_text):
        self.lineEdit.setText(self.lineEdit.text() + btn_text)


    def enterBtnEvent(self):
        print(f'{self.lineEdit.text()} = {eval((self.lineEdit.text()))}')
        self.lineEdit.setText(f'{self.lineEdit.text()} = {eval((self.lineEdit.text()))}')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    print(calculator.umnozBtn.text())
    sys.exit(app.exec_())