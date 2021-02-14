# This Python file uses the following encoding: utf-8
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from tabs.miningpoolstabui import Ui_MiningPoolsTab
from utils.utils import Utils
import uuid

class MiningPoolsTab(QWidget):
    miningPoolCreated = pyqtSignal(dict)
    miningPoolRemoved = pyqtSignal(str)
    openMessageBox = pyqtSignal(int, str, str)

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.ui = Ui_MiningPoolsTab()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnHidden(0, True)
        self.ui.addButton.clicked.connect(self.addButtonClicked)
        self.ui.removeButton.clicked.connect(self.removeButtonClicked)

    def setupData(self, data):
        for miningPool in data['miningPools']:
            self.addMiningPoolToTable(miningPool)

    def setMiningPoolFormValues(self, name="", url=""):
        self.ui.nameLineEdit.setText(name)
        self.ui.urlLineEdit.setText(url)

    def addButtonClicked(self):
        name = self.ui.nameLineEdit.text()
        url = self.ui.urlLineEdit.text()

        if not name:
            self.openMessageBox.emit(QMessageBox.Warning, "Warning", "Name can not be empty!")
            return
        if not url:
            self.openMessageBox.emit(QMessageBox.Warning, "Warning", "URL can not be empty!")
            return
        if not Utils.isMiningPoolUrlValid(url):
            self.openMessageBox.emit(QMessageBox.Warning, "Warning", "Mining pool URL is not valid!")
            return

        self.addMiningPool(name, url)

    def addMiningPool(self, name, url):
        id = str(uuid.uuid4())
        miningPool = { "id": id, "name": name, "url": url }
        self.addMiningPoolToTable(miningPool)
        self.setMiningPoolFormValues()
        self.miningPoolCreated.emit(miningPool)

    def addMiningPoolToTable(self, miningPool):
        index = self.ui.tableWidget.rowCount()

        self.ui.tableWidget.insertRow(index)
        self.ui.tableWidget.setItem(index, 0, QTableWidgetItem(miningPool['id']))
        self.ui.tableWidget.setItem(index, 1, QTableWidgetItem(miningPool['name']))
        self.ui.tableWidget.setItem(index, 2, QTableWidgetItem(miningPool['url']))

    def removeButtonClicked(self):
        tableCurrentRow = self.ui.tableWidget.currentRow()
        if tableCurrentRow >= 0:
            miningPoolId = self.ui.tableWidget.takeItem(tableCurrentRow, 0).text()
            self.ui.tableWidget.removeRow(tableCurrentRow)
            self.miningPoolRemoved.emit(miningPoolId)
