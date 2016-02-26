from PyQt4 import QtGui
import ConfigParser
import glob
import numpy
import os
import sys
import RG_Enose_GUI

sys.path.insert(0, 'Statistical Analysis/')
import pca
import preprocessing

class RG_EnoseApp(QtGui.QMainWindow, RG_Enose_GUI.Ui_MainWindow):

    def __init__(self):
        """Constructor"""

        super(self.__class__, self).__init__()
        self.setupUi(self)

        config = ConfigParser.ConfigParser()
        config.read("config.ini")

        self.n_components = int(config.get("Parameters", 
                                           "n_components"))
        
        self.preprocessingComboBox.addItems(config.get(
            "Preprocessing", "Options").split("\n"))
        self.preprocessingComboBox.currentIndexChanged.connect(
            lambda: self.do_preprocessing(
            self.preprocessingComboBox.currentIndex()))
        self.preprocessingComboBox.setEnabled(False)

        self.normalizationComboBox.addItems(config.get(
            "Normalization", "Options").split("\n"))
        self.normalizationComboBox.currentIndexChanged.connect(
            lambda: self.do_normalization(
            self.normalizationComboBox.currentIndex()))
        self.normalizationComboBox.setEnabled(False)

        self.statisticalAnalysisComboBox.addItems(config.get(
            "Statistical Analysis", "Options").split("\n"))
        self.statisticalAnalysisComboBox.currentIndexChanged.connect(
            lambda: self.do_statisticalAnalysis(
            self.statisticalAnalysisComboBox.currentIndex()))
        self.statisticalAnalysisComboBox.setEnabled(False)

        self.sVMComboBox.addItems(config.get(
            "SVM", "Options").split("\n"))
        self.sVMComboBox.setEnabled(False)

        self.neuralNetworkComboBox.addItems(config.get(
            "Neural Network", "Options").split("\n"))
        self.neuralNetworkComboBox.setEnabled(False)

        self.dataSelectionComboBox.addItems(config.get(
            "Data selection", "Options").split("\n"))
        self.dataSelectionComboBox.setEnabled(False)

        self.sVMSelectionComboBox.addItems(config.get(
            "SVM selection", "Options").split("\n"))
        self.sVMSelectionComboBox.setEnabled(False)

        self.actionLoad.triggered.connect(self.open_what)
        self.buttonBox.button(QtGui.QDialogButtonBox.Reset
            ).clicked.connect(self.load_data)

    def open_what(self):
            self.directory = str(QtGui.QFileDialog.getExistingDirectory(self, 'Open', '~'))
            self.load_data()

    def load_data(self):

        data_temp = []
        for filename in sorted(glob.glob(os.path.join(
        self.directory, '*.txt'))):
            with open(filename, "rb") as data_file:
                data_temp.append([line.split() for line in data_file])

        self.data = numpy.hstack(data_temp).astype('float')
        self.preprocessingComboBox.setCurrentIndex(0)
        self.preprocessingComboBox.setEnabled(True)
        self.normalizationComboBox.setCurrentIndex(0)
        self.normalizationComboBox.setEnabled(True)
        self.statisticalAnalysisComboBox.setCurrentIndex(0)
        self.statisticalAnalysisComboBox.setEnabled(True)

    def do_preprocessing(self, index):

        if index:
            self.data = preprocessing.parameters(
                        self.data, index, self.n_components)
            self.preprocessingComboBox.setEnabled(False)

        print(self.data)

    def do_normalization(self, index):

        if index:
            self.data = preprocessing.normalize(
                        self.data, index)
            self.normalizationComboBox.setEnabled(False)

    def do_statisticalAnalysis(self, index):

        if index:
            if self.preprocessingComboBox.isEnabled():
                self.preprocessingComboBox.setCurrentIndex(1)
            if self.normalizationComboBox.isEnabled():
                self.normalizationComboBox.setCurrentIndex(3)
            if index == 1:
                [self.scores, self.loads, self.ssq, self.res, self.q,
                self.tsq, self.tsqs] = pca.pca(self.data, 5)
            self.statisticalAnalysisComboBox.setEnabled(False)



def main():
    app = QtGui.QApplication(sys.argv)
    form = RG_EnoseApp()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()

