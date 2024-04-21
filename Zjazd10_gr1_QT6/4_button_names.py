from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton
from PyQt6.QtCore import QSize
import sys
from random import choice

tytuly_okien = [
    'Lukasz',
    'Lukasz',
    'Rafal',
    'Rafal',
    'Sylwia',
    'Sylwia',
    'Ania',
    'Ania',
    'BLAD!'
]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Moja aplikacja')
        self.setFixedSize(QSize(600, 400))
        self.button = QPushButton('przycisk')
        self.button.clicked.connect(self.button_clicked)
        self.windowTitleChanged.connect(self.wrong_title)
        self.setCentralWidget(self.button)

    def button_clicked(self):
        print('klikniety')
        tytul = choice(tytuly_okien)
        print('nowy tytul to: ',tytul)
        self.setWindowTitle(tytul)

    def wrong_title(self, tytul_okna):
        print('Tytul zmieniono na ',tytul_okna)
        if tytul_okna == 'BLAD!':
            self.button.setText('Nieaktywny')
            self.button.setDisabled(True)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()