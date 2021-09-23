from PyQt5.QtCore import Qt, QDate, QDateTime, QLocale
from PyQt5.QtSql import (
    QSqlTableModel, QSqlRelationalTableModel, QSqlRelationalDelegate,
    QSqlQueryModel,
    QSqlQuery, QSqlRelation, QSqlIndex
)
from PyQt5.QtWidgets import (
    QMessageBox,
    QTableView, QDialog, QPushButton
)

import locale
# Custom Module
from ui.therapymaindialog_ui import Ui_lytMain
from obj import services
from .models import DataModels


class WindowTherapy(QDialog, Ui_lytMain, DataModels):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.loc = locale
        self.loc.setlocale(locale.LC_ALL, 'de_de')
        # self.qloc = QLocale
        # self.qloc.setDefault(QLocale.German, QLocale.German)
        # initialize Variables

        self.actual_Customer_id = None
        self.active_customer_index = None
        self.actual_animal_id = None
        self.actual_treatment_id = None
        self.actual_tab_showed = 0

        # Initialize Models
        self.dm = DataModels()
        self.customer_view = self.tbvcustomerselection
        self.dm.evt_on_kunden_searchtext_change("")
        self.set_customer_view()

        # Signals Buttons

        # Signals views
        self.le_searchfield.textChanged.connect(self.dm.evt_on_kunden_searchtext_change)
        self.tbvcustomerselection.clicked.connect(self.evt_selectcustomer_clicked)
        self.livanimal.clicked.connect(self.evt_animal_clicked)
        self.tbvtreatselection.clicked.connect(self.evt_treatment_clicked)
        self.tbwtreatment.tabBarClicked.connect(self.evt_select_tab)
        # self.btn_service_calc_price.clicked.connect(self.refresh_service)
        self.dm.treatment_service_model.dataChanged.connect(self.refresh_data_treatment_service)
        self.btntreatsave.clicked.connect(self.evt_btn_save_clicked)
        self.btntreat_cancel.clicked.connect(self.evt_btn_cancel_clicked)
        self.btntbwnew.clicked.connect(self.evt_btn_clicked_new_treatment_item)
        self.btntbwdelete.clicked.connect(self.evt_btn_clicked_delete_treatment_item)

    def insert_treatment_diagnosis(self):
        lc = self.dm.treatment_diagnosis_model.rowCount()
        self.dm.treatment_diagnosis_model.insertRow(lc+1)

    def get_therapies_from_animal(self, animalid):
        if animalid:
            self.dm.set_treatment_model(animalid)
            self.tbvtreatselection.setModel(self.dm.treatment_selection_model)
            self.initialize_treatment_view()

    def fill_treatment_form(self, recordrow=0):
        self.dtetherapy.setDate(self.dm.treatment_model.record(recordrow).value('Datum'))
        self.actual_treatment_id = self.dm.get_treatid_from_treatmodel_row(recordrow)
        self.tbwtreatment.setTabText(1,
                                     f'Leistungen: {self.dm.calc_sum_from_service_treatment(self.actual_treatment_id)}')
        self.tbwtreatment.setTabText(2,
                                     f'Medikamente: {self.dm.calc_sum_from_medics_treatment(self.actual_treatment_id)}')

        self.ledshortdisscribtion.setText(self.dm.treatment_model.record(recordrow).value('Kurz_Text'))
        self.tewananemsis.setText(self.dm.treatment_model.record(recordrow).value('Anamnese'))
        self.tewfindings.setText(self.dm.treatment_model.record(recordrow).value('Befund'))
        self.set_treatment_detail_tabw(self.actual_tab_showed)

    def initialize_treatment_view(self):
        # self.treatment_model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.tbvtreatselection.setSelectionBehavior(QTableView.SelectRows)
        self.tbvtreatselection.resizeColumnsToContents()
        self.tbvtreatselection.setAlternatingRowColors(True)
        self.tbvtreatselection.sortByColumn(2, Qt.SortOrder(1))
        for column in range(self.dm.treatment_selection_model.columnCount()):
            if column == 2:
                self.tbvtreatselection.setColumnHidden(column, False)
                self.tbvtreatselection.setColumnWidth(column, 80)
            elif column == 3:
                self.tbvtreatselection.setColumnHidden(column, False)
                self.tbvtreatselection.setColumnWidth(column, 180)
            elif column == 6 or column == 9:
                self.tbvtreatselection.setColumnHidden(column, False)
                self.tbvtreatselection.setColumnWidth(column, 200)
            else:
                self.tbvtreatselection.setColumnHidden(column, True)

    def set_medics_view(self, treat_id):
        self.dm.set_treatment_medics_model(treat_id)
        self.tbvmedics.setModel(self.dm.treatment_medics_model)
        self.tbvmedics.setColumnHidden(0, True)
        self.tbvmedics.setColumnHidden(1, True)
        self.tbvmedics.setColumnHidden(4, True)
        self.tbvmedics.resizeColumnsToContents()
        self.tbvmedics.setItemDelegate(QSqlRelationalDelegate(self.tbvmedics))

    def set_service_view(self, treat_id):
        self.dm.set_treatment_service_module(treat_id)
        self.tbvservice.setModel(self.dm.treatment_service_model)
        self.tbvservice.setColumnHidden(0, True)
        self.tbvservice.setColumnHidden(1, True)
        self.tbvservice.setColumnHidden(4, True)
        self.tbvservice.resizeColumnsToContents()
        self.tbvservice.setItemDelegate(QSqlRelationalDelegate(self.tbvservice))

    # Load Diagnosis Data into Table in Tabwidget
    def set_diagnosis_view(self, treat_id):
        self.dm.set_treatment_diagnosis_module(treat_id)
        self.tbvdiagnose.setModel(self.dm.treatment_diagnosis_model)
        self.tbvdiagnose.setColumnHidden(0, True)
        self.tbvdiagnose.setColumnHidden(1, True)
        self.tbvdiagnose.setColumnHidden(3, True)
        self.tbvdiagnose.resizeColumnsToContents()
        self.tbvdiagnose.setItemDelegate(QSqlRelationalDelegate(self.tbvdiagnose))

    # set Tabwidget
    def set_treatment_detail_tabw(self, tabindex=0):
        self.tbwtreatment.setCurrentIndex(tabindex)
        self.tbwtreatment.setTabText(1,
                                     f'Leistungen: {self.dm.calc_sum_from_service_treatment(self.actual_treatment_id)}')
        self.tbwtreatment.setTabText(2,
                                     f'Medikamente: {self.dm.calc_sum_from_medics_treatment(self.actual_treatment_id)}')
        if tabindex == 0:
            self.set_diagnosis_view(self.actual_treatment_id)
        elif tabindex == 1:
            self.set_service_view(self.actual_treatment_id)
        elif tabindex == 2:
            self.set_medics_view(self.actual_treatment_id)

    def set_customer_view(self):
        self.customer_view.setModel(self.dm.kunden_model)
        self.customer_view.setSortingEnabled(False)
        self.customer_view.verticalHeader().setVisible(False)
        self.customer_view.resizeRowsToContents()
        self.customer_view.resizeColumnsToContents()
        self.customer_view.setSelectionBehavior(QTableView.SelectRows)
        self.customer_view.setSelectionMode(QTableView.SingleSelection)
        self.customer_view.setColumnHidden(0, True)
        self.customer_view.setColumnHidden(1, True)

    def form_refresh(self):
        # ToDo
        pass

    # Helper Funcions

    # Signal Handler
    def evt_selectcustomer_clicked(self, idx):
        row = idx.row()
        self.actual_Customer_id = self.dm.get_customerid_from_customermodel_row(row)
        self.dm.get_animals_from_customer(self.actual_Customer_id)
        self.livanimal.setModel(self.dm.owned_animals_model)
        self.livanimal.setCurrentIndex(self.dm.owned_animals_model.index(0, 0))
        self.evt_animal_clicked(self.livanimal.currentIndex())

    def evt_animal_clicked(self, idx):
        row = idx.row()
        self.actual_animal_id = self.dm.get_animalid_from_animimalmodel_row(row)
        self.get_therapies_from_animal(self.actual_animal_id)
        self.dm.treatment_selection_model.select()
        self.tbvtreatselection.selectRow(0)
        self.tbvtreatselection.setModel(self.dm.treatment_selection_model)
        self.evt_treatment_clicked(self.tbvtreatselection.currentIndex())

    def evt_treatment_clicked(self, idx):
        row = idx.row()
        self.dm.treatment_model = self.dm.treatment_selection_model
        self.actual_treatment_id = self.dm.get_treatid_from_treatmodel_row(row)
        self.dm.treatment_model.selectRow(row)
        self.fill_treatment_form(row)

    def evt_select_tab(self, tabindex):
        self.actual_tab_showed = tabindex
        self.set_treatment_detail_tabw(tabindex)

    def refresh_data_treatment_service(self, idx):
        row = idx.row()
        treat_id = self.dm.get_treatid_from_treatmodel_row(row)
        b = services.Services()
        b.set_data_by_id(treat_id)
        b.calc_gross_price()
        test = b.get_sum_service_treatment()
        print(test)
        self.evt_treatment_clicked(idx)

    def evt_btn_save_clicked(self):
        if self.actual_tab_showed == 0:
            tok = self.dm.treatment_diagnosis_model.submitAll()
        elif self.actual_tab_showed == 1:
            tok = self.dm.treatment_service_model.submitAll()
        elif self.actual_tab_showed == 2:
            tok = self.dm.treatment_medics_model.submitAll()
        if not tok:
            QMessageBox(self, 'Fehler beim Speicher', 'Der Speichervorgang schlug fehl.')

    def evt_btn_cancel_clicked(self):
        if self.actual_tab_showed == 0:
            tok = self.dm.treatment_diagnosis_model.revertAll()
        elif self.actual_tab_showed == 1:
            tok = self.dm.treatment_service_model.revertAll()
        elif self.actual_tab_showed == 2:
            tok = self.dm.treatment_medics_model.revertAll()

    def evt_btn_clicked_new_treatment_item(self):
        self.insert_treatment_diagnosis()

    def evt_btn_clicked_delete_treatment_item(self):
        # Todo
        pass