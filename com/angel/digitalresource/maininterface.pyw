# -*- coding: utf-8 -*-
import sys

################################################################################
## Form generated from reading UI file 'maininterfacexcOaCR.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                          QRect, QSize, QUrl, Qt, QFile, QIODevice)
from PyQt5.QtGui import ( QBrush, QColor, QConicalGradient, QCursor, QFont,
                         QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                         QRadialGradient, QStandardItemModel, QStandardItem)
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QFrame, QLabel, QTreeWidget, QMainWindow, QWidget,
                             QListView, QMenuBar, QApplication, QComboBox)
from PyQt5.QtXml import QDomDocument
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(680, 510)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"border: none;\n"
"background-color: transparent;\n"
"color:#ffffff;\n"
"}\n"
"#treeFrame{\n"
"background-color:#071e26;\n"
"border-radius:20px;\n"
"}\n"
"QComboBox{\n"
"padding: 10px;\n"
"background-color: #0c0c24;\n"
"border-radius:5px;\n"
"}\n"
"#mainFrame{\n"
"background-color:#b5d3ff;\n"
"border-radius:10px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.treeFrame = QFrame(self.centralwidget)
        self.treeFrame.setObjectName(u"treeFrame")
        self.treeFrame.setMinimumSize(QSize(150, 0))
        self.treeFrame.setFrameShape(QFrame.StyledPanel)
        self.treeFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.treeFrame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.treeView = QTreeWidget(self.treeFrame)
        self.treeView.setObjectName(u"treeView")
        self.treeView.itemClicked.connect(self.handleItemClicked)

        self.verticalLayout.addWidget(self.treeView)
        self.load_xml_file("data.xml")

        self.horizontalLayout.addWidget(self.treeFrame, 0, Qt.AlignLeft)

        #self.listFrame = QFrame(self.centralwidget)
        #self.listFrame.setObjectName(u"listFrame")
        #self.listFrame.setMinimumSize(QSize(150, 0))
        #self.listFrame.setFrameShape(QFrame.StyledPanel)
        #self.listFrame.setFrameShadow(QFrame.Raised)
        #self.verticalLayout_2 = QVBoxLayout(self.listFrame)
        #self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        #self.listView = QListView(self.listFrame)
        #self.listView.setObjectName(u"listView")

        #self.verticalLayout_2.addWidget(self.listView)


        #self.horizontalLayout.addWidget(self.listFrame, 0, Qt.AlignLeft)

        #self.mainFrame = QFrame(self.centralwidget)
        #self.mainFrame.setObjectName(u"mainFrame")
        #self.mainFrame.setMinimumSize(QSize(350, 0))
        #self.mainFrame.setFrameShape(QFrame.StyledPanel)
        #self.mainFrame.setFrameShadow(QFrame.Raised)
        self.langBox = QComboBox(self.centralwidget)
        self.langBox.setObjectName(u"langBox")
        self.langBox.addItems(["English", "Hausa", "Igbo", "Yoruba"])
        self.mainLayout = QVBoxLayout(self.centralwidget)

        self.webView = QWebEngineView(self.centralwidget)
        self.webView.setObjectName(u"webView")
        self.webView.setMinimumSize(QSize(350, 0))
        self.webView.setHtml("<p>Welcome to Digital Resource Page.</p>")
        self.webView.show()

        # self.mainFrame.setFrameShadow(QFrame.Raised)


        #self.horizontalLayout.addWidget(self.mainFrame, 0, Qt.AlignRight)
        self.mainLayout.addWidget(self.langBox)
        self.mainLayout.addWidget(self.webView)
        self.horizontalLayout.addLayout(self.mainLayout,Qt.AlignRight)

        #self.horizontalLayout.addWidget(self.webView, 0, Qt.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 680, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    def handleItemClicked(self, item):
        if item.isSelectable():
            self.webView.setHtml("<p>"+item+"</p>")
    def retranslateUi(self, MainWindow):
        #QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts, True)
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi

    def load_xml_file(self, file_path):
        # Create a QDomDocument to parse the XML file
        xml_doc = QDomDocument()

        # Open the XML file
        file = QFile(file_path)
        if not file.open(QIODevice.ReadOnly | QIODevice.Text):
            print("Failed to open file:", file.errorString())
            return

        # Set the content of the QDomDocument from the file
        if not xml_doc.setContent(file):
            file.close()
            print("Failed to parse XML content.")
            return

        file.close()

        # Clear the QTreeView
        #self.treeView.hide()

        # Create the root item for the QTreeView
        root_item = xml_doc.documentElement()

        # Set the root item as the model for the QTreeView
        self.treeView.setModel(QDomModel(root_item))

        # Expand all items in the QTreeView
        self.treeView.expandAll()

class QDomModel(QStandardItemModel):
    def __init__(self, root):
        super().__init__()
        self.root_item = self.create_items(root, self.invisibleRootItem())

    def create_items(self, node, parent_item):
        print(node.nodeName(),end="\t")
        item = QStandardItem(node.nodeName())
        print(node.attributes().count(), end="\t")
        if node.nodeName() != "item":
            parent_item.appendRow(item)
        else:
            for i in range(node.attributes().count()):
                attr = node.attributes().item(i)
                attr_item = QStandardItem(f"{attr.nodeValue()}")
                parent_item.appendRow(attr_item)

        child_nodes = node.childNodes()
        print(type(child_nodes), len(child_nodes))

        for i in range(child_nodes.count()):
            self.create_items(child_nodes.at(i), item)

        return item




class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

if __name__ == "__main__":
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts, True)
    app = QApplication(sys.argv)
    interface = MainWindow()
    interface.show()
    sys.exit(app.exec_())
    #import pandas as pd
    #data = pd.read_csv()
    #data.index()