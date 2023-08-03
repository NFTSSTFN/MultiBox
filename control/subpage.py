

from PySide2 import QtCore,QtGui,QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtMultimediaWidgets import QVideoWidget
from PySide2.QtMultimedia import QMediaPlayer,QMediaContent

import keyboard as kb
import threading
import time
import glob
import re

from utils.code_export import *

from ui.ui_video_recording import Ui_VideoRecording
from ui.ui_codeexport import Ui_CodeExport
from ui.ui_video_player import Ui_VideoWidget

class VideoRecording(Ui_VideoRecording,QWidget):
    '''录屏页面'''
    def __init__(self):
        super(VideoRecording, self).__init__()
        self.setupUi(self)
        self.center()

    def center(self):
        '''窗体居中显示'''
        size = self.frameGeometry()
        screen = QDesktopWidget().availableGeometry().center()
        size.moveCenter(screen)
        self.move(size.topLeft())


class CodeExport(Ui_CodeExport,QWidget):
    '''代码导出页面'''
    def __init__(self):
        super(CodeExport, self).__init__()
        self.setupUi(self)
        self.center()

        self.blacklist = ['.idea', '__pycache__', '.git']    # 黑名单
        self.dirs_number = None     # 目录数量
        self.codes_number = None    # 代码数量
        self.files_number = None    # py文件数量

        self.import_folder.clicked.connect(self.file_processing)    # 导入数据按钮
        self.export_single_file.clicked.connect(self.export_single) # 导出单文件按钮
        self.export_many_file.clicked.connect(self.export_many)     # 导出多文件按钮
        self.dir_tree.clicked.connect(lambda: self.tree_clicked(self.dir, self.dir_tree.currentIndex().data()))     # 目录被点击事件

    def center(self):
        '''窗体居中显示'''
        size = self.frameGeometry()
        screen = QDesktopWidget().availableGeometry().center()
        size.moveCenter(screen)
        self.move(size.topLeft())

    def file_processing(self):
        '''导入文件后，处理数据'''
        self.dirs_number = 0
        self.path = QFileDialog.getExistingDirectory(self,'选择文件夹')      # 获取文件夹路径
        self.status_box.append('文件已选择：%s' % self.path)

        if self.selection.currentText() == 'Python':
            # 启动文件解析子线程，并拿到字典树
            self.status_box.append('数据处理中······')
            self.child_thread = RecvValue(target=dir_process,args=(self.path, self.blacklist))
            self.child_thread.start()
            self.child_thread.join()
            self.dir = self.child_thread.get_return()  # 字典树，里面储存着各级目录与代码处理后的内容


        model = QStandardItemModel(self.dir_tree)                   # 建立目录模型
        model.setHorizontalHeaderItem(0,QStandardItem(self.path))   # 设置目录标题名称
        self.add_dir(model, self.dir)           # 执行tree与目录转换函数
        self.dir_tree.setModel(model)           # 设置模型至QTreeView窗体中
        self.status_box.append('Finished！！！！！！！！！！！！！\n共计: %s 个目录' % self.dirs_number)

    def add_dir(self, model, dic):
        '''将字典树转换为treeview目录结构'''
        for key, value in dic.items():
            if value and type(value) != list:
                self.dirs_number += 1
                new_parent = QStandardItem(key)
                model.appendRow(new_parent)
                self.add_dir(new_parent, value)
            else:
                new_child = QStandardItem(key)
                model.appendRow(new_child)


    def export_many(self):
        '''绑定导出单文件'''
        self.codes_number = 0
        self.files_number = 0
        self.save_path = QFileDialog.getExistingDirectory(self, '选择文件夹')    # 保存文件路径
        self.many_analysis(self.save_path + '/' + self.path.split('/')[-1], self.dir)
        self.status_box.append('导出完成！！！！！！！！！！！！！\n共计: %s 个目录\n共计: %s 个py文件\n共计: %s 行代码'
                               % (self.dirs_number, self.files_number, self.codes_number))

    def many_analysis(self, real_path, dic):
        '''处理保留目录的代码导出'''
        for key, value in dic.items():
            if '.py' in key and type(value) == list:
                self.files_number += 1
                if not os.path.exists(real_path):
                    os.makedirs(real_path)
                with open(real_path + '/' + key, 'w', encoding='utf8') as f:
                    for i in value:
                        f.write(i)
                        self.codes_number += 1
            else:
                if not os.path.exists(real_path + '/' + key):
                    os.makedirs(real_path + '/' + key)
                self.many_analysis(real_path + '/' + key, value)

    def export_single(self):
        '''绑定导出多文件'''
        self.codes_number = 0
        self.files_number = 0
        if os.path.exists('C:/Users/Administrator/Desktop/soft.py'):
            with open('C:/Users/Administrator/Desktop/soft.py', 'w', encoding='utf8') as f:
                f.write('')
        self.single_analysis(self.dir)
        self.status_box.append('导出完成，文件在桌面！！！！！！！！！！！！！\n共计: %s 个目录\n共计: %s 个py文件\n共计: %s 行代码'
                               % (self.dirs_number, self.files_number, self.codes_number))

    def single_analysis(self, dic):
        '''处理软著形式的代码导出'''
        for key, value in dic.items():
            if '.py' in key and type(value) == list:
                self.files_number += 1
                with open('C:/Users/Administrator/Desktop/soft.py', 'a', encoding='utf8') as f:
                    for i in value:
                        f.write(i)
                        self.codes_number += 1

            else:
                self.single_analysis(value)

    def tree_clicked(self, dic, key):
        if isinstance(dic, dict):
            for k,v in dic.items():
                if key == k:
                    self.content.clear()
                    for i in v:
                        self.content.append(i.replace('\n',''))
                    self.content.setFocus()                     # 让TextEdit获取焦点
                    textCursor = self.content.textCursor()      # 获取光标
                    textCursor.movePosition(QTextCursor.Start)  # 将光标移动到文本开始处
                    self.content.setTextCursor(textCursor)      # 将光标设置到TextEdit中
                    raise
                self.tree_clicked(v, key)


class VideoPlayer(QWidget,Ui_VideoWidget):
    '''视频播放器'''
    def __init__(self):
        super(VideoPlayer, self).__init__()
        self.setupUi(self)
        self.center()
        self.init_play()  # 初始化播放界面信息

        self.open_file.clicked.connect(self.open)                           # 打开视频文件
        self.start_pause.clicked.connect(self.start_or_pause)               # 视频开始/暂停
        self.player.positionChanged.connect(self.poschange)                 # 刷新进度条/时间戳
        self.progress_bar.sliderMoved.connect(self.on_slider_moved)         # 释放进度条
        self.video_widget.signal_double_clicked.connect(self.screen_size)   # 视频窗口最大化/正常化
        self.video_dir.clicked.connect(self.dir_change)                     # 目录被点击

    def center(self):
        '''窗体居中显示'''
        size = self.frameGeometry()
        screen = QDesktopWidget().availableGeometry().center()
        size.moveCenter(screen)
        self.move(size.topLeft())

    def init_play(self):
        '''初始化播放界面信息'''
        # 添加自定义的视频播放窗口
        self.video_widget = MyVideoWidget(self)
        self.verticalLayout_2.insertWidget(0,self.video_widget)

        # 添加自定义的播放进度条
        self.progress_bar = CustomSlider(Qt.Horizontal, self)       # 获取进度条
        self.verticalLayout_2.insertWidget(1, self.progress_bar)    # 添加进度条
        self.progress_bar.setSingleStep(1)              # 设置进度条步长
        self.progress_bar.setMaximum(0)                 # 设置进度条初始长度

        # 添加视频解析模块
        self.player = QMediaPlayer()                    # 设置视频组件
        self.player.setVideoOutput(self.video_widget)   # 设置播放窗口

        # 设置初始变量值
        self.video_status = None                        # 视频播放状态
        self.video_screen_status = False                # 屏幕大小状态
        self.old_dir_index = None                       # 上次播放视频

        # 读取配置文件,设置视频目录
        with open('temp/video_player.txt','r',encoding='utf8') as f:
            self.default = f.readlines()     # 储存配置文件信息,0-所有文件，1-文件所在目录，2-播放进度
            f.close()
        if self.default:
            self.video_dir_data = list(self.default[0].strip()[0:-1].split(','))   # 储存当前文件下所有视频
            self.video_dir.setRowCount(len(self.video_dir_data))
            self.video_dir.setColumnCount(1)
            for i in range(len(self.video_dir_data)):
                self.video_dir.setItem(i,0,QTableWidgetItem(self.video_dir_data[i].split('\\')[-1].split('.')[0]+'.mp4'))
        self.video_dir.horizontalHeader().setVisible(False)     # 表头横向不可见
        self.video_dir.verticalHeader().setVisible(False)       # 表头纵向不可见
        self.video_dir.horizontalHeader().setStretchLastSection(True)   # 表格宽度占满
        self.video_dir.setEditTriggers(QTableWidget.NoEditTriggers)     # 表格不可被编辑
        self.video_dir.selectRow(0)
        for i in range(len(self.default[2].split(','))):
            if self.default[2].split(',')[i].strip() != '0':
                self.video_dir.selectRow(i)
                self.old_dir_index = i
        # 断点续播
        self.player.setMedia(QMediaContent(self.default[1].strip() + '/' + self.video_dir.currentIndex().data()))
        self.player.setPosition(int(self.default[2].split(',')[self.video_dir.currentIndex().row()]))
        self.player.play()
        self.video_status = True
        self.old_dir_index = self.video_dir.currentIndex().row()

        # 添加action，用于快进与快退
        self.action_right = QAction('Change message', self.video_widget)
        self.action_right.setShortcut(QKeySequence(Qt.Key_Right))
        self.addAction(self.action_right)
        self.action_right.triggered.connect(lambda: self.change_message('right'))

        self.action_left = QAction('Change message', self.video_widget)
        self.action_left.setShortcut(QKeySequence(Qt.Key_Left))
        self.addAction(self.action_left)
        self.action_left.triggered.connect(lambda: self.change_message('left'))

        self.action_up = QAction('Change message', self.video_widget)
        self.action_up.setShortcut(QKeySequence(Qt.Key_Up))
        self.addAction(self.action_up)
        self.action_up.triggered.connect(lambda: self.change_message('up'))

        self.action_down = QAction('Change message', self.video_widget)
        self.action_down.setShortcut(QKeySequence(Qt.Key_Down))
        self.addAction(self.action_down)
        self.action_down.triggered.connect(lambda: self.change_message('down'))

        self.action_esc = QAction('Change message', self.video_widget)
        self.action_esc.setShortcut(QKeySequence('Esc'))
        self.addAction(self.action_esc)
        self.action_esc.triggered.connect(lambda: self.change_message('esc'))

        self.action_next = QAction('Change message', self.video_widget)
        self.action_next.setShortcut(QKeySequence(Qt.ControlModifier + Qt.Key_Right))
        self.addAction(self.action_next)
        self.action_next.triggered.connect(lambda: self.change_message('next'))

        self.action_last = QAction('Change message', self.video_widget)
        self.action_last.setShortcut(QKeySequence(Qt.ControlModifier + Qt.Key_Left))
        self.addAction(self.action_last)
        self.action_last.triggered.connect(lambda: self.change_message('last'))

    def open(self):
        '''播放视频'''
        current_file = QFileDialog.getOpenFileUrl()[0]
        self.player.setMedia(QMediaContent(current_file))    # 设置视频

        self.video_dir_data = sorted(glob.glob('/'.join(str(current_file).split('/')[3:-1])+'/*.mp4'),
               key=lambda s: [(s, int(n)) for s, n in re.findall('(\D+)(\d+)', 'a%s0' % s)], reverse=True)    # 获取所有的路径并排序
        with open('temp/video_player.txt', 'w', encoding='utf8') as f:
            f.write(','.join(self.video_dir_data) + '\n')           # 储存播放文件
            f.write(self.video_dir_data[0].split('\\')[0] + '\n')   # 储存播放文件所在目录
            f.write(','.join('0'*len(self.video_dir_data)))         # 储存播放进度
            f.close()
        self.video_dir.clear()
        self.video_dir.setRowCount(len(self.video_dir_data))
        self.video_dir.setColumnCount(1)
        for i in range(len(self.video_dir_data)):  # 储存当前文件下所有视频
            self.video_dir.setItem(i, 0, QTableWidgetItem(self.video_dir_data[i].split('\\')[-1].split('.')[0]+'.mp4'))
            if self.video_dir.item(i,0).text() == str(current_file).split("/")[-1][0:-2]:      # 判断当前播放视频，并选中
                self.video_dir.selectRow(i)
                self.old_dir_index = i


        self.player.play()              # 播放视频
        self.video_status = True        # 更改视频状态

    def start_or_pause(self):
        '''暂停或继续播放'''
        if self.video_status:
            self.player.pause()
            self.video_status = False
        else:
            self.player.play()
            self.video_status = True

    def poschange(self):
        '''根据当前播放进度刷新进度条、时间戳'''
        video_total_time = self.player.duration()                 # 获取视频时间
        seconds_total = int((video_total_time / 1000) % 60)
        minutes_total = int((video_total_time / (1000 * 60)) % 60)
        hours_total = int(video_total_time / (1000 * 60 * 60))
        time_str_total = "{:02d}:{:02d}:{:02d}".format(hours_total, minutes_total, seconds_total)
        video_current_time = self.player.position()
        seconds_current = int((video_current_time / 1000) % 60)
        minutes_current = int((video_current_time / (1000 * 60)) % 60)
        hours_current = int(video_current_time / (1000 * 60 * 60))
        time_str_current = "{:02d}:{:02d}:{:02d}".format(hours_current, minutes_current, seconds_current)
        self.time__stamp.setText(time_str_current + '/' + time_str_total)    # 设置时间戳

        self.progress_bar.setMaximum(video_total_time)          # 设置进度条最大时间
        self.progress_bar.setValue(int(video_current_time))     # 设置进度条当前播放时间

        # 如果当前视频播放完成，将当前视频进度重置为0，并播放下一条
        if video_total_time == int(video_current_time) and video_total_time != 0:
            with open('temp/video_player.txt', 'w', encoding='utf8') as f:
                video_progress = self.default[2].split(',')
                video_progress[self.old_dir_index] = 0
                self.default[2] = ','.join(str(i) for i in video_progress)
                f.writelines(self.default)
                f.close()
            self.player.stop()

            # 播放当前选中视频的下一个
            if self.video_dir.currentIndex().row()+1 != self.video_dir.rowCount():  # 如果下一个视频存在
                self.player.setMedia(QMediaContent(self.default[1].strip() + '/' + self.video_dir.item(self.video_dir.currentIndex().row()+1,0).text()))
                self.video_dir.selectRow(self.video_dir.currentIndex().row() + 1)
                self.old_dir_index = self.video_dir.currentIndex().row()
                self.player.setPosition(int(self.default[2].strip().split(',')[self.video_dir.currentIndex().row()]))
                self.player.play()

    def on_slider_moved(self,value):
        '''接收重写的QSlider类传来的emit，并刷新视频进度'''
        self.player.setPosition(self.progress_bar.value())      # 重设视频进度
        self.player.play()              # 播放视频
        self.video_status = True        # 更改视频状态

    def screen_size(self,val):
        '''播放屏幕大小控制'''
        if val == 'max':
            self.video_widget.setFullScreen(1)
            self.video_screen_status = True
        else:
            if self.video_screen_status:
                self.video_widget.setFullScreen(0)
                self.verticalLayout_2.insertWidget(0, self.video_widget)
                self.video_screen_status = False
            else:
                self.video_widget.setFullScreen(1)
                self.video_screen_status = True

    def dir_change(self):
        '''视频目录被点击后执行此函数'''
        # 储存被切换视频的播放进度
        with open('temp/video_player.txt','w',encoding='utf8') as f:
            video_progress = self.default[2].strip().split(',')
            video_progress[self.old_dir_index] = self.player.position()
            self.default[2] = ','.join(str(i) for i in video_progress)
            f.writelines(self.default)
            f.close()
        self.old_dir_index = self.video_dir.currentIndex().row()
        self.player.stop()

        # 播放当前选中视频
        self.player.setMedia(QMediaContent(self.default[1].strip() + '/' +  self.video_dir.currentIndex().data()))
        self.player.setPosition(int(self.default[2].split(',')[self.video_dir.currentIndex().row()]))
        self.player.play()

    def change_message(self,val):
        '''添加键盘热键'''
        if val == 'left':
            print('left')
        elif val == 'right':
            print('right')
        elif val == 'up':
            print('up')
        elif val == 'down':
            print('down')
        elif val == 'next':
            print('next')
        elif val == 'last':
            print('last')
        elif val == 'esc':
            print('esc')


class CustomSlider(QSlider):
    '''重写的QSlider类，用于视频播放器'''
    def mousePressEvent(self, event):
        pos = event.pos()
        width = self.width()
        value = self.maximum() * pos.x() / width
        self.setSliderPosition(int(value))      # 设置进度条进度
        self.sliderMoved.emit(int(value))       # 发送鼠标移动信号


class MyVideoWidget(QVideoWidget):
    '''重写的videowidget类'''
    signal_double_clicked = Signal(str)
    def mouseDoubleClickEvent(self, event):
        self.signal_double_clicked.emit('double_clicked')

