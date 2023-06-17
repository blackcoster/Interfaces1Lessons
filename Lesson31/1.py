from PyQt5 import QtCore, QtWidgets,QtGui,QtPrintSupport
import sys


app = QtWidgets.QApplication(sys.argv)

printer = QtPrintSupport.QPrinter()
printer.setOutputFileName('output.pdf')

painter = QtGui.QPainter()
painter.begin(printer)

pen = QtGui.QPen(QtGui.QColor(QtCore.Qt.blue),5,style = QtCore.Qt.DotLine)
painter.setPen(pen)
painter.drawRect(0,0,printer.width(),printer.height())
color = QtGui.QColor(QtCore.Qt.black)
painter.setPen(QtGui.QPen(color))
painter.setBrush((QtGui.QBrush(color)))
font = QtGui.QFont('Verdana',pointSize = 42)
painter.setFont(font)
painter.drawText(10,printer.height()//2-100,printer.width()-20,50,QtCore.Qt.AlignCenter|QtCore.Qt.TextDontClip,'QPrinter')

printer.setPageOrientation(QtGui.QPageLayout.Landscape)
printer.newPage()
pixmap = QtGui.QPixmap('img.jpg')
pixmap = pixmap.scaled(printer.width(),printer.height(),aspectRatioMode=QtCore.Qt.KeepAspectRatio)
painter.drawPixmap(0,0,pixmap)
painter.end()