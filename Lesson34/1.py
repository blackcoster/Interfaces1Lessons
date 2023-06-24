from PyQt5 import QtCore, QtWidgets
import sys

app = QtWidgets.QApplication(sys.argv)
settings = QtCore.QSettings('Рога и копыта', 'Тест1')

v1 = 123
v2 = 'Python'
v3 = QtCore.QSize(640,480)

print(v1,v2,v3,sep=' | ')
print('Сохраняем настройки')
settings.setValue('Значение1', v1)
settings.setValue('Значение2', v2)
settings.setValue('Значение3', v3)
settings.sync()
print('Считываем настройки')


lv1 = settings.value('Значение1')
lv2 = settings.value('Значение2')
lv3 = settings.value('Значение3')
print(lv1,lv2,lv3,sep=' | ')
if settings.contains('Значение4'):
    print('4 есть')
else:
    print('4 нет')
print('Очищаем хранилище')
settings.clear()