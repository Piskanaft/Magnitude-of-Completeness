import sys
import os.path
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import uic
import pandas as pd
from functools import partial

import Predst_func_forGUI as MC

MyWindow, base_class = uic.loadUiType('./GUI/predst.ui')
class MainWindow(base_class):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.ui = MyWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Представительная магнитуда')
        self.show()

        self.ui.load_file_button.clicked.connect(self.load_catalog)
        self.ui.calculate_all_methods_button.clicked.connect(lambda: self.clicked_methods('maxcgftlls'))
        self.ui.calculate_maxc_button.clicked.connect(lambda: self.clicked_methods('maxc'))
        self.ui.calculate_gft_button.clicked.connect(lambda: self.clicked_methods('gft'))
        self.ui.calculate_lls_button.clicked.connect(lambda: self.clicked_methods('lls'))
        self.ui.show_graph_button.clicked.connect(lambda: MC.draw(self.mag_values,self.discrete_counts,self.cumulative_counts))

    def load_catalog(self):
        
        file_path = qtw.QFileDialog.getOpenFileName(self, 'Open File')
        if file_path[0]:
            file_name = os.path.basename(file_path[0])
            self.ui.chosen_catalog_label.setText('Выбранный каталог: ' + file_name)
        self.chosen_catalog_path = file_path[0]
        self.add_available_sheets()
    
    def add_available_sheets(self):
        available_sheets = pd.ExcelFile(self.chosen_catalog_path).sheet_names
        for sheet in available_sheets:
            self.ui.sheets_layout.addWidget(qtw.QPushButton(str(sheet)))
        
        items = [self.ui.sheets_layout.itemAt(i) for i in range(self.ui.sheets_layout.count())]

        for i,layout_element in enumerate(items):
            widget = layout_element.widget()
            widget.clicked.connect(partial(self.clicked_chosen_sheet, i))
        
    def clicked_chosen_sheet(self,index):
        # if not hasattr(self, 'mag'):
        print('dont have')
        self.mag = MC.simple_read(self.chosen_catalog_path,index, 'ML')
        self.mag_values,self.discrete_counts,self.cumulative_counts = MC.calculate(self.mag)
        print(self.mag)
        
        
    def clicked_methods(self,method):
        
        if 'maxc' in method:
            M_MAXC = MC.MAXC(self.mag_values,self.discrete_counts)
            self.ui.calculate_maxc_label.setText(str(M_MAXC))
        if 'gft' in method:
            M_GFT = MC.Goodness_of_fit(self.mag,self.mag_values,self.discrete_counts,self.cumulative_counts)
            self.ui.calculate_gft_label.setText(str(M_GFT))
        if 'lls' in method:
            M_LLS = MC.LLS(self.mag,self.mag_values)
            self.ui.calculate_lls_label.setText(str(M_LLS))
        


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())