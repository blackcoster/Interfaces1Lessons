import sqlite3
import sys

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300,100,300,200)
        self.setWindowTitle('Войти в систему')

        vbox = QVBoxLayout()
        self.label = QLabel('Войти')
        self.hint = QLabel('Введите свои данные')
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.hint.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.button = QPushButton('Войти')
        self.button.clicked.connect(self.auth)
        vbox.addWidget(self.label)
        vbox.addWidget(self.hint)
        vbox.addWidget(self.username)
        vbox.addWidget(self.password)
        vbox.addWidget(self.button)

        self.setLayout(vbox)

    def auth(self):
        try:
            login =self.username.text()
            password = self.password.text()
            print(f'{login}: {password}')
            if login!='' and password!='':
                con = sqlite3.connect('test.db')
                cur = con.cursor()
                cur.execute(f'SELECT * FROM users WHERE login =="{login}"')
                value = cur.fetchone()
                if value is None:
                    self.hint.setText('Нет такого пользователя')
                    self.username.clear()
                    self.password.clear()
                else:
                    if value[1]==password:
                        print('ВХОД........')
                        self.hide()
                    else:
                        self.password.clear()
                        self.hint.setText('Пароль неверный')
            else:
                self.hint.setText('Поля не могут быть пустыми')
        except Exception as e:
            print(e)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())