from qgis.PyQt.QtWidgets import *
from .impact_dialog_table import Ui_Digimpactsss

class DlgTable(QDialog, Ui_Digimpactsss):
    def __init__(self):
        super(DlgTable, self).__init__()
        self.setupUi(self)