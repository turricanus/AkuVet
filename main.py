import sys
import locale
from configparser import ConfigParser
from PyQt5.QtSql import QSqlDatabase
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow, QMdiSubWindow, QMdiArea)

# User Module
from ui.akvmain_ui import Ui_MainWindow
from modules.treatment_form import WindowTherapy


class AkuvetConfiguration:
    def __init__(self, config_file=r'.\config.ini'):
        self.config_file = config_file
        self.config = ConfigParser()

    def read(self, *args):
        output = []
        self.config.read(self.config_file)
        if not args:
            for section in self.config.sections():
                options_list = {}
                for option in self.config.options(section):
                    options_list.update({option: self.config.get(section, option)})
                output.append((section, options_list))
        else:
            for arg in args:
                options_list = {}
                for option in self.config.options(arg):
                    options_list.update({option: self.config.get(arg, option)})
                output.append((arg, options_list))
        return output


class DatabaseConnection:
    def __init__(self):
        self.config = 'DATABASE'

    def get_config(self):
        dbconfig = AkuvetConfiguration().read(self.config)
        return dbconfig[0]

    def connect_database(self):
        # ToDo
        pass


# Initialize Main Window

class WdMain(QMainWindow, Ui_MainWindow):
    windowcount = 0

    def __init__(self):
        super(WdMain, self).__init__()
        # self.locale.setlocale(locale.LC_ALL, 'de_de')

        self.setupUi(self)

        self.setWindowTitle("Akuvet 2020")
        configtype, config = DatabaseConnection().get_config()

        self.db = QSqlDatabase.addDatabase(config['databasedriver'])
        self.db.setDatabaseName(config['connectionname'])
        if not self.db.open():
            sys.exit(1)

        self.offset = 0
        self.views = []
        self.statusBar().showMessage('Start', 2000)

        # Config MDi Area
        self.mdi = QMdiArea()
        self.setCentralWidget(self.mdi)

        #  Actions
        self.actionClose.triggered.connect(self.evt_app_close)
        self.actionTherapy.triggered.connect(self.evt_call_therapy)

    #  Event Cals
    @staticmethod
    def evt_app_close():
        sys.exit(1)

    def evt_call_therapy(self):
        beh = WindowTherapy()
        sub = QMdiSubWindow()
        sub.setWidget(beh)
        sub.setWindowTitle("Sub Window" + str(self.windowcount))
        self.mdi.addSubWindow(sub)
        sub.showMaximized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dlgMain = WdMain()
    dlgMain.show()
    sys.exit(app.exec_())
