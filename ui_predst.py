# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'predst.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(663, 435)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(99999, 99999))
        MainWindow.setBaseSize(QSize(0, 0))
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"/*QLabel {\n"
"font-size: 20px;\n"
"font-family: consolas;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LeftMenu = QWidget(self.centralwidget)
        self.LeftMenu.setObjectName(u"LeftMenu")
        self.verticalLayout = QVBoxLayout(self.LeftMenu)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.load_file_button = QPushButton(self.LeftMenu)
        self.load_file_button.setObjectName(u"load_file_button")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.load_file_button.sizePolicy().hasHeightForWidth())
        self.load_file_button.setSizePolicy(sizePolicy)
        self.load_file_button.setMinimumSize(QSize(0, 50))
        self.load_file_button.setMaximumSize(QSize(99999, 70))

        self.verticalLayout.addWidget(self.load_file_button)

        self.chosen_catalog_label = QLabel(self.LeftMenu)
        self.chosen_catalog_label.setObjectName(u"chosen_catalog_label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.chosen_catalog_label.sizePolicy().hasHeightForWidth())
        self.chosen_catalog_label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Bahnschrift Condensed"])
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferDefault)
        self.chosen_catalog_label.setFont(font)
        self.chosen_catalog_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.chosen_catalog_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.chosen_catalog_label)

        self.frame = QFrame(self.LeftMenu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.Mag_column_label = QLabel(self.frame)
        self.Mag_column_label.setObjectName(u"Mag_column_label")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Mag_column_label.sizePolicy().hasHeightForWidth())
        self.Mag_column_label.setSizePolicy(sizePolicy2)

        self.horizontalLayout_2.addWidget(self.Mag_column_label)

        self.Mag_column_lineedit = QLineEdit(self.frame)
        self.Mag_column_lineedit.setObjectName(u"Mag_column_lineedit")
        self.Mag_column_lineedit.setEnabled(True)
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.Mag_column_lineedit.sizePolicy().hasHeightForWidth())
        self.Mag_column_lineedit.setSizePolicy(sizePolicy3)
        self.Mag_column_lineedit.setMaxLength(32762)
        self.Mag_column_lineedit.setClearButtonEnabled(False)

        self.horizontalLayout_2.addWidget(self.Mag_column_lineedit)


        self.verticalLayout.addWidget(self.frame, 0, Qt.AlignLeft)

        self.available_sheets_label = QLabel(self.LeftMenu)
        self.available_sheets_label.setObjectName(u"available_sheets_label")
        self.available_sheets_label.setEnabled(True)
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.available_sheets_label.sizePolicy().hasHeightForWidth())
        self.available_sheets_label.setSizePolicy(sizePolicy4)
        font1 = QFont()
        font1.setFamilies([u"Consolas"])
        font1.setPointSize(10)
        font1.setBold(False)
        self.available_sheets_label.setFont(font1)
        self.available_sheets_label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.available_sheets_label)

        self.sheets_layout = QVBoxLayout()
        self.sheets_layout.setObjectName(u"sheets_layout")

        self.verticalLayout.addLayout(self.sheets_layout)


        self.horizontalLayout.addWidget(self.LeftMenu, 0, Qt.AlignTop)

        self.RightMenu = QWidget(self.centralwidget)
        self.RightMenu.setObjectName(u"RightMenu")
        self.RightMenuLayout = QVBoxLayout(self.RightMenu)
        self.RightMenuLayout.setSpacing(5)
        self.RightMenuLayout.setObjectName(u"RightMenuLayout")
        self.RightMenuLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.RightMenuLayout.setContentsMargins(1, -1, 1, 1)
        self.chosen_sheet_status = QLabel(self.RightMenu)
        self.chosen_sheet_status.setObjectName(u"chosen_sheet_status")
        self.chosen_sheet_status.setEnabled(True)
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Ignored)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.chosen_sheet_status.sizePolicy().hasHeightForWidth())
        self.chosen_sheet_status.setSizePolicy(sizePolicy5)
        self.chosen_sheet_status.setMinimumSize(QSize(0, 0))
        self.chosen_sheet_status.setMaximumSize(QSize(16777215, 23))
        font2 = QFont()
        font2.setFamilies([u"consolas"])
        font2.setPointSize(6)
        self.chosen_sheet_status.setFont(font2)
        self.chosen_sheet_status.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.chosen_sheet_status.setWordWrap(True)

        self.RightMenuLayout.addWidget(self.chosen_sheet_status)

        self.show_graph_button = QPushButton(self.RightMenu)
        self.show_graph_button.setObjectName(u"show_graph_button")
        self.show_graph_button.setEnabled(False)
        sizePolicy6 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.show_graph_button.sizePolicy().hasHeightForWidth())
        self.show_graph_button.setSizePolicy(sizePolicy6)
        self.show_graph_button.setAutoRepeatDelay(300)

        self.RightMenuLayout.addWidget(self.show_graph_button, 0, Qt.AlignTop)

        self.show_mc_on_graph_checkbox = QCheckBox(self.RightMenu)
        self.show_mc_on_graph_checkbox.setObjectName(u"show_mc_on_graph_checkbox")
        self.show_mc_on_graph_checkbox.setEnabled(False)
        self.show_mc_on_graph_checkbox.setChecked(True)

        self.RightMenuLayout.addWidget(self.show_mc_on_graph_checkbox)

        self.calculate_all_methods_button = QPushButton(self.RightMenu)
        self.calculate_all_methods_button.setObjectName(u"calculate_all_methods_button")
        self.calculate_all_methods_button.setEnabled(False)

        self.RightMenuLayout.addWidget(self.calculate_all_methods_button)

        self.methods_form = QWidget(self.RightMenu)
        self.methods_form.setObjectName(u"methods_form")
        self.methods_formLayout = QFormLayout(self.methods_form)
        self.methods_formLayout.setObjectName(u"methods_formLayout")
        self.calculate_maxc_button = QPushButton(self.methods_form)
        self.calculate_maxc_button.setObjectName(u"calculate_maxc_button")
        self.calculate_maxc_button.setEnabled(False)

        self.methods_formLayout.setWidget(0, QFormLayout.LabelRole, self.calculate_maxc_button)

        self.calculate_maxc_label = QLabel(self.methods_form)
        self.calculate_maxc_label.setObjectName(u"calculate_maxc_label")

        self.methods_formLayout.setWidget(0, QFormLayout.FieldRole, self.calculate_maxc_label)

        self.calculate_gft_button = QPushButton(self.methods_form)
        self.calculate_gft_button.setObjectName(u"calculate_gft_button")
        self.calculate_gft_button.setEnabled(False)

        self.methods_formLayout.setWidget(1, QFormLayout.LabelRole, self.calculate_gft_button)

        self.calculate_gft_label = QLabel(self.methods_form)
        self.calculate_gft_label.setObjectName(u"calculate_gft_label")

        self.methods_formLayout.setWidget(1, QFormLayout.FieldRole, self.calculate_gft_label)

        self.calculate_lls_button = QPushButton(self.methods_form)
        self.calculate_lls_button.setObjectName(u"calculate_lls_button")
        self.calculate_lls_button.setEnabled(False)

        self.methods_formLayout.setWidget(2, QFormLayout.LabelRole, self.calculate_lls_button)

        self.calculate_lls_label = QLabel(self.methods_form)
        self.calculate_lls_label.setObjectName(u"calculate_lls_label")

        self.methods_formLayout.setWidget(2, QFormLayout.FieldRole, self.calculate_lls_label)

        self.calculate_emr_button = QPushButton(self.methods_form)
        self.calculate_emr_button.setObjectName(u"calculate_emr_button")
        self.calculate_emr_button.setEnabled(False)

        self.methods_formLayout.setWidget(3, QFormLayout.LabelRole, self.calculate_emr_button)

        self.calculate_emr_label = QLabel(self.methods_form)
        self.calculate_emr_label.setObjectName(u"calculate_emr_label")

        self.methods_formLayout.setWidget(3, QFormLayout.FieldRole, self.calculate_emr_label)


        self.RightMenuLayout.addWidget(self.methods_form)


        self.horizontalLayout.addWidget(self.RightMenu, 0, Qt.AlignTop)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 663, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.load_file_button.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043a\u0430\u0442\u0430\u043b\u043e\u0433", None))
        self.chosen_catalog_label.setText(QCoreApplication.translate("MainWindow", u"\u041a\u0430\u0442\u0430\u043b\u043e\u0433 \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.Mag_column_label.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0442\u043e\u043b\u0431\u0435\u0446 \u043c\u0430\u0433\u043d\u0438\u0442\u0443\u0434", None))
        self.Mag_column_lineedit.setText(QCoreApplication.translate("MainWindow", u"ML", None))
        self.available_sheets_label.setText("")
        self.chosen_sheet_status.setText("")
        self.show_graph_button.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0438\u0441\u0443\u043d\u043e\u043a", None))
        self.show_mc_on_graph_checkbox.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u043d\u0430 \u0440\u0438\u0441\u0443\u043d\u043a\u0435 \u043f\u043e\u0441\u0447\u0438\u0442\u0430\u043d\u043d\u044b\u0435 Mc", None))
        self.calculate_all_methods_button.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0447\u0438\u0442\u0430\u0442\u044c \u0432\u0441\u0435\u043c\u0438 \u0441\u043f\u043e\u0441\u043e\u0431\u0430\u043c\u0438", None))
        self.calculate_maxc_button.setText(QCoreApplication.translate("MainWindow", u"MAXC", None))
        self.calculate_maxc_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.calculate_gft_button.setText(QCoreApplication.translate("MainWindow", u"GFT", None))
        self.calculate_gft_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.calculate_lls_button.setText(QCoreApplication.translate("MainWindow", u"LLS", None))
        self.calculate_lls_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.calculate_emr_button.setText(QCoreApplication.translate("MainWindow", u"EMR", None))
        self.calculate_emr_label.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

