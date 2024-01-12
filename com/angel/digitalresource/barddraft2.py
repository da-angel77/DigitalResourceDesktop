import sys
from PyQt5.QtCore import QFile, QDomDocument, QDomElement, QDomNodeList
from PyQt5.QtGui import QTreeView
from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.treeView = QTreeView()
        self.model = QDomModel()
        self.model.setRootPath(QFile("data.xml").absoluteFilePath())
        self.treeView.setModel(self.model)

        self.setCentralWidget(self.treeView)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())