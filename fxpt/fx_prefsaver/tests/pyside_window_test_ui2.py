# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt_window_test_ui.ui'
#
# Created: Sat Nov 19 01:35:15 2016
#      by: pyside2-uic  running on PySide2 2.0.0~alpha0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(962, 771)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.uiSPL_test1 = QtWidgets.QSplitter(self.centralwidget)
        self.uiSPL_test1.setOrientation(QtCore.Qt.Horizontal)
        self.uiSPL_test1.setHandleWidth(10)
        self.uiSPL_test1.setObjectName("uiSPL_test1")
        self.layoutWidget = QtWidgets.QWidget(self.uiSPL_test1)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiCHK_test1 = QtWidgets.QCheckBox(self.layoutWidget)
        self.uiCHK_test1.setObjectName("uiCHK_test1")
        self.verticalLayout.addWidget(self.uiCHK_test1)
        self.uiCHK_testTri1 = QtWidgets.QCheckBox(self.layoutWidget)
        self.uiCHK_testTri1.setTristate(True)
        self.uiCHK_testTri1.setObjectName("uiCHK_testTri1")
        self.verticalLayout.addWidget(self.uiCHK_testTri1)
        self.uiGRPBOX_test1 = QtWidgets.QGroupBox(self.layoutWidget)
        self.uiGRPBOX_test1.setCheckable(True)
        self.uiGRPBOX_test1.setChecked(True)
        self.uiGRPBOX_test1.setObjectName("uiGRPBOX_test1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.uiGRPBOX_test1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiRAD_test1 = QtWidgets.QRadioButton(self.uiGRPBOX_test1)
        self.uiRAD_test1.setObjectName("uiRAD_test1")
        self.horizontalLayout.addWidget(self.uiRAD_test1)
        self.uiRAD_test2 = QtWidgets.QRadioButton(self.uiGRPBOX_test1)
        self.uiRAD_test2.setObjectName("uiRAD_test2")
        self.horizontalLayout.addWidget(self.uiRAD_test2)
        self.verticalLayout.addWidget(self.uiGRPBOX_test1)
        self.uiLED_test1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.uiLED_test1.setObjectName("uiLED_test1")
        self.verticalLayout.addWidget(self.uiLED_test1)
        self.uiSPN_test1 = QtWidgets.QSpinBox(self.layoutWidget)
        self.uiSPN_test1.setObjectName("uiSPN_test1")
        self.verticalLayout.addWidget(self.uiSPN_test1)
        self.uiSPNDBL_test1 = QtWidgets.QDoubleSpinBox(self.layoutWidget)
        self.uiSPNDBL_test1.setObjectName("uiSPNDBL_test1")
        self.verticalLayout.addWidget(self.uiSPNDBL_test1)
        self.uiTIMEDT_test1 = QtWidgets.QTimeEdit(self.layoutWidget)
        self.uiTIMEDT_test1.setObjectName("uiTIMEDT_test1")
        self.verticalLayout.addWidget(self.uiTIMEDT_test1)
        self.uiDATEDT_test1 = QtWidgets.QDateEdit(self.layoutWidget)
        self.uiDATEDT_test1.setObjectName("uiDATEDT_test1")
        self.verticalLayout.addWidget(self.uiDATEDT_test1)
        self.uiDTEDIT_test1 = QtWidgets.QDateTimeEdit(self.layoutWidget)
        self.uiDTEDIT_test1.setObjectName("uiDTEDIT_test1")
        self.verticalLayout.addWidget(self.uiDTEDIT_test1)
        self.uiBTN_test1 = QtWidgets.QPushButton(self.layoutWidget)
        self.uiBTN_test1.setCheckable(True)
        self.uiBTN_test1.setObjectName("uiBTN_test1")
        self.verticalLayout.addWidget(self.uiBTN_test1)
        self.uiCBX_test1 = QtWidgets.QComboBox(self.layoutWidget)
        self.uiCBX_test1.setObjectName("uiCBX_test1")
        self.uiCBX_test1.addItem("")
        self.uiCBX_test1.addItem("")
        self.uiCBX_test1.addItem("")
        self.uiCBX_test1.addItem("")
        self.uiCBX_test1.addItem("")
        self.uiCBX_test1.addItem("")
        self.uiCBX_test1.addItem("")
        self.verticalLayout.addWidget(self.uiCBX_test1)
        self.uiCBX_test2 = QtWidgets.QComboBox(self.layoutWidget)
        self.uiCBX_test2.setEditable(True)
        self.uiCBX_test2.setObjectName("uiCBX_test2")
        self.verticalLayout.addWidget(self.uiCBX_test2)
        self.uiSCR_test1 = QtWidgets.QScrollBar(self.layoutWidget)
        self.uiSCR_test1.setOrientation(QtCore.Qt.Horizontal)
        self.uiSCR_test1.setObjectName("uiSCR_test1")
        self.verticalLayout.addWidget(self.uiSCR_test1)
        self.uiSLD_test1 = QtWidgets.QSlider(self.layoutWidget)
        self.uiSLD_test1.setOrientation(QtCore.Qt.Horizontal)
        self.uiSLD_test1.setObjectName("uiSLD_test1")
        self.verticalLayout.addWidget(self.uiSLD_test1)
        self.uiDIA_test1 = QtWidgets.QDial(self.layoutWidget)
        self.uiDIA_test1.setObjectName("uiDIA_test1")
        self.verticalLayout.addWidget(self.uiDIA_test1)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_15.addWidget(self.label_4)
        self.uiLED_testVariable1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.uiLED_testVariable1.setObjectName("uiLED_testVariable1")
        self.horizontalLayout_15.addWidget(self.uiLED_testVariable1)
        self.verticalLayout.addLayout(self.horizontalLayout_15)
        self.uiBTN_showDialog = QtWidgets.QPushButton(self.layoutWidget)
        self.uiBTN_showDialog.setObjectName("uiBTN_showDialog")
        self.verticalLayout.addWidget(self.uiBTN_showDialog)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.uiTAB_test1 = QtWidgets.QTabWidget(self.uiSPL_test1)
        self.uiTAB_test1.setObjectName("uiTAB_test1")
        self.uiTABPG_listWidget = QtWidgets.QWidget()
        self.uiTABPG_listWidget.setObjectName("uiTABPG_listWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.uiTABPG_listWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uiLSTWID_test1 = QtWidgets.QListWidget(self.uiTABPG_listWidget)
        self.uiLSTWID_test1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.uiLSTWID_test1.setObjectName("uiLSTWID_test1")
        QtWidgets.QListWidgetItem(self.uiLSTWID_test1)
        QtWidgets.QListWidgetItem(self.uiLSTWID_test1)
        QtWidgets.QListWidgetItem(self.uiLSTWID_test1)
        QtWidgets.QListWidgetItem(self.uiLSTWID_test1)
        QtWidgets.QListWidgetItem(self.uiLSTWID_test1)
        QtWidgets.QListWidgetItem(self.uiLSTWID_test1)
        QtWidgets.QListWidgetItem(self.uiLSTWID_test1)
        self.horizontalLayout_2.addWidget(self.uiLSTWID_test1)
        self.uiTAB_test1.addTab(self.uiTABPG_listWidget, "")
        self.uiTABPG_treeWidget = QtWidgets.QWidget()
        self.uiTABPG_treeWidget.setObjectName("uiTABPG_treeWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.uiTABPG_treeWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.uiTREW_test1 = QtWidgets.QTreeWidget(self.uiTABPG_treeWidget)
        self.uiTREW_test1.setAlternatingRowColors(True)
        self.uiTREW_test1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.uiTREW_test1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.uiTREW_test1.setObjectName("uiTREW_test1")
        item_0 = QtWidgets.QTreeWidgetItem(self.uiTREW_test1)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiTREW_test1)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiTREW_test1)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiTREW_test1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiTREW_test1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_0 = QtWidgets.QTreeWidgetItem(self.uiTREW_test1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        self.uiTREW_test1.header().setDefaultSectionSize(200)
        self.uiTREW_test1.header().setMinimumSectionSize(200)
        self.uiTREW_test1.header().setSortIndicatorShown(True)
        self.horizontalLayout_3.addWidget(self.uiTREW_test1)
        self.uiTAB_test1.addTab(self.uiTABPG_treeWidget, "")
        self.uiTABPG_tableWidget = QtWidgets.QWidget()
        self.uiTABPG_tableWidget.setObjectName("uiTABPG_tableWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.uiTABPG_tableWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.uiTBLWID_test1 = QtWidgets.QTableWidget(self.uiTABPG_tableWidget)
        self.uiTBLWID_test1.setObjectName("uiTBLWID_test1")
        self.uiTBLWID_test1.setColumnCount(2)
        self.uiTBLWID_test1.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(3, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(4, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(4, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(5, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(5, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(6, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.uiTBLWID_test1.setItem(6, 1, item)
        self.uiTBLWID_test1.horizontalHeader().setSortIndicatorShown(True)
        self.horizontalLayout_4.addWidget(self.uiTBLWID_test1)
        self.uiTAB_test1.addTab(self.uiTABPG_tableWidget, "")
        self.uiTABPG_listView = QtWidgets.QWidget()
        self.uiTABPG_listView.setObjectName("uiTABPG_listView")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.uiTABPG_listView)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.uiLSTV_test1 = QtWidgets.QListView(self.uiTABPG_listView)
        self.uiLSTV_test1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.uiLSTV_test1.setObjectName("uiLSTV_test1")
        self.horizontalLayout_7.addWidget(self.uiLSTV_test1)
        self.uiTAB_test1.addTab(self.uiTABPG_listView, "")
        self.uiTABPG_treeView = QtWidgets.QWidget()
        self.uiTABPG_treeView.setObjectName("uiTABPG_treeView")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.uiTABPG_treeView)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.uiTREV_test1 = QtWidgets.QTreeView(self.uiTABPG_treeView)
        self.uiTREV_test1.setAlternatingRowColors(True)
        self.uiTREV_test1.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.uiTREV_test1.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.uiTREV_test1.setSortingEnabled(True)
        self.uiTREV_test1.setObjectName("uiTREV_test1")
        self.uiTREV_test1.header().setDefaultSectionSize(200)
        self.uiTREV_test1.header().setMinimumSectionSize(200)
        self.uiTREV_test1.header().setSortIndicatorShown(True)
        self.horizontalLayout_8.addWidget(self.uiTREV_test1)
        self.uiTAB_test1.addTab(self.uiTABPG_treeView, "")
        self.uiTABPG_tableView = QtWidgets.QWidget()
        self.uiTABPG_tableView.setObjectName("uiTABPG_tableView")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.uiTABPG_tableView)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.uiTBLV_test1 = QtWidgets.QTableView(self.uiTABPG_tableView)
        self.uiTBLV_test1.setSortingEnabled(True)
        self.uiTBLV_test1.setObjectName("uiTBLV_test1")
        self.uiTBLV_test1.horizontalHeader().setSortIndicatorShown(True)
        self.horizontalLayout_10.addWidget(self.uiTBLV_test1)
        self.uiTAB_test1.addTab(self.uiTABPG_tableView, "")
        self.uiTABPG_columnView = QtWidgets.QWidget()
        self.uiTABPG_columnView.setObjectName("uiTABPG_columnView")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.uiTABPG_columnView)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.uiCOLV_test1 = QtWidgets.QColumnView(self.uiTABPG_columnView)
        self.uiCOLV_test1.setObjectName("uiCOLV_test1")
        self.horizontalLayout_9.addWidget(self.uiCOLV_test1)
        self.uiTAB_test1.addTab(self.uiTABPG_columnView, "")
        self.uiTABPG_scrollText = QtWidgets.QWidget()
        self.uiTABPG_scrollText.setObjectName("uiTABPG_scrollText")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.uiTABPG_scrollText)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.uiSCA_test1 = QtWidgets.QScrollArea(self.uiTABPG_scrollText)
        self.uiSCA_test1.setWidgetResizable(True)
        self.uiSCA_test1.setObjectName("uiSCA_test1")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 634, 676))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.uiTXTEDT_test1 = QtWidgets.QTextEdit(self.scrollAreaWidgetContents)
        self.uiTXTEDT_test1.setMinimumSize(QtCore.QSize(300, 600))
        self.uiTXTEDT_test1.setObjectName("uiTXTEDT_test1")
        self.horizontalLayout_11.addWidget(self.uiTXTEDT_test1)
        self.uiPTXEDT_test1 = QtWidgets.QPlainTextEdit(self.scrollAreaWidgetContents)
        self.uiPTXEDT_test1.setMinimumSize(QtCore.QSize(300, 600))
        self.uiPTXEDT_test1.setObjectName("uiPTXEDT_test1")
        self.horizontalLayout_11.addWidget(self.uiPTXEDT_test1)
        self.uiSCA_test1.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.addWidget(self.uiSCA_test1)
        self.uiTAB_test1.addTab(self.uiTABPG_scrollText, "")
        self.uiTABPG_stackTool = QtWidgets.QWidget()
        self.uiTABPG_stackTool.setObjectName("uiTABPG_stackTool")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.uiTABPG_stackTool)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setContentsMargins(4, 6, 4, 4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem1)
        self.uiBTN_stackDec = QtWidgets.QPushButton(self.uiTABPG_stackTool)
        self.uiBTN_stackDec.setObjectName("uiBTN_stackDec")
        self.horizontalLayout_12.addWidget(self.uiBTN_stackDec)
        self.uiBTN_stackInc = QtWidgets.QPushButton(self.uiTABPG_stackTool)
        self.uiBTN_stackInc.setObjectName("uiBTN_stackInc")
        self.horizontalLayout_12.addWidget(self.uiBTN_stackInc)
        self.verticalLayout_6.addLayout(self.horizontalLayout_12)
        self.uiSTK_test1 = QtWidgets.QStackedWidget(self.uiTABPG_stackTool)
        self.uiSTK_test1.setObjectName("uiSTK_test1")
        self.page0 = QtWidgets.QWidget()
        self.page0.setObjectName("page0")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.page0)
        self.horizontalLayout_14.setSpacing(0)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.page0)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.uiTBX_test1 = QtWidgets.QToolBox(self.page0)
        self.uiTBX_test1.setObjectName("uiTBX_test1")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.page.setObjectName("page")
        self.uiTBX_test1.addItem(self.page, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.page_2.setObjectName("page_2")
        self.uiTBX_test1.addItem(self.page_2, "")
        self.page_5 = QtWidgets.QWidget()
        self.page_5.setGeometry(QtCore.QRect(0, 0, 318, 557))
        self.page_5.setObjectName("page_5")
        self.uiTBX_test1.addItem(self.page_5, "")
        self.horizontalLayout_13.addWidget(self.uiTBX_test1)
        self.uiTBX_test2 = QtWidgets.QToolBox(self.page0)
        self.uiTBX_test2.setObjectName("uiTBX_test2")
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.page_3.setObjectName("page_3")
        self.uiTBX_test2.addItem(self.page_3, "")
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setGeometry(QtCore.QRect(0, 0, 98, 28))
        self.page_4.setObjectName("page_4")
        self.uiTBX_test2.addItem(self.page_4, "")
        self.page_6 = QtWidgets.QWidget()
        self.page_6.setGeometry(QtCore.QRect(0, 0, 318, 557))
        self.page_6.setObjectName("page_6")
        self.uiTBX_test2.addItem(self.page_6, "")
        self.horizontalLayout_13.addWidget(self.uiTBX_test2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_14.addLayout(self.verticalLayout_3)
        self.uiSTK_test1.addWidget(self.page0)
        self.page1 = QtWidgets.QWidget()
        self.page1.setObjectName("page1")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.page1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.page1)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.uiSTK_test1.addWidget(self.page1)
        self.page2 = QtWidgets.QWidget()
        self.page2.setObjectName("page2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.page2)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.page2)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_5.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.uiSTK_test1.addWidget(self.page2)
        self.verticalLayout_6.addWidget(self.uiSTK_test1)
        self.uiTAB_test1.addTab(self.uiTABPG_stackTool, "")
        self.verticalLayout_2.addWidget(self.uiSPL_test1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.uiBTN_savePrefs = QtWidgets.QPushButton(self.centralwidget)
        self.uiBTN_savePrefs.setObjectName("uiBTN_savePrefs")
        self.horizontalLayout_5.addWidget(self.uiBTN_savePrefs)
        self.uiBTN_loadPrefs = QtWidgets.QPushButton(self.centralwidget)
        self.uiBTN_loadPrefs.setObjectName("uiBTN_loadPrefs")
        self.horizontalLayout_5.addWidget(self.uiBTN_loadPrefs)
        self.uiBTN_resetPrefs = QtWidgets.QPushButton(self.centralwidget)
        self.uiBTN_resetPrefs.setObjectName("uiBTN_resetPrefs")
        self.horizontalLayout_5.addWidget(self.uiBTN_resetPrefs)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.uiTAB_test1.setCurrentIndex(2)
        self.uiSTK_test1.setCurrentIndex(0)
        self.uiTBX_test1.setCurrentIndex(2)
        self.uiTBX_test2.setCurrentIndex(2)
        QtCore.QObject.connect(self.uiBTN_savePrefs, QtCore.SIGNAL("clicked()"), MainWindow.onSavePrefsClicked)
        QtCore.QObject.connect(self.uiBTN_loadPrefs, QtCore.SIGNAL("clicked()"), MainWindow.onLoadPrefsClicked)
        QtCore.QObject.connect(self.uiBTN_resetPrefs, QtCore.SIGNAL("clicked()"), MainWindow.onResetPrefsClicked)
        QtCore.QObject.connect(self.uiBTN_showDialog, QtCore.SIGNAL("clicked()"), MainWindow.onShowDialogClicked)
        QtCore.QObject.connect(self.uiBTN_stackDec, QtCore.SIGNAL("clicked()"), MainWindow.onStackedWidgetPageDec)
        QtCore.QObject.connect(self.uiBTN_stackInc, QtCore.SIGNAL("clicked()"), MainWindow.onStackedWidgetPageInc)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.uiCHK_test1.setText(QtWidgets.QApplication.translate("MainWindow", "CheckBox", None, -1))
        self.uiCHK_testTri1.setText(QtWidgets.QApplication.translate("MainWindow", "TriState CheckBox", None, -1))
        self.uiGRPBOX_test1.setTitle(QtWidgets.QApplication.translate("MainWindow", "GroupBox", None, -1))
        self.uiRAD_test1.setText(QtWidgets.QApplication.translate("MainWindow", "RadioButton1", None, -1))
        self.uiRAD_test2.setText(QtWidgets.QApplication.translate("MainWindow", "RadioButton2", None, -1))
        self.uiBTN_test1.setText(QtWidgets.QApplication.translate("MainWindow", "Check Button", None, -1))
        self.uiCBX_test1.setItemText(0, QtWidgets.QApplication.translate("MainWindow", "Item1", None, -1))
        self.uiCBX_test1.setItemText(1, QtWidgets.QApplication.translate("MainWindow", "Item2", None, -1))
        self.uiCBX_test1.setItemText(2, QtWidgets.QApplication.translate("MainWindow", "Item3", None, -1))
        self.uiCBX_test1.setItemText(3, QtWidgets.QApplication.translate("MainWindow", "Item4", None, -1))
        self.uiCBX_test1.setItemText(4, QtWidgets.QApplication.translate("MainWindow", "Item5", None, -1))
        self.uiCBX_test1.setItemText(5, QtWidgets.QApplication.translate("MainWindow", "Item6", None, -1))
        self.uiCBX_test1.setItemText(6, QtWidgets.QApplication.translate("MainWindow", "Item7", None, -1))
        self.label_4.setText(QtWidgets.QApplication.translate("MainWindow", "Variable:", None, -1))
        self.uiBTN_showDialog.setText(QtWidgets.QApplication.translate("MainWindow", "Show Dialog", None, -1))
        __sortingEnabled = self.uiLSTWID_test1.isSortingEnabled()
        self.uiLSTWID_test1.setSortingEnabled(False)
        self.uiLSTWID_test1.item(0).setText(QtWidgets.QApplication.translate("MainWindow", "Item1", None, -1))
        self.uiLSTWID_test1.item(1).setText(QtWidgets.QApplication.translate("MainWindow", "Item2", None, -1))
        self.uiLSTWID_test1.item(2).setText(QtWidgets.QApplication.translate("MainWindow", "Item3", None, -1))
        self.uiLSTWID_test1.item(3).setText(QtWidgets.QApplication.translate("MainWindow", "Item4", None, -1))
        self.uiLSTWID_test1.item(4).setText(QtWidgets.QApplication.translate("MainWindow", "Item7", None, -1))
        self.uiLSTWID_test1.item(5).setText(QtWidgets.QApplication.translate("MainWindow", "Item6", None, -1))
        self.uiLSTWID_test1.item(6).setText(QtWidgets.QApplication.translate("MainWindow", "Item5", None, -1))
        self.uiLSTWID_test1.setSortingEnabled(__sortingEnabled)
        self.uiTAB_test1.setTabText(self.uiTAB_test1.indexOf(self.uiTABPG_listWidget), QtWidgets.QApplication.translate("MainWindow", "List Widget", None, -1))
        self.uiTREW_test1.setSortingEnabled(True)
        self.uiTREW_test1.headerItem().setText(0, QtWidgets.QApplication.translate("MainWindow", "column1", None, -1))
        self.uiTREW_test1.headerItem().setText(1, QtWidgets.QApplication.translate("MainWindow", "column2", None, -1))
        __sortingEnabled = self.uiTREW_test1.isSortingEnabled()
        self.uiTREW_test1.setSortingEnabled(False)
        self.uiTREW_test1.topLevelItem(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "rootItem3", None, -1))
        self.uiTREW_test1.topLevelItem(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "rootItem2", None, -1))
        self.uiTREW_test1.topLevelItem(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "rootItem1", None, -1))
        self.uiTREW_test1.topLevelItem(3).setText(0, QtWidgets.QApplication.translate("MainWindow", "folder3", None, -1))
        self.uiTREW_test1.topLevelItem(3).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "folder31", None, -1))
        self.uiTREW_test1.topLevelItem(3).child(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "item313", None, -1))
        self.uiTREW_test1.topLevelItem(3).child(0).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "item312", None, -1))
        self.uiTREW_test1.topLevelItem(3).child(0).child(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "item311", None, -1))
        self.uiTREW_test1.topLevelItem(4).setText(0, QtWidgets.QApplication.translate("MainWindow", "folder2", None, -1))
        self.uiTREW_test1.topLevelItem(4).setText(1, QtWidgets.QApplication.translate("MainWindow", "value6", None, -1))
        self.uiTREW_test1.topLevelItem(4).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "folder21", None, -1))
        self.uiTREW_test1.topLevelItem(4).child(0).setText(1, QtWidgets.QApplication.translate("MainWindow", "value7", None, -1))
        self.uiTREW_test1.topLevelItem(4).child(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "item213", None, -1))
        self.uiTREW_test1.topLevelItem(4).child(0).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "item212", None, -1))
        self.uiTREW_test1.topLevelItem(4).child(0).child(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "item211", None, -1))
        self.uiTREW_test1.topLevelItem(4).child(0).child(2).setText(1, QtWidgets.QApplication.translate("MainWindow", "value8", None, -1))
        self.uiTREW_test1.topLevelItem(5).setText(0, QtWidgets.QApplication.translate("MainWindow", "folder1", None, -1))
        self.uiTREW_test1.topLevelItem(5).setText(1, QtWidgets.QApplication.translate("MainWindow", "value1", None, -1))
        self.uiTREW_test1.topLevelItem(5).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "folder11", None, -1))
        self.uiTREW_test1.topLevelItem(5).child(0).setText(1, QtWidgets.QApplication.translate("MainWindow", "value2", None, -1))
        self.uiTREW_test1.topLevelItem(5).child(0).child(0).setText(0, QtWidgets.QApplication.translate("MainWindow", "item113", None, -1))
        self.uiTREW_test1.topLevelItem(5).child(0).child(0).setText(1, QtWidgets.QApplication.translate("MainWindow", "value5", None, -1))
        self.uiTREW_test1.topLevelItem(5).child(0).child(1).setText(0, QtWidgets.QApplication.translate("MainWindow", "item112", None, -1))
        self.uiTREW_test1.topLevelItem(5).child(0).child(1).setText(1, QtWidgets.QApplication.translate("MainWindow", "value4", None, -1))
        self.uiTREW_test1.topLevelItem(5).child(0).child(2).setText(0, QtWidgets.QApplication.translate("MainWindow", "item111", None, -1))
        self.uiTREW_test1.topLevelItem(5).child(0).child(2).setText(1, QtWidgets.QApplication.translate("MainWindow", "value3", None, -1))
        self.uiTREW_test1.setSortingEnabled(__sortingEnabled)
        self.uiTAB_test1.setTabText(self.uiTAB_test1.indexOf(self.uiTABPG_treeWidget), QtWidgets.QApplication.translate("MainWindow", "Tree Widget", None, -1))
        self.uiTBLWID_test1.setSortingEnabled(True)
        self.uiTBLWID_test1.verticalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "Row1", None, -1))
        self.uiTBLWID_test1.verticalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "Row2", None, -1))
        self.uiTBLWID_test1.verticalHeaderItem(2).setText(QtWidgets.QApplication.translate("MainWindow", "Row3", None, -1))
        self.uiTBLWID_test1.verticalHeaderItem(3).setText(QtWidgets.QApplication.translate("MainWindow", "Row4", None, -1))
        self.uiTBLWID_test1.verticalHeaderItem(4).setText(QtWidgets.QApplication.translate("MainWindow", "Row5", None, -1))
        self.uiTBLWID_test1.verticalHeaderItem(5).setText(QtWidgets.QApplication.translate("MainWindow", "Row6", None, -1))
        self.uiTBLWID_test1.verticalHeaderItem(6).setText(QtWidgets.QApplication.translate("MainWindow", "Row7", None, -1))
        self.uiTBLWID_test1.horizontalHeaderItem(0).setText(QtWidgets.QApplication.translate("MainWindow", "Column1", None, -1))
        self.uiTBLWID_test1.horizontalHeaderItem(1).setText(QtWidgets.QApplication.translate("MainWindow", "Column2", None, -1))
        __sortingEnabled = self.uiTBLWID_test1.isSortingEnabled()
        self.uiTBLWID_test1.setSortingEnabled(False)
        self.uiTBLWID_test1.item(0, 0).setText(QtWidgets.QApplication.translate("MainWindow", "value11", None, -1))
        self.uiTBLWID_test1.item(0, 1).setText(QtWidgets.QApplication.translate("MainWindow", "value12", None, -1))
        self.uiTBLWID_test1.item(1, 0).setText(QtWidgets.QApplication.translate("MainWindow", "value61", None, -1))
        self.uiTBLWID_test1.item(1, 1).setText(QtWidgets.QApplication.translate("MainWindow", "value62", None, -1))
        self.uiTBLWID_test1.item(2, 0).setText(QtWidgets.QApplication.translate("MainWindow", "value51", None, -1))
        self.uiTBLWID_test1.item(2, 1).setText(QtWidgets.QApplication.translate("MainWindow", "value52", None, -1))
        self.uiTBLWID_test1.item(3, 0).setText(QtWidgets.QApplication.translate("MainWindow", "value41", None, -1))
        self.uiTBLWID_test1.item(3, 1).setText(QtWidgets.QApplication.translate("MainWindow", "value42", None, -1))
        self.uiTBLWID_test1.item(4, 0).setText(QtWidgets.QApplication.translate("MainWindow", "value31", None, -1))
        self.uiTBLWID_test1.item(4, 1).setText(QtWidgets.QApplication.translate("MainWindow", "value32", None, -1))
        self.uiTBLWID_test1.item(5, 0).setText(QtWidgets.QApplication.translate("MainWindow", "value21", None, -1))
        self.uiTBLWID_test1.item(5, 1).setText(QtWidgets.QApplication.translate("MainWindow", "value22", None, -1))
        self.uiTBLWID_test1.item(6, 0).setText(QtWidgets.QApplication.translate("MainWindow", "value71", None, -1))
        self.uiTBLWID_test1.item(6, 1).setText(QtWidgets.QApplication.translate("MainWindow", "value72", None, -1))
        self.uiTBLWID_test1.setSortingEnabled(__sortingEnabled)
        self.uiTAB_test1.setTabText(self.uiTAB_test1.indexOf(self.uiTABPG_tableWidget), QtWidgets.QApplication.translate("MainWindow", "Table Widget", None, -1))
        self.uiTAB_test1.setTabText(self.uiTAB_test1.indexOf(self.uiTABPG_listView), QtWidgets.QApplication.translate("MainWindow", "List View", None, -1))
        self.uiTAB_test1.setTabText(self.uiTAB_test1.indexOf(self.uiTABPG_treeView), QtWidgets.QApplication.translate("MainWindow", "Tree View", None, -1))
        self.uiTAB_test1.setTabText(self.uiTAB_test1.indexOf(self.uiTABPG_tableView), QtWidgets.QApplication.translate("MainWindow", "Table View", None, -1))
        self.uiTAB_test1.setTabText(self.uiTAB_test1.indexOf(self.uiTABPG_columnView), QtWidgets.QApplication.translate("MainWindow", "Column View", None, -1))
        self.uiTAB_test1.setTabText(self.uiTAB_test1.indexOf(self.uiTABPG_scrollText), QtWidgets.QApplication.translate("MainWindow", "ScrollArea And Text", None, -1))
        self.uiBTN_stackDec.setText(QtWidgets.QApplication.translate("MainWindow", "<<", None, -1))
        self.uiBTN_stackInc.setText(QtWidgets.QApplication.translate("MainWindow", ">>", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "StackedWidget Page 0", None, -1))
        self.uiTBX_test1.setItemText(self.uiTBX_test1.indexOf(self.page), QtWidgets.QApplication.translate("MainWindow", "Page 1", None, -1))
        self.uiTBX_test1.setItemText(self.uiTBX_test1.indexOf(self.page_2), QtWidgets.QApplication.translate("MainWindow", "Page 2", None, -1))
        self.uiTBX_test1.setItemText(self.uiTBX_test1.indexOf(self.page_5), QtWidgets.QApplication.translate("MainWindow", "Page 3", None, -1))
        self.uiTBX_test2.setItemText(self.uiTBX_test2.indexOf(self.page_3), QtWidgets.QApplication.translate("MainWindow", "Page 1", None, -1))
        self.uiTBX_test2.setItemText(self.uiTBX_test2.indexOf(self.page_4), QtWidgets.QApplication.translate("MainWindow", "Page 2", None, -1))
        self.uiTBX_test2.setItemText(self.uiTBX_test2.indexOf(self.page_6), QtWidgets.QApplication.translate("MainWindow", "Page 3", None, -1))
        self.label_2.setText(QtWidgets.QApplication.translate("MainWindow", "StackedWidget Page 1", None, -1))
        self.label_3.setText(QtWidgets.QApplication.translate("MainWindow", "StackedWidget Page 2", None, -1))
        self.uiTAB_test1.setTabText(self.uiTAB_test1.indexOf(self.uiTABPG_stackTool), QtWidgets.QApplication.translate("MainWindow", "Stacked Widget and ToolBox", None, -1))
        self.uiBTN_savePrefs.setText(QtWidgets.QApplication.translate("MainWindow", "Save Prefs", None, -1))
        self.uiBTN_loadPrefs.setText(QtWidgets.QApplication.translate("MainWindow", "Load Prefs", None, -1))
        self.uiBTN_resetPrefs.setText(QtWidgets.QApplication.translate("MainWindow", "Reset Prefs", None, -1))
