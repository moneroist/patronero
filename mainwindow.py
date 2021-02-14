# This Python file uses the following encoding: utf-8
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from utils.messagebox import MessageBox
from mainwindowui import Ui_MainWindow
from tabs.generaltab import GeneralTab
from tabs.protegestab import ProtegesTab
from tabs.miningpoolstab import MiningPoolsTab
from utils.miner import Miner
from utils.config import Config

class MainWindow(QMainWindow):
    showTrayIconTooltip = pyqtSignal(str, str, int)

    def __init__(self):
        QMainWindow.__init__(self)

        self.messageBox = MessageBox(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Patronero")

        self.config = Config()
        self.config.openMessageBox.connect(self.messageBox.show)
        self.config.readConfig()

        self.generalTab = GeneralTab(self)
        self.generalTab.setupData(self.config.data)
        self.generalTab.openMessageBox.connect(self.messageBox.show)
        self.generalTab.configPropertyChanged.connect(self.configPropertyChanged)
        self.generalTab.startMining.connect(self.startMining)
        self.generalTab.stopMining.connect(self.stopMining)

        self.protegesTab = ProtegesTab(self)
        self.protegesTab.setupData(self.config.data)
        self.protegesTab.openMessageBox.connect(self.messageBox.show)
        self.protegesTab.protegeCreated.connect(self.protegeCreated)
        self.protegesTab.protegeRemoved.connect(self.protegeRemoved)

        self.miningPoolsTab = MiningPoolsTab(self)
        self.miningPoolsTab.setupData(self.config.data)
        self.miningPoolsTab.openMessageBox.connect(self.messageBox.show)
        self.miningPoolsTab.miningPoolCreated.connect(self.miningPoolCreated)
        self.miningPoolsTab.miningPoolRemoved.connect(self.miningPoolRemoved)

        self.ui.tabs.addTab(self.generalTab, "General")
        self.ui.tabs.addTab(self.protegesTab, "Proteges")
        self.ui.tabs.addTab(self.miningPoolsTab, "Mining Pools")

    def protegeCreated(self, protege):
        self.config.addProtege(protege)
        self.generalTab.addProtegeComboBox(protege)

    def protegeRemoved(self, protegeId):
        self.config.removeProtege(protegeId)
        self.generalTab.removeProtegeComboBox(protegeId)

    def miningPoolCreated(self, miningPool):
        self.config.addMiningPool(miningPool)
        self.generalTab.addMiningPoolComboBox(miningPool)

    def miningPoolRemoved(self, miningPoolId):
        self.config.removeMiningPool(miningPoolId)
        self.generalTab.removeMiningPoolComboBox(miningPoolId)

    def configPropertyChanged(self, arg):
        self.config.setProperty(arg['property'], arg['value'])

    def startMining(self, args):
        self.miner = Miner()
        self.miner.stateChanged.connect(self.minerStateChanged)
        self.miner.finished.connect(self.minerFinished)
        self.miner.startMining(args)

    def stopMining(self):
        self.miner.stopMining()

    def enableUi(self):
        self.ui.tabs.setTabEnabled(1, True)
        self.ui.tabs.setTabEnabled(2, True)
        self.generalTab.enableUi()

    def disableUi(self):
        self.ui.tabs.setTabEnabled(1, False)
        self.ui.tabs.setTabEnabled(2, False)
        self.generalTab.disableUi()

    def minerStateChanged(self, state):
        if state == QProcess.Running:
            self.disableUi()
            self.showTrayIconTooltip.emit("Patronero started", "Patronero is now running in background", 5000)
            self.hide()
        elif state == QProcess.NotRunning:
            self.showTrayIconTooltip.emit("Patronero stopped", "Patronero background process has been stopped", 5000)
            self.enableUi()

    def minerFinished(self, exitCode, exitStatus):
        pass

