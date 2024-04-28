import sys
from PyQt6.QtWidgets import QHBoxLayout, QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt6.QtGui import QPalette, QColor

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Kolory')
        self.layout = QVBoxLayout()
        self.layout.addWidget(Color('red'))
        self.layout.addWidget(Color('green'))
        self.layout.addWidget(Color('blue'))

        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()