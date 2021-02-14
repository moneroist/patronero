# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generaltab.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.protegeLabel = QtWidgets.QLabel(Form)
        self.protegeLabel.setObjectName("protegeLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.protegeLabel)
        self.protegeComboBox = QtWidgets.QComboBox(Form)
        self.protegeComboBox.setObjectName("protegeComboBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.protegeComboBox)
        self.miningPoolLabel = QtWidgets.QLabel(Form)
        self.miningPoolLabel.setObjectName("miningPoolLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.miningPoolLabel)
        self.miningPoolComboBox = QtWidgets.QComboBox(Form)
        self.miningPoolComboBox.setObjectName("miningPoolComboBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.miningPoolComboBox)
        self.modeLabel = QtWidgets.QLabel(Form)
        self.modeLabel.setObjectName("modeLabel")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.modeLabel)
        self.modeComboBox = QtWidgets.QComboBox(Form)
        self.modeComboBox.setObjectName("modeComboBox")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.modeComboBox)
        self.cpuUsageLabel = QtWidgets.QLabel(Form)
        self.cpuUsageLabel.setObjectName("cpuUsageLabel")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.cpuUsageLabel)
        self.cpuUsageWidget = QtWidgets.QWidget(Form)
        self.cpuUsageWidget.setObjectName("cpuUsageWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.cpuUsageWidget)
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
        self.startButton = QtWidgets.QPushButton(Form)
        self.startButton.setObjectName("startButton")
        self.verticalLayout.addWidget(self.startButton)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.protegeLabel.setText(_translate("Form", "Protege"))
        self.miningPoolLabel.setText(_translate("Form", "Mining Pool"))
        self.modeLabel.setText(_translate("Form", "Mode"))
        self.cpuUsageLabel.setText(_translate("Form", "CPU Usage"))
        self.cpuUsagePercentage.setText(_translate("Form", "100%"))
        self.startButton.setText(_translate("Form", "Start"))
