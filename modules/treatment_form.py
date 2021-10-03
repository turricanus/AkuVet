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
from datetime import date

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
        self.qloc = QLocale
        # self.qloc.setDefault(QLocale.German, QLocale.German)
        # initialize Variables

        self.actual_Customer_id = None
        self.active_customer_index = None
        self.actual_animal_id = None
        self.actual_treatment_id = None
        self.actual_treatment_row = None
        self.actual_tab_showed = 0
        self.actual_treatment_locked = False

        # Initialize Models
        self.dm = DataModels()
        self.customer_view = self.tbvcustomerselection
        self.dm.evt_on_kunden_searchtext_change("")
        self.set_customer_view()

        # Signals Buttons
        self.btntreatsave.clicked.connect(self.evt_btn_save_clicked)
        self.btntreat_cancel.clicked.connect(self.evt_btn_cancel_clicked)
        self.btntbwnew.clicked.connect(self.evt_btn_clicked_new_treatment_item)
        self.btntbwdelete.clicked.connect(self.evt_btn_clicked_delete_treatment_item)
        self.btnnewtherapie.clicked.connect(self.evt_btn_new_treatment)
        self.btnlocktreatment.toggled.connect(self.evt_btn_locktretment_toggle)

        # Signals views
        self.le_searchfield.textChanged.connect(self.dm.evt_on_kunden_searchtext_change)
        self.tbvcustomerselection.clicked.connect(self.evt_selectcustomer_clicked)
        self.livanimal.clicked.connect(self.evt_animal_clicked)
        self.tbvtreatselection.clicked.connect(self.evt_treatment_clicked)
        self.tbwtreatment.tabBarClicked.connect(self.evt_select_tab)
        # self.ledshortdisscribtion.editingFinished.connect(self.evt_edit_treatment)
        # self.btn_service_calc_price.clicked.connect(self.refresh_service)
        self.dm.treatment_service_model.dataChanged.connect(self.refresh_data_treatment_service)

    def insert_treatment(self):
        animal_id = self.actual_animal_id
        new_index = self.get_new_index(self.dm.treatment_model, 4)
        data_record = self.dm.treatment_model.record()
        data_record.setValue('ID_Tier', animal_id)
        data_record.setValue('Datum', QDate(date.today()))
        data_record.setValue('order', new_index)
        data_record.setValue('Kurz_Text', 'Bitte neuen Kurztextanlegen')
        data_record.setValue('Behandlung_abgeschlossen', False)
        self.dm.treatment_model.insertRecord(-1, data_record)
        self.dm.treatment_model.submitAll()
        self.get_therapies_from_animal(animal_id)

    def insert_treatment_item(self, model):
        r = model.record()
        r.setValue('ID_Behandlung', self.actual_treatment_id)
        if model == self.dm.treatment_diagnosis_model:
            r.setValue('Diagnose_Freitext', 'Bitte neue Diagnose eintragen')
            new_index = self.get_new_index(model, 3)
            r.setValue('order', new_index)
        elif model == self.dm.treatment_service_model:
            r.setValue('Leistung', 0)
            new_index = self.get_new_index(model, 4)
            r.setValue('order', new_index)
        elif model == self.dm.treatment_medics_model:
            r.setValue('Medikament', 0)
            new_index = self.get_new_index(model, 4)
            r.setValue('order', new_index)
        elif model == self.dm.treatment_progress_model:
            r.setValue('Datum_Erhebung', QDate(date.today()))
            r.setValue('Verlauf', 'Bitte neuen Verlauf einteragen')
        model.insertRecord(-1, r)
        model.submitAll()
        model.select()

    def remove_treatment_item(self, view, model):
        idxs = view.selectedIndexes()
        if model.isDirty():
            model.submitAll()
        if idxs:
            mba = QMessageBox.question(self, 'Sicher', 'Soll der Datensatz wirklich gelsöcht werden?')
            if mba == QMessageBox.Yes:
                for idx in idxs:
                    model.removeRow(idx.row())
            else:
                return
        else:
            QMessageBox.information(self, 'Kein Auswahl getroffen', 'Bitte eine Zeile zum löschen auswählen')

    def get_therapies_from_animal(self, animalid):
        if animalid:
            self.dm.set_treatment_model(animalid)
            self.tbvtreatselection.setModel(self.dm.treatment_model)
            self.initialize_treatment_view()

    def fill_treatment_form(self, recordrow=0):
        self.dtetherapy.setDate(self.dm.treatment_model.record(recordrow).value('Datum'))
        self.actual_treatment_id = self.dm.get_treatid_from_treatmodel_row(recordrow)
        sum_treatment_service = locale.currency(self.dm.calc_sum_from_service_treatment(self.actual_treatment_id))
        sum_medics = locale.currency(self.dm.calc_sum_from_medics_treatment(self.actual_treatment_id))
        self.tbwtreatment.setTabText(1,
                                     f'Leistungen: {sum_treatment_service}')
        self.tbwtreatment.setTabText(2,
                                     f'Medikamente: {sum_medics}')

        self.ledshortdisscribtion.setText(self.dm.treatment_model.record(recordrow).value('Kurz_Text'))
        self.tewananemsis.setText(self.dm.treatment_model.record(recordrow).value('Anamnese'))
        self.tewfindings.setText(self.dm.treatment_model.record(recordrow).value('Befund'))
        if self.dm.treatment_model.record(recordrow).value('Behandlung_abgeschlossen'):
            self.btnlocktreatment.setChecked(True)
            self.actual_treatment_locked = True
        else:
            self.btnlocktreatment.setChecked(False)
            self.actual_treatment_locked = False
        self.set_treatment_data_lock(self.actual_treatment_locked)
        self.set_treatment_detail_tabw(self.actual_tab_showed)

    def initialize_treatment_view(self):
        # self.treatment_model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.tbvtreatselection.setSelectionBehavior(QTableView.SelectRows)
        self.tbvtreatselection.resizeColumnsToContents()
        self.tbvtreatselection.setAlternatingRowColors(True)
        self.tbvtreatselection.sortByColumn(2, Qt.SortOrder(1))
        for column in range(self.dm.treatment_model.columnCount()):
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

    def set_diagnosis_view(self, treat_id):
        self.dm.set_treatment_diagnosis_model(treat_id)
        self.tbvdiagnose.setModel(self.dm.treatment_diagnosis_model)
        self.tbvdiagnose.setColumnHidden(0, True)
        self.tbvdiagnose.setColumnHidden(1, True)
        self.tbvdiagnose.setColumnHidden(3, True)
        self.tbvdiagnose.resizeColumnsToContents()
        self.tbvdiagnose.setItemDelegate(QSqlRelationalDelegate(self.tbvdiagnose))

    def set_medics_view(self, treat_id):
        self.dm.set_treatment_medics_model(treat_id)
        self.tbvmedics.setModel(self.dm.treatment_medics_model)
        self.tbvmedics.setColumnHidden(0, True)
        self.tbvmedics.setColumnHidden(1, True)
        self.tbvmedics.setColumnHidden(4, True)
        self.tbvmedics.resizeColumnsToContents()
        self.tbvmedics.setItemDelegate(QSqlRelationalDelegate(self.tbvmedics))

    def set_service_view(self, treat_id):
        self.dm.set_treatment_service_model(treat_id)
        self.tbvservice.setModel(self.dm.treatment_service_model)
        self.tbvservice.setColumnHidden(0, True)
        self.tbvservice.setColumnHidden(1, True)
        self.tbvservice.setColumnHidden(4, True)
        self.tbvservice.resizeColumnsToContents()
        self.tbvservice.setItemDelegate(QSqlRelationalDelegate(self.tbvservice))

    def set_progress_view(self, treat_id):
        self.dm.set_treatment_progress_model(treat_id)
        self.tbvprogress.setModel(self.dm.treatment_progress_model)
        self.tbvprogress.setColumnHidden(0, True)
        self.tbvprogress.setColumnHidden(1, True)
        self.tbvprogress.resizeColumnsToContents()

    # set Tabwidget
    def set_treatment_detail_tabw(self, tabindex=0):
        self.tbwtreatment.setCurrentIndex(tabindex)
        sum_treatment_service = locale.currency(self.dm.calc_sum_from_service_treatment(self.actual_treatment_id))
        sum_medics = locale.currency(self.dm.calc_sum_from_medics_treatment(self.actual_treatment_id))
        self.tbwtreatment.setTabText(1,
                                     f'Leistungen: {sum_treatment_service}')
        self.tbwtreatment.setTabText(2,
                                     f'Medikamente: {sum_medics}')
        if tabindex == 0:
            self.set_diagnosis_view(self.actual_treatment_id)
        elif tabindex == 1:
            self.set_service_view(self.actual_treatment_id)
        elif tabindex == 2:
            self.set_medics_view(self.actual_treatment_id)
        elif tabindex == 3:
            self.set_progress_view(self.actual_treatment_id)

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

    # Helper Functions
    def set_treatment_data_lock(self, locked):
        if locked:
            self.tbvdiagnose.setEnabled(False)
            self.tbvmedics.setEnabled(False)
            self.tbvservice.setEnabled(False)
            self.tbvprogress.setEnabled(False)
            self.ledshortdisscribtion.setEnabled(False)
            self.dtetherapy.setEnabled(False)
            self.tewfindings.setEnabled(False)
            self.tewananemsis.setEnabled(False)
        else:
            self.tbvdiagnose.setEnabled(True)
            self.tbvmedics.setEnabled(True)
            self.tbvservice.setEnabled(True)
            self.tbvprogress.setEnabled(True)
            self.ledshortdisscribtion.setEnabled(True)
            self.dtetherapy.setEnabled(True)
            self.tewfindings.setEnabled(True)
            self.tewananemsis.setEnabled(True)



    def get_new_index(self, model, column):
        model.setSort(column, Qt.DescendingOrder)
        last_index = model.data(model.index(0, column))
        if last_index is not None:
            return last_index + 1
        else:
            return 0

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
        self.dm.treatment_model.select()
        self.tbvtreatselection.selectRow(0)
        self.tbvtreatselection.setModel(self.dm.treatment_model)
        self.evt_treatment_clicked(self.tbvtreatselection.currentIndex())

    def evt_treatment_clicked(self, idx):
        row = idx.row()
        self.actual_treatment_row = row
        self.dm.treatment_model = self.dm.treatment_model
        self.actual_treatment_id = self.dm.get_treatid_from_treatmodel_row(row)
        self.dm.treatment_model.selectRow(row)
        self.fill_treatment_form(row)

    def evt_select_tab(self, tabindex):
        self.actual_tab_showed = tabindex
        # Todo Speichernabfrage Tabwechsel
        self.set_treatment_detail_tabw(tabindex)

    def refresh_data_treatment_service(self, idx):
        row = idx.row()

        treat_id = self.dm.get_treatid_from_treatmodel_row(row)
        b = services.Services()
        b.set_data_by_id(treat_id)
        b.calc_gross_price()
        self.evt_treatment_clicked(idx)

    # Button Events
    def evt_btn_save_clicked(self):
        self.evt_edit_treatment()
        if self.actual_tab_showed == 0:
            tok = self.dm.treatment_diagnosis_model.submitAll()
        elif self.actual_tab_showed == 1:
            tok = self.dm.treatment_service_model.submitAll()
        elif self.actual_tab_showed == 2:
            tok = self.dm.treatment_medics_model.submitAll()
        elif self.actual_tab_showed == 3:
            tok = self.dm.treatment_progress_model.submitAll()
        if not tok:
            QMessageBox(self, 'Fehler beim Speicher', 'Der Speichervorgang schlug fehl.')

    def evt_btn_cancel_clicked(self):
        if self.actual_tab_showed == 0:
            self.dm.treatment_diagnosis_model.revertAll()
        elif self.actual_tab_showed == 1:
            self.dm.treatment_service_model.revertAll()
        elif self.actual_tab_showed == 2:
            self.dm.treatment_medics_model.revertAll()
        elif self.actual_tab_showed == 3:
            self.dm.treatment_progress_model.revertAll()

    def evt_btn_clicked_new_treatment_item(self):
        if self.actual_tab_showed == 0:
            self.insert_treatment_item(self.dm.treatment_diagnosis_model)
        elif self.actual_tab_showed == 1:
            self.insert_treatment_item(self.dm.treatment_service_model)
        elif self.actual_tab_showed == 2:
            self.insert_treatment_item(self.dm.treatment_medics_model)
        elif self.actual_tab_showed == 3:
            self.insert_treatment_item(self.dm.treatment_progress_model)

    def evt_btn_clicked_delete_treatment_item(self):
        if self.actual_tab_showed == 0:
            self.remove_treatment_item(self.tbvdiagnose, self.dm.treatment_diagnosis_model)
        elif self.actual_tab_showed == 1:
            self.remove_treatment_item(self.tbvservice, self.dm.treatment_service_model)
        elif self.actual_tab_showed == 2:
            self.remove_treatment_item(self.tbvmedics, self.dm.treatment_medics_model)
        elif self.actual_tab_showed == 3:
            self.remove_treatment_item(self.tbvprogress, self.dm.treatment_progress_model)

    def evt_btn_new_treatment(self):
        self.insert_treatment()

    def evt_edit_treatment(self):
        self.dm.treatment_model.setData(self.dm.treatment_model.index(self.actual_treatment_row, 2), self.dtetherapy.date())
        self.dm.treatment_model.setData(self.dm.treatment_model.index(self.actual_treatment_row, 3), self.ledshortdisscribtion.text())
        self.dm.treatment_model.setData(self.dm.treatment_model.index(self.actual_treatment_row, 5), self.tewananemsis.toPlainText())
        self.dm.treatment_model.setData(self.dm.treatment_model.index(self.actual_treatment_row, 6), self.tewfindings.toPlainText())
        self.dm.treatment_model.submitAll()

    def evt_btn_locktretment_toggle(self):
        if self.btnlocktreatment.isChecked():
            self.dm.treatment_model.setData(self.dm.treatment_model.index(self.actual_treatment_row, 9), 1)
        else:
            self.dm.treatment_model.setData(self.dm.treatment_model.index(self.actual_treatment_row, 9), 0)
        self.dm.treatment_model.submitAll()
        self.fill_treatment_form(self.actual_treatment_row)

