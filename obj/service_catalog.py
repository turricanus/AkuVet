import string
from dataclasses import dataclass
import decimal
from modules.models import DataModels
import services


@dataclass()
class ServiceCatalog(DataModels, services):
    service_catalog_id: int = 0
    got1: string = None
    got2: string = None
    got3: string = None
    service_text: string = None
    service_price: decimal = None
    time_factor: bool = False

    def __init__(self):
        super().__init__()
        self.dm = DataModels()

    def set_catalog_by_id(self, service_catalog_id):
        row = 0
        self.service_catalog_id = service_catalog_id
        self.dm.set_service_catalog_by_id(service_catalog_id)
        self.got1 = self.dm.service_catalog_table_model.record(row).value('Got1')
        self.got2 = self.dm.service_catalog_table_model.record(row).value('Got2')
        self.got3 = self.dm.service_catalog_table_model.record(row).value('Got3')
        self.service_text = self.dm.service_catalog_table_model.record(row).value('Text')
        self.service_price = self.dm.service_catalog_table_model.record(row).value('Gebühr')
        self.time_factor = self.dm.service_catalog_table_model.record(row).value('Zeitfaktor')

    def service_is_time_based(self):
        return self.time_factor

    def service_single_price(self):
        return self.service_price
