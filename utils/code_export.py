

import os
import threading
import time


        
def dir_process(path,blacklist):
    '''处理目录，按层级保存目录信息，返回值tree为目录信息'''
    tree = {}
    if os.path.isdir(path):
        for name in os.listdir(path):
            if name not in blacklist:
                file_path = os.path.join(path,name)
                if os.path.isdir(file_path):
                    tree[name] = dir_process(file_path,blacklist)
                else:
                    if '.py' in name:
                        tree[name] = dir_process(file_path, blacklist)
    else:
        if '.py' in path:
            return clear_annotation(path)
    return tree

def clear_annotation(path):
    '''
    清除文件注释
    :param path: 文件路径
    :return: list，包含所有已清除注释的代码
    '''
    res = []
    with open(path, 'r', encoding='utf8') as f:
        data = f.readlines()
        num = 0
        while num < len(data):
            if not data[num].strip():                   # 空行
                pass
            elif data[num].lstrip()[0] == '#':          # 单行#号注释
                pass
            elif data[num].lstrip()[0:3] == '"""' and data[num].count('"""') >= 2:      # 单行"""注释
                pass
            elif data[num].lstrip()[0:3] == "'''" and data[num].count("'''") >= 2:      # 单行'''注释
                pass

            elif data[num].lstrip()[0:3] == '"""' and data[num].lstrip()[3] != ')':     # 多行'''注释
                num += 1
                while True:
                    if '"""' in data[num]:
                        break
                    else:
                        num += 1
            elif data[num].lstrip()[0:3] == "'''" and data[num].lstrip()[3] != ")":     # 多行"""注释
                num += 1
                while True:
                    if "'''" in data[num]:
                        break
                    else:
                        num += 1
            else:
                if '# ' in data[num]:
                    res.append(data[num].split('#')[0].rstrip() + '\n')
                else:
                    if num == len(data) - 1:
                        res.append(data[num] + '\n')
                    else:
                        res.append(data[num])

            num += 1
    return res

def extract_directory(self, menu, kg):
    '''能够提取tree目录中的结构，暂时没用'''
    for i in menu:
        if type(i) == str:
            if menu[i] and type(menu[i]) != list:
                print(kg + i)
                kg += '\t'
                now = menu[i]
                self.extract_directory(now,kg)
                kg = kg.replace('\t','',1)
            else:
                print(kg+i)

        

class RecvValue(threading.Thread):
    '''接收子线程的返回值，用来开始上面的几个函数，再subpage页面被调用'''
    def __init__(self, target, args=()):
        super(RecvValue, self).__init__()
        self.target = target    # 函数名
        self.args = args        # 函数参数
        self._result = None     # 函数返回值

    def run(self) -> None:
        '''启动函数线程'''
        if self.target:
            self._result = self.target(*self.args)

    def get_return(self):
        '''通过join获取返回值'''
        self.join()
        return self._result







