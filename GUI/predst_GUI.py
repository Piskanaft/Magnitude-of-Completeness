
import sys
# import sip
import os.path
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from PyQt5 import uic,QtGui
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
        

        self.ui.load_file_button.clicked.connect(self.load_catalog)
        self.ui.calculate_all_methods_button.clicked.connect(lambda: self.clicked_methods('maxcgftllsemr'))
        self.ui.calculate_maxc_button.clicked.connect(lambda: self.clicked_methods('maxc'))
        self.ui.calculate_gft_button.clicked.connect(lambda: self.clicked_methods('gft'))
        self.ui.calculate_lls_button.clicked.connect(lambda: self.clicked_methods('lls'))
        self.ui.calculate_emr_button.clicked.connect(lambda: self.clicked_methods('emr'))

        self.ui.show_graph_button.clicked.connect(self.clicked_show_graph)

        self.ui.Mag_column_label.hide()
        self.ui.Mag_column_lineedit.hide()

        # self.show()
    def load_catalog(self):
        
        file_path = qtw.QFileDialog.getOpenFileName(self, 'Open File',filter="Excel Catalogs (*.xlsx)")
        if not file_path[0]:
            print('passing')
            return None
        
        self.filename_to_open = os.path.basename(file_path[0])
        self.ui.chosen_catalog_label.setText('Выбранный каталог: ' + self.filename_to_open)
        self.chosen_catalog_path = file_path[0]
        self.add_available_sheets()
        self.ui.chosen_sheet_status.setText('Лист не выбран')
        self.ui.available_sheets_label.setText('Доступные листы:')
        self.ui.Mag_column_label.show()
        self.ui.Mag_column_lineedit.show()
    
    def add_available_sheets(self):
        available_sheets = pd.ExcelFile(self.chosen_catalog_path).sheet_names
        #deleting before adding new sheets
        for i in range(self.ui.sheets_layout.count()):
            self.ui.sheets_layout.removeWidget(self.ui.sheets_layout.itemAt(0).widget())
        #adding sheets
        for sheet in available_sheets:
            self.ui.sheets_layout.addWidget(qtw.QPushButton(str(sheet)))
        
        #connecting every sheet button
        items = [self.ui.sheets_layout.itemAt(i) for i in range(self.ui.sheets_layout.count())]
        for i,layout_element in enumerate(items):
            widget = layout_element.widget()
            sheet_name = widget.text()
            widget.clicked.connect(partial(self.clicked_chosen_sheet, i,sheet_name))
        
    def clicked_chosen_sheet(self,index,sheet_name):
        
        column_name = self.ui.Mag_column_lineedit.text()
        try:
            self.mag = MC.simple_read(self.chosen_catalog_path,index, column_name)
        except:
            qtw.QMessageBox.critical(self,'Ошибка',f'Не найден столбец магнитуд {column_name} на листе {sheet_name}')
            return None
        self.chosen_sheet_name = sheet_name
        self.mag_values,self.discrete_counts,self.cumulative_counts = MC.calculate(self.mag)
        for widget in self.ui.RightMenu.findChildren((qtw.QPushButton,qtw.QCheckBox)):
            widget.setEnabled(True)
        self.ui.chosen_sheet_status.setText(f'{sheet_name};{column_name}')
        
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
        if 'emr' in method:
            M_EMR = MC.EMR(self.mag,self.mag_values)
            self.ui.calculate_emr_label.setText(str(M_EMR))
    
    def clicked_show_graph(self):
        
        Mc_MAXC = self.ui.calculate_maxc_label.text()
        Mc_GFT = self.ui.calculate_gft_label.text()
        Mc_LLS = self.ui.calculate_lls_label.text()
        Mc_EMR = self.ui.calculate_emr_label.text()
        lst = [Mc_MAXC,Mc_GFT,Mc_LLS,Mc_EMR]
        for i,Mc in enumerate(lst):
            try:
                Mc = float(Mc)
            except:
                Mc=0
            lst[i] = Mc
        self.Mc_list = lst
        MC.draw(self.mag_values,self.discrete_counts,self.cumulative_counts,mw)
        
        
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    app.setStyleSheet("""
    QLabel {
    font-size: 20px;
    font-family: consolas;
    }
    QCheckBox {
    font-size: 17px;
    font-family: consolas;  
        }""")
    mw = MainWindow()
    
    mw.show()
    sys.exit(app.exec_())