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
        MainWindow.resize(1554, 999)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout_5 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.widget_bg = QWidget(self.centralwidget)
        self.widget_bg.setObjectName(u"widget_bg")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_bg)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.widget_control = QWidget(self.widget_bg)
        self.widget_control.setObjectName(u"widget_control")
        self.verticalLayout_3 = QVBoxLayout(self.widget_control)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.widget_control)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.widget_control)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.note_book = QPushButton(self.widget_control)
        self.note_book.setObjectName(u"note_book")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.note_book.sizePolicy().hasHeightForWidth())
        self.note_book.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.note_book)

        self.reader = QPushButton(self.widget_control)
        self.reader.setObjectName(u"reader")
        sizePolicy.setHeightForWidth(self.reader.sizePolicy().hasHeightForWidth())
        self.reader.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.reader)

        self.player = QPushButton(self.widget_control)
        self.player.setObjectName(u"player")
        sizePolicy.setHeightForWidth(self.player.sizePolicy().hasHeightForWidth())
        self.player.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.player)

        self.label_3 = QLabel(self.widget_control)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.recording = QPushButton(self.widget_control)
        self.recording.setObjectName(u"recording")
        sizePolicy.setHeightForWidth(self.recording.sizePolicy().hasHeightForWidth())
        self.recording.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.recording)

        self.screen_recording = QPushButton(self.widget_control)
        self.screen_recording.setObjectName(u"screen_recording")
        sizePolicy.setHeightForWidth(self.screen_recording.sizePolicy().hasHeightForWidth())
        self.screen_recording.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.screen_recording)

        self.screen_shot = QPushButton(self.widget_control)
        self.screen_shot.setObjectName(u"screen_shot")
        sizePolicy.setHeightForWidth(self.screen_shot.sizePolicy().hasHeightForWidth())
        self.screen_shot.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.screen_shot)

        self.video_clip = QPushButton(self.widget_control)
        self.video_clip.setObjectName(u"video_clip")
        sizePolicy.setHeightForWidth(self.video_clip.sizePolicy().hasHeightForWidth())
        self.video_clip.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.video_clip)

        self.audio_clips = QPushButton(self.widget_control)
        self.audio_clips.setObjectName(u"audio_clips")
        sizePolicy.setHeightForWidth(self.audio_clips.sizePolicy().hasHeightForWidth())
        self.audio_clips.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.audio_clips)

        self.label_4 = QLabel(self.widget_control)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.color_picker = QPushButton(self.widget_control)
        self.color_picker.setObjectName(u"color_picker")
        sizePolicy.setHeightForWidth(self.color_picker.sizePolicy().hasHeightForWidth())
        self.color_picker.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.color_picker)

        self.code_export = QPushButton(self.widget_control)
        self.code_export.setObjectName(u"code_export")
        sizePolicy.setHeightForWidth(self.code_export.sizePolicy().hasHeightForWidth())
        self.code_export.setSizePolicy(sizePolicy)

        self.verticalLayout.addWidget(self.code_export)

        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(4, 1)
        self.verticalLayout.setStretch(5, 1)
        self.verticalLayout.setStretch(6, 1)
        self.verticalLayout.setStretch(7, 1)
        self.verticalLayout.setStretch(8, 1)
        self.verticalLayout.setStretch(9, 1)
        self.verticalLayout.setStretch(10, 1)
        self.verticalLayout.setStretch(11, 1)
        self.verticalLayout.setStretch(12, 1)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 24)
        self.verticalLayout_2.setStretch(3, 14)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.horizontalLayout_3.addWidget(self.widget_control)

        self.widget = QWidget(self.widget_bg)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_tittle = QWidget(self.widget)
        self.widget_tittle.setObjectName(u"widget_tittle")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_tittle)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.compact_mode = QPushButton(self.widget_tittle)
        self.compact_mode.setObjectName(u"compact_mode")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.compact_mode.sizePolicy().hasHeightForWidth())
        self.compact_mode.setSizePolicy(sizePolicy1)
        self.compact_mode.setMinimumSize(QSize(80, 40))

        self.horizontalLayout.addWidget(self.compact_mode)

        self.pushButton = QPushButton(self.widget_tittle)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.widget_tittle)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.widget_tittle)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy1.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy1)
        self.pushButton_3.setMinimumSize(QSize(40, 40))

        self.horizontalLayout.addWidget(self.pushButton_3)

        self.horizontalLayout.setStretch(0, 100)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 1)

        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_4.addWidget(self.widget_tittle)

        self.widget_main = QWidget(self.widget)
        self.widget_main.setObjectName(u"widget_main")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_main)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.stackedWidget = QStackedWidget(self.widget_main)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_6.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.widget_main)

        self.verticalLayout_4.setStretch(0, 1)
        self.verticalLayout_4.setStretch(1, 20)

        self.verticalLayout_5.addLayout(self.verticalLayout_4)


        self.horizontalLayout_3.addWidget(self.widget)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 8)

        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_5.addWidget(self.widget_bg)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"LOGO", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u5b66\u4e60\u4e13\u7528", None))
        self.note_book.setText(QCoreApplication.translate("MainWindow", u"\u7b14\u8bb0\u672c", None))
        self.reader.setText(QCoreApplication.translate("MainWindow", u"\u9605\u8bfb\u5668", None))
        self.player.setText(QCoreApplication.translate("MainWindow", u"\u64ad\u653e\u5668", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u529e\u516c\u4e13\u7528", None))
        self.recording.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u97f3", None))
        self.screen_recording.setText(QCoreApplication.translate("MainWindow", u"\u5f55\u5c4f", None))
        self.screen_shot.setText(QCoreApplication.translate("MainWindow", u"\u622a\u5c4f", None))
        self.video_clip.setText(QCoreApplication.translate("MainWindow", u"\u89c6\u9891\u526a\u8f91", None))
        self.audio_clips.setText(QCoreApplication.translate("MainWindow", u"\u97f3\u9891\u526a\u8f91", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u5176\u4ed6\u529f\u80fd", None))
        self.color_picker.setText(QCoreApplication.translate("MainWindow", u"\u62fe\u8272\u5668", None))
        self.code_export.setText(QCoreApplication.translate("MainWindow", u"\u4ee3\u7801\u5bfc\u51fa", None))
        self.compact_mode.setText(QCoreApplication.translate("MainWindow", u"\u7b80\u6d01\u6a21\u5f0f", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u2014", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u53e3", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
    # retranslateUi

