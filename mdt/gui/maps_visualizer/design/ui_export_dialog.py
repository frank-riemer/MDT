# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'export_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExportImageDialog(object):
    def setupUi(self, ExportImageDialog):
        ExportImageDialog.setObjectName("ExportImageDialog")
        ExportImageDialog.resize(722, 253)
        self.verticalLayout = QtWidgets.QVBoxLayout(ExportImageDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(ExportImageDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(ExportImageDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(ExportImageDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.outputFile_chooser = QtWidgets.QPushButton(ExportImageDialog)
        self.outputFile_chooser.setEnabled(True)
        self.outputFile_chooser.setObjectName("outputFile_chooser")
        self.horizontalLayout.addWidget(self.outputFile_chooser)
        self.outputFile_box = QtWidgets.QLineEdit(ExportImageDialog)
        self.outputFile_box.setEnabled(True)
        self.outputFile_box.setObjectName("outputFile_box")
        self.horizontalLayout.addWidget(self.outputFile_box)
        self.horizontalLayout.setStretch(1, 1)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(ExportImageDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 0, 2, 1, 1)
        self.label_11 = QtWidgets.QLabel(ExportImageDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 2, 1, 1)
        self.width_box = QtWidgets.QSpinBox(ExportImageDialog)
        self.width_box.setMinimum(100)
        self.width_box.setMaximum(9999)
        self.width_box.setProperty("value", 1280)
        self.width_box.setObjectName("width_box")
        self.gridLayout.addWidget(self.width_box, 0, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(ExportImageDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 1, 2, 1, 1)
        self.label_6 = QtWidgets.QLabel(ExportImageDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(ExportImageDialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(ExportImageDialog)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.height_box = QtWidgets.QSpinBox(ExportImageDialog)
        self.height_box.setMinimum(100)
        self.height_box.setMaximum(9999)
        self.height_box.setProperty("value", 720)
        self.height_box.setObjectName("height_box")
        self.gridLayout.addWidget(self.height_box, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(ExportImageDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.dpi_box = QtWidgets.QSpinBox(ExportImageDialog)
        self.dpi_box.setMinimum(10)
        self.dpi_box.setMaximum(1000)
        self.dpi_box.setProperty("value", 100)
        self.dpi_box.setObjectName("dpi_box")
        self.gridLayout.addWidget(self.dpi_box, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line_3 = QtWidgets.QFrame(ExportImageDialog)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(ExportImageDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ExportImageDialog)
        self.buttonBox.accepted.connect(ExportImageDialog.accept)
        self.buttonBox.rejected.connect(ExportImageDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(ExportImageDialog)
        ExportImageDialog.setTabOrder(self.dpi_box, self.outputFile_chooser)
        ExportImageDialog.setTabOrder(self.outputFile_chooser, self.outputFile_box)

    def retranslateUi(self, ExportImageDialog):
        _translate = QtCore.QCoreApplication.translate
        ExportImageDialog.setWindowTitle(_translate("ExportImageDialog", "Export image"))
        self.label_3.setText(_translate("ExportImageDialog", "Export image"))
        self.label_4.setText(_translate("ExportImageDialog", "Export the current view to an image."))
        self.outputFile_chooser.setText(_translate("ExportImageDialog", "Browse"))
        self.label_12.setText(_translate("ExportImageDialog", "(The width of the image in pixels)"))
        self.label_11.setText(_translate("ExportImageDialog", "(Dots/pixels per inch)"))
        self.label_14.setText(_translate("ExportImageDialog", "(The height of the image in pixels)"))
        self.label_6.setText(_translate("ExportImageDialog", "Width:"))
        self.label_7.setText(_translate("ExportImageDialog", "Output file:"))
        self.label.setText(_translate("ExportImageDialog", "Height:"))
        self.label_5.setText(_translate("ExportImageDialog", "DPI:"))
