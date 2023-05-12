# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'simplifiedwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SimplifiedWindow(object):
    def setupUi(self, SimplifiedWindow):
        if not SimplifiedWindow.objectName():
            SimplifiedWindow.setObjectName(u"SimplifiedWindow")
        SimplifiedWindow.resize(743, 179)
        self.centralwidget = QWidget(SimplifiedWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(11, 66, 711, 30))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.note_book = QPushButton(self.widget)
        self.note_book.setObjectName(u"note_book")

        self.horizontalLayout.addWidget(self.note_book)

        self.recording = QPushButton(self.widget)
        self.recording.setObjectName(u"recording")

        self.horizontalLayout.addWidget(self.recording)

        self.screen_recording = QPushButton(self.widget)
        self.screen_recording.setObjectName(u"screen_recording")

        self.horizontalLayout.addWidget(self.screen_recording)

        self.screen_shot = QPushButton(self.widget)
        self.screen_shot.setObjectName(u"screen_shot")

        self.horizontalLayout.addWidget(self.screen_shot)

        self.video_clip = QPushButton(self.widget)
        self.video_clip.setObjectName(u"video_clip")

        self.horizontalLayout.addWidget(self.video_clip)

        self.audio_clips = QPushButton(self.widget)
        self.audio_clips.setObjectName(u"audio_clips")

        self.horizontalLayout.addWidget(self.audio_clips)

        self.color_picker = QPushButton(self.widget)
        self.color_picker.setObjectName(u"color_picker")

        self.horizontalLayout.addWidget(self.color_picker)

        self.reader = QPushButton(self.widget)
        self.reader.setObjectName(u"reader")

        self.horizontalLayout.addWidget(self.reader)

        self.main_window = QPushButton(self.widget)
        self.main_window.setObjectName(u"main_window")

        self.horizontalLayout.addWidget(self.main_window)

        SimplifiedWindow.setCentralWidget(self.centralwidget)
        self.dockWidget = QDockWidget(SimplifiedWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidgetContents = QWidget()
        self.dockWidgetContents.setObjectName(u"dockWidgetContents")
        self.horizontalLayout_2 = QHBoxLayout(self.dockWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stackedWidget = QStackedWidget(self.dockWidgetContents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_2.addWidget(self.stackedWidget)

        self.dockWidget.setWidget(self.dockWidgetContents)
        SimplifiedWindow.addDockWidget(Qt.BottomDockWidgetArea, self.dockWidget)

        self.retranslateUi(SimplifiedWindow)

        QMetaObject.connectSlotsByName(SimplifiedWindow)
    # setupUi

    def retranslateUi(self, SimplifiedWindow):
        SimplifiedWindow.setWindowTitle(QCoreApplication.translate("SimplifiedWindow", u"MainWindow", None))
        self.note_book.setText(QCoreApplication.translate("SimplifiedWindow", u"\u7b14\u8bb0\u672c", None))
        self.recording.setText(QCoreApplication.translate("SimplifiedWindow", u"\u5f55\u97f3", None))
        self.screen_recording.setText(QCoreApplication.translate("SimplifiedWindow", u"\u5f55\u5c4f", None))
        self.screen_shot.setText(QCoreApplication.translate("SimplifiedWindow", u"\u622a\u5c4f", None))
        self.video_clip.setText(QCoreApplication.translate("SimplifiedWindow", u"\u89c6\u9891\u526a\u8f91", None))
        self.audio_clips.setText(QCoreApplication.translate("SimplifiedWindow", u"\u97f3\u9891\u526a\u8f91", None))
        self.color_picker.setText(QCoreApplication.translate("SimplifiedWindow", u"\u62fe\u8272\u5668", None))
        self.reader.setText(QCoreApplication.translate("SimplifiedWindow", u"\u9605\u8bfb\u5668", None))
        self.main_window.setText(QCoreApplication.translate("SimplifiedWindow", u"\u4e3b\u754c\u9762", None))
    # retranslateUi

