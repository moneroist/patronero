# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'miningpoolstab.ui'
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
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.removeButton = QtWidgets.QPushButton(Form)
        self.removeButton.setObjectName("removeButton")
        self.verticalLayout.addWidget(self.removeButton)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.groupBox)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.urlLabel = QtWidgets.QLabel(self.groupBox)
        self.urlLabel.setObjectName("urlLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.urlLabel)
        self.urlLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.urlLineEdit.setObjectName("urlLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.urlLineEdit)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.addButton = QtWidgets.QPushButton(self.groupBox)
        self.addButton.setObjectName("addButton")
        self.verticalLayout_2.addWidget(self.addButton)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "URL"))
        self.removeButton.setText(_translate("Form", "Remove"))
        self.groupBox.setTitle(_translate("Form", "New Mining Pool"))
        self.nameLabel.setText(_translate("Form", "Name"))
        self.urlLabel.setText(_translate("Form", "URL"))
        self.addButton.setText(_translate("Form", "Add"))
