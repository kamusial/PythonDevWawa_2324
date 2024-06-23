from PyQt6.QtWidgets import QApplication, QWidget, QTreeView, QMainWindow
import sys
from PyQt6.QtGui import QStandardItem, QStandardItemModel, QIcon
from PyQt6.QtCore import Qt

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
        self.tree_view.setDragEnabled(True)
        self.tree_view.setAcceptDrops(True)
        self.tree_view.setDropIndicatorShown(True)


    def file_explorer(self):
        root_item = QStandardItem("Root")
        self.model.appendRow(root_item)

        folder_item = QStandardItem('Folder1')
        file_item = QStandardItem('File 1')
        file_item.setIcon(QIcon('icon.png'))
        file_item.setToolTip('To jest plik 1')
        root_item.appendRow(folder_item)
        folder_item.appendRow(file_item)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mineData.hasUrls():
            event.setDropAction(Qt.DropAction.MoveAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropActions(Qt.DropAction.MoveAction)
            event.accept()
        else:
            event.ignore()



app = QApplication(sys.argv)
window = TreeViewWindow()
window.show()
app.exec()


