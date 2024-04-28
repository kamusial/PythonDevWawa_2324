import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = QLabel('Moja labelka')
        self.setCentralWidget(self.label)

    def mouseMoveEvent(self, a0):
        self.label.setText('ruch')

    def mousePressEvent(self, e):
        if e.button() == Qt.MouseButton.LeftButton:
            self.label.setText('Nacisnieto lewy')
        elif e.button() == Qt.MouseButton.MiddleButton:
            self.label.setText('Nacisnieto srodkowy')
        elif e.button() == Qt.MouseButton.RightButton:
            self.label.setText('Nacisnieto prawy')

    def mouseReleaseEvent(self, e):
        self.label.setText('mysz puszczona')
        print('Mysz puszczona')

    def mouseDoubleClickEvent(self, e):
        self.label.setText('kliknieto 2 razy')
        print('Nacisneto 2 razy')

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
