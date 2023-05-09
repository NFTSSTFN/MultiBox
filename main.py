
from PySide2.QtWidgets import QApplication
import threading

from control.login import Login
from control.simplifiedwindow import SimplifiedWindow


class Main:
    def __init__(self):
        Login.signal.connect(self.start)

    def start(self,aaa):
        print(aaa)
        self.SimplifiedWindow = SimplifiedWindow()
        Login.close()

if __name__ == '__main__':
    app = QApplication([])
    Login = Login()
    Main = Main()
    app.exec_()
