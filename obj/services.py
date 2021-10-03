from dataclasses import dataclass
import decimal
import time
from PyQt5.QtSql import QSqlIndex
from modules.models import DataModels


@dataclass()
class Services(DataModels):
    id_service_pk: int
    id_treatment: int = 0
    service: int = 0
    single_price: decimal = None
    index: int = 0
    amount: int = 0
    duration: time = None
    service_faktor: decimal = None
    tax_factor: decimal = None
    gross_price: decimal = None
    model_index: QSqlIndex = None
    __sum_services_treatment__: decimal = None

    def __init__(self):
        super().__init__()
        self.dm = DataModels()

    def set_data_by_id(self, id_service_pk):
        row = 0
        self.id_service_pk = id_service_pk
        self.dm = self.dm.set_treatment_service_by_id(id_service_pk)
        self.single_price = self.dm.treatment_service_model.record(row).value('Preis')
        self.service = self.dm.treatment_service_model.record(row).value('Leistung')
        self.single_price = self.dm.treatment_service_model.record(row).value('Preis')
        self.amount = self.dm.treatment_service_model.record(row).value('Menge')
        self.service_faktor = self.dm.treatment_service_model.record(row).value('Faktor')
        self.tax_factor = self.dm.treatment_service_model.record(row).value('Steuersatz')
        self.id_treatment = self.dm.treatment_service_model.record(row).value('ID_Behandlung')
        self.duration = self.dm.treatment_service_model.record(row).value('Dauer')
        self.gross_price = self.dm.treatment_service_model.record(row).value('brutto')
        self.model_index = self.dm.treatment_service_model.index(row, 9)

    def calc_gross_price(self):
        calc_price = self.single_price * self.amount * self.service_faktor
        self.gross_price = round(calc_price + (calc_price * (self.tax_factor / 100)), 2)
        self.dm.treatment_service_model.setData(self.model_index, self.gross_price)

    def calc_gross_price_timebased(self) -> decimal:
        # Todo calc_gross_price_timebased
        pass

    def calc_service_factor(self) -> decimal:
        # Todo calc_service_factor
        pass

    def calc_service_factor_timebased(self):
        # Todo calc_service_factor_timebased
        pass


if __name__ == '__main__':
    a = Services()
