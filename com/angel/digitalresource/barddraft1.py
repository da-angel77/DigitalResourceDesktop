import sys
from PyQt5.QtCore import QDir, QFile, QFileInfo
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView,QFileDialog
from PyQt5.QtXml import QDomDocument


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.model = QStandardItemModel()
        self.treeView = QTreeView()
        self.treeView.setModel(self.model)

        self.loadFile()

        self.setCentralWidget(self.treeView)

    def loadFile(self):
        fileInfo = QFileInfo("data.xml")
        self.model.clear()

        with QFile("data.xml") as f:
            dom = QDomDocument()
            dom.setContent(f)

            for node in dom.documentElement.childNodes():
                item = QStandardItem(node.nodeName())
                item.setEditable(False)

                for child in node.childNodes():
                    item.appendRow(QStandardItem(child.nodeName()))

                self.model.appendRow(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
