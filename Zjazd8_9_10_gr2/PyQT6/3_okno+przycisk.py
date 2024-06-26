from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QPushButton
from PyQt6.QtCore import QSize
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Moja aplikacja')
        self.setFixedSize(QSize(600, 400))
        self.button = QPushButton('przycisk')
        self.button.setCheckable(True)
        self.button.pressed.connect(self.button_pressed)
        self.button.released.connect(self.button_released)
        self.button.clicked.connect(self.button_clicked)
        self.button.clicked.connect(self.button_toogle)

        self.setCentralWidget(self.button)

    def button_pressed(self):
        print('wcisniety')

    def button_released(self):
        print('Puszczony')

    def button_clicked(self):
        print('kliniety')

    def button_toogle(self, checked):
        print('Stan przycisku: ',checked)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()



app.exec()

