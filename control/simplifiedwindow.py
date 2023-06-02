

from PySide2.QtWidgets import QWidget,QDesktopWidget,QMainWindow
from PySide2 import QtCore,QtGui

from ui.ui_simplifiedwindow import Ui_SimplifiedWindow

from control.subpage import *
from control.mainwindow import MainWindow


class SimplifiedWindow(QMainWindow,Ui_SimplifiedWindow):
    def __init__(self):
        super(SimplifiedWindow, self).__init__()
        self.setupUi(self)
        self.show()
        self.center()

        self.MainWindow = None
        self.Video = None

        self.drawing_style()    # 样式函数



        self.screen_recording.clicked.connect(self.screen_recording_excute)     # 屏幕录制
        self.main_window.clicked.connect(lambda:self.main_window_excute(None))       # 打开主窗口


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
        if self.Video == None:
            self.Video = Video()
            self.stackedWidget.addWidget(self.Video)
            self.stackedWidget.setCurrentWidget(self.Video)
            print(self.Video)
        else:
            print(self.Video)
            self.stackedWidget.setCurrentWidget(self.Video)


    def main_window_excute(self,status):
        '''打开主窗口'''
        if status == None:
            if self.MainWindow == None:
                self.MainWindow = MainWindow()
                self.MainWindow.Main_Signal.connect(self.main_window_excute)
        else:
            self.MainWindow = None