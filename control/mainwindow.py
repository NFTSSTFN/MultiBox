
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

        self.VideoRecording = None
        self.CodeExport = None
        self.Player = None

        self.draw_style()   # 样式函数

        self.screen_recording.clicked.connect(lambda: self.window_change('screen_recording'))   # 屏幕录制
        self.code_export.clicked.connect(lambda: self.window_change('code_export'))             # 代码导出
        self.player.clicked.connect(lambda: self.window_change('player'))                       # 播放器

    def draw_style(self):
        '''界面ui绘制'''
        pass

    def window_change(self,status):
        '''子窗体切换'''
        if self.Player:
            print(self.Player.player.position())
            self.Player.player.pause()
        if status == 'screen_recording':
            if self.VideoRecording == None:
                self.VideoRecording = VideoRecording()  # 录屏窗体
                self.stackedWidget.addWidget(self.VideoRecording)
                self.stackedWidget.setCurrentWidget(self.VideoRecording)
            else:
                self.stackedWidget.setCurrentWidget(self.VideoRecording)
        elif status == 'code_export':
            if self.CodeExport == None:   # 代码导出窗体
                self.CodeExport = CodeExport()
                self.stackedWidget.addWidget(self.CodeExport)
                self.stackedWidget.setCurrentWidget(self.CodeExport)
            else:
                self.stackedWidget.setCurrentWidget(self.CodeExport)
        elif status == 'player':
            if self.Player == None:
                self.Player = VideoPlayer()
                self.stackedWidget.addWidget(self.Player)
                self.stackedWidget.setCurrentWidget(self.Player)
            else:
                self.stackedWidget.setCurrentWidget(self.Player)
                self.Player.player.play()

    def closeEvent(self, event):
        '''窗体关闭事件'''
        self.Main_Signal.emit('Main Window Close')
        if self.Player:             # 如果视频播放开启，关闭播放
            with open('temp/video_player.txt','r',encoding='utf8') as f:
                content = f.readlines()
                video_progress = content[2].split(',')
                video_progress[self.Player.video_dir.currentIndex().row()] = self.Player.player.position()
                content[2] = ','.join(str(i) for i in video_progress)
                f.close()
            with open('temp/video_player.txt', 'w', encoding='utf8') as f:
                f.writelines(content)
                f.close()

            self.Player.player.stop()