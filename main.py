from PySide6 import QtWidgets, QtGui, QtCore, QtWebEngineWidgets, QtWebEngineCore
from configparser import ConfigParser
from src.config_setup import get_config, get_last_directory, update_last_directory
import ctypes
import sys
from pydub import AudioSegment

from assets.ui.main_window_ui import Ui_MainWindow

appid = 'Audio-Converter'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)

class AudioConverter(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.set_config()
        self.actionGet_FFmpeg_codecs.setIcon(QtGui.QPixmap("assets/images/icon.png"))

        self.open_but.clicked.connect(self.open_file)
        self.convert_but.clicked.connect(self.convert_file)
        self.actionGet_FFmpeg_codecs.triggered.connect(self.get_codecs)

        self.current_file = {}


    def open_file(self):
        folder_path = get_last_directory(self.config)
        file_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Select source audio file to convert', folder_path, '*.mp3;*.wav;*.flac;*.m4a;*.opus')
        if not file_path[0]:
            return
        
        update_last_directory(self.config, file_path[0])

        self.current_file = {
            'file': file_path[0],
            'ext': file_path[0].split(".", 1)[-1]
        }

        self.path_line_edit.setText(file_path[0].split("/", 1)[-1])

    def convert_file(self):
        if not self.current_file:
            return
        
        folder_path = get_last_directory(self.config)
        file_path = QtWidgets.QFileDialog.getSaveFileName(self, 'Select output for converted file', folder_path, '*.mp3;*.wav;*.flac;*.m4a;*.opus')[0]
        if not file_path:
            return
        
        update_last_directory(self.config, file_path)
        
        audio = AudioSegment.from_file(self.current_file.get('file'), format=self.current_file.get('ext'))
        audio.export(file_path, format=self.format_combo.currentText().lower())

    def get_codecs(self):
        self.browser = QtWebEngineWidgets.QWebEngineView()
        self.profile = QtWebEngineCore.QWebEngineProfile.defaultProfile()

        def download_requested(download):
            folder_path = get_last_directory(self.config)
            download_dir = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Download Directory', folder_path)
            if download_dir:
                update_last_directory(self.config, download_dir)
                full_path = QtCore.QDir(download_dir).filePath(download.downloadFileName())
                download.setDownloadFileName(full_path)
                download.accept()
            else:
                download.cancel()

        self.profile.downloadRequested.connect(download_requested)
        self.browser.setUrl(QtCore.QUrl("https://blog.gregzaal.com/how-to-install-ffmpeg-on-windows/"))
        self.browser.resize(1200, 800) 
        self.browser.show()

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