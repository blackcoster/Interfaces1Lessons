import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication,QLabel,QMainWindow,QMenu,QToolBar,QAction

class Window(QMainWindow):
    def __init__(self,parent = None):
        super().__init__(parent)

        self.setWindowTitle('Menu and Toolbar')
        self.resize(400,200)
        self.text = QLabel('Hello, World!')
        self.text.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.setCentralWidget(self.text)
        self.createAction()
        self.createMenuBar()
        self.createToolBar()
        self.createContextMenu()


    def createMenuBar(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('File')
        fileMenu.addAction(self.newAction)
        fileMenu.addAction(self.openAction)
        fileMenu.addAction(self.saveAction)
        fileMenu.addAction(self.exitAction)

        editMenu = menuBar.addMenu('Edit')
        editMenu.addAction(self.copyAction)
        editMenu.addAction(self.pasteAction)
        editMenu.addAction(self.cutAction)
        findMenu = editMenu.addMenu('Find and Replace')
        findMenu.addAction('Find...')
        findMenu.addAction('Replace...')

        helpMenu = menuBar.addMenu('Help')
        helpMenu.addAction(self.helpAction)
        helpMenu.addAction(self.aboutAction)
    def createAction(self):
        self.newAction = QAction('New',self)
        self.openAction = QAction('Open',self)
        self.saveAction = QAction('Save',self)
        self.exitAction = QAction('Exit',self)
        self.copyAction = QAction('Copy',self)
        self.pasteAction = QAction('Paste',self)
        self.cutAction = QAction('Cut',self)
        self.helpAction = QAction('Help',self)
        self.aboutAction = QAction('About',self)

    def createToolBar(self):
        fileToolBar = self.addToolBar('File')
        editToolBar = self.addToolBar('Edit')
        helpToolBar = QToolBar('Help',self)
        self.addToolBar(Qt.LeftToolBarArea,helpToolBar)

        fileToolBar.addAction(self.newAction)
        fileToolBar.addAction(self.openAction)
        fileToolBar.addAction(self.saveAction)
        fileToolBar.addAction(self.exitAction)
        editToolBar.addAction(self.copyAction)
        editToolBar.addAction(self.pasteAction)
        editToolBar.addAction(self.cutAction)
        helpToolBar.addAction(self.helpAction)
        helpToolBar.addAction(self.aboutAction)

    def createContextMenu(self):
        self.text.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.text.addAction(self.copyAction)
        self.text.addAction(self.pasteAction)
        self.text.addAction(self.aboutAction)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
