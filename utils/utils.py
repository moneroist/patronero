# This Python file uses the following encoding: utf-8
from PyQt5.QtWidgets import *
from re import search as reSearch

class MessageBox(QMessageBox):
    def __init__(self, parent=None):
        QMessageBox.__init__(self, parent)

    def show(self, icon, title, text, buttons):
        self.setIcon(icon)
        self.setWindowTitle(title)
        self.setText(text)
        self.setStandardButtons(buttons)
        self.exec_()

class Utils:
    @staticmethod
    def isUrlValid(url):
        return reSearch(r"^(?:https?:\/\/)?(?:www\.)?[a-zA-Z0-9./]+$", url)

    @staticmethod
    def isOpenAliasMonero(txtRecord):
        return reSearch(r"^oa1:xmr", txtRecord)

    @staticmethod
    def unpackOpenAliasRecord(txtRecord):
        entries = txtRecord.replace(r"oa1:xmr ", '').replace('"', '').split(";")
        filtered = map(lambda x: x.split("="), list(filter(lambda e: reSearch(r"=", e), entries)))
        return filtered
