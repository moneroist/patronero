# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'protegestab.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProtegesTab(object):
    def setupUi(self, ProtegesTab):
        ProtegesTab.setObjectName("ProtegesTab")
        ProtegesTab.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(ProtegesTab)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableWidget = QtWidgets.QTableWidget(ProtegesTab)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
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
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.verticalLayout.addWidget(self.tableWidget)
        self.removeButton = QtWidgets.QPushButton(ProtegesTab)
        self.removeButton.setObjectName("removeButton")
        self.verticalLayout.addWidget(self.removeButton)
        self.groupBox = QtWidgets.QGroupBox(ProtegesTab)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.searchUrlLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.searchUrlLineEdit.setObjectName("searchUrlLineEdit")
        self.horizontalLayout.addWidget(self.searchUrlLineEdit)
        self.searchUrlButton = QtWidgets.QPushButton(self.groupBox)
        self.searchUrlButton.setObjectName("searchUrlButton")
        self.horizontalLayout.addWidget(self.searchUrlButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setHorizontalSpacing(40)
        self.formLayout.setObjectName("formLayout")
        self.nameLabel = QtWidgets.QLabel(self.groupBox)
        self.nameLabel.setObjectName("nameLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.nameLabel)
        self.nameLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.nameLineEdit)
        self.addressLabel = QtWidgets.QLabel(self.groupBox)
        self.addressLabel.setObjectName("addressLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.addressLabel)
        self.addressLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.addressLineEdit.setObjectName("addressLineEdit")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.addressLineEdit)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.addButton = QtWidgets.QPushButton(self.groupBox)
        self.addButton.setObjectName("addButton")
        self.verticalLayout_2.addWidget(self.addButton)
        self.verticalLayout.addWidget(self.groupBox)

        self.retranslateUi(ProtegesTab)
        QtCore.QMetaObject.connectSlotsByName(ProtegesTab)

    def retranslateUi(self, ProtegesTab):
        _translate = QtCore.QCoreApplication.translate
        ProtegesTab.setWindowTitle(_translate("ProtegesTab", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ProtegesTab", "Id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ProtegesTab", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ProtegesTab", "Address"))
        self.removeButton.setText(_translate("ProtegesTab", "Remove"))
        self.groupBox.setTitle(_translate("ProtegesTab", "New Protege"))
        self.searchUrlLineEdit.setPlaceholderText(_translate("ProtegesTab", "Search URL for OpenAlias"))
        self.searchUrlButton.setText(_translate("ProtegesTab", "Search"))
        self.nameLabel.setText(_translate("ProtegesTab", "Name"))
        self.addressLabel.setText(_translate("ProtegesTab", "Address"))
        self.addButton.setText(_translate("ProtegesTab", "Add"))
