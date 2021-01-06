from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel

from Qtcontrollers.elements_structure import Elements_Structure
from Qtcontrollers.elements_structure_graph import Elements_Structure_Graph
from Qtcontrollers.emission_layer import Emission_Layer
from Qtcontrollers.emission_layer_graph import Emission_Layer_Graph
from Qtcontrollers.emission_zone_setting import Emission_Zone_Setting
from Qtcontrollers.execute import Execute
from Qtcontrollers.logo_image import Logo_Image
from Qtcontrollers.project_info import Project_Info

class Tab1(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        #grid = QGridLayout(self)
        for position, table in zip(self.positions, self.tables):
            self.addWidget(table, *position)

    def initUI(self):
        es_table = Elements_Structure()
        el_table = Emission_Layer()
        logo_image = Logo_Image()
        emission_image = Emission_Layer_Graph()
        elements_structure_graph = Elements_Structure_Graph()
        emission_zone_setting = Emission_Zone_Setting()
        execute = Execute()
        project_info = Project_Info()

        self.tables = [es_table, el_table, logo_image, emission_image, emission_zone_setting, execute, project_info,
                  elements_structure_graph]
        self.positions = [(i, j) for i in range(4) for j in range(4)]



