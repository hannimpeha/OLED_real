import sys
from PyQt5.QtWidgets import QWidget, QAction, QTabWidget, QVBoxLayout, QApplication, QMenuBar, QGridLayout
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon

from Qtcontrollers.elements_structure import Elements_Structure
from Qtcontrollers.elements_structure_graph import Elements_Structure_Graph
from Qtcontrollers.emission_layer import Emission_Layer
from Qtcontrollers.emission_layer_graph import Emission_Layer_Graph
from Qtcontrollers.emission_zone_setting import Emission_Zone_Setting
from Qtcontrollers.execute import Execute
from Qtcontrollers.logo_image import Logo_Image
from Qtcontrollers.project_info import Project_Info

class Real(QWidget):
    def __init__(self):
        super().__init__()
        self.making_file()
        self.making_tabs()

        layout = QGridLayout()
        layout.addWidget(self.menuBar)

        self.setMinimumSize(QSize(1600, 900))
        self.setWindowTitle('JooAm Angular Luminence Spectometer')


    def making_file(self):
        self.menuBar = QMenuBar()

        newAction = QAction(QIcon('new.png'), '&New', self)
        newAction.setShortcut('Ctrl+N')

        openAction = QAction(QIcon('open.png'), '&Open', self)
        openAction.setShortcut('Ctrl+O')

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')

        fileMenu = self.menuBar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)


    def making_tabs(self):
        tab1 = QWidget()
        tab2 = QWidget()

        elem = [Elements_Structure_Graph(), Emission_Layer_Graph(),
                Elements_Structure(), Emission_Zone_Setting(),
                Logo_Image()]
        grid_tab1 = QGridLayout()
        positions = [(i, j) for i in range(4) for j in range(4)]

        for position, ele in zip(positions, elem):
            grid_tab1.addWidget(ele, *position)

        tabs = QTabWidget()
        tabs.addTab(tab1, '2PPlAn_PL')
        tabs.addTab(tab2, 'Result')


        tab1.setLayout(grid_tab1)

        grid = QVBoxLayout()
        grid.addWidget(tabs)

        # logo_image = Logo_Image()
        # emission_image = Emission_Layer_Graph()
        # elements_structure_graph = Elements_Structure_Graph()
        # emission_zone_setting = Emission_Zone_Setting()
        # execute = Execute()
        # project_info = Project_Info()

        # tables = [es_table, el_table, logo_image, emission_image,
        #                emission_zone_setting, execute, project_info,
        #                elements_structure_graph]
        # tables = [tab1, tab2]
        # positions = [(i, j) for i in range(4) for j in range(1)]
        #
        # for position, table in zip(positions, tables):
        #     grid.addWidget(table, *position)

        self.setLayout(grid)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Real()
    window.show()
    sys.exit(app.exec_())
