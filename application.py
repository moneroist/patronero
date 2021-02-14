# This Python file uses the following encoding: utf-8
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from mainwindow import MainWindow


class Application(QApplication):
    def __init__(self, arr):
        QApplication.__init__(self, arr)
        self.mainWindow = MainWindow()
        self.mainWindow.showTrayIconTooltip.connect(self.showTrayIconTooltip)
        self.setQuitOnLastWindowClosed(False)
        self.icon = QIcon("icon.png")
        self.setWindowIcon(self.icon)

        self.setupTray()
        self.mainWindow.show()
        sys.exit(self.exec_())

    def setupTray(self):
        self.tray = QSystemTrayIcon()
        self.tray.setIcon(self.icon)
        self.tray.setVisible(True)

        self.menu = QMenu()

        self.showAction = QAction("Show")
        self.menu.addAction(self.showAction)
        self.showAction.triggered.connect(self.mainWindow.show)

        self.quitAction = QAction("Quit")
        self.menu.addAction(self.quitAction)
        self.quitAction.triggered.connect(self.quit)

        self.tray.setContextMenu(self.menu)

    def showTrayIconTooltip(self, text, message, time):
        self.tray.showMessage(text, message, QSystemTrayIcon.NoIcon, time)

if __name__ == "__main__":
    Application([])

