# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Rainer\PycharmProjects\Akuvet2020\ui\main.ui.old.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1749, 1242)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 1172, 20, 20))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(1370, 200, 77, 214))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainMenuBtn1 = QtWidgets.QPushButton(self.layoutWidget)
        self.mainMenuBtn1.setObjectName("mainMenuBtn1")
        self.verticalLayout.addWidget(self.mainMenuBtn1)
        self.mainMenuBtn2 = QtWidgets.QPushButton(self.layoutWidget)
        self.mainMenuBtn2.setObjectName("mainMenuBtn2")
        self.verticalLayout.addWidget(self.mainMenuBtn2)
        self.mainMenuBtn3 = QtWidgets.QPushButton(self.layoutWidget)
        self.mainMenuBtn3.setObjectName("mainMenuBtn3")
        self.verticalLayout.addWidget(self.mainMenuBtn3)
        self.mainMenuBtn4 = QtWidgets.QPushButton(self.layoutWidget)
        self.mainMenuBtn4.setObjectName("mainMenuBtn4")
        self.verticalLayout.addWidget(self.mainMenuBtn4)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.apptitle = QtWidgets.QLabel(self.centralwidget)
        self.apptitle.setGeometry(QtCore.QRect(250, 10, 511, 81))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(60)
        self.apptitle.setFont(font)
        self.apptitle.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.apptitle.setObjectName("apptitle")
        self.twkunden = QtWidgets.QTableWidget(self.centralwidget)
        self.twkunden.setGeometry(QtCore.QRect(780, 350, 256, 564))
        self.twkunden.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.twkunden.setAlternatingRowColors(False)
        self.twkunden.setGridStyle(QtCore.Qt.DashLine)
        self.twkunden.setObjectName("twkunden")
        self.twkunden.setColumnCount(0)
        self.twkunden.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1749, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.searchDW = QtWidgets.QDockWidget(MainWindow)
        self.searchDW.setObjectName("searchDW")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tw1 = QtWidgets.QTableWidget(self.dockWidgetContents_2)
        self.tw1.setObjectName("tw1")
        self.tw1.setColumnCount(0)
        self.tw1.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tw1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.label = QtWidgets.QLabel(self.dockWidgetContents_2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.le_searchfield = QtWidgets.QLineEdit(self.dockWidgetContents_2)
        self.le_searchfield.setObjectName("le_searchfield")
        self.horizontalLayout.addWidget(self.le_searchfield)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.searchDW.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.searchDW)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.mainMenuBtn1.setText(_translate("MainWindow", "Praxisdaten"))
        self.mainMenuBtn2.setText(_translate("MainWindow", "Kundenkartei"))
        self.mainMenuBtn3.setText(_translate("MainWindow", "Tiere"))
        self.mainMenuBtn4.setText(_translate("MainWindow", "Grunddaten"))
        self.apptitle.setText(_translate("MainWindow", "Akuvet 2020"))
        self.twkunden.setSortingEnabled(True)
        self.label.setText(_translate("MainWindow", "Suche:"))
from . import akuvet_rc
