from PyQt6.QtWidgets import QApplication, QWidget, QMainWindow, QDialog
import sys

app = QApplication(sys.argv)    #proste okno, tylko z Xem do zamkniecia

window1 = QDialog()
window1.setWindowTitle('QDialog window')

window2 = QWidget()
window2.setWindowTitle('QWidget window')

window3 = QMainWindow()  #zaawansowane okno z wiekszą liczbą funkcji
window3.setWindowTitle('QMainWindow')
window3.statusBar().showMessage('Status to .......')
window3.menuBar().addMenu('Options')

window1.show()
window2.show()
window3.show()

app.exec()
