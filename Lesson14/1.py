from PyQt5 import QtCore
stroka = 'polina'
a = bytes(stroka,'cp1251')
arr = QtCore.QByteArray(a)
print(arr)

from PyQt5 import QtCore
n = QtCore.QVariant('ehd')
a = QtCore.QVariant(5)
print(n)
print(n.value())
print(n.typeName())
print(a.typeName())