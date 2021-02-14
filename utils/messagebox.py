# This Python file uses the following encoding: utf-8
from PyQt5.QtWidgets import *

class MessageBox(QMessageBox):
    def __init__(self, parent=None):
        QMessageBox.__init__(self, parent)

    def show(self, icon, title, text):
        self.setIcon(icon)
        self.setWindowTitle(title)
        self.setText(text)
        self.setStandardButtons(QMessageBox.Ok)
        self.exec_()
