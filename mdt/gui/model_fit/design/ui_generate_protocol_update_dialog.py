# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generate_protocol_update_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_UpdateColumnDialog(object):
    def setupUi(self, UpdateColumnDialog):
        UpdateColumnDialog.setObjectName("UpdateColumnDialog")
        UpdateColumnDialog.resize(831, 304)
        self.verticalLayout = QtWidgets.QVBoxLayout(UpdateColumnDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(UpdateColumnDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(UpdateColumnDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(UpdateColumnDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.fileInput = QtWidgets.QPushButton(UpdateColumnDialog)
        self.fileInput.setEnabled(True)
        self.fileInput.setObjectName("fileInput")
        self.horizontalLayout.addWidget(self.fileInput)
        self.selectedFile = QtWidgets.QLineEdit(UpdateColumnDialog)
        self.selectedFile.setEnabled(True)
        self.selectedFile.setObjectName("selectedFile")
        self.horizontalLayout.addWidget(self.selectedFile)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(UpdateColumnDialog)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.inputMethodSelector = QtWidgets.QComboBox(UpdateColumnDialog)
        self.inputMethodSelector.setObjectName("inputMethodSelector")
        self.inputMethodSelector.addItem("")
        self.inputMethodSelector.addItem("")
        self.gridLayout.addWidget(self.inputMethodSelector, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(UpdateColumnDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.valueScale = QtWidgets.QLineEdit(UpdateColumnDialog)
        self.valueScale.setObjectName("valueScale")
        self.gridLayout.addWidget(self.valueScale, 6, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(UpdateColumnDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 2, 1, 1)
        self.label_10 = QtWidgets.QLabel(UpdateColumnDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(UpdateColumnDialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(UpdateColumnDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.columnNameInput = QtWidgets.QLineEdit(UpdateColumnDialog)
        self.columnNameInput.setObjectName("columnNameInput")
        self.gridLayout.addWidget(self.columnNameInput, 0, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(UpdateColumnDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 4, 2, 1, 1)
        self.label_13 = QtWidgets.QLabel(UpdateColumnDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 6, 2, 1, 1)
        self.line_2 = QtWidgets.QFrame(UpdateColumnDialog)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout.addWidget(self.line_2, 2, 0, 1, 3)
        self.label_6 = QtWidgets.QLabel(UpdateColumnDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)
        self.singleValueInput = QtWidgets.QLineEdit(UpdateColumnDialog)
        self.singleValueInput.setObjectName("singleValueInput")
        self.gridLayout.addWidget(self.singleValueInput, 3, 1, 1, 1)
        self.line_4 = QtWidgets.QFrame(UpdateColumnDialog)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.gridLayout.addWidget(self.line_4, 5, 0, 1, 3)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line_3 = QtWidgets.QFrame(UpdateColumnDialog)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(UpdateColumnDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(UpdateColumnDialog)
        self.buttonBox.accepted.connect(UpdateColumnDialog.accept)
        self.buttonBox.rejected.connect(UpdateColumnDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(UpdateColumnDialog)
        UpdateColumnDialog.setTabOrder(self.columnNameInput, self.inputMethodSelector)
        UpdateColumnDialog.setTabOrder(self.inputMethodSelector, self.singleValueInput)
        UpdateColumnDialog.setTabOrder(self.singleValueInput, self.fileInput)
        UpdateColumnDialog.setTabOrder(self.fileInput, self.selectedFile)
        UpdateColumnDialog.setTabOrder(self.selectedFile, self.valueScale)

    def retranslateUi(self, UpdateColumnDialog):
        _translate = QtCore.QCoreApplication.translate
        UpdateColumnDialog.setWindowTitle(_translate("UpdateColumnDialog", "Add / Update column"))
        self.label_3.setText(_translate("UpdateColumnDialog", "Add / Update column"))
        self.label_4.setText(_translate("UpdateColumnDialog", "Add a column to the current protocol or overwrite an existing column."))
        self.fileInput.setText(_translate("UpdateColumnDialog", "Browse"))
        self.label_2.setText(_translate("UpdateColumnDialog", "Method:"))
        self.inputMethodSelector.setItemText(0, _translate("UpdateColumnDialog", "From file"))
        self.inputMethodSelector.setItemText(1, _translate("UpdateColumnDialog", "Single value"))
        self.label.setText(_translate("UpdateColumnDialog", "Column name: "))
        self.label_11.setText(_translate("UpdateColumnDialog", "(A single value for every row)"))
        self.label_10.setText(_translate("UpdateColumnDialog", "(The column name, for example \"g\", \"b\" or \"TE\")"))
        self.label_7.setText(_translate("UpdateColumnDialog", "Scale:"))
        self.label_5.setText(_translate("UpdateColumnDialog", "Single value:"))
        self.label_12.setText(_translate("UpdateColumnDialog", "(File with a single value, a row, a column or a matrix)"))
        self.label_13.setText(_translate("UpdateColumnDialog", "(Optionally, scale the input with this amount)"))
        self.label_6.setText(_translate("UpdateColumnDialog", "File input:"))

