#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os,  shutil, time
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QFileDialog, QLabel, QLineEdit, QTextEdit, QGridLayout, QComboBox, QInputDialog, QGridLayout, QVBoxLayout, QSpinBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
# import copy

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.left=10
        self.top=10
        self.width=400
        self.height=140
        self.initUI()

    def initUI(self):

        # Source button
        self.button = QPushButton('Source folder', self)
        self.button.move(20,20)
        self.button.clicked.connect(self.SelectSourceDirectory)

        self.labelsource = QLabel(self)
        self.labelsource.move(150, 23)

        # Target button
        self.button = QPushButton('Target folder', self)
        self.button.move(20,50)
        self.button.clicked.connect(self.SelectTargetDirectory)

        self.labeltarget = QLabel(self)
        self.labeltarget.move(150, 53)

        # Time set
        self.label = QLabel('Sec', self)
        self.label.move(20,83)

        self.timelabel = QSpinBox(self)
        self.timelabel.move(50, 83)
        self.timelabel.resize(40,20)

        # Copy button
        self.button = QPushButton('Copy', self)
        self.button.move(20,120)
        self.button.clicked.connect(self.CopyAllFiles)

        # Mian window paramater
        self.setGeometry(200, 200, 500, 200)
        self.setWindowTitle('Copy files')
        self.show()

    @pyqtSlot()
    def SelectSourceDirectory(self):
        self.statusbar = 'Select Dir'
        self.directory = QFileDialog.getExistingDirectory(self, 'Choose Source Directory', os.path.expanduser('~'))
        self.sourcedir = self.directory
        self.labelsource.setText(self.directory)
        self.labelsource.adjustSize()

    def SelectTargetDirectory(self):
        self.statusbar = 'Select Dir'
        self.directory = QFileDialog.getExistingDirectory(self, 'Choose Target Directory', os.path.expanduser('~'))
        self.targetdir = self.directory
        self.labeltarget.setText(self.directory)
        self.labeltarget.adjustSize()

    def CopyAllFiles(self):
        self.timer = self.timelabel.value()
        src_files = os.listdir(self.sourcedir)
        for file_name in src_files:
            full_file_name = os.path.join(self.sourcedir, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, self.targetdir)
                time.sleep(self.timer)
                # ki kell iratni az átmásolt file-okat és hogy hány darab van még hátra


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
