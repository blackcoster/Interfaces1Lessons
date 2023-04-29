from PyQt5 import QtWidgets

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.resize(300,100)

    def closeEvent(self, e):
        result = QtWidgets.QMessageBox.question(self,'Подтверждение закрытия окна',
                                                'Вы уверены что хотите закрыть окно?',
                                                QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No,
                                                QtWidgets.QMessageBox.No)
        if result == QtWidgets.QMessageBox.Yes:
            e.accept()
        else:
            e.ignore()

import sys
app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())