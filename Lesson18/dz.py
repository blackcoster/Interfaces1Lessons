from PyQt5 import QtWidgets, QtCore, QtGui
import sys
from PyQt5.QtGui import QIcon

class Window(QtWidgets.QWidget):
    def __init__(self,parent = None):
        QtWidgets.QWidget.__init__(self,parent)
        self.resize(250,100)
        self.text1 = QtWidgets.QTextEdit(self)
        box = QtWidgets.QVBoxLayout()
        box.addWidget(self.text1)
        self.setLayout(box)
        self.filter = MyFilter(parent=self)

class MyFilter(QtCore.QObject):
    def __init__(self,parent=None):
        QtCore.QObject.__init__(self,parent)
        self.parent = parent

    def eventFilter(self, obj, e):
        if e.type() == QtCore.QEvent.MouseButtonDblClick:
            xmouse = e.pos().x()
            ymouse = e.pos().y()

            h = self.parent.text1.geometry().height()
            w = self.parent.text1.geometry().width()
            x_txt = self.parent.text1.geometry().x()
            y_txt = self.parent.text1.geometry().y()

            if x_txt <xmouse <(x_txt+w) and y_txt <ymouse <(y_txt+h):
                print(self.parent.text1.toPlainText())
            return True

        return QtCore.QObject.eventFilter(self,obj,e)




if __name__ == "__main__":
   import sys

   app = QtWidgets.QApplication(sys.argv)
   window = Window()
   window.show()
   app.installEventFilter(window.filter)
   sys.exit(app.exec())