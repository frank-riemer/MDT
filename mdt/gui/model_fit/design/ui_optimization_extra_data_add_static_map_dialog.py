# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'optimization_extra_data_add_static_map_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AddStaticMapDialog(object):
    def setupUi(self, AddStaticMapDialog):
        AddStaticMapDialog.setObjectName("AddStaticMapDialog")
        AddStaticMapDialog.resize(719, 187)
        self.verticalLayout = QtWidgets.QVBoxLayout(AddStaticMapDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(AddStaticMapDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(AddStaticMapDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(AddStaticMapDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(AddStaticMapDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 0, 2, 1, 1)
        self.label = QtWidgets.QLabel(AddStaticMapDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.valueInput = QtWidgets.QLineEdit(AddStaticMapDialog)
        self.valueInput.setEnabled(True)
        self.valueInput.setObjectName("valueInput")
        self.horizontalLayout.addWidget(self.valueInput)
        self.fileBrowse = QtWidgets.QPushButton(AddStaticMapDialog)
        self.fileBrowse.setEnabled(True)
        self.fileBrowse.setObjectName("fileBrowse")
        self.horizontalLayout.addWidget(self.fileBrowse)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(AddStaticMapDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 2, 1, 1)
        self.mapNameInput = QtWidgets.QLineEdit(AddStaticMapDialog)
        self.mapNameInput.setObjectName("mapNameInput")
        self.gridLayout.addWidget(self.mapNameInput, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(AddStaticMapDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line_3 = QtWidgets.QFrame(AddStaticMapDialog)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(AddStaticMapDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AddStaticMapDialog)
        self.buttonBox.accepted.connect(AddStaticMapDialog.accept)
        self.buttonBox.rejected.connect(AddStaticMapDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AddStaticMapDialog)
        AddStaticMapDialog.setTabOrder(self.mapNameInput, self.valueInput)
        AddStaticMapDialog.setTabOrder(self.valueInput, self.fileBrowse)

    def retranslateUi(self, AddStaticMapDialog):
        _translate = QtCore.QCoreApplication.translate
        AddStaticMapDialog.setWindowTitle(_translate("AddStaticMapDialog", "Add map"))
        self.label_3.setText(_translate("AddStaticMapDialog", "Add static map"))
        self.label_4.setText(_translate("AddStaticMapDialog", "Add an additional static map to the problem data"))
        self.label_10.setText(_translate("AddStaticMapDialog", "(The map name matching the static parameters of the model)"))
        self.label.setText(_translate("AddStaticMapDialog", "Map name: "))
        self.fileBrowse.setText(_translate("AddStaticMapDialog", "File browser"))
        self.label_12.setText(_translate("AddStaticMapDialog", "(Either a nifti file or a scalar value)"))
        self.label_6.setText(_translate("AddStaticMapDialog", "Value:"))

