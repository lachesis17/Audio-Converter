# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(600, 150)
        self.actionGet_FFmpeg_codecs = QAction(MainWindow)
        self.actionGet_FFmpeg_codecs.setObjectName(u"actionGet_FFmpeg_codecs")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.convert_but = QPushButton(self.centralwidget)
        self.convert_but.setObjectName(u"convert_but")
        self.convert_but.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.convert_but, 1, 0, 1, 1)

        self.open_but = QPushButton(self.centralwidget)
        self.open_but.setObjectName(u"open_but")
        self.open_but.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.open_but, 0, 0, 1, 1)

        self.format_combo = QComboBox(self.centralwidget)
        self.format_combo.addItem("")
        self.format_combo.addItem("")
        self.format_combo.addItem("")
        self.format_combo.addItem("")
        self.format_combo.setObjectName(u"format_combo")
        self.format_combo.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.format_combo, 1, 1, 1, 1)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.comboBox, 1, 2, 1, 1)

        self.path_line_edit = QLineEdit(self.centralwidget)
        self.path_line_edit.setObjectName(u"path_line_edit")
        self.path_line_edit.setMinimumSize(QSize(0, 25))

        self.gridLayout.addWidget(self.path_line_edit, 0, 1, 1, 2)

        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout.setColumnStretch(2, 2)

        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 600, 22))
        self.menuMenu = QMenu(self.menubar)
        self.menuMenu.setObjectName(u"menuMenu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMenu.menuAction())
        self.menuMenu.addAction(self.actionGet_FFmpeg_codecs)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Audio Converter", None))
        self.actionGet_FFmpeg_codecs.setText(QCoreApplication.translate("MainWindow", u"Get FFmpeg codecs", None))
        self.convert_but.setText(QCoreApplication.translate("MainWindow", u"Convert", None))
        self.open_but.setText(QCoreApplication.translate("MainWindow", u"Open File...", None))
        self.format_combo.setItemText(0, QCoreApplication.translate("MainWindow", u"MP3", None))
        self.format_combo.setItemText(1, QCoreApplication.translate("MainWindow", u"WAV", None))
        self.format_combo.setItemText(2, QCoreApplication.translate("MainWindow", u"FLAC", None))
        self.format_combo.setItemText(3, QCoreApplication.translate("MainWindow", u"M4A", None))

        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"320kb/s", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"256kb/s", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"128kb/s", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"96kb/s", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"64kb/s", None))

        self.menuMenu.setTitle(QCoreApplication.translate("MainWindow", u"Menu", None))
    # retranslateUi

