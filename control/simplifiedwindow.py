

from PySide2.QtWidgets import QWidget
from ui.ui_simplifiedwindow import Ui_Form


class SimplifiedWindow(QWidget,Ui_Form):
    def __init__(self):
        super(SimplifiedWindow, self).__init__()
        self.setupUi(self)
        self.show()