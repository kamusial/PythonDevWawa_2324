from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt6.QtCore import QSize
import sys
from random import choice

tytuly = [
    'Kamil',
    'Marcin',
    'Piotr',
    'Marta',
    'Urszula',
    'BLAD!'
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Moja aplikacja')
        self.setFixedSize(600, 400)
        self.button = QPushButton('przycisk')
        self.button.clicked.connect(self.button_clicked)
        self.windowTitleChanged.connect(self.zly_tytul)
        self.setCentralWidget(self.button)

    def button_clicked(self):
        print('klikniety')
        nowy_tytul = choice(tytuly)
        print('nowy tytul to: ',nowy_tytul)
        self.setWindowTitle(nowy_tytul)

    def zly_tytul(self, tytul):
        print('Tytul zmieniono na ',tytul)
        if tytul == 'BLAD!':
            self.button.setDisabled(True)
            self.button.setText('Nieaktywny')


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()