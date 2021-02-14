# This Python file uses the following encoding: utf-8
from PyQt5.QtCore import *
import os, random


class Miner(QProcess):
    def __init__(self, parent=None):
        QProcess.__init__(self, parent)
        self.minerPath = os.getcwd() + "/xmrig"

    def startMining(self, args):
        self.currentArgs = args
        if self.state() == QProcess.NotRunning:
            self.currentArgs = args
            self.start(self.minerPath, ["-u", args['address'], "-o", args['miningPool'], "-t", str(args['threads']), f"--randomx-mode={args['mode']}", "--cpu-priority 0", "-k"])

    def stopMining(self):
        if self.state() != QProcess.NotRunning:
            self.terminate()
            self.waitForFinished()
