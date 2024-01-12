import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, QVBoxLayout, QLineEdit, QWidget


class TreeSearchApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tree Search App")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        # Create QTreeWidget
        self.tree_widget = QTreeWidget()
        self.tree_widget.setHeaderLabels(['Items'])
        self.populate_tree()
        self.layout.addWidget(self.tree_widget)

        # Create QLineEdit for searching
        self.search_line_edit = QLineEdit()
        self.search_line_edit.setPlaceholderText("Search...")
        self.search_line_edit.textChanged.connect(self.search_items)
        self.layout.addWidget(self.search_line_edit)

        self.central_widget.setLayout(self.layout)

    def populate_tree(self):
        for i in range(1, 6):
            parent_item = QTreeWidgetItem(self.tree_widget, ['Parent {}'.format(i)])
            for j in range(1, 4):
                child_item = QTreeWidgetItem(parent_item, ['Child {}'.format(j)])

    def search_items(self):
        search_text = self.search_line_edit.text().lower()

        for i in range(self.tree_widget.topLevelItemCount()):
            parent_item = self.tree_widget.topLevelItem(i)
            parent_text = parent_item.text(0).lower()
            parent_item.setHidden(search_text not in parent_text)

            for j in range(parent_item.childCount()):
                child_item = parent_item.child(j)
                child_text = child_item.text(0).lower()
                child_item.setHidden(search_text not in child_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = TreeSearchApp()
    main_window.show()
    sys.exit(app.exec_())
