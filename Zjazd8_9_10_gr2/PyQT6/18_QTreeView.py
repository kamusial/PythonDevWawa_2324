from PyQt6.QtWidgets import QApplication, QWidget, QTreeView, QMainWindow
import sys
from PyQt6.QtGui import QStandardItem, QStandardItemModel

class TreeViewWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry(800, 200, 700, 400)
        self.setWindowTitle("Drzewko")

        self.tree_view = QTreeView()
        self.setCentralWidget(self.tree_view)

        self.model = QStandardItemModel()
        self.tree_view.setModel(self.model)

        self.file_explorer()

    def file_explorer(self):
        root_item = QStandardItem("Root")
        self.model.appendRow(root_item)

        folder_item = QStandardItem('Folder1')
        file_item = QStandardItem('File 1')
        root_item.appendRow(folder_item)
        folder_item.appendRow(file_item)


app = QApplication(sys.argv)
window = TreeViewWindow()
window.show()
app.exec()


