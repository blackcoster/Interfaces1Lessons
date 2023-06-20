from PyQt5 import QtCore, QtWidgets, QtGui, QtPrintSupport
import sys

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        self.setWindowTitle('Печать изображения')
        self.printer = QtPrintSupport.QPrinter()
        self.printer.setPageOrientation(QtGui.QPageLayout.Landscape)
        self.file = None
        vbox = QtWidgets.QVBoxLayout()
        btnOpen = QtWidgets.QPushButton('Открыть файл...')
        btnOpen.clicked.connect(self.openFile)
        vbox.addWidget(btnOpen)
        btnOptions = QtWidgets.QPushButton('Настройки...')
        btnOptions.clicked.connect(self.showOptions)
        vbox.addWidget(btnOptions)
        btnPreview = QtWidgets.QPushButton('Просмотр...')
        btnPreview.clicked.connect(self.preview)
        vbox.addWidget(btnPreview)
        btnPrint = QtWidgets.QPushButton('Печать...')
        btnPrint.clicked.connect(self.print)
        vbox.addWidget(btnPrint)
        self.setLayout(vbox)
        self.resize(200,100)

    def openFile(self):
        self.file = QtWidgets.QFileDialog.getOpenFileName(parent= self,
                                                          caption='Выберите графический файл',
                                                          filter = 'Графические файлы (*.jpg *.png)')[0]

    def showOptions(self):
        pd = QtPrintSupport.QPageSetupDialog(self.printer,parent=self)
        pd.exec()

    def preview(self):
        pp = QtPrintSupport.QPrintPreviewDialog(self.printer,parent = self)
        pp.paintRequested.connect(self.printImage)
        pp.exec()
    def print(self):
        pd = QtPrintSupport.QPrintDialog(self.printer,parent=self)
        pd.setOptions(QtPrintSupport.QAbstractPrintDialog.PrintToFile |
                      QtPrintSupport.QAbstractPrintDialog.PrintSelection)
        if pd.exec() == QtWidgets.QDialog.Accepted:
            self.printImage()

    def printImage(self):
        painter = QtGui.QPainter()
        painter.begin(self.printer)
        pixmap = QtGui.QPixmap(self.file)
        pixmap = pixmap.scaled(self.printer.width(), self.printer.height(),
                               aspectRatioMode=QtCore.Qt.KeepAspectRatio)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()

app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())

