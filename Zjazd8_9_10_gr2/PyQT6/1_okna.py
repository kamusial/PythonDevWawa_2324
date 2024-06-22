from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog, QPushButton
import sys

app = QApplication(sys.argv)

window1 = QDialog()
window1.setWindowTitle('Proste okno tylko z Xem do zamkniecia')
window1.show()

window2 = QWidget()
window2.setWindowTitle('proste okno, z Xem, minimalizacją i pełnym ekranem')
window2.show()

window3 = QMainWindow()
window3.setWindowTitle('Zaawansowane okno')
window3.statusBar().showMessage('na dole leci progress......')
window3.menuBar().addMenu('Options')
window3.show()

app.exec()