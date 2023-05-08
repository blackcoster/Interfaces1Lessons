from PyQt5 import QtWidgets
import sys

from PyQt5.QtWidgets import QMenuBar, QMenu, QDialogButtonBox


class Window(QtWidgets.QDialog):

    def __init__(self):
        super(Window,self).__init__()

        self.setWindowTitle('Basic Layouts')
        self.createMenu()
        self.createHorizontalGroup()
        self.createGrid()
        self.createForm()

        text = QtWidgets.QTextEdit()
        text.setPlainText("этот виджет занимает все ост пространство")

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok|QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.accept) # подкрутили автоматический обработчик
        buttonBox.rejected.connect(self.reject)


        mainbox = QtWidgets.QVBoxLayout()

        mainbox.setMenuBar(self.menuBar)
        mainbox.addWidget(self.groupBox)
        mainbox.addWidget(self.groupGrid)
        mainbox.addWidget(self.groupForm)
        mainbox.addWidget(text)
        mainbox.addWidget(buttonBox)

        self.setLayout(mainbox)


    def createMenu(self):
        self.menuBar = QMenuBar()
        self.fileMenu = QMenu('File',self)
        self.exit = self.fileMenu.addAction('Exit')
        self.menuBar.addMenu(self.fileMenu)

        self.exit.triggered.connect(self.accept)

    def createHorizontalGroup(self):
        self.groupBox = QtWidgets.QGroupBox('Horizontal Layout')
        box = QtWidgets.QHBoxLayout()

        for i in range(4):
            button = QtWidgets.QPushButton(f'Button {i+1}')
            box.addWidget(button)
        self.groupBox.setLayout(box)


    def createGrid(self):
        self.groupGrid = QtWidgets.QGroupBox('Grid Layout')
        grid = QtWidgets.QGridLayout()

        for i in range(3):
            label = QtWidgets.QLabel(f'Line{i+1}: ')
            lineEdit = QtWidgets.QLineEdit()
            grid.addWidget(label,i,0)
            grid.addWidget(lineEdit,i,1)

        self.text = QtWidgets.QTextEdit()
        self.text.setPlainText('Это виджет на 2/3 макета')

        grid.addWidget(self.text,0,2,5,1)

        # grid.setColumnStretch(0, 1)
        grid.setColumnStretch(1,10)
        grid.setColumnStretch(2,20)


        self.groupGrid.setLayout(grid)

    def createForm(self):
        self.groupForm = QtWidgets.QGroupBox('Form Layout')
        form = QtWidgets.QFormLayout()
        form.addRow('line 1',QtWidgets.QLineEdit())
        form.addRow('line 2 длинная строка', QtWidgets.QComboBox())
        form.addRow('line 3', QtWidgets.QSpinBox())
        self.groupForm.setLayout(form)





app = QtWidgets.QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
