from PyQt5 import QtCore
from PyQt5.QtWidgets import *

file = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/text.csv'
class Elements_Structure(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        label = QLabel()
        label.setText("Elements Structure")
        layout.addWidget(label)

        grid = QGridLayout()
        connectButton = QPushButton('Add')
        connectButton.clicked.connect(self.onConnectButtonClicked)
        connectButton.setFixedSize(200, 30)

        removeButton = QPushButton('Delete')
        removeButton.clicked.connect(self.onRemoveButtonClicked)
        removeButton.setFixedSize(200, 30)

        es_table = self.init_es_table()
        drawButton = QPushButton("Draw")
        drawButton.clicked.connect(self.onDrawButtonClicked)
        drawButton.setFixedSize(200, 30)

        el_table = Emission_Layer()
        emission_zone_setting = Emission_Zone_Setting()
        grid.addWidget(connectButton, 0, 0)
        grid.addWidget(removeButton, 0, 1)
        grid.addWidget(drawButton, 0, 2)

        layout.addLayout(grid)
        layout.addWidget(es_table)

        layout.addWidget(el_table)
        layout.addWidget(emission_zone_setting)

        self.setLayout(layout)

    def init_es_table(self):

        self.table = QTableWidget()
        self.table.setRowCount(6)
        self.table.setColumnCount(6)
        self.cols_element = ['L#', 'LayerName', 'Material', 'RefractiveIndex', 'Thickness', 'Unit']
        self.table.setHorizontalHeaderLabels(self.cols_element)

        self.layer_name = ["Al", "ETL", "EML", "HTL2", "HTL1", "ITO"]
        self.material = ["Al", "ETL", "EML", "HTL2", "HTL1", "ITO"]
        self.refractive_index = ["Al.dat", "ETL.dat", "EML.dat", "HTL.dat", "HTL1.dat", "ITO.dat"]
        self.thickness = [100, 100.5, 20, 10, 100.5, 70]
        self.unit = ["nm", "nm", "nm", "nm", "nm", "nm"]
        self.tempList = [[self.layer_name, self.material, self.refractive_index, self.thickness, self.unit]]
        self.num_row = len(self.tempList)
        self.table.setFixedSize(610, 250)

        for i in range(len(self.layer_name)):
            self.num_row = i
            self.table.setItem(self.num_row, 0, QTableWidgetItem(str(self.num_row)))
            self.table.setItem(self.num_row, 1, QTableWidgetItem(self.layer_name[i]))
            self.table.setItem(self.num_row, 2, QTableWidgetItem(self.material[i]))
            self.table.setItem(self.num_row, 3, QTableWidgetItem(self.refractive_index[i]))
            self.table.setItem(self.num_row, 4, QTableWidgetItem(str(self.thickness[i])))
            self.table.setItem(self.num_row, 5, QTableWidgetItem(self.unit[i]))
        self.table.horizontalHeader().setStretchLastSection(True)
        #self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.MultiSelection)
        return self.table

    def onConnectButtonClicked(self):
        self.currentRowCount = self.table.rowCount()
        self.table.insertRow(self.currentRowCount)

    @QtCore.pyqtSlot()
    def onRemoveButtonClicked(self):
        button = self.sender()
        if button:
            row = self.table.indexAt(button.pos()).row()
            self.table.removeRow(row)

    def onDrawButtonClicked(self):
        l = self.onDraw()
        for k in range(int(len(l)/6) + 1):
            with open(file, 'w') as out:
                out.write(",".join(l[k * 6:(k + 1) * 6])+"\n")

    def onDraw(self):
        self.cell = []
        # row = self.table.currentRow()
        row = self.table.rowCount()
        col = self.table.columnCount()
        for i in range(row):
            for j in range(col):
                self.cell.append(self.table.item(i, j).text())
        return self.cell







class Emission_Layer(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.initUI()

        label = QLabel()
        label.setText("Emission Layer")
        layout.addWidget(label)

        grid = QGridLayout()
        connectButton = QPushButton('Add')
        connectButton.clicked.connect(self.onConnectButtonClicked)
        connectButton.setFixedSize(300, 30)

        removeButton = QPushButton('Delete')
        removeButton.clicked.connect(self.onRemoveButtonClicked)
        removeButton.setFixedSize(300, 30)

        grid.addWidget(connectButton, 0, 0)
        grid.addWidget(removeButton, 0, 1)
        layout.addLayout(grid)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def initUI(self):
        self.table = QTableWidget()
        self.table.setRowCount(1)
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
        self.table.setFixedSize(720, 300)

        for i in range(len(self.em_materials)):
            self.num_row = i
            self.table.setItem(self.num_row, 0, QTableWidgetItem(str(self.num_row)))
            self.table.setItem(self.num_row, 1, QTableWidgetItem(self.em_materials[i]))
            self.table.setItem(self.num_row, 2, QTableWidgetItem(self.spectrum[i]))
            self.table.setItem(self.num_row, 3, QTableWidgetItem(str(self.exciton_prop[i])))
            self.table.setItem(self.num_row, 4, QTableWidgetItem(str(self.qy[i])))
            self.table.setItem(self.num_row, 5, QTableWidgetItem(str(self.pq[i])))
            self.table.setItem(self.num_row, 6, QTableWidgetItem(str(self.em_zone[i])))
        self.table.horizontalHeader().setStretchLastSection(True)
        return self.table

    def onConnectButtonClicked(self):
        self.currentRowCount = self.table.rowCount()
        self.table.insertRow(self.currentRowCount)

    @QtCore.pyqtSlot()
    def onRemoveButtonClicked(self):
        button = self.sender()
        if button:
            row = self.table.indexAt(button.pos()).row()
            self.table.removeRow(row)

class Emission_Zone_Setting(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)

        label = QLabel()
        label.setText("Emission Zone Setting")
        layout.addWidget(label, 0, 0)

        radiobutton = QRadioButton("Sheet")
        radiobutton.setChecked(True)
        radiobutton.type = ""
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 1, 0)

        radiobutton = QRadioButton("Constant")
        radiobutton.type = "x=a"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 2, 0)

        radiobutton = QRadioButton("Linear")
        radiobutton.type = "y=ax+b"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 3, 0)

        radiobutton = QRadioButton("Gaussian")
        radiobutton.type = "y = a*e^{b+x}+c"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 4, 0)

        label = QLabel()
        label.setText("Equation")
        layout.addWidget(label, 0, 1)

        self.qlabel = QLabel()
        layout.addWidget(self.qlabel, 1, 1)

        label = QLabel()
        label.setText("Emit Range(nm): ")
        layout.addWidget(label, 2, 1)

        textLine = QLineEdit()
        textLine.setFixedSize(100, 20)
        layout.addWidget(textLine, 3, 1)

        label = QLabel()
        label.setText("Value a :")
        layout.addWidget(label, 2, 2)

        textLine = QLineEdit()
        textLine.setFixedSize(100, 20)
        layout.addWidget(textLine, 3, 2)

        label = QLabel()
        label.setText("Value b :")
        layout.addWidget(label, 2, 3)

        textLine = QLineEdit()
        textLine.setFixedSize(100, 20)
        layout.addWidget(textLine, 3, 3)

        label = QLabel()
        label.setText("Value c :")
        layout.addWidget(label, 2, 4)

        textLine = QLineEdit()
        textLine.setFixedSize(100, 20)
        layout.addWidget(textLine, 3, 4)


    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.qlabel.setText(radioButton.type)
