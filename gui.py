#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os,  shutil, time
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QFileDialog, QLabel, QLineEdit, QTextEdit, QGridLayout, QComboBox, QInputDialog, QGridLayout, QVBoxLayout, QSpinBox, QListWidget, QSplitter
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtCore import pyqtSlot, Qt
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
        self.button.clicked.connect(self.SourceDirFilesNumber)

        self.labelsource = QLabel(self)
        self.labelsource.move(150,23)

        self.sourcelabeltitle = QLabel('Source Folder files:', self)
        self.sourcelabeltitle.move(20,180)
        self.sourcefilesnumberlabel = QLabel(self)
        self.sourcefilesnumberlabel.move(162,180)
        self.sourcefileslabel = QLabel(self)
        self.sourcefileslabel.move(20,200)
        self.sourcefileslabel.resize(100,200)

        # Target button
        self.button = QPushButton('Target folder', self)
        self.button.move(20,50)
        self.button.clicked.connect(self.SelectTargetDirectory)

        self.labeltarget = QLabel(self)
        self.labeltarget.move(150,53)

        self.targetlabeltitle = QLabel('Target Folder files:', self)
        self.targetlabeltitle.move(200,180)
        self.targetfilesnumberlabel = QLabel(self)
        self.targetfilesnumberlabel.move(335,180)
        # self.targetfileslabel = QLabel(self)
        # self.targetfileslabel.move(320, 200)
        # self.targetfileslabel.resize(380,300)

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

        self.finishlabel = QLabel(self)
        self.finishlabel.move(150,125)

        # Mian window paramater
        self.setGeometry(200, 200, 470, 250)
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
        count = 0
        for file_name in src_files:
            full_file_name = os.path.join(self.sourcedir, file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, self.targetdir)
                time.sleep(self.timer)
                count = count + 1
                self.targetfilesnumberlabel.setText(str(count))
                self.targetfilesnumberlabel.adjustSize()
                self.finishlabel.setText('Finish copy')
                self.finishlabel.adjustSize()
                self.finishlabel.setStyleSheet('color: green')

# ki kell iratni az átmásolt file-okat és hogy hány darab van még hátra
    def SourceDirFilesNumber(self):
        count = 0
        for sourcefiles in os.listdir(self.sourcedir):
            if os.path.isfile(os.path.join(self.sourcedir, sourcefiles)):
                # self.sourcefiles = sourcefiles
                count = count + 1
                # print(sourcefiles, count)
                # self.sourcefileslabel.setText(self.sourcefiles)
                # self.sourcefileslabel.adjustSize()
                self.sourcefilesnumberlabel.setText(str(count))
                self.sourcefilesnumberlabel.adjustSize()

    # def TargetDirFilesNumber(self):
    #     count = 0
    #     for targetfiles in os.listdir(self.targetdir):
    #         if os.path.isfile(os.path.join(self.targetdir, targetfiles)):
    #             self.targetfiles = targetfiles
    #             count = count + 1
    #             self.targetfileslabel.setText(self.targetfiles)
    #             self.targetfileslabel.adjustSize()
    #             self.targetfilesnumberlabel.setText(str(count))
    #             self.targetfilesnumberlabel.adjustSize()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
