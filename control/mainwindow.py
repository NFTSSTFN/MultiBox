
from PySide2 import QtCore,QtGui,QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtGui import *

from ui.ui_mainwindow import Ui_MainWindow

from control.subpage import *


class MainWindow(QMainWindow,Ui_MainWindow):
    Main_Signal = Signal(str)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.show()

        self.Video = None
        self.CodeExport = None

        self.draw_style()   # 样式函数

        self.screen_recording.clicked.connect(lambda: self.window_change('screen_recording'))
        self.code_export.clicked.connect(lambda: self.window_change('code_export'))

    def draw_style(self):
        '''界面ui绘制'''
        pass

    def window_change(self,status):
        '''子窗体切换'''
        if status == 'screen_recording':
            if self.Video == None:
                self.Video = Video()  # 录屏窗体
                self.stackedWidget.addWidget(self.Video)
                self.stackedWidget.setCurrentWidget(self.Video)
                print(self.Video)
            else:
                print(self.Video)
                self.stackedWidget.setCurrentWidget(self.Video)
        elif status == 'code_export':
            if self.CodeExport == None:   # 代码导出窗体
                self.CodeExport = CodeExport()
                self.stackedWidget.addWidget(self.CodeExport)
                self.stackedWidget.setCurrentWidget(self.CodeExport)
            else:
                self.stackedWidget.setCurrentWidget(self.CodeExport)

    def closeEvent(self, event):
        '''窗体关闭事件'''
        self.Main_Signal.emit('Main Window Close')