# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1023, 684)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.reader_2 = QPushButton(self.centralwidget)
        self.reader_2.setObjectName(u"reader_2")
        self.reader_2.setGeometry(QRect(10, 340, 93, 28))
        self.treeView = QTreeView(self.centralwidget)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setGeometry(QRect(220, 50, 481, 561))
        self.reader = QPushButton(self.centralwidget)
        self.reader.setObjectName(u"reader")
        self.reader.setGeometry(QRect(20, 290, 93, 28))
        self.screen_shot = QPushButton(self.centralwidget)
        self.screen_shot.setObjectName(u"screen_shot")
        self.screen_shot.setGeometry(QRect(20, 130, 93, 28))
        self.video_clip = QPushButton(self.centralwidget)
        self.video_clip.setObjectName(u"video_clip")
        self.video_clip.setGeometry(QRect(20, 170, 93, 28))
        self.recording = QPushButton(self.centralwidget)
        self.recording.setObjectName(u"recording")
        self.recording.setGeometry(QRect(20, 50, 93, 28))
        self.screen_recording = QPushButton(self.centralwidget)
        self.screen_recording.setObjectName(u"screen_recording")
        self.screen_recording.setGeometry(QRect(20, 90, 93, 28))
        self.note_book = QPushButton(self.centralwidget)
        self.note_book.setObjectName(u"note_book")
        self.note_book.setGeometry(QRect(10, 10, 93, 28))
        self.audio_clips = QPushButton(self.centralwidget)
        self.audio_clips.setObjectName(u"audio_clips")
        self.audio_clips.setGeometry(QRect(20, 210, 93, 28))
        self.color_picker = QPushButton(self.centralwidget)
        self.color_picker.setObjectName(u"color_picker")
        self.color_picker.setGeometry(QRect(20, 250, 93, 28))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.reader_2.setText(QCoreApplication.translate("MainWindow", u"\u4ee3\u7801\u5bfc\u51fa", None))
        self.reader.setText(QCoreApplication.translate("MainWindow", u"\u9605\u8bfb\u5668", None))
        self.screen_shot.setText(QCoreApplication.translate("MainWindow", u"\u622a\u5c4f", None))
        self.video_clip.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u526a\u8f91", None))
        self.recording.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u97f3", None))
        self.screen_recording.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5c4f", None))
        self.note_book.setText(QCoreApplication.translate("MainWindow", u"\u7b14\u8bb0\u672c", None))
        self.audio_clips.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u9891\u526a\u8f91", None))
        self.color_picker.setText(QCoreApplication.translate("MainWindow", u"\u62fe\u8272\u5668", None))
    # retranslateUi

