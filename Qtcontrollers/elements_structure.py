import csv

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *

file = 'Qtcontrollers/resources/text.csv'
file_em = 'Qtcontrollers/resources/text_em.csv'

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
        drawButton = QPushButton("Save")
        drawButton.clicked.connect(self.handleSave)
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
        self.table.setRowCount(12)
        self.table.setColumnCount(6)
        self.cols_element = ['L#', 'LayerName', 'Material', 'RefractiveIndex', 'Thickness', 'Unit']
        self.table.setHorizontalHeaderLabels(self.cols_element)

        self.layer_name = ["Al", "TPBi", "TPBi", "mCBP", "mCBP", "TCTA_B3PYMPM", "TCTA", "NPB", "NPB", "TAPC", "ITO_Geomatec", "glass_Eagle2000"]
        self.material = ["Al", "TPBi", "TPBi", "mCBP", "mCBP", "TCTA_B3PYMPM", "TCTA", "NPB", "NPB", "TAPC", "ITO_Geomatec", "glass_Eagle2000"]
        self.refractive_index = ["Al.dat", "TPBi.dat", "TPBi.dat", "mCBP.dat", "mCBP.dat", "TCTA_B3PYMPM.dat", "TCTA.dat", "NPB.dat", "NPB.dat", "TAPC.dat", "ITO_Geomatec.dat", "glass_Eagle2000.dat"]
        self.thickness = [100, 100, 10, 20, 20, 20, 20, 30, 20, 50, 70, 0]
        self.unit = ["nm", "nm", "nm", "nm", "nm", "nm", "nm", "nm", "nm", "nm", "nm", "nm"]

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

        # i = 0
        # for j in range(len(self.layer_name)):
        #     self.table.setItem(i, 5, QtWidgets.QTableWidgetItem(j))
        #     comboBox = QComboBox()
        #     comboBox.addItem("nm")
        #     comboBox.addItem("pm")
        #     self.table.setCellWidget(i, 5, comboBox)
        #     i += 1

        self.table.horizontalHeader().setStretchLastSection(True)
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

    # def onDrawButtonClicked(self):
    #     l = self.onDraw()
    #     for k in range(int(len(l)/6) + 1):
    #         with open(file, 'w') as out:
    #             out.write(",".join(l[k * 6:(k + 1) * 6])+"\n")
    #
    # def onDraw(self):
    #     self.cell = []
    #     # row = self.table.currentRow()
    #     row = self.table.rowCount()
    #     col = self.table.columnCount()
    #     for i in range(row):
    #         for j in range(col):
    #             self.cell.append(self.table.item(i, j).text())
    #     return self.cell

    def handleSave(self):
#        with open('monschedule.csv', 'wb') as stream:
        with open(file, 'w') as stream:                  # 'w'
            writer = csv.writer(stream, lineterminator='\n')          # + , lineterminator='\n'
            for row in range(self.table.rowCount()):
                rowdata = []
                for column in range(self.table.columnCount()):
                    item = self.table.item(row, column)
                    if item is not None:
                        # rowdata.append(unicode(item.text()).encode('utf8'))
                        rowdata.append(item.text())                   # +
                    # else:
                    #     rowdata.append('')
                writer.writerow(rowdata)


class Emission_Layer(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.init_em_table()

        label = QLabel()
        label.setText("Emission Layer")
        layout.addWidget(label)

        grid = QGridLayout()
        connectButton = QPushButton('Add')
        connectButton.clicked.connect(self.onConnectButtonClicked)
        connectButton.setFixedSize(200, 30)

        removeButton = QPushButton('Delete')
        removeButton.clicked.connect(self.onRemoveButtonClicked)
        removeButton.setFixedSize(200, 30)

        drawButton = QPushButton("Save")
        drawButton.clicked.connect(self.handleSave)
        drawButton.setFixedSize(200, 30)


        grid.addWidget(connectButton, 0, 0)
        grid.addWidget(removeButton, 0, 1)
        grid.addWidget(drawButton, 0, 2)
        layout.addLayout(grid)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def init_em_table(self):
        self.table = QTableWidget()
        self.table.setRowCount(4)
        self.table.setColumnCount(7)

        cols_element = ['L#', 'EMMaterials', 'Spectrum', 'ExcitonProp', 'QY', 'PQ', 'EMZone']
        self.table.setHorizontalHeaderLabels(cols_element)

        self.em_materials = ["FCNlr", "Irppy2tmd", "Irmphmq2tmd"]
        self.spectrum = ["FCNlr", "Irppy2tmd", "Irmphmq2tmd"]
        self.exciton_prop = [1, 1, 1]
        self.qy = [90, 96, 96]
        self.pq = [75, 75, 78]
        self.em_zone = ["constant", "linear_pos", "delta_50"]
        self.tempList = [[self.em_materials, self.spectrum, self.exciton_prop,
                          self.qy, self.pq, self.em_zone]]
        self.num_row = len(self.tempList)
        self.table.setFixedSize(610, 300)

        for i in range(len(self.em_materials)):
            self.num_row = i
            self.table.setItem(self.num_row, 0, QTableWidgetItem(str(self.num_row)))
            self.table.setItem(self.num_row, 1, QTableWidgetItem(self.em_materials[i]))
            self.table.setItem(self.num_row, 2, QTableWidgetItem(self.spectrum[i]))
            self.table.setItem(self.num_row, 3, QTableWidgetItem(str(self.exciton_prop[i])))
            self.table.setItem(self.num_row, 4, QTableWidgetItem(str(self.qy[i])))
            self.table.setItem(self.num_row, 5, QTableWidgetItem(str(self.pq[i])))
            self.table.setItem(self.num_row, 6, QTableWidgetItem(str(self.em_zone[i])))

        # i = 0
        # for j in range(len(self.em_materials)):
        #     self.table.setItem(i, 6, QtWidgets.QTableWidgetItem(j))
        #     comboBox = QComboBox()
        #     comboBox.addItem("Sheet")
        #     comboBox.addItem("Constant")
        #     comboBox.addItem("Linear")
        #     comboBox.addItem("Gaussian")
        #     self.table.setCellWidget(i, 6, comboBox)
        #     i += 1

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)
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

    # def onDrawButtonClicked(self):
    #     self.cell = []
    #     row = self.table.currentRow()
    #     col = self.table.currentColumn()
    #     self.cell.append(self.table.item(row, col).text())
    #     with open(file_em, 'w') as out:
    #         out.write(self.cell[0] + "\n")

    # def onDrawButtonClicked(self):
    #     l = self.onDraw()
    #     for k in range(int(len(l)/7) + 1):
    #         with open(file_em, 'a') as out:
    #             out.write(",".join(l[k * 7:(k + 1) * 7])+"\n")
    #
    # def onDraw(self):
    #     self.cell = []
    #     # row = self.table.currentRow()
    #     row = self.table.rowCount()
    #     col = self.table.columnCount()
    #     for i in range(row):
    #         for j in range(col):
    #             self.cell.append(self.table.item(i,j).text())
    #     return self.cell

    def handleSave(self):
#        with open('monschedule.csv', 'wb') as stream:
        with open(file_em, 'w') as stream:                  # 'w'
            writer = csv.writer(stream, lineterminator='\n')          # + , lineterminator='\n'
            for row in range(self.table.rowCount()):
                rowdata = []
                for column in range(self.table.columnCount()):
                    item = self.table.item(row, column)
                    if item is not None:
                        # rowdata.append(unicode(item.text()).encode('utf8'))
                        rowdata.append(item.text())                   # +
                    # else:
                    #     rowdata.append('')
                writer.writerow(rowdata)


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
        radiobutton.type = "x = a"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 2, 0)

        radiobutton = QRadioButton("Linear")
        radiobutton.type = "y = ax+b"
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
