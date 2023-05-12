

from PySide2.QtWidgets import QWidget,QDesktopWidget,QMainWindow
from PySide2 import QtCore,QtGui
from ui.ui_simplifiedwindow import Ui_SimplifiedWindow
from control.video import Video
from control.mainwindow import MainWindow


class SimplifiedWindow(QMainWindow,Ui_SimplifiedWindow):
    def __init__(self):
        super(SimplifiedWindow, self).__init__()
        self.setupUi(self)
        self.show()
        self.center()


        self.drawing_style()    # 样式函数

        self.screen_recording.clicked.connect(self.screen_recording_excute)     # 屏幕录制
        self.main_window.clicked.connect(self.main_window_excute)       # 打开主窗口


    def center(self):
        '''窗体居中显示'''
        size = self.frameGeometry()
        screen = QDesktopWidget().availableGeometry().center()
        size.moveCenter(screen)
        self.move(size.topLeft())


    def drawing_style(self):
        '''界面ui绘制'''

        # 去掉菜单栏栏
        # self.current_window.setWindowFlags(QtCore.Qt.FramelessWindowHint)

        self.setStyleSheet('''
                
        ''')


    def screen_recording_excute(self):
        '''打开屏幕录制窗口'''
        self.Video = Video()
        self.stackedWidget.addWidget(self.Video)
        self.stackedWidget.setCurrentWidget(self.Video)
        self.dockWidget.show()

    def main_window_excute(self):
        self.MainWindow = MainWindow()

