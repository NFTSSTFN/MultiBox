# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'video_player.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_VideoWidget(object):
    def setupUi(self, VideoWidget):
        if not VideoWidget.objectName():
            VideoWidget.setObjectName(u"VideoWidget")
        VideoWidget.resize(1035, 716)
        self.horizontalLayout_4 = QHBoxLayout(VideoWidget)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget = QWidget(VideoWidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_3 = QHBoxLayout(self.widget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.start_pause = QPushButton(self.widget)
        self.start_pause.setObjectName(u"start_pause")

        self.horizontalLayout.addWidget(self.start_pause)

        self.next = QPushButton(self.widget)
        self.next.setObjectName(u"next")

        self.horizontalLayout.addWidget(self.next)

        self.time__stamp = QLabel(self.widget)
        self.time__stamp.setObjectName(u"time__stamp")

        self.horizontalLayout.addWidget(self.time__stamp)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.settings = QPushButton(self.widget)
        self.settings.setObjectName(u"settings")

        self.horizontalLayout.addWidget(self.settings)

        self.adjust_volume = QPushButton(self.widget)
        self.adjust_volume.setObjectName(u"adjust_volume")

        self.horizontalLayout.addWidget(self.adjust_volume)

        self.max_screen = QPushButton(self.widget)
        self.max_screen.setObjectName(u"max_screen")

        self.horizontalLayout.addWidget(self.max_screen)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.video_dir = QTableWidget(self.widget)
        self.video_dir.setObjectName(u"video_dir")

        self.verticalLayout.addWidget(self.video_dir)

        self.open_file = QPushButton(self.widget)
        self.open_file.setObjectName(u"open_file")

        self.verticalLayout.addWidget(self.open_file)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_4.addWidget(self.widget)


        self.retranslateUi(VideoWidget)

        QMetaObject.connectSlotsByName(VideoWidget)
    # setupUi

    def retranslateUi(self, VideoWidget):
        VideoWidget.setWindowTitle(QCoreApplication.translate("VideoWidget", u"Form", None))
        self.start_pause.setText(QCoreApplication.translate("VideoWidget", u"start", None))
        self.next.setText(QCoreApplication.translate("VideoWidget", u"next", None))
        self.time__stamp.setText(QCoreApplication.translate("VideoWidget", u"00:00:00/00:00:00", None))
        self.settings.setText(QCoreApplication.translate("VideoWidget", u"set", None))
        self.adjust_volume.setText(QCoreApplication.translate("VideoWidget", u"audio", None))
        self.max_screen.setText(QCoreApplication.translate("VideoWidget", u"max", None))
        self.open_file.setText(QCoreApplication.translate("VideoWidget", u"open", None))
    # retranslateUi

