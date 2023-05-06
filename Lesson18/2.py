import sys

import PyQt5
from PyQt5 import QtWidgets,QtCore

class Window(QtWidgets.QLabel):

    def __init__(self):
        QtWidgets.QLabel.__init__(self,'я заголовок')
        self.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.resize(300,100)

class MyFiler(QtCore.QObject):
    def __init__(self,parent=None):
        QtCore.QObject.__init__(self,parent)

    def eventFilter(self, obj, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if event.key() == QtCore.Qt.Key_B:
                print('это не дошло до компонента')
                return True
            else:
                print('Это событие дошло до компонента')

        return QtCore.QObject.eventFilter(self,obj,event)


app = QtWidgets.QApplication(sys.argv)
label = Window()

filter = MyFiler(label)
label.installEventFilter(filter)
label.show()
sys.exit(app.exec_())