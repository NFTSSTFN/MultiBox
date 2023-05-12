

from PySide2.QtWidgets import QWidget,QDesktopWidget
from PySide2 import QtCore,QtGui
from PySide2.QtCore import Qt
from PySide2.QtGui import QCursor
from ui.ui_video import Ui_Video

class Video(Ui_Video,QWidget):
    def __init__(self):
        super(Video, self).__init__()
        self.setupUi(self)
        self.center()

    def center(self):
        '''窗体居中显示'''
        size = self.frameGeometry()
        screen = QDesktopWidget().availableGeometry().center()
        size.moveCenter(screen)
        self.move(size.topLeft())
