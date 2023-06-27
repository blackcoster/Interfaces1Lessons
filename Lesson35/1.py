from PyQt5 import QtCore,QtWidgets
import sys

l = ['Python','Ruby','PHP','JavaScript']

app = QtWidgets.QApplication(sys.argv)
settings =QtCore.QSettings('Рога и копыта','Тест 2')
print(l)
print('Сохраняем список')
settings.beginWriteArray('Список')
for i in range(len(l)):
    settings.setArrayIndex(i)
    settings.setValue('Элемент',l[i])
settings.endArray()
settings.sync()
# print(settings.isWritable())
print('считываем список')
l1 = []
lsize = settings.beginReadArray('Список')
for i in range(lsize):
    settings.setArrayIndex(i)
    l1.append(settings.value('Элемент'))
settings.endArray()
# print(settings.status())
print(l1)
print(settings.fileName())
settings.clear()
