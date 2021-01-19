import csv
import math
import os

from PyQt5 import QtCore, QtWidgets
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from PyQt5.QtGui import QFont
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from Qtcontrollers.logo_image import *

file = 'resources/text.csv'
file_em = 'resources/text_em.csv'
file_emz = 'resources/text_emz.txt'
file_p = 'resources/text_p.csv'
path_p = 'resources/properties'
em_figure = 'resources/EML_graph.png'
project_info = 'resources/project_info.csv'
arrow = 'resources/arrow.png'


class Elements_Structure(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.setContentsMargins(0,0,0,0)

        label = QLabel()
        label.setText("Elements Structure")
        label.setFont(QFont("Arial", 15, weight=QFont.Bold))
        layout.addWidget(label)

        grid = QGridLayout()
        connectButton = QPushButton('Add')
        connectButton.clicked.connect(self.onConnectButtonClicked)
        connectButton.setFixedSize(230, 30)

        removeButton = QPushButton('Delete')
        removeButton.clicked.connect(self.onRemoveButtonClicked)
        removeButton.setFixedSize(230, 30)

        es_table = self.init_es_table()
        drawButton = QPushButton("Save")
        drawButton.clicked.connect(self.handleSave)
        drawButton.setFixedSize(230, 30)

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
        self.table.setColumnCount(7)
        self.cols_element = ['L#', 'LayerName', 'Material', 'RefractiveIndex', 'Thickness', 'Unit' ,'Properties']
        self.table.setHorizontalHeaderLabels(self.cols_element)

        self.layer_name = ["Al", "TPBi", "TPBi", "mCBP", "mCBP", "TCTA_B3PYMPM", "TCTA", "NPB", "NPB", "TAPC", "ITO_Geomatec", "glass_Eagle2000"]
        self.material = ["Al", "TPBi", "TPBi", "mCBP", "mCBP", "TCTA_B3PYMPM", "TCTA", "NPB", "NPB", "TAPC", "ITO_Geomatec", "glass_Eagle2000"]
        self.refractive_index = ["Al.dat", "TPBi.dat", "TPBi.dat", "mCBP.dat", "mCBP.dat", "TCTA_B3PYMPM.dat", "TCTA.dat", "NPB.dat", "NPB.dat", "TAPC.dat", "ITO_Geomatec.dat", "glass_Eagle2000.dat"]

        self.thickness = [100, 100, 10, 20, 20, 20, 20, 30, 20, 50, 70, 0]
        self.tempList = [[self.layer_name, self.material, self.thickness]]
        self.num_row = len(self.tempList)
        self.table.setFixedSize(700, 250)

        for i in range(len(self.layer_name)):
            self.num_row = i
            self.table.setItem(self.num_row, 0, QTableWidgetItem(str(self.num_row)))
            self.table.setItem(self.num_row, 1, QTableWidgetItem(self.layer_name[i]))
            self.table.setItem(self.num_row, 2, QTableWidgetItem(self.material[i]))
            self.table.setItem(self.num_row, 4, QTableWidgetItem(str(self.thickness[i])))

        i = 0
        for j in range(len(self.layer_name)):
            self.table.setItem(i, 3, QTableWidgetItem(j))
            label = QLabel()
            layout = QHBoxLayout()
            layout.setContentsMargins(0,0,0,0)

            ri_name = self.refractive_index[j]

            another_label = QLabel()
            another_label.setText(ri_name)
            layout.addWidget(another_label)

            button = QPushButton()
            button.setText("b")
            button.setFixedSize(30, 30)
            layout.addWidget(button)

            label.setLayout(layout)
            self.table.setCellWidget(i, 3, label)

            self.table.setItem(i, 5, QTableWidgetItem(j))
            measure = QComboBox()
            measure.addItems(["nm", "um", "pm"])
            self.table.setCellWidget(i, 5, measure)

            self.table.setItem(i, 6, QTableWidgetItem(j))
            selectButton = QPushButton()
            selectButton.setText("Settings")
            selectButton.setFixedSize(140, 20)
            selectButton.clicked.connect(self.saveDirectory)
            self.table.setCellWidget(i, 6, selectButton)
            i += 1

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.Stretch)


        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setSelectionMode(QAbstractItemView.MultiSelection)
        return self.table

    def saveDirectory(self):
        real_path = []
        for item in self.layer_name:
            path = os.getcwd()
            path_interim = os.path.join(path, path_p)
            path_real = os.path.join(path_interim, item)+".csv"
            real_path.append(path_real)

        for property_path in real_path:
            with open(property_path, 'w') as stream:
                writer = csv.writer(stream, lineterminator='\n')
                for row in self.read_csv():
                    writer.writerow(row)

    def read_csv(self):
        data = []
        with open(file_p, 'r') as f:
            rows = f.readlines()
            rows = list(map(lambda x: x.strip(), rows))
            for row in rows:
                row = row.split(',')
                data.append(row)
        return data

    def onConnectButtonClicked(self):
        self.currentRowCount = self.table.rowCount()
        self.table.insertRow(self.currentRowCount)

    @QtCore.pyqtSlot()
    def onRemoveButtonClicked(self):
        button = self.sender()
        if button:
            row = self.table.indexAt(button.pos()).row()
            self.table.removeRow(row)

    def handleSave(self):
        with open(file, 'w') as stream:
            writer = csv.writer(stream, lineterminator='\n')
            for row in range(self.table.rowCount()):
                rowdata = []
                for column in range(self.table.columnCount()):
                    item = self.table.item(row, column)
                    if item is not None:
                        rowdata.append(item.text())
                writer.writerow(rowdata)


class Emission_Layer(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.init_em_table()

        label = QLabel()
        label.setText("Emission Layer")
        label.setFont(QFont("Arial", 15, weight=QFont.Bold))
        layout.addWidget(label)

        grid = QGridLayout()
        connectButton = QPushButton('Add')
        connectButton.clicked.connect(self.onConnectButtonClicked)
        connectButton.setFixedSize(230, 30)

        removeButton = QPushButton('Delete')
        removeButton.clicked.connect(self.onRemoveButtonClicked)
        removeButton.setFixedSize(230, 30)

        drawButton = QPushButton("Save")
        drawButton.clicked.connect(self.handleSave)
        drawButton.setFixedSize(230, 30)


        grid.addWidget(connectButton, 0, 0)
        grid.addWidget(removeButton, 0, 1)
        grid.addWidget(drawButton, 0, 2)
        layout.addLayout(grid)
        layout.addWidget(self.table)
        self.setLayout(layout)

    def init_em_table(self):
        self.table = QTableWidget()
        self.table.setRowCount(4)
        self.table.setColumnCount(8)

        cols_element = ['L#', 'EMMaterials', 'Spectrum', 'Exciton Prop', 'QY', 'HDR', 'EMZone', 'Properties']
        self.table.setHorizontalHeaderLabels(cols_element)

        self.num = [4, 6, 8]
        self.em_materials = ["FCNlr", "Irppy2tmd", "Irmphmq2tmd"]
        self.spectrum = ["FCNlr", "Irppy2tmd", "Irmphmq2tmd"]
        self.exciton_prop = [1, 1, 1]
        self.qy = [90, 96, 96]
        self.pq = [75, 75, 78]
        self.em_zone = ["constant", "linear_pos", "delta_50"]
        self.tempList = [[self.em_materials, self.spectrum, self.exciton_prop,
                          self.qy, self.pq, self.em_zone]]
        self.num_row = len(self.tempList)
        self.table.setFixedSize(700, 140)

        for i in range(len(self.em_materials)):
            self.num_row = i
            self.table.setItem(self.num_row, 0, QTableWidgetItem(str(self.num[i])))
            self.table.setItem(self.num_row, 1, QTableWidgetItem(self.em_materials[i]))
            self.table.setItem(self.num_row, 2, QTableWidgetItem(self.spectrum[i]))
            self.table.setItem(self.num_row, 3, QTableWidgetItem(str(self.exciton_prop[i])))
            self.table.setItem(self.num_row, 4, QTableWidgetItem(str(self.qy[i])))
            self.table.setItem(self.num_row, 5, QTableWidgetItem(str(self.pq[i])))
            self.table.setItem(self.num_row, 6, QTableWidgetItem(str(self.em_zone[i])))


        i = 0
        for j in range(len(self.em_materials)):
            self.table.setItem(i, 7, QTableWidgetItem(j))
            selectButton = QPushButton()
            selectButton.setText("Settings")
            selectButton.setFixedSize(230, 20)
            # selectButton.clicked.connect(self.saveDirectory)
            self.table.setCellWidget(i, 7, selectButton)
            i += 1

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(6, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(7, QtWidgets.QHeaderView.Stretch)
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

    def handleSave(self):
        with open(file_em, 'w') as stream:
            writer = csv.writer(stream, lineterminator='\n')
            for row in range(self.table.rowCount()):
                rowdata = []
                for column in range(self.table.columnCount()):
                    item = self.table.item(row, column)
                    if item is not None:
                        rowdata.append(item.text())
                writer.writerow(rowdata)


class Emission_Zone_Setting(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        layout1 = QGridLayout()
        layout2 = QGridLayout()

        layout.addLayout(layout1)
        layout.addLayout(layout2)

        self.setLayout(layout)

        label = QLabel()
        label.setText("Emission Zone Setting")
        label.setFont(QFont("Arial", 15, weight=QFont.Bold))
        label.setFixedSize(180, 20)
        layout1.addWidget(label, 0, 0)

        textLine_emit = QLineEdit()
        textLine_emit.setFixedSize(100, 20)
        textLine_emit.setText("0,100,10")
        layout1.addWidget(textLine_emit, 1, 2)

        label = QLabel()
        label.setText("Value a :")
        layout1.addWidget(label, 2, 1)

        self.textLine_a = QLineEdit()
        self.textLine_a.setFixedSize(100, 20)
        self.textLine_a.setText("0.5")
        layout1.addWidget(self.textLine_a, 2, 2)

        label = QLabel()
        label.setText("Value b :")
        layout1.addWidget(label, 3, 1)

        self.textLine_b = QLineEdit()
        self.textLine_b.setFixedSize(100, 20)
        self.textLine_b.setText("1")
        layout1.addWidget(self.textLine_b, 3, 2)

        label = QLabel()
        label.setText("Value c :")
        label.setFixedSize(100, 20)
        layout1.addWidget(label, 4, 1)

        self.textLine_c = QLineEdit()
        self.textLine_c.setFixedSize(100, 20)
        self.textLine_c.setText("2")
        layout1.addWidget(self.textLine_c, 4, 2)

        self.radiobutton_sheet = QRadioButton("Sheet")
        self.radiobutton_sheet.setChecked(True)
        self.radiobutton_sheet.type = "x = %s" %(self.textLine_a.text())
        self.radiobutton_sheet.toggled.connect(self.onClicked)
        layout1.addWidget(self.radiobutton_sheet, 1, 0)

        self.radiobutton_constant = QRadioButton("Constant")
        self.radiobutton_constant.type = "%s" %(self.textLine_a.text())
        self.radiobutton_constant.toggled.connect(self.onClicked)
        layout1.addWidget(self.radiobutton_constant, 2, 0)

        self.radiobutton_linear = QRadioButton("Linear")
        self.radiobutton_linear.type = "%s*x + %s" %(self.textLine_a.text(), self.textLine_b.text())
        self.radiobutton_linear.toggled.connect(self.onClicked)
        layout1.addWidget(self.radiobutton_linear, 3, 0)

        self.radiobutton_gaussian = QRadioButton("Exponential")
        self.radiobutton_gaussian.type = "%s*math.exp(%s + x) + %s" %(self.textLine_a.text(), self.textLine_b.text(), self.textLine_c.text())
        self.radiobutton_gaussian.toggled.connect(self.onClicked)
        layout1.addWidget(self.radiobutton_gaussian, 4, 0)

        self.radiobutton_gaussian = QRadioButton("Gaussian")
        self.radiobutton_gaussian.type = "(%s*(math.sqrt(2*math.pi)))**(-1)*math.exp((x-%s)/(2*%s**2))" \
                                         %(self.textLine_b.text(), self.textLine_a.text(), self.textLine_b.text())
        self.radiobutton_gaussian.toggled.connect(self.onClicked)
        layout1.addWidget(self.radiobutton_gaussian, 5, 0)

        label = QLabel()
        label.setText("Emit Range(nm): ")
        label.setFixedSize(100, 20)
        layout1.addWidget(label, 1, 1)

        # drawButton = QPushButton("Save")
        # drawButton.clicked.connect(self.drawPic)
        # drawButton.setFixedSize(110, 30)
        # layout1.addWidget(drawButton, 5, 2)

        drawButton = QPushButton("Draw")
        drawButton.clicked.connect(self.arrow)
        drawButton.setFixedSize(110, 30)
        layout1.addWidget(drawButton, 6, 2)


        label = QLabel()
        label.setText("Equation: ")
        label.setFixedSize(100, 20)
        layout1.addWidget(label, 7, 0)

        self.qlabel = QTextEdit()
        self.qlabel.setFixedSize(220, 40)
        self.qlabel.setText("x = %s" %(self.textLine_a.text()))
        layout1.addWidget(self.qlabel, 7, 1)

        label = QLabel()
        label.setText("Emission Zone Graph")
        label.setFont(QFont("Arial", 15, weight=QFont.Bold))
        layout2.addWidget(label, 0, 0)

        arrow = self.arrow()
        layout2.addWidget(arrow, 1, 0)

        self.RIList = pd.read_csv(file, header=None)
        self.RI_name = []
        self.RI_data = []
        # self.RIList.itemSelectionChanged.connect(self.chkItemClicked)
        self.readData()
        self.initPlot()

    def arrow(self):
        label = QLabel()
        pixmap = QPixmap(em_figure)
        pixmap = pixmap.scaled(330, 330, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        return label

    def handleSave(self):
        with open(file_emz, 'w') as stream:
            writer = csv.writer(stream, lineterminator='\n')
            rowdata = [self.qlabel.text()]
            writer.writerow(rowdata)

    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.qlabel.setText(radioButton.type)

    def drawPic(self):
        equation = open(file_emz, "r").readline()
        plt.axvline(equation)
        plt.xlabel("Emit Range(nm)")
        # equation = open(file_emz, "r").readline()
        # x_range = 1
        # x = np.array(x_range)
        # y = eval(equation)   # need modoule math
        # plt.plot(x, y)
        # plt.show()
        plt.savefig(em_figure, transparent=True)


    def readData(self):
        path = os.path.join(os.getcwd(), "c/data/Refractive_index")
        files = os.listdir(path)

        for file in files:
            t = file.split('.')
            if len(t) < 2:
                pass
            elif t[1] != 'ri':
                pass
            else:
                self.RI_name.append(t[0])
                # self.RIList.addItem(t[0])
                # file open
                file_path = os.path.join(path, file)
                f = open(file_path, 'r')
                data = []
                while True:
                    line = f.readline()
                    if not line:
                        break
                    line = line.rstrip()
                    tt = line.split('\t')
                    if len(tt) != 3:
                        pass
                    try:
                        tt = list(map(float, tt))
                        data.append(tt)
                    except ValueError:
                        pass

                data_ = np.array(data)
                # print(data_)
                self.RI_data.append(data_)
                f.close()

    def initPlot(self):
        self.fig = plt.Figure()
        self.canvas = FigureCanvas(self.fig)
        layout = QHBoxLayout()
        layout.layoutLeftMargin = 0
        layout.layoutRightMargin = 0
        layout.layoutTopMargin = 0
        layout.layoutBottomMargin = 0
        layout.addWidget(self.canvas)

    def updatePlotAndTable(self, name):
        self.fig.clear()

        idx = self.RI_name.index(name)
        data = self.RI_data[idx]

        wavelength = np.around(data[:, 0], decimals=1)
        wavelength = wavelength.astype(np.int64)
        n = np.round(data[:, 1], 4)
        if len(data[0]) == 2:
            k = None
        else:
            k = np.round(data[:, 2], 4)

        self.tableWidget.setRowCount(0)
        count = len(n)

        if k is None:
            for i in range(count):
                self.addData(wavelength[i], n[i], '')
        else:
            for i in range(count):
                self.addData(wavelength[i], n[i], k[i])

        ax = self.fig.add_subplot()
        ax.set_title(name)
        ax.set_xlabel('Wavelength(nm)')
        ax.set_ylabel('Refractive Index n')
        ax.set_xlim(min(wavelength), max(wavelength))
        ax.set_ylim(min(n), max(n) * 1.1)
        ax.xaxis.grid(True)
        ax.yaxis.grid(True)

        line, = ax.plot([], [], 'r-', label="n", linewidth=2.0)
        line.set_data(wavelength, n)

        if k is not None:
            ax2 = ax.twinx()
            ax2.set_ylabel('Extinction coefficient k', rotation=270, labelpad=20)
            ax2.set_ylim(min(k), max(k) * 1.1)
            line2, = ax2.plot([], [], 'b-', label='k', linewidth=2.0)
            line2.set_data(wavelength, k)

        self.fig.legend()
        self.fig.tight_layout()
        self.canvas.draw()


class Properties(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        label = QLabel()
        label.setText("Properties")
        layout.addWidget(label, 0, 0)

        label = QLabel()
        label.setText("Wavelength Range (nm): ")
        layout.addWidget(label, 1, 0)

        self.lineEdit_wave = QLineEdit()
        self.lineEdit_wave.setFixedSize(230, 20)
        self.lineEdit_wave.setText("400,700,5")
        layout.addWidget(self.lineEdit_wave, 1, 1)

        label = QLabel()
        label.setText("Angle Range (degree): ")
        layout.addWidget(label, 2, 0)

        self.lineEdit_angle = QLineEdit()
        self.lineEdit_angle.setFixedSize(230, 20)
        self.lineEdit_angle.setText("0,90,10")
        layout.addWidget(self.lineEdit_angle, 2, 1)

        label = QLabel()
        label.setText("Calculation Types:")
        layout.addWidget(label, 3, 0)

        self.checkBox_mode = QCheckBox()
        self.checkBox_mode.setText("Mode Analysis")
        self.checkBox_mode.setCheckState(True)
        layout.addWidget(self.checkBox_mode, 3, 1)

        self.checkBox_emission = QCheckBox()
        self.checkBox_emission.setText("Emission Spectrum")
        self.checkBox_emission.setCheckState(True)
        layout.addWidget(self.checkBox_emission, 4, 1)

        self.checkBox_power = QCheckBox()
        self.checkBox_power.setText("Power Dissipation Curve")
        self.checkBox_power.setCheckState(True)
        layout.addWidget(self.checkBox_power, 5, 1)

        self.setLayout(layout)