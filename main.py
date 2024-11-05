from PySide6 import QtWidgets, QtGui, QtCore
from configparser import ConfigParser
from src.config_setup import get_config, get_last_directory, update_last_directory
import ctypes
import sys

from assets.ui.main_window_ui import Ui_MainWindow

appid = 'Audio-Converter'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

class AudioConverter(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_config()

        self.open_but.clicked.connect(self.open_file)
        self.convert_but.clicked.connect(self.convert_file)


    def open_file(self):
        pass

    def convert_file(self):
        pass

    def set_config(self, config: ConfigParser = None) -> None:
        if config is None:
            self.config = get_config()
        else:
            self.config = config

            
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)

if __name__ == "__main__":
    sys.excepthook = except_hook
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QPixmap("assets/images/icon.png"))
    window = AudioConverter()
    window.show()
    sys.exit(app.exec())