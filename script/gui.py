from PySide6.QtWidgets import QMainWindow

from gui_lib import Ui_Form


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)