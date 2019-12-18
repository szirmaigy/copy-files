#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, os
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QFileDialog, QLabel, QLineEdit, QTextEdit, QGridLayout, QComboBox, QInputDialog
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import copy

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

        self.textbox = QLineEdit(self)
        self.textbox.move(50, 83)
        self.textbox.resize(30,20)

        self.timelabel = QLabel()
        self.timelabel.move(30,83)
        self.timelabel.clicked.connect(self.getDouble)


        #
        # combo = QComboBox(self)
        # combo.addItem("1")
        # combo.addItem("2")
        # combo.addItem("3")
        # combo.addItem("4")
        # combo.addItem("5")
        #
        # combo.move(50, 50)

        #
        # combo.activated[str].connect(self.onPath)

        # Copy button
        qbtn = QPushButton('Start copy', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(20, 120)

        self.setGeometry(200, 200, 500, 200)
        self.setWindowTitle('Copy files')
        self.show()

    @pyqtSlot()
    # def open_dir (self):
    #     self.dir_name = QFileDialog.getExistingDirectory(self, 'Select Directory')
    #     if self.dir_name:
    #         self.btn_file.setText(self.dir_name)
    #         self.lbl.setText(dir_name)
    #         self.lbl.adjustSize()

    def SelectSourceDirectory(self):
        self.statusbar = 'Select Dir'
        self.directory = QFileDialog.getExistingDirectory(self, 'Choose Directory', os.path.expanduser('~'))
        # self.directory = self.sourcedir
        self.labelsource.setText(self.directory)
        self.labelsource.adjustSize()
        # self.directory = sourcedir

    def SelectTargetDirectory(self):
        self.statusbar = 'Select Dir'
        self.directory = QFileDialog.getExistingDirectory(self, 'Choose Directory', os.path.expanduser('~'))
        # self.directory = self.targetdir
        self.labeltarget.setText(self.directory)
        self.labeltarget.adjustSize()
        # self.directory = targetdir

    def getTimer(self):
        i, okPressed = QInputDialog.getInt(self, "Get time","Percentage:", 28, 0, 100, 1)
        if okPressed:
            print(i)

    def getDouble(self):
       d,okPressed=QInputDialog.getDouble(self,'Get double','Value',9,0.5,100,9.5)
       if okPressed:
               print(d)

    # def onPath(self, path):
    #
    #     self.lbl.setText(path)
    #     self.lbl.adjustSize()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
