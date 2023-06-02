# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'codeexport.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CodeExport(object):
    def setupUi(self, CodeExport):
        if not CodeExport.objectName():
            CodeExport.setObjectName(u"CodeExport")
        CodeExport.resize(677, 680)
        self.horizontalLayout_5 = QHBoxLayout(CodeExport)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget = QWidget(CodeExport)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_4 = QHBoxLayout(self.widget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.dir_tree = QTreeView(self.widget)
        self.dir_tree.setObjectName(u"dir_tree")

        self.horizontalLayout_3.addWidget(self.dir_tree)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.status_box = QTextEdit(self.widget)
        self.status_box.setObjectName(u"status_box")

        self.verticalLayout_3.addWidget(self.status_box)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label)

        self.selection = QComboBox(self.widget)
        self.selection.addItem("")
        self.selection.addItem("")
        self.selection.addItem("")
        self.selection.addItem("")
        self.selection.setObjectName(u"selection")

        self.horizontalLayout.addWidget(self.selection)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.import_folder = QPushButton(self.widget)
        self.import_folder.setObjectName(u"import_folder")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.import_folder.sizePolicy().hasHeightForWidth())
        self.import_folder.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.import_folder)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.export_single_file = QPushButton(self.widget)
        self.export_single_file.setObjectName(u"export_single_file")
        sizePolicy.setHeightForWidth(self.export_single_file.sizePolicy().hasHeightForWidth())
        self.export_single_file.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.export_single_file)

        self.export_many_file = QPushButton(self.widget)
        self.export_many_file.setObjectName(u"export_many_file")
        sizePolicy.setHeightForWidth(self.export_many_file.sizePolicy().hasHeightForWidth())
        self.export_many_file.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.export_many_file)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.verticalLayout_3.setStretch(0, 2)
        self.verticalLayout_3.setStretch(1, 1)

        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.content = QTextEdit(self.widget)
        self.content.setObjectName(u"content")

        self.verticalLayout_4.addWidget(self.content)


        self.horizontalLayout_4.addLayout(self.verticalLayout_4)


        self.horizontalLayout_5.addWidget(self.widget)


        self.retranslateUi(CodeExport)

        QMetaObject.connectSlotsByName(CodeExport)
    # setupUi

    def retranslateUi(self, CodeExport):
        CodeExport.setWindowTitle(QCoreApplication.translate("CodeExport", u"Form", None))
        self.label.setText(QCoreApplication.translate("CodeExport", u"\u8bed\u8a00\uff1a", None))
        self.selection.setItemText(0, QCoreApplication.translate("CodeExport", u"Python", None))
        self.selection.setItemText(1, QCoreApplication.translate("CodeExport", u"C", None))
        self.selection.setItemText(2, QCoreApplication.translate("CodeExport", u"C++", None))
        self.selection.setItemText(3, QCoreApplication.translate("CodeExport", u"Golang", None))

        self.import_folder.setText(QCoreApplication.translate("CodeExport", u"\u5bfc\u5165\u6587\u4ef6\u5939", None))
        self.export_single_file.setText(QCoreApplication.translate("CodeExport", u"\u5bfc\u51fa\u5355\u6587\u4ef6", None))
        self.export_many_file.setText(QCoreApplication.translate("CodeExport", u"\u5bfc\u51fa\u591a\u6587\u4ef6", None))
    # retranslateUi

