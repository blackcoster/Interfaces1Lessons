from PyQt5 import QtCore, QtWidgets, QtWinExtras
import sys

class Window(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('список быстрого доступа')
        jumpList = QtWinExtras.QWinJumpList(parent=self)
        jumpList.clear()
        recent = jumpList.recent()
        item1 = QtWinExtras.QWinJumpListItem(QtWinExtras.QWinJumpListItem.Link)
        item1.setTitle('Открыть po.txt')
        item1.setFilePath(r'C:\Users\fc462t\Desktop\INNOPOLIS\interface2\Lesson33\po.txt')

        recent.addItem(item1)
        recent.setVisible(True)

        frequent = jumpList.frequent()
        frequent.addLink('другой файл',r'C:\Users\fc462t\Desktop\INNOPOLIS\interface2\Lesson33\img.jpg')
        frequent.setVisible(True)

        tasks = jumpList.tasks()
        tasks.addLink('Блокнот', r'C:\Windows\notepad.exe')
        tasks.setVisible(True)

        my_category = QtWinExtras.QWinJumpListCategory()
        my_category.setTitle('Иное....')
        my_category.addLink('Designer',r'C:\Program Files (x86)\Qt Designer\designer.exe')
        my_category.setVisible(True)

        jumpList.addCategory(my_category)


        self.resize(200, 50)
app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())