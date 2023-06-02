


from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import keyboard as kb
import threading
import time

from ui.ui_video import Ui_Video
from ui.ui_codeexport import Ui_CodeExport
from utils.code_export import *


class Video(Ui_Video,QWidget):
    '''录屏页面'''
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
