import sys
from PyQt6.QtWidgets import QHBoxLayout, QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Kolory')



app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()