# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_gui.ui'
#
# Created: Fri Aug 19 15:38:40 2016
#      by: PyQt5 UI code generator 5.2.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(870, 650)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/main_gui/logo.gif"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(3, 0, 3, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.MainTabs = QtWidgets.QTabWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.MainTabs.sizePolicy().hasHeightForWidth())
        self.MainTabs.setSizePolicy(sizePolicy)
        self.MainTabs.setObjectName("MainTabs")
        self.fitModelTab = QtWidgets.QWidget()
        self.fitModelTab.setObjectName("fitModelTab")
        self.MainTabs.addTab(self.fitModelTab, "")
        self.generateBrainMaskTab = QtWidgets.QWidget()
        self.generateBrainMaskTab.setObjectName("generateBrainMaskTab")
        self.MainTabs.addTab(self.generateBrainMaskTab, "")
        self.generateROIMaskTab = QtWidgets.QWidget()
        self.generateROIMaskTab.setObjectName("generateROIMaskTab")
        self.MainTabs.addTab(self.generateROIMaskTab, "")
        self.generateProtocolTab = QtWidgets.QWidget()
        self.generateProtocolTab.setObjectName("generateProtocolTab")
        self.MainTabs.addTab(self.generateProtocolTab, "")
        self.viewResultsTab = QtWidgets.QWidget()
        self.viewResultsTab.setObjectName("viewResultsTab")
        self.MainTabs.addTab(self.viewResultsTab, "")
        self.loggingTextBox = QtWidgets.QPlainTextEdit(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loggingTextBox.sizePolicy().hasHeightForWidth())
        self.loggingTextBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Droid Sans Mono")
        self.loggingTextBox.setFont(font)
        self.loggingTextBox.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.loggingTextBox.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.loggingTextBox.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.loggingTextBox.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.loggingTextBox.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.loggingTextBox.setReadOnly(True)
        self.loggingTextBox.setPlainText("")
        self.loggingTextBox.setTabStopWidth(80)
        self.loggingTextBox.setObjectName("loggingTextBox")
        self.verticalLayout_2.addWidget(self.splitter)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setContentsMargins(-1, 0, 8, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.executionStatusLabel = QtWidgets.QLabel(self.centralwidget)
        self.executionStatusLabel.setObjectName("executionStatusLabel")
        self.horizontalLayout.addWidget(self.executionStatusLabel)
        self.executionStatusIcon = QtWidgets.QLabel(self.centralwidget)
        self.executionStatusIcon.setObjectName("executionStatusIcon")
        self.horizontalLayout.addWidget(self.executionStatusIcon)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 870, 27))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.action_RuntimeSettings = QtWidgets.QAction(MainWindow)
        self.action_RuntimeSettings.setObjectName("action_RuntimeSettings")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuMenu.addAction(self.action_RuntimeSettings)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.MainTabs.setCurrentIndex(0)
        self.actionExit.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Maastricht Diffusion Toolbox"))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.fitModelTab), _translate("MainWindow", "Fit model"))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.generateBrainMaskTab), _translate("MainWindow", "Generate brain mask"))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.generateROIMaskTab), _translate("MainWindow", "Generate ROI mask"))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.generateProtocolTab), _translate("MainWindow", "Generate protocol file"))
        self.MainTabs.setTabText(self.MainTabs.indexOf(self.viewResultsTab), _translate("MainWindow", "View results"))
        self.executionStatusLabel.setText(_translate("MainWindow", "TextLabel"))
        self.executionStatusIcon.setText(_translate("MainWindow", "TextLabel"))
        self.menuMenu.setTitle(_translate("MainWindow", "&File"))
        self.menuHelp.setTitle(_translate("MainWindow", "&Help"))
        self.actionExit.setText(_translate("MainWindow", "&Quit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.action_RuntimeSettings.setText(_translate("MainWindow", "&Runtime settings"))
        self.actionAbout.setText(_translate("MainWindow", "About"))

from . import main_gui_rc
