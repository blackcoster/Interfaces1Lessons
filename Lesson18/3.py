import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from PyQt5.QtGui import QIcon

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Программа расчета')
        self.setWindowIcon(QIcon('icon.png'))
        self.setFixedSize(500,350)

        self.main_box = QtWidgets.QVBoxLayout()
        self.setLayout(self.main_box)

        self.text_box = QtWidgets.QHBoxLayout()
        self.main_box.addLayout(self.text_box)

        self.text_area = QtWidgets.QLineEdit()
        self.text_perimeter = QtWidgets.QLineEdit()
        self.text_box.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.text_box.addWidget(self.text_area)
        self.text_box.addWidget(self.text_perimeter)

        self.answer = QtWidgets.QLabel('Ответ:')
        self.answer.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.answer.setFont(QtGui.QFont('Arial',15))
        self.main_box.addWidget(self.answer)

        self.knopka_box = QtWidgets.QHBoxLayout()
        self.main_box.addLayout(self.knopka_box)

        self.area_button = QtWidgets.QPushButton('Площадь')
        self.perimeter_button = QtWidgets.QPushButton('Периметр')

        self.knopka_box.addWidget(self.area_button)
        self.knopka_box.addWidget(self.perimeter_button)

        self.area_button.clicked.connect(self.get_area)
        self.perimeter_button.clicked.connect(self.get_perimeter)

    def get_area(self):
        try:
            a = float(self.text_area.text())
            b = float(self.text_perimeter.text())
            result = a * b
            self.answer.setText(f'Ответ: {result}')
        except ValueError:
            self.answer.setText(f'Ошибка ввода')
        finally:
            self.area_button.setEnabled(False)
            self.perimeter_button.setEnabled(False)
            timer = QtCore.QTimer()
            timer.singleShot(3000,self.reset_data)

    def get_perimeter(self):
        try:
            a = float(self.text_area.text())
            b = float(self.text_perimeter.text())
            result = a + a + b + b
            self.answer.setText(f'Ответ: {result}')
        except ValueError:
            self.answer.setText(f'Ошибка ввода')
        finally:
            self.area_button.setEnabled(False)
            self.perimeter_button.setEnabled(False)
            timer = QtCore.QTimer()
            timer.singleShot(3000,self.reset_data)


    def reset_data(self):
        self.answer.setText('Ответ:')
        self.text_perimeter.clear()
        self.text_area.clear()
        self.text_area.setFocus()
        self.area_button.setEnabled(True)
        self.perimeter_button.setEnabled(True)

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self,'вопросик...',
                                               'Точно хочешь выйти?',
                                               QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                               QtWidgets.QMessageBox.No)
        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())