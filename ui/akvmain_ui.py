# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Benutzer\rainer_holland\Documents\PycharmProjects\AkuVet\ui\akvmain.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1797, 1241)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1797, 20))
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
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(24, 24))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtWidgets.QAction(MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionPreferences = QtWidgets.QAction(MainWindow)
        self.actionPreferences.setObjectName("actionPreferences")
        self.actionClose = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/others/black/Shutdown Filled.png"), QtGui.QIcon.Active, QtGui.QIcon.Off)
        self.actionClose.setIcon(icon)
        self.actionClose.setObjectName("actionClose")
        self.actionCustomer = QtWidgets.QAction(MainWindow)
        self.actionCustomer.setObjectName("actionCustomer")
        self.actionTiere = QtWidgets.QAction(MainWindow)
        self.actionTiere.setObjectName("actionTiere")
        self.actionFinance = QtWidgets.QAction(MainWindow)
        self.actionFinance.setObjectName("actionFinance")
        self.actionTherapy = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/others/black/Horse Filled.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTherapy.setIcon(icon1)
        self.actionTherapy.setObjectName("actionTherapy")
        self.menuDatei.addAction(self.actionImport)
        self.menuDatei.addAction(self.actionExport)
        self.menuDatei.addAction(self.actionPreferences)
        self.menuDatei.addSeparator()
        self.menuDatei.addAction(self.actionClose)
        self.menuModule.addAction(self.actionCustomer)
        self.menuModule.addAction(self.actionTherapy)
        self.menuModule.addAction(self.actionFinance)
        self.menubar.addAction(self.menuDatei.menuAction())
        self.menubar.addAction(self.menuBearbeiten.menuAction())
        self.menubar.addAction(self.menuModule.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHilfe.menuAction())
        self.toolBar.addAction(self.actionClose)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTherapy)
        self.toolBar.addSeparator()

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
        self.label_2.setText(_translate("MainWindow", "Akuvet 2020"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionPreferences.setText(_translate("MainWindow", "Einstellungen"))
        self.actionClose.setText(_translate("MainWindow", "Beenden"))
        self.actionCustomer.setText(_translate("MainWindow", "Kunden"))
        self.actionTiere.setText(_translate("MainWindow", "Tiere"))
        self.actionFinance.setText(_translate("MainWindow", "Finanzen"))
        self.actionTherapy.setText(_translate("MainWindow", "Behandlungen"))
from . import akuvet_rc
