# -*- coding: utf-8 -*-
import sys
import os
import xml.etree.ElementTree as et
################################################################################
## Form generated from reading UI file 'maininterfacexcOaCR.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                          QRect, QSize, QUrl, Qt, QFile, QIODevice, )
from PyQt5.QtGui import ( QBrush, QColor, QConicalGradient, QCursor, QFont,
                         QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                         QRadialGradient, QStandardItemModel, QStandardItem, )
from PyQt5.QtWidgets import (QHBoxLayout, QVBoxLayout, QFrame, QLabel, QTreeWidget, QTreeWidgetItem, QMainWindow, QWidget,
                             QListView, QMenuBar, QApplication, QComboBox, QPushButton, QLineEdit)
from PyQt5.QtXml import QDomDocument
from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5 import Qt

'''try:
    _fromUtf8 = QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s:s'''
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
"QPushButton{\n"
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
        self.searchBar = QLineEdit(self.treeFrame)
        self.searchBar.setObjectName(u"searchBar")
        self.searchBar.setPlaceholderText("Search...")
        self.treeWidget = QTreeWidget(self.treeFrame)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setHeaderLabel("REsOUrcES")
        self.searchBar.textChanged[str].connect(self.searchItem)
        self.verticalLayout.addWidget(self.searchBar)
        self.verticalLayout.addWidget(self.treeWidget)
        #self.load_xml_file("data.xml")
        self.f = open("data.xml", "r",1,"utf-8").read()
        self.printTree(self.f,"English")

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
        self.langBox.addItems(["English", "Hausa", "Igbo", "Yorùbá"])
        self.langBox.currentIndexChanged.connect(self.refreshTree)
        icon = QIcon()
        icon.addPixmap(QPixmap("speaker-icon.jpeg"))

        self.sound = QPushButton()
        self.sound.setIcon(icon)
        self.mainLayout = QVBoxLayout(self.centralwidget)

        self.webView = QWebEngineView(self.centralwidget)
        self.webView.setObjectName(u"webView")
        self.webView.setMinimumSize(QSize(350, 0))
        self.webView.setHtml("<p>Welcome to Digital Resource Page.</p>")
        self.treeWidget.itemClicked.connect(self.onItemClicked)
        self.webView.show()

        # self.mainFrame.setFrameShadow(QFrame.Raised)


        #self.horizontalLayout.addWidget(self.mainFrame, 0, Qt.AlignRight)
        self.preholay = QHBoxLayout()
        self.preholay.addWidget(self.langBox)
        self.preholay.addWidget(self.sound)
        self.mainLayout.addLayout(self.preholay)
        self.mainLayout.addWidget(self.webView)
        self.horizontalLayout.addLayout(self.mainLayout,Qt.AlignRight)

        #self.horizontalLayouct.addWidget(self.webView, 0, Qt.AlignRight)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 680, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    def searchItem(self):
        print("It works to point1")
        text = self.searchBar.text()
        print(text)
        itemfound = self.treeWidget.findItems(text,Qt.Qt.MatchContains)
        print(itemfound)
    def refreshTree(self,i):
        print("Current index", i, "selection changed ", self.langBox.currentText())
        self.treeWidget.clear()
        self.printTree(self.f,self.langBox.currentText())
    def printTree(self,s, lang):
        tree = et.fromstring(s)
        self.treeWidget.setColumnCount(1)
        a = QTreeWidgetItem([tree.tag])
        self.treeWidget.addTopLevelItem(a)

        def displaytree(a,s,lang):
            for child in s:
                if child.tag != "item":
                    if lang == "English":
                        branch = QTreeWidgetItem([child.attrib["name"]])
                        branch.setText(1, child.attrib["name"])
                    elif lang == "Hausa":
                        branch = QTreeWidgetItem([child.attrib["hname"]])
                        branch.setText(1, child.attrib["name"])
                    elif lang == "Igbo":
                        branch = QTreeWidgetItem([child.attrib["iname"]])
                        branch.setText(1, child.attrib["name"])
                    elif lang == "Yorùbá":
                        branch = QTreeWidgetItem([child.attrib["yname"]])
                        branch.setText(1, child.attrib["name"])
                else:
                    if lang == "English":
                        branch = QTreeWidgetItem([child.attrib["name"]])
                        branch.setText(1, child.attrib["name"])
                        branch.setText(2, child.attrib["desc"])
                    elif lang == "Hausa":
                        branch = QTreeWidgetItem([child.attrib["hname"]])
                        branch.setText(1, child.attrib["name"])
                        branch.setText(2, child.attrib["desc"])
                        branch.setText(3, child.attrib["hdesc"])
                    elif lang == "Igbo":
                        branch = QTreeWidgetItem([child.attrib["iname"]])
                        branch.setText(1, child.attrib["name"])
                        branch.setText(2, child.attrib["desc"])
                        branch.setText(3, child.attrib["idesc"])
                    elif lang == "Yorùbá":
                        branch = QTreeWidgetItem([child.attrib["yname"]])
                        branch.setText(1,child.attrib["name"] )
                        branch.setText(2, child.attrib["desc"])
                        branch.setText(3, child.attrib["ydesc"])
                    #print(child.attrib)
                a.addChild(branch)
                displaytree(branch,child,lang)
        displaytree(a,tree,lang)
    # setupUi

    def onItemClicked(self):
        item = self.treeWidget.currentItem()
        print(item.text(0))
        itemimage = "Resource"+self.getParentPath(item)+".jpg"
        print(itemimage)
        print(item.text(1))
        alttext = item.text(0)
        etext = item.text(2)
        desc = item.text(3)
        if self.langBox.currentText() == "English":
            self.webView.setHtml('''<h3>''' + alttext + '''</h3><img  height="200" src="''' + itemimage + '''" style="display: block; text-align: left;" width="300"/>
                    <h4>Description</h4><p>'''+etext+'''</p>''', baseUrl=QUrl.fromLocalFile(os.getcwd() + os.path.sep))
        elif self.langBox.currentText() == "Hausa":
            self.webView.setHtml('''<h3>''' + alttext + '''</h3><img  height="200" src="''' + itemimage + '''" style="display: block; text-align: left;" width="300"/>
                                <h4>Description</h4><p>''' + etext + '''</p><h4>Hausa Description</h4><p>'''+desc+'''</p>''',
                                 baseUrl=QUrl.fromLocalFile(os.getcwd() + os.path.sep))
        elif self.langBox.currentText() == "Igbo":
            self.webView.setHtml('''<h3>''' + alttext + '''</h3><img  height="200" src="''' + itemimage + '''" style="display: block; text-align: left;" width="300"/>
                                            <h4>Description</h4><p>''' + etext + '''</p><h4>Igbo Description</h4><p>''' + desc + '''</p>''',
                                 baseUrl=QUrl.fromLocalFile(os.getcwd() + os.path.sep))
        elif self.langBox.currentText() == "Yorùbá":
            self.webView.setHtml('''<h3>''' + alttext + '''</h3><img  height="200" src="''' + itemimage + '''" style="display: block; text-align: left;" width="300"/>
                                            <h4>Description</h4><p>''' + etext + '''</p><h4>Yorùbá Description</h4><p>''' + desc + '''</p>''',
                                 baseUrl=QUrl.fromLocalFile(os.getcwd() + os.path.sep))

        #self.webView.setHtml('''<h3>''' + item.text(0) +''' : '''+item.text(3) +'''</h3><img  height="200" src="'''+itempath+'''" style="display: block; text-align: left;" width="300"/>''', baseUrl=QUrl.fromLocalFile(os.getcwd()+os.path.sep))
        #self.webView.setHtml('''<h3>''' + alttext +'''</h3><img  height="200" src="''' + itempath + '''" style="display: block; text-align: left;" width="300"/>
        #<h4>E</h4>''', baseUrl=QUrl.fromLocalFile(os.getcwd() + os.path.sep))
        #print(self.getParentPath(item))

    def getParentPath(self, item):
        def getParent(item,outstring):
            if item.parent() is None:
                return outstring
            outstring = item.parent().text(1) + "/"+outstring
            return getParent(item.parent(), outstring)
        output = getParent(item, item.text(1))
        #print(output)
        return output

    def retranslateUi(self, MainWindow):
        #QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts, True)
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
    # retranslateUi
"""
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

        # Clear the QtreeWidget
        #self.treeWidget.hide()

        # Create the root item for the QtreeWidget
        root_item = xml_doc.documentElement()

        # Set the root item as the model for the QtreeWidget
        self.treeWidget.setModel(QDomModel(root_item))

        # Expand all items in the QtreeWidget
        self.treeWidget.expandAll()

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

"""


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