# This Python file uses the following encoding: utf-8
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from tabs.protegestabui import Ui_ProtegesTab
from dns.resolver import query as dnsResolverQuery, NoAnswer
from utils.utils import Utils
from utils.validation import Validation
import uuid

class ProtegesTab(QWidget):
    protegeCreated = pyqtSignal(dict)
    protegeRemoved = pyqtSignal(str)
    openMessageBox = pyqtSignal(int, str, str)

    def __init__(self, parent):
        QWidget.__init__(self, parent)
        self.ui = Ui_ProtegesTab()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnHidden(0, True)
        self.ui.searchUrlButton.clicked.connect(self.searchUrlButtonClicked)
        self.ui.addButton.clicked.connect(self.addButtonClicked)
        self.ui.removeButton.clicked.connect(self.removeButtonClicked)

    def setupData(self, data):
        for protege in data['proteges']:
            self.addProtegeToTable(protege)

    def searchUrlButtonClicked(self):
        url = self.ui.searchUrlLineEdit.text()
        if Utils.isUrlValid(url):
            try:
                answers = dnsResolverQuery(url, "TXT")
            except NoAnswer:
                self.openMessageBox.emit(QMessageBox.Warning, "Warning", "Given URL doesn't contain TXT record!")
                return
            except:
                self.openMessageBox.emit(QMessageBox.Critical, "Error", "Upps something really goes wrong!")
                return

            for answer in answers:
                answer = str(answer).replace('"', '')
                if Utils.isOpenAliasMonero(answer):
                    protege = Utils.unpackOpenAliasRecord(answer)
                    if protege:
                        if Validation.isMoneroAddress(protege['recipient_address']):
                            self.setProtegeFormValues(protege['recipient_name'], protege['recipient_address'])
                            return
                        else:
                            self.openMessageBox.emit(QMessageBox.Warning, "Warning", "Found OpenAlias record but given Monero address is invalid!")
                            return
                    else:
                        self.openMessageBox.emit(QMessageBox.Warning, "Warning", "Given URL doesn't contain valid OpenAlias record for Monero!")
                        return

            self.openMessageBox.emit(QMessageBox.Warning, "Warning", "Given URL doesn't contain OpenAlias record for Monero!")
        else:
            self.openMessageBox.emit(QMessageBox.Warning, "Warning", "Search URL is invalid!")

    def setProtegeFormValues(self, name="", address="", searchUrl=""):
        self.ui.nameLineEdit.setText(name)
        self.ui.addressLineEdit.setText(address)
        self.ui.searchUrlLineEdit.setText(searchUrl)

    def addButtonClicked(self):
        name = self.ui.nameLineEdit.text()
        address = self.ui.addressLineEdit.text()

        if not name:
            self.openMessageBox.emit(QMessageBox.Warning, "Warning", "Name can not be empty!")
            return
        if not address:
            self.openMessageBox.emit(QMessageBox.Warning, "Warning", "Address can not be empty!")
            return
        if not Validation.isMoneroAddress(address):
            self.openMessageBox.emit(QMessageBox.Warning, "Warning", "Given Monero address is not valid!")
            return

        self.addProtege(name, address)

    def addProtege(self, name, address):
        id = str(uuid.uuid4())
        protege = { "id": id, "name": name, "address": address }
        self.addProtegeToTable(protege)
        self.setProtegeFormValues()
        self.protegeCreated.emit(protege)

    def addProtegeToTable(self, protege):
        index = self.ui.tableWidget.rowCount()

        self.ui.tableWidget.insertRow(index)
        self.ui.tableWidget.setItem(index, 0, QTableWidgetItem(protege['id']))
        self.ui.tableWidget.setItem(index, 1, QTableWidgetItem(protege['name']))
        self.ui.tableWidget.setItem(index, 2, QTableWidgetItem(protege['address']))

    def removeButtonClicked(self):
        tableCurrentRow = self.ui.tableWidget.currentRow()
        if tableCurrentRow >= 0:
            protegeId = self.ui.tableWidget.takeItem(tableCurrentRow, 0).text()
            self.ui.tableWidget.removeRow(tableCurrentRow)
            self.protegeRemoved.emit(protegeId)
