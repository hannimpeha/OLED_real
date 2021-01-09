import sys

from PyQt5.QtWidgets import QWidget, QAction, QTabWidget, QVBoxLayout, QApplication, QMenuBar, QGridLayout
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon

from Qtcontrollers.axes_properties import Axes_Properties
from Qtcontrollers.elements_structure import Elements_Structure
from Qtcontrollers.elements_structure_graph import Elements_Structure_Graph
from Qtcontrollers.logo_image import Logo_Image
from Qtcontrollers.plotting_param import Plotting_Param


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

        elem = [Elements_Structure_Graph(), Elements_Structure(), Logo_Image()]
        grid_tab1 = QGridLayout()
        positions = [(i, j) for i in range(4) for j in range(4)]

        for position, element in zip(positions, elem):
            grid_tab1.addWidget(element, *position)
        tab1.setLayout(grid_tab1)

        mlem = [Elements_Structure_Graph(), Axes_Properties(), Plotting_Param()]
        grid_tab2 = QGridLayout()
        positions = [(i, j) for i in range(4) for j in range(4)]

        for position, element in zip(positions, mlem):
            grid_tab2.addWidget(element, *position)
        tab2.setLayout(grid_tab2)

        tabs = QTabWidget()
        tabs.addTab(tab1, '2PPlAn_PL')
        tabs.addTab(tab2, 'Result')
        grid = QVBoxLayout()
        grid.addWidget(tabs)

        self.setLayout(grid)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Real()
    window.show()
    sys.exit(app.exec_())
