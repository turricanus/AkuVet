# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Benutzer\rainer_holland\Documents\PycharmProjects\AkuVet\ui\tiere_behandlung_wg.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(890, 728)
        self.trvtiere_behandlungen = QtWidgets.QTreeView(Form)
        self.trvtiere_behandlungen.setGeometry(QtCore.QRect(20, 10, 841, 501))
        self.trvtiere_behandlungen.setObjectName("trvtiere_behandlungen")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
