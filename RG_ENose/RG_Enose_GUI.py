# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RG_Enose.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1087, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.inputWidget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.inputWidget.sizePolicy().hasHeightForWidth())
        self.inputWidget.setSizePolicy(sizePolicy)
        self.inputWidget.setObjectName(_fromUtf8("inputWidget"))
        self.formLayout = QtGui.QFormLayout(self.inputWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setRowWrapPolicy(QtGui.QFormLayout.WrapAllRows)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.preprocessingLabel = QtGui.QLabel(self.inputWidget)
        self.preprocessingLabel.setObjectName(_fromUtf8("preprocessingLabel"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.preprocessingLabel)
        self.preprocessingComboBox = QtGui.QComboBox(self.inputWidget)
        self.preprocessingComboBox.setObjectName(_fromUtf8("preprocessingComboBox"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.preprocessingComboBox)
        self.normalizationLabel = QtGui.QLabel(self.inputWidget)
        self.normalizationLabel.setObjectName(_fromUtf8("normalizationLabel"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.normalizationLabel)
        self.normalizationComboBox = QtGui.QComboBox(self.inputWidget)
        self.normalizationComboBox.setObjectName(_fromUtf8("normalizationComboBox"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.normalizationComboBox)
        self.statisticalAnalysisLabel = QtGui.QLabel(self.inputWidget)
        self.statisticalAnalysisLabel.setObjectName(_fromUtf8("statisticalAnalysisLabel"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.statisticalAnalysisLabel)
        self.statisticalAnalysisComboBox = QtGui.QComboBox(self.inputWidget)
        self.statisticalAnalysisComboBox.setObjectName(_fromUtf8("statisticalAnalysisComboBox"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.statisticalAnalysisComboBox)
        self.sVMLabel = QtGui.QLabel(self.inputWidget)
        self.sVMLabel.setObjectName(_fromUtf8("sVMLabel"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.sVMLabel)
        self.sVMComboBox = QtGui.QComboBox(self.inputWidget)
        self.sVMComboBox.setObjectName(_fromUtf8("sVMComboBox"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.sVMComboBox)
        self.neuralNetworkLabel = QtGui.QLabel(self.inputWidget)
        self.neuralNetworkLabel.setObjectName(_fromUtf8("neuralNetworkLabel"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.neuralNetworkLabel)
        self.neuralNetworkComboBox = QtGui.QComboBox(self.inputWidget)
        self.neuralNetworkComboBox.setObjectName(_fromUtf8("neuralNetworkComboBox"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.neuralNetworkComboBox)
        self.dataSelectionLabel = QtGui.QLabel(self.inputWidget)
        self.dataSelectionLabel.setObjectName(_fromUtf8("dataSelectionLabel"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.dataSelectionLabel)
        self.dataSelectionComboBox = QtGui.QComboBox(self.inputWidget)
        self.dataSelectionComboBox.setObjectName(_fromUtf8("dataSelectionComboBox"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.dataSelectionComboBox)
        self.sVMSelectionLabel = QtGui.QLabel(self.inputWidget)
        self.sVMSelectionLabel.setObjectName(_fromUtf8("sVMSelectionLabel"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.sVMSelectionLabel)
        self.sVMSelectionComboBox = QtGui.QComboBox(self.inputWidget)
        self.sVMSelectionComboBox.setObjectName(_fromUtf8("sVMSelectionComboBox"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.sVMSelectionComboBox)
        self.horizontalLayout.addWidget(self.inputWidget)
        self.verticalWidget = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setObjectName(_fromUtf8("verticalWidget"))
        self.gridLayout = QtGui.QGridLayout(self.verticalWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMinAndMaxSize)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.outputView = QtGui.QGraphicsView(self.verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(33)
        sizePolicy.setHeightForWidth(self.outputView.sizePolicy().hasHeightForWidth())
        self.outputView.setSizePolicy(sizePolicy)
        self.outputView.setAlignment(QtCore.Qt.AlignCenter)
        self.outputView.setObjectName(_fromUtf8("outputView"))
        self.gridLayout.addWidget(self.outputView, 0, 0, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(self.verticalWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonBox.setMouseTracking(False)
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setAutoFillBackground(False)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Abort|QtGui.QDialogButtonBox.Reset)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.verticalWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1087, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionSensor_data = QtGui.QAction(MainWindow)
        self.actionSensor_data.setObjectName(_fromUtf8("actionSensor_data"))
        self.actionMat_File = QtGui.QAction(MainWindow)
        self.actionMat_File.setObjectName(_fromUtf8("actionMat_File"))
        self.actionLoad = QtGui.QAction(MainWindow)
        self.actionLoad.setObjectName(_fromUtf8("actionLoad"))
        self.menuFile.addAction(self.actionLoad)
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.preprocessingLabel.setText(_translate("MainWindow", "Preprocessing", None))
        self.normalizationLabel.setText(_translate("MainWindow", "Normalization", None))
        self.statisticalAnalysisLabel.setText(_translate("MainWindow", "Statistical Analysis", None))
        self.sVMLabel.setText(_translate("MainWindow", "SVM", None))
        self.neuralNetworkLabel.setText(_translate("MainWindow", "Neural Network", None))
        self.dataSelectionLabel.setText(_translate("MainWindow", "Data selection", None))
        self.sVMSelectionLabel.setText(_translate("MainWindow", "SVM Selection", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionSensor_data.setText(_translate("MainWindow", "Raw data", None))
        self.actionMat_File.setText(_translate("MainWindow", "mat File", None))
        self.actionLoad.setText(_translate("MainWindow", "Load", None))

