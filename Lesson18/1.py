import sys

import PyQt5
from PyQt5 import QtWidgets,QtCore


class MyEvent(QtCore.QEvent):
    idType = QtCore.QEvent.registerEventType()

    def __init__(self,data):
        QtCore.QEvent.__init__(self,MyEvent.idType)
        self.data = data

    def getData(self):
        return self.data



class Text(QtWidgets.QLabel):

    def __init__(self):
        QtWidgets.QLabel.__init__(self,'я заголовок')
        self.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.resize(300,100)

    def customEvent(self, e):
        if e.type() == MyEvent.idType:
            self.setText(f'Отловили событие: {e.getData()}')

app = QtWidgets.QApplication(sys.argv)
label = Text()

label.show()
#кидаем событие

QtCore.QCoreApplication.sendEvent(label,MyEvent('данные события'))
sys.exit(app.exec_())
