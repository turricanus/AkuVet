# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Benutzer\rainer_holland\Documents\PycharmProjects\AkuVet\ui\main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1797, 1242)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1797, 21))
        self.menubar.setObjectName("menubar")
        self.menuDatei = QtWidgets.QMenu(self.menubar)
        self.menuDatei.setObjectName("menuDatei")
        self.menuBearbeiten = QtWidgets.QMenu(self.menubar)
        self.menuBearbeiten.setObjectName("menuBearbeiten")
        self.menuModule = QtWidgets.QMenu(self.menubar)
        self.menuModule.setObjectName("menuModule")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuHilfe = QtWidgets.QMenu(self.menubar)
        self.menuHilfe.setObjectName("menuHilfe")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.searchDW = QtWidgets.QDockWidget(MainWindow)
        self.searchDW.setMinimumSize(QtCore.QSize(185, 500))
        self.searchDW.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.searchDW.setObjectName("searchDW")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tvKundenAuswahl = QtWidgets.QTableView(self.dockWidgetContents_2)
        self.tvKundenAuswahl.setFrameShape(QtWidgets.QFrame.Box)
        self.tvKundenAuswahl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.tvKundenAuswahl.setLineWidth(2)
        self.tvKundenAuswahl.setObjectName("tvKundenAuswahl")
        self.verticalLayout_2.addWidget(self.tvKundenAuswahl)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.dockWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.le_searchfield = QtWidgets.QLineEdit(self.dockWidgetContents_2)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.le_searchfield.setFont(font)
        self.le_searchfield.setObjectName("le_searchfield")
        self.verticalLayout_2.addWidget(self.le_searchfield)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.searchDW.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.searchDW)
        self.dockWidget = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.praxisdaten = QtWidgets.QWidget(self.dockWidgetContents)
        self.praxisdaten.setObjectName("praxisdaten")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.praxisdaten)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.praxisdaten)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.tb_pg1_la1 = QtWidgets.QLabel(self.splitter_2)
        self.tb_pg1_la1.setObjectName("tb_pg1_la1")
        self.tb_pg1_le1 = QtWidgets.QLineEdit(self.splitter_2)
        self.tb_pg1_le1.setMinimumSize(QtCore.QSize(0, 20))
        self.tb_pg1_le1.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le1.setObjectName("tb_pg1_le1")
        self.horizontalLayout_2.addWidget(self.splitter_2)
        self.splitter_3 = QtWidgets.QSplitter(self.praxisdaten)
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.tb_pg1_la2 = QtWidgets.QLabel(self.splitter_3)
        self.tb_pg1_la2.setObjectName("tb_pg1_la2")
        self.tb_pg1_le2 = QtWidgets.QLineEdit(self.splitter_3)
        self.tb_pg1_le2.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le2.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le2.setObjectName("tb_pg1_le2")
        self.horizontalLayout_2.addWidget(self.splitter_3)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.praxisdaten)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.tb_pg1_la0 = QtWidgets.QLabel(self.splitter)
        self.tb_pg1_la0.setObjectName("tb_pg1_la0")
        self.tb_pg1_le0 = QtWidgets.QLineEdit(self.splitter)
        self.tb_pg1_le0.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le0.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le0.setObjectName("tb_pg1_le0")
        self.gridLayout_2.addWidget(self.splitter, 0, 0, 1, 1)
        self.splitter_7 = QtWidgets.QSplitter(self.praxisdaten)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.tb_pg1_la6 = QtWidgets.QLabel(self.splitter_7)
        self.tb_pg1_la6.setObjectName("tb_pg1_la6")
        self.tb_pg1_le6 = QtWidgets.QLineEdit(self.splitter_7)
        self.tb_pg1_le6.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le6.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le6.setObjectName("tb_pg1_le6")
        self.gridLayout_2.addWidget(self.splitter_7, 2, 0, 1, 1)
        self.splitter_10 = QtWidgets.QSplitter(self.praxisdaten)
        self.splitter_10.setOrientation(QtCore.Qt.Vertical)
        self.splitter_10.setObjectName("splitter_10")
        self.tb_pg1_la9 = QtWidgets.QLabel(self.splitter_10)
        self.tb_pg1_la9.setObjectName("tb_pg1_la9")
        self.tb_pg1_le9 = QtWidgets.QLineEdit(self.splitter_10)
        self.tb_pg1_le9.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le9.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le9.setObjectName("tb_pg1_le9")
        self.gridLayout_2.addWidget(self.splitter_10, 3, 0, 1, 1)
        self.splitter_12 = QtWidgets.QSplitter(self.praxisdaten)
        self.splitter_12.setOrientation(QtCore.Qt.Vertical)
        self.splitter_12.setObjectName("splitter_12")
        self.tb_pg1_la11 = QtWidgets.QLabel(self.splitter_12)
        self.tb_pg1_la11.setObjectName("tb_pg1_la11")
        self.tb_pg1_le11 = QtWidgets.QLineEdit(self.splitter_12)
        self.tb_pg1_le11.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le11.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le11.setObjectName("tb_pg1_le11")
        self.gridLayout_2.addWidget(self.splitter_12, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.splitter_5 = QtWidgets.QSplitter(self.praxisdaten)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.tb_pg1_la4 = QtWidgets.QLabel(self.splitter_5)
        self.tb_pg1_la4.setObjectName("tb_pg1_la4")
        self.tb_pg1_le4 = QtWidgets.QLineEdit(self.splitter_5)
        self.tb_pg1_le4.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le4.setObjectName("tb_pg1_le4")
        self.horizontalLayout_3.addWidget(self.splitter_5)
        self.splitter_6 = QtWidgets.QSplitter(self.praxisdaten)
        self.splitter_6.setOrientation(QtCore.Qt.Vertical)
        self.splitter_6.setObjectName("splitter_6")
        self.tb_pg1_la5 = QtWidgets.QLabel(self.splitter_6)
        self.tb_pg1_la5.setObjectName("tb_pg1_la5")
        self.tb_pg1_le5 = QtWidgets.QLineEdit(self.splitter_6)
        self.tb_pg1_le5.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le5.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le5.setObjectName("tb_pg1_le5")
        self.horizontalLayout_3.addWidget(self.splitter_6)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.splitter_9 = QtWidgets.QSplitter(self.praxisdaten)
        self.splitter_9.setOrientation(QtCore.Qt.Vertical)
        self.splitter_9.setObjectName("splitter_9")
        self.tb_pg1_la7 = QtWidgets.QLabel(self.splitter_9)
        self.tb_pg1_la7.setObjectName("tb_pg1_la7")
        self.tb_pg1_le7 = QtWidgets.QLineEdit(self.splitter_9)
        self.tb_pg1_le7.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le7.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le7.setObjectName("tb_pg1_le7")
        self.horizontalLayout_4.addWidget(self.splitter_9)
        self.splitter_8 = QtWidgets.QSplitter(self.praxisdaten)
        self.splitter_8.setOrientation(QtCore.Qt.Vertical)
        self.splitter_8.setObjectName("splitter_8")
        self.tb_pg1_la8 = QtWidgets.QLabel(self.splitter_8)
        self.tb_pg1_la8.setObjectName("tb_pg1_la8")
        self.tb_pg1_le8 = QtWidgets.QLineEdit(self.splitter_8)
        self.tb_pg1_le8.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le8.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le8.setObjectName("tb_pg1_le8")
        self.horizontalLayout_4.addWidget(self.splitter_8)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 2, 1, 1, 1)
        self.splitter_11 = QtWidgets.QSplitter(self.praxisdaten)
        self.splitter_11.setOrientation(QtCore.Qt.Vertical)
        self.splitter_11.setObjectName("splitter_11")
        self.tb_pg1_la10 = QtWidgets.QLabel(self.splitter_11)
        self.tb_pg1_la10.setObjectName("tb_pg1_la10")
        self.tb_pg1_le10 = QtWidgets.QLineEdit(self.splitter_11)
        self.tb_pg1_le10.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le10.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le10.setObjectName("tb_pg1_le10")
        self.gridLayout_2.addWidget(self.splitter_11, 3, 1, 1, 1)
        self.splitter_13 = QtWidgets.QSplitter(self.praxisdaten)
        self.splitter_13.setOrientation(QtCore.Qt.Vertical)
        self.splitter_13.setObjectName("splitter_13")
        self.tb_pg1_la12 = QtWidgets.QLabel(self.splitter_13)
        self.tb_pg1_la12.setObjectName("tb_pg1_la12")
        self.tb_pg1_le12 = QtWidgets.QLineEdit(self.splitter_13)
        self.tb_pg1_le12.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le12.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le12.setObjectName("tb_pg1_le12")
        self.gridLayout_2.addWidget(self.splitter_13, 4, 1, 1, 1)
        self.splitter_4 = QtWidgets.QSplitter(self.praxisdaten)
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.tb_pg1_la3 = QtWidgets.QLabel(self.splitter_4)
        self.tb_pg1_la3.setObjectName("tb_pg1_la3")
        self.tb_pg1_le3 = QtWidgets.QLineEdit(self.splitter_4)
        self.tb_pg1_le3.setMinimumSize(QtCore.QSize(0, 30))
        self.tb_pg1_le3.setMaximumSize(QtCore.QSize(16777215, 30))
        self.tb_pg1_le3.setObjectName("tb_pg1_le3")
        self.gridLayout_2.addWidget(self.splitter_4, 1, 0, 1, 1)
        self.verticalLayout_4.addLayout(self.gridLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainMenuBtn1 = QtWidgets.QPushButton(self.praxisdaten)
        self.mainMenuBtn1.setObjectName("mainMenuBtn1")
        self.verticalLayout.addWidget(self.mainMenuBtn1)
        self.mainMenuBtn2 = QtWidgets.QPushButton(self.praxisdaten)
        self.mainMenuBtn2.setObjectName("mainMenuBtn2")
        self.verticalLayout.addWidget(self.mainMenuBtn2)
        self.mainMenuBtn3 = QtWidgets.QPushButton(self.praxisdaten)
        self.mainMenuBtn3.setObjectName("mainMenuBtn3")
        self.verticalLayout.addWidget(self.mainMenuBtn3)
        self.mainMenuBtn4 = QtWidgets.QPushButton(self.praxisdaten)
        self.mainMenuBtn4.setObjectName("mainMenuBtn4")
        self.verticalLayout.addWidget(self.mainMenuBtn4)
        self.verticalLayout_4.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
        self.verticalLayout_3.addWidget(self.praxisdaten)
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidget)
        self.dockWidget_2 = QtWidgets.QDockWidget(MainWindow)
        self.dockWidget_2.setFloating(False)
        self.dockWidget_2.setFeatures(QtWidgets.QDockWidget.NoDockWidgetFeatures)
        self.dockWidget_2.setAllowedAreas(QtCore.Qt.TopDockWidgetArea)
        self.dockWidget_2.setObjectName("dockWidget_2")
        self.dockWidgetContents_3 = QtWidgets.QWidget()
        self.dockWidgetContents_3.setObjectName("dockWidgetContents_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.dockWidgetContents_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_3.setMinimumSize(QtCore.QSize(60, 60))
        self.label_3.setMaximumSize(QtCore.QSize(120, 120))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(":/logo/images/praxislogotrans.gif"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        self.label_2 = QtWidgets.QLabel(self.dockWidgetContents_3)
        font = QtGui.QFont()
        font.setFamily("MS PGothic")
        font.setPointSize(48)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.dockWidgetContents_3)
        self.label_4.setMinimumSize(QtCore.QSize(60, 60))
        self.label_4.setMaximumSize(QtCore.QSize(120, 120))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/logo/images/a_Vetlogo2.gif"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.dockWidget_2.setWidget(self.dockWidgetContents_3)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(4), self.dockWidget_2)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionEinstellungen = QtWidgets.QAction(MainWindow)
        self.actionEinstellungen.setObjectName("actionEinstellungen")
        self.actionBeenden = QtWidgets.QAction(MainWindow)
        self.actionBeenden.setObjectName("actionBeenden")
        self.actionKunden = QtWidgets.QAction(MainWindow)
        self.actionKunden.setObjectName("actionKunden")
        self.actionTiere = QtWidgets.QAction(MainWindow)
        self.actionTiere.setObjectName("actionTiere")
        self.actionFinanzen = QtWidgets.QAction(MainWindow)
        self.actionFinanzen.setObjectName("actionFinanzen")
        self.menuDatei.addAction(self.actionImport)
        self.menuDatei.addAction(self.actionExport)
        self.menuDatei.addAction(self.actionEinstellungen)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionBeenden)
        self.menuModule.addAction(self.actionKunden)
        self.menuModule.addAction(self.actionTiere)
        self.menuModule.addAction(self.actionFinanzen)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuBearbeiten.menuAction())
        self.menubar.addAction(self.menuModule.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHilfe.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuDatei.setTitle(_translate("MainWindow", "Datei"))
        self.menuBearbeiten.setTitle(_translate("MainWindow", "Bearbeiten"))
        self.menuModule.setTitle(_translate("MainWindow", "Module"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuHilfe.setTitle(_translate("MainWindow", "Hilfe"))
        self.label.setText(_translate("MainWindow", "Suche:"))
        self.tb_pg1_la1.setText(_translate("MainWindow", "TextLabel"))
        self.tb_pg1_la2.setText(_translate("MainWindow", "TextLabel"))
        self.tb_pg1_la0.setText(_translate("MainWindow", "TextLabel"))
        self.tb_pg1_la6.setText(_translate("MainWindow", "TextLabel"))
        self.tb_pg1_la9.setText(_translate("MainWindow", "TextLabel"))
        self.tb_pg1_la11.setText(_translate("MainWindow", "TextLabel"))
        self.tb_pg1_la4.setText(_translate("MainWindow", "TextLabel"))
        self.tb_pg1_la5.setText(_translate("MainWindow", "TextLabel"))
        self.tb_pg1_la7.setText(_translate("MainWindow", "TextLabel"))
        self.tb_pg1_la8.setText(_translate("MainWindow", "TextLabel"))
        self.tb_pg1_la10.setText(_translate("MainWindow", "TextLabel"))
        self.tb_pg1_la12.setText(_translate("MainWindow", "TextLabel"))
        self.tb_pg1_la3.setText(_translate("MainWindow", "TextLabel"))
        self.mainMenuBtn1.setText(_translate("MainWindow", "Praxisdaten"))
        self.mainMenuBtn2.setText(_translate("MainWindow", "Kundenkartei"))
        self.mainMenuBtn3.setText(_translate("MainWindow", "Behandlung"))
        self.mainMenuBtn4.setText(_translate("MainWindow", "Grunddaten"))
        self.label_2.setText(_translate("MainWindow", "Akuvet 2020"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionEinstellungen.setText(_translate("MainWindow", "Einstellungen"))
        self.actionBeenden.setText(_translate("MainWindow", "Beenden"))
        self.actionKunden.setText(_translate("MainWindow", "Kunden"))
        self.actionTiere.setText(_translate("MainWindow", "Tiere"))
        self.actionFinanzen.setText(_translate("MainWindow", "Finanzen"))
from . import akuvet_rc
