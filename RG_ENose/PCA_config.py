# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PCA_config.ui'
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
        Dialog.resize(465, 120)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(465, 120))
        Dialog.setMaximumSize(QtCore.QSize(465, 120))
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.componentsLabel_2 = QtGui.QLabel(Dialog)
        self.componentsLabel_2.setObjectName(_fromUtf8("componentsLabel_2"))
        self.gridLayout.addWidget(self.componentsLabel_2, 1, 2, 1, 1)
        self.varianceLabel_2 = QtGui.QLabel(Dialog)
        self.varianceLabel_2.setObjectName(_fromUtf8("varianceLabel_2"))
        self.gridLayout.addWidget(self.varianceLabel_2, 0, 2, 1, 1)
        self.componentslabel_1 = QtGui.QLabel(Dialog)
        self.componentslabel_1.setObjectName(_fromUtf8("componentslabel_1"))
        self.gridLayout.addWidget(self.componentslabel_1, 1, 0, 1, 1)
        self.varianceSpinBox = QtGui.QDoubleSpinBox(Dialog)
        self.varianceSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.varianceSpinBox.setAccelerated(True)
        self.varianceSpinBox.setMaximum(100.0)
        self.varianceSpinBox.setSingleStep(0.01)
        self.varianceSpinBox.setProperty("value", 80.0)
        self.varianceSpinBox.setObjectName(_fromUtf8("varianceSpinBox"))
        self.gridLayout.addWidget(self.varianceSpinBox, 0, 1, 1, 1)
        self.varianceLabel_1 = QtGui.QLabel(Dialog)
        self.varianceLabel_1.setObjectName(_fromUtf8("varianceLabel_1"))
        self.gridLayout.addWidget(self.varianceLabel_1, 0, 0, 1, 1)
        self.componentsSpinBox = QtGui.QDoubleSpinBox(Dialog)
        self.componentsSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.componentsSpinBox.setDecimals(0)
        self.componentsSpinBox.setMinimum(1.0)
        self.componentsSpinBox.setMaximum(100.0)
        self.componentsSpinBox.setProperty("value", 3.0)
        self.componentsSpinBox.setObjectName(_fromUtf8("componentsSpinBox"))
        self.gridLayout.addWidget(self.componentsSpinBox, 1, 1, 1, 1)
        self.varianceButton = QtGui.QCommandLinkButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.varianceButton.sizePolicy().hasHeightForWidth())
        self.varianceButton.setSizePolicy(sizePolicy)
        self.varianceButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.varianceButton.setObjectName(_fromUtf8("varianceButton"))
        self.gridLayout.addWidget(self.varianceButton, 0, 3, 1, 1)
        self.componentsButton = QtGui.QCommandLinkButton(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.componentsButton.sizePolicy().hasHeightForWidth())
        self.componentsButton.setSizePolicy(sizePolicy)
        self.componentsButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.componentsButton.setObjectName(_fromUtf8("componentsButton"))
        self.gridLayout.addWidget(self.componentsButton, 1, 3, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "PCA configuration", None))
        self.componentsLabel_2.setText(_translate("Dialog", "components.", None))
        self.varianceLabel_2.setText(_translate("Dialog", "% of variance.", None))
        self.componentslabel_1.setText(_translate("Dialog", "Keep exactly", None))
        self.varianceLabel_1.setText(_translate("Dialog", "Keep at least", None))
        self.varianceButton.setText(_translate("Dialog", "Go", None))
        self.componentsButton.setText(_translate("Dialog", "Go", None))

