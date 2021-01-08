from PyQt5.QtWidgets import *

class Elements_Structure(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        es_table = self.init_es_table()
        el_table = Emission_Layer()
        emission_zone_setting = Emission_Zone_Setting()

        tables = [es_table, el_table, emission_zone_setting]
        positions = [(i, j) for i in range(4) for j in range(1)]

        for position, table in zip(positions, tables):
            grid.addWidget(table, *position)

        self.setLayout(grid)

    def init_es_table(self):
        self.table = QTableWidget()
        self.table.setRowCount(6)
        self.table.setColumnCount(6)
        cols_element = ['L#', 'LayerName', 'Material', 'RefractiveIndex', 'Thickness', 'Unit']
        self.table.setHorizontalHeaderLabels(cols_element)

        self.layer_name = ["Al", "ETL", "EML", "HTL2", "HTL1", "ITO"]
        self.material = ["Al", "ETL", "EML", "HTL2", "HTL1", "ITO"]
        self.refractive_index = ["Al.dat", "ETL.dat", "EML.dat", "HTL.dat", "HTL1.dat", "ITO.dat"]
        self.thickness = [100, 100.5, 20, 10, 100.5, 70]
        self.unit = ["nm", "nm", "nm", "nm", "nm", "nm"]
        self.tempList = [[self.layer_name, self.material, self.refractive_index, self.thickness, self.unit]]
        self.num_row = len(self.tempList)
        self.table.setFixedSize(600, 200)

        for i in range(len(self.layer_name)):
            self.num_row = i
            self.table.setItem(self.num_row, 0, QTableWidgetItem(str(self.num_row)))
            self.table.setItem(self.num_row, 1, QTableWidgetItem(self.layer_name[i]))
            self.table.setItem(self.num_row, 2, QTableWidgetItem(self.material[i]))
            self.table.setItem(self.num_row, 3, QTableWidgetItem(self.refractive_index[i]))
            self.table.setItem(self.num_row, 4, QTableWidgetItem(str(self.thickness[i])))
            self.table.setItem(self.num_row, 5, QTableWidgetItem(self.unit[i]))
        return self.table

class Emission_Layer(QWidget):
    def __init__(self):
        super().__init__()
        layer = QVBoxLayout()
        self.initUI()
        layer.addWidget(self.table)
        self.setLayout(layer)

    def initUI(self):
        self.table = QTableWidget()
        self.table.setRowCount(6)
        self.table.setColumnCount(7)

        cols_element = ['L#', 'EMMaterials', 'Spectrum', 'ExcitonProp', 'QY', 'PQ', 'EMZone']
        self.table.setHorizontalHeaderLabels(cols_element)

        self.em_materials = ["None"]
        self.spectrum = ["2pplAn_PL"]
        self.exciton_prop = [1]
        self.qy = [83]
        self.pq = [94]
        self.em_zone = ["Sheet"]
        self.tempList = [[self.em_materials, self.spectrum, self.exciton_prop,
                          self.qy, self.pq, self.em_zone]]
        self.num_row = len(self.tempList)
        self.table.setFixedSize(720, 200)

        for i in range(len(self.em_materials)):
            self.num_row = i
            self.table.setItem(self.num_row, 0, QTableWidgetItem(str(self.num_row)))
            self.table.setItem(self.num_row, 1, QTableWidgetItem(self.em_materials[i]))
            self.table.setItem(self.num_row, 2, QTableWidgetItem(self.spectrum[i]))
            self.table.setItem(self.num_row, 3, QTableWidgetItem(str(self.exciton_prop[i])))
            self.table.setItem(self.num_row, 4, QTableWidgetItem(str(self.qy[i])))
            self.table.setItem(self.num_row, 5, QTableWidgetItem(str(self.pq[i])))
            self.table.setItem(self.num_row, 6, QTableWidgetItem(str(self.em_zone[i])))

        return self.table

class Emission_Zone_Setting(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)

        radiobutton = QRadioButton("Sheet")
        radiobutton.setChecked(True)
        radiobutton.type = ""
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 0, 0)

        radiobutton = QRadioButton("Constant")
        radiobutton.type = "x=a"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 0, 1)

        radiobutton = QRadioButton("Linear")
        radiobutton.type = "y=ax+b"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 0, 2)

        radiobutton = QRadioButton("Gaussian")
        radiobutton.type = "y = a*e^{b+x}+c"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 0, 3)

        self.qlabel = QLabel()
        layout.addWidget(self.qlabel, 0, 4)


    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.qlabel.setText(radioButton.type)
