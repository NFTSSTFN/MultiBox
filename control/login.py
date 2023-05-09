

from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Signal
import keyboard as kb
import threading
import time
from ui.ui_login import Ui_Login



class Login(QWidget,Ui_Login):
    '''登录验证'''
    signal = Signal(int)
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.show()
        
        self.t1 = threading.Thread(target=self.listen)
        self.t1.setDaemon(True)
        self.t1.start()


    def listen(self):
        count = 0
        while True:
            event = kb.read_event()
            if event.event_type == 'up' and event.name == 'k':
                count += 1
            elif event.event_type == 'up' and event.name != 'k':
                count = 0
            if count == 5:
                self.signal.emit(123456)
                break




