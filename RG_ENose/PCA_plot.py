# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PCA_plot.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(9)
        sizePolicy.setVerticalStretch(9)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.verticalLayout.addWidget(self.textBrowser)
        self.verticalWidget = QtGui.QWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setObjectName(_fromUtf8("verticalWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.verticalWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.xLabel = QtGui.QLabel(self.verticalWidget)
        self.xLabel.setObjectName(_fromUtf8("xLabel"))
        self.horizontalLayout.addWidget(self.xLabel, QtCore.Qt.AlignRight)
        self.xSpinBox = QtGui.QDoubleSpinBox(self.verticalWidget)
        self.xSpinBox.setDecimals(0)
        self.xSpinBox.setMinimum(1.0)
        self.xSpinBox.setProperty("value", 1.0)
        self.xSpinBox.setObjectName(_fromUtf8("xSpinBox"))
        self.horizontalLayout.addWidget(self.xSpinBox)
        self.yLabel = QtGui.QLabel(self.verticalWidget)
        self.yLabel.setObjectName(_fromUtf8("yLabel"))
        self.horizontalLayout.addWidget(self.yLabel, QtCore.Qt.AlignRight)
        self.ySpinBox = QtGui.QDoubleSpinBox(self.verticalWidget)
        self.ySpinBox.setDecimals(0)
        self.ySpinBox.setMinimum(1.0)
        self.ySpinBox.setProperty("value", 2.0)
        self.ySpinBox.setObjectName(_fromUtf8("ySpinBox"))
        self.horizontalLayout.addWidget(self.ySpinBox)
        self.zLabel = QtGui.QLabel(self.verticalWidget)
        self.zLabel.setObjectName(_fromUtf8("zLabel"))
        self.horizontalLayout.addWidget(self.zLabel, QtCore.Qt.AlignRight)
        self.zSpinBox = QtGui.QDoubleSpinBox(self.verticalWidget)
        self.zSpinBox.setDecimals(0)
        self.zSpinBox.setMinimum(1.0)
        self.zSpinBox.setProperty("value", 3.0)
        self.zSpinBox.setObjectName(_fromUtf8("zSpinBox"))
        self.horizontalLayout.addWidget(self.zSpinBox)
        self.verticalLayout.addWidget(self.verticalWidget)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Plot PCA", None))
        self.xLabel.setText(_translate("Dialog", "x", None))
        self.yLabel.setText(_translate("Dialog", "y", None))
        self.zLabel.setText(_translate("Dialog", "z", None))

