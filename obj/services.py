from dataclasses import dataclass
import decimal, datetime, time
from PyQt5.QtSql import *
from modules import treatment_form



@dataclass()
class Services:
    id: int
    id_treatment: int = None
    service: int = None
    single_price: decimal = None
    index: int = None
    amount: int = None
    duration: time = None
    service_faktor: decimal = None
    tax_factor: decimal = None
    gross_price: decimal = None


    def calc_gross_price(self) -> decimal:
        calc_price = self.single_price * self.amount * self.service_faktor
        self.gross_price = calc_price + (calc_price*(self.tax_factor/100))
        return self.gross_price

    def calc_gross_price_timebased(self) ->decimal:
        # Todo calc_gross_price_timebased
        pass

    def calc_service_factor(self) ->decimal:
        # Todo calc_service_factor
        pass

    def calc_service_factor_timebased(self):
        # Todo calc_service_factor_timebased
        pass


if __name__ == '__main__':
    leistung1 = Services('test', 2.5,  19, 1.25 ,5).calc_grossprice()
    print(leistung1)



