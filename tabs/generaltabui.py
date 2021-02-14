# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generaltab.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GeneralTab(object):
    def setupUi(self, GeneralTab):
        GeneralTab.setObjectName("GeneralTab")
        GeneralTab.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(GeneralTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(40)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.protegeLabel = QtWidgets.QLabel(GeneralTab)
        self.protegeLabel.setObjectName("protegeLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.protegeLabel)
        self.protegeComboBox = QtWidgets.QComboBox(GeneralTab)
        self.protegeComboBox.setObjectName("protegeComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.protegeComboBox)
        self.miningPoolLabel = QtWidgets.QLabel(GeneralTab)
        self.miningPoolLabel.setObjectName("miningPoolLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.miningPoolLabel)
        self.miningPoolComboBox = QtWidgets.QComboBox(GeneralTab)
        self.miningPoolComboBox.setObjectName("miningPoolComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.miningPoolComboBox)
        self.modeLabel = QtWidgets.QLabel(GeneralTab)
        self.modeLabel.setObjectName("modeLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.modeLabel)
        self.modeComboBox = QtWidgets.QComboBox(GeneralTab)
        self.modeComboBox.setObjectName("modeComboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.modeComboBox)
        self.cpuUsageLabel = QtWidgets.QLabel(GeneralTab)
        self.cpuUsageLabel.setObjectName("cpuUsageLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.cpuUsageLabel)
        self.cpuUsageWidget = QtWidgets.QWidget(GeneralTab)
        self.cpuUsageWidget.setObjectName("cpuUsageWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.cpuUsageWidget)
        self.horizontalLayout.setContentsMargins(0, 9, 0, 9)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cpuUsageSlider = QtWidgets.QSlider(self.cpuUsageWidget)
        self.cpuUsageSlider.setOrientation(QtCore.Qt.Horizontal)
        self.cpuUsageSlider.setObjectName("cpuUsageSlider")
        self.horizontalLayout.addWidget(self.cpuUsageSlider)
        self.cpuUsagePercentage = QtWidgets.QLabel(self.cpuUsageWidget)
        self.cpuUsagePercentage.setMinimumSize(QtCore.QSize(40, 0))
        self.cpuUsagePercentage.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.cpuUsagePercentage.setObjectName("cpuUsagePercentage")
        self.horizontalLayout.addWidget(self.cpuUsagePercentage)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cpuUsageWidget)
        self.verticalLayout.addLayout(self.formLayout)
        self.startButton = QtWidgets.QPushButton(GeneralTab)
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)

        self.retranslateUi(GeneralTab)
        QtCore.QMetaObject.connectSlotsByName(GeneralTab)

    def retranslateUi(self, GeneralTab):
        _translate = QtCore.QCoreApplication.translate
        GeneralTab.setWindowTitle(_translate("GeneralTab", "Form"))
        self.protegeLabel.setText(_translate("GeneralTab", "Protege"))
        self.miningPoolLabel.setText(_translate("GeneralTab", "Mining Pool"))
        self.modeLabel.setText(_translate("GeneralTab", "Mode"))
        self.cpuUsageLabel.setText(_translate("GeneralTab", "CPU Usage"))
        self.cpuUsagePercentage.setText(_translate("GeneralTab", "100%"))
        self.startButton.setText(_translate("GeneralTab", "Start"))
