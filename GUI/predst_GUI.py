import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import uic

import Predst_func_forGUI as MC

MyWindow, base_class = uic.loadUiType('./predst.ui')
class MainWindow(base_class):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.ui = MyWindow()
        self.ui.setupUi(self)
        self.show()

        self.ui.load_file_button.clicked.connect(self.choose_file)
        self.ui.calculate_maxc_button.clicked.connect(self.clicked_maxc)

    def choose_file(self):
        #TODO sheet chosing
        print('clicked')
        file_name = qtw.QFileDialog.getOpenFileName(self, 'Open File')
        if file_name[0]:
            self.ui.choosen_catalog_label.setText(file_name[0])
        self.chosen_catalog_url = file_name[0]


        
    def clicked_maxc(self):
        if not hasattr(self, 'mag'):
            print('dont have')
            self.mag = MC.simple_read(self.chosen_catalog_url, 'ML')
            self.mag_values,self.discrete_counts,self.cumulative_counts = MC.calculate(self.mag)
        
        M_MAXC = MC.MAXC(self.mag_values,self.discrete_counts)
        self.ui.calculate_maxc_label.setText(str(M_MAXC))
        


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())