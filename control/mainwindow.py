
from PySide2 import QtCore,QtGui,QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from ui.ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

        self.draw_style()

    def draw_style(self):
        model = QStandardItemModel()
        self.treeView.setModel(model)

        root = model.invisibleRootItem()

        # 添加“姓名”节点的子节点
        zhangsan_item = QStandardItem('张三')
        item1 = QStandardItem('张三')
        item2 = QStandardItem('李四')
        item3 = QStandardItem('王五')
        zhangsan_item.appendRow(item1)
        zhangsan_item.appendRow(item2)
        zhangsan_item.appendRow(item3)
        root.appendRow(zhangsan_item)

        root.appendRow(QStandardItem('李四'))
        root.appendRow(QStandardItem('王五'))

        # 添加“性别”节点的子节点
        gender_item = QStandardItem('性别')
        gender_item.appendRow(QStandardItem('男'))
        gender_item.appendRow(QStandardItem('女'))
        root.appendRow(gender_item)

        self.treeView.expandAll()
        self.treeView.setModel(model)
