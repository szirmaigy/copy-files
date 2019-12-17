#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QFileDialog, QLabel, QLineEdit, QTextEdit, QGridLayout
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

        # Target button
        self.button = QPushButton('Source folder', self)
        self.button.move(20,20)
        self.button.clicked.connect(self.open_dir)
        # lbl3 = QLabel('test', self)
        # lbl3.move(150, 23)
        # self.button1 = QtGui.QFileDialog.getExistingDirectory(self, 'Select directory')
        # self.button1.move(150, 23)

        # Target button
        self.button = QPushButton('Target folder', self)
        self.button.move(20,50)
        self.button.clicked.connect(self.open_dir)

        # Time set
        self.label = QLabel('Sec', self)
        self.label.move(20,83)

        self.textbox = QLineEdit(self)
        self.textbox.move(50, 83)
        self.textbox.resize(30,20)

        # Copy button
        qbtn = QPushButton('Start copy', self)
        qbtn.clicked.connect(QApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(20, 120)

        self.setGeometry(300, 300, 250, 170)
        self.setWindowTitle('Copy files')
        self.show()

    @pyqtSlot()
    def open_dir (self):
        self.dir_name = QFileDialog.getExistingDirectory(self, 'Select Directory')
        if self.dir_name:
            self.btn_file.setText(self.dir_name)

    def getTimer(self):
        i, okPressed = QInputDialog.getInt(self, "Get time","Percentage:", 28, 0, 100, 1)
        if okPressed:
            print(i)


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
