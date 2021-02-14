# This Python file uses the following encoding: utf-8
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from tabs.generaltabui import Ui_GeneralTab
import os

class GeneralTab(QWidget):
    configPropertyChanged = pyqtSignal(dict)
    openMessageBox = pyqtSignal(int, str, str)
    startMining = pyqtSignal(dict)
    stopMining = pyqtSignal()

    def __init__(self, parent):
        QWidget.__init__(self, parent)

        self.ui = Ui_GeneralTab()
        self.ui.setupUi(self)
        self.initThreads()

        self.ui.protegeComboBox.currentIndexChanged.connect(self.protegeComboBoxChanged)
        self.ui.miningPoolComboBox.currentIndexChanged.connect(self.miningPoolComboBoxChanged)
        self.ui.modeComboBox.currentIndexChanged.connect(self.modeComboBoxChanged)
        self.ui.cpuUsageSlider.valueChanged.connect(self.cpuUsageSliderChanged)
        self.ui.startButton.clicked.connect(self.startButtonClicked)

    def setupData(self, data):
        self.setupProtegeComboBox(data['proteges'])
        self.setProtegeComboBox(data['currentProtegeId'])
        self.setupMiningPoolComboBox(data['miningPools'])
        self.setMiningPoolComboBox(data['currentMiningPoolId'])
        self.setupModeComboBox()
        self.setModeComboBox(data['currentMode'])
        self.setupCpuUsageSlider()
        self.setCpuUsageSlider(data['currentThreads'])

    def setupProtegeComboBox(self, proteges):
        for protege in proteges:
            self.ui.protegeComboBox.addItem(protege['name'], protege)

    def setupMiningPoolComboBox(self, miningPools):
        for miningPool in miningPools:
            self.ui.miningPoolComboBox.addItem(miningPool['name'], miningPool)

    def setupModeComboBox(self):
        self.ui.modeComboBox.addItem("Fast - 2GB RAM", "fast")
        self.ui.modeComboBox.addItem("Slow - 256MB RAM", "light")

    def initThreads(self):
       self.maxThreads = os.cpu_count()

    def setupCpuUsageSlider(self):
        self.ui.cpuUsageSlider.setMinimum(1)
        self.ui.cpuUsageSlider.setMaximum(int(self.maxThreads/2))
        self.ui.cpuUsageSlider.setPageStep(1)
        self.updateCpuUsagePercentage(self.ui.cpuUsageSlider.value())

    def protegeComboBoxChanged(self, index):
        protegeData = self.ui.protegeComboBox.itemData(index)
        arg = { "property": "currentProtegeId", "value": protegeData['id'] }
        self.configPropertyChanged.emit(arg)

    def setProtegeComboBox(self, protegeId):
        for protegeIndex in range(self.ui.protegeComboBox.count()):
            protegeData = self.ui.protegeComboBox.itemData(protegeIndex)
            if protegeData['id'] == protegeId:
                self.ui.protegeComboBox.setCurrentIndex(protegeIndex)
                return

    def removeProtegeComboBox(self, protegeId):
        for protegeIndex in range(self.ui.protegeComboBox.count()):
            protegeData = self.ui.protegeComboBox.itemData(protegeIndex)
            if protegeData['id'] == protegeId:
                self.ui.protegeComboBox.removeItem(protegeIndex)
                return

    def addProtegeComboBox(self, protege):
        print(protege)
        self.ui.protegeComboBox.addItem(protege['name'], protege)

    def miningPoolComboBoxChanged(self, index):
        miningPoolData = self.ui.miningPoolComboBox.itemData(index)
        arg = { "property": "currentMiningPoolId", "value": miningPoolData['id'] }
        self.configPropertyChanged.emit(arg)

    def setMiningPoolComboBox(self, miningPoolId):
        for miningPoolIndex in range(self.ui.miningPoolComboBox.count()):
            miningPoolData = self.ui.miningPoolComboBox.itemData(miningPoolIndex)
            if miningPoolData['id'] == miningPoolId:
                self.ui.miningPoolComboBox.setCurrentIndex(miningPoolIndex)
                return

    def removeMiningPoolComboBox(self, miningPoolId):
        for miningPoolIndex in range(self.ui.miningPoolComboBox.count()):
            miningPoolData = self.ui.miningPoolComboBox.itemData(miningPoolIndex)
            if miningPoolData['id'] == miningPoolId:
                self.ui.miningPoolComboBox.removeItem(miningPoolIndex)
                return

    def addMiningPoolComboBox(self, miningPool):
        self.ui.miningPoolComboBox.addItem(miningPool['name'], miningPool)

    def modeComboBoxChanged(self, index):
        modeData = self.ui.modeComboBox.itemData(index)
        arg = { "property": "currentMode", "value": modeData }
        self.configPropertyChanged.emit(arg)

    def setModeComboBox(self, mode):
        for modeIndex in range(self.ui.modeComboBox.count()):
            currentMode = self.ui.modeComboBox.itemData(modeIndex)
            if currentMode == mode:
                self.ui.modeComboBox.setCurrentIndex(modeIndex)
                return

    def setCpuUsageSlider(self, value):
        self.ui.cpuUsageSlider.setValue(value)

    def cpuUsageSliderChanged(self, value):
        arg = { "property": "currentThreads", "value": value }
        self.updateCpuUsagePercentage(value)
        self.configPropertyChanged.emit(arg)

    def updateCpuUsagePercentage(self, value):
        cpuPercentage = "{0:.0%}".format(float(value)/(self.maxThreads))
        self.ui.cpuUsagePercentage.setText(cpuPercentage)

    def startButtonClicked(self):

        protege = self.ui.protegeComboBox.currentData()
        miningPool = self.ui.miningPoolComboBox.currentData()
        mode = self.ui.modeComboBox.currentData()
        threads = self.ui.cpuUsageSlider.value()

        if not protege:
            self.openMessageBox.emit(QMessageBox.Warning, "Warning", "You need choose protege first!")
            return
        if not miningPool:
            self.openMessageBox.emit(QMessageBox.Warning, "Warning", "You need choose mining pool first!")
            return
        if not mode:
            self.openMessageBox.emit(QMessageBox.Warning, "Warning", "You need choose protege first!")
            return



        args = { "address": protege['address'], "miningPool": miningPool['url'], "mode": mode, "threads": threads }
        self.startMining.emit(args)

    def stopButtonClicked(self):
        self.stopMining.emit()

    def disableUi(self):
        self.ui.protegeComboBox.setDisabled(True)
        self.ui.miningPoolComboBox.setDisabled(True)
        self.ui.modeComboBox.setDisabled(True)
        self.ui.cpuUsageSlider.setDisabled(True)

        self.ui.startButton.setText("Stop")
        self.ui.startButton.clicked.disconnect(self.startButtonClicked)
        self.ui.startButton.clicked.connect(self.stopButtonClicked)

    def enableUi(self):
        self.ui.protegeComboBox.setDisabled(False)
        self.ui.miningPoolComboBox.setDisabled(False)
        self.ui.modeComboBox.setDisabled(False)
        self.ui.cpuUsageSlider.setDisabled(False)

        self.ui.startButton.setText("Start")
        self.ui.startButton.clicked.disconnect(self.stopButtonClicked)
        self.ui.startButton.clicked.connect(self.startButtonClicked)
