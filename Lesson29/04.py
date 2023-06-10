from PyQt5 import QtCore, QtWidgets, QtMultimedia
import sys, os


class MyWindow(QtWidgets.QWidget):
   def __init__(self, parent=None):
       QtWidgets.QWidget.__init__(self, parent, flags=QtCore.Qt.Window |
                                                      QtCore.Qt.MSWindowsFixedSizeDialogHint)
       self.setWindowTitle("Плейлист")
       self.mplPlayer = QtMultimedia.QMediaPlayer()
       # Создаем плейлист и наполняем его файлами
       self.playlist = QtMultimedia.QMediaPlaylist()
       files = ["audio1.mp3", "audio2.mp3", "audio3.mp3", "audio4.mp3"]
       for f in files:
           fn = QtCore.QUrl.fromLocalFile(os.path.abspath(f))
           self.playlist.addMedia(QtMultimedia.QMediaContent(fn))
       # Поэкспериментируем со вставкой и удалением позиций в плейлисте
       # Вставляем вторую позицию в конец плейлиста
       self.playlist.insertMedia(4, self.playlist.media(1))
       # Удаляем вторую позицию
       self.playlist.removeMedia(1)
       self.playlist.setCurrentIndex(0)
       self.mplPlayer.setPlaylist(self.playlist)
       # Создаем элементы управления воспроизведением
       vbox = QtWidgets.QVBoxLayout()
       hbox = QtWidgets.QHBoxLayout()
       self.btnPlay = QtWidgets.QPushButton("&Пуск")
       self.btnPlay.clicked.connect(self.mplPlayer.play)
       hbox.addWidget(self.btnPlay)
       self.btnNext = QtWidgets.QPushButton("П&редыдущая")
       self.btnNext.clicked.connect(self.playlist.previous)
       hbox.addWidget(self.btnNext)
       self.btnPrevious = QtWidgets.QPushButton("&Следующая")
       self.btnPrevious.clicked.connect(self.playlist.next)
       hbox.addWidget(self.btnPrevious)
       vbox.addLayout(hbox)
       self.lblCurrent = QtWidgets.QLabel("")
       vbox.addWidget(self.lblCurrent)
       self.playlist.currentMediaChanged.connect(self.showFile)
       self.setLayout(vbox)
       self.resize(300, 70)
       # Выводим на экран имя файла, воспроизводящегося в данный момент
       # Метод canonicalUrl() класса QMediaContent возвращает
       # путь к файлу экземпляра класса QUrl, а метод fileName()
       # класса QUrl позволяет узнать имя файла

   def showFile(self, content):
       self.lblCurrent.setText(content.canonicalUrl().fileName())


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())
