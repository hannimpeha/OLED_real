from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data_polar_plot = "output/#3-2/angular_intensity/output_angular_intensity_bottom.txt"
polar_plot = 'resources/polar_plot.png'
plotting_option = 'resources/plotting_option.csv'

class Axes_Properties(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel()
        label.setText("Axes Properties")
        label.setFixedSize(100, 20)
        layout.addWidget(label)

        table = self.making_table()
        layout.addWidget(table)

        button_plot = QPushButton()
        button_plot.setText("Plot")
        button_plot.setFixedSize(700, 80)
        button_plot.clicked.connect(self.making_image)
        layout.addWidget(button_plot)

        image = self.making_image()

        layout.addWidget(image)
        self.setLayout(layout)

    def making_table(self):
        self.table = QTableWidget()
        self.table.setRowCount(3)
        self.table.setColumnCount(5)
        cols_element = ["Axis", 'Name', 'Minimum', 'Maximum', "Remark"]
        self.table.setHorizontalHeaderLabels(cols_element)

        self.axis = ["X-axis", "Y-axis", "Z-axis"]

        data = pd.read_csv(plotting_option, header=None, skiprows=[0])
        data.fillna("-", inplace=True)
        self.name = data[0].astype(str).tolist()

        min_max = []
        for i in range(len(self.name)):
            if self.name[i] == "Thickness of b3p":
                min_max.append([10, 50])
            elif self.name[i] == "Thickness of npb":
                min_max.append([10, 50])

            elif self.name[i] == "Optical Modes":
                min_max.append([0.1, 0.3])
            elif self.name[i] == "Air Mode":
                min_max.append([0.1, 0.3])
            elif self.name[i] == "Substrate-Guided Mode":
                min_max.append([0.1, 0.3])
            elif self.name[i] == "Wave-Guided Mode":
                min_max.append([0.1, 0.3])
            elif self.name[i] == "SPP Mode":
                min_max.append([0.1, 0.3])
            elif self.name[i] == "Absorption":
                min_max.append([0.1, 0.3])
            elif self.name[i] == "NR Losses":
                min_max.append([0.1, 0.3])

            elif self.name[i] == "Wavelength":
                min_max.append([400, 700])
            elif self.name[i] == "Angle":
                min_max.append([0, 90])

            elif self.name[i] == "Cd/A (photometry)":
                min_max.append([11.5, 28.6])
            elif self.name[i] == "W/mA/sr (radiometry)":
                min_max.append([71, 217])

            elif self.name[i] == "Intensity":
                min_max.append([0.0, 3.0])
            elif self.name[i] == "Intensity (p-pol)":
                min_max.append([0.0, 3.0])
            elif self.name[i] == "Intensity (h-dipole, p-pol)":
                min_max.append([0.0, 3.0])
            elif self.name[i] == "Intensity (v-dipole, p-pol)":
                min_max.append([0.0, 3.0])

            elif self.name[i] == "In-plane Wavevector":
                min_max.append([0.0, 1.96])

            elif self.name[i] == "Dissipated Power":
                min_max.append([0, 412])
            elif self.name[i] == "Dissipated Power (p-pol)":
                min_max.append([0, 412])
            elif self.name[i] == "Dissipated Power (s-pol)":
                min_max.append([0, 412])

            elif self.name[i] == "Effective Quantum Efficiency":
                min_max.append([0.77, 0.87])
            elif self.name[i] == "Purcell Factor":
                min_max.append([0.87, 1.67])
            else:
                min_max.append(["-","-"])

        # text = pd.read_csv(plotting_option).columns.tolist()[0] # later in labels of graph
        mat = np.array(min_max).transpose()
        self.min = mat[0]
        self.max = mat[1]


        self.remark = ["-","-","-"]
        self.tempList = [[self.axis, self.name, self.min, self.max, self.remark]]
        self.num_row = len(self.tempList)
        self.table.setFixedSize(700, 110)

        for i in range(len(self.axis)):
            self.num_row = i
            self.table.setItem(self.num_row, 0, QTableWidgetItem(self.axis[i]))
            self.table.setItem(self.num_row, 1, QTableWidgetItem(self.name[i]))
            self.table.setItem(self.num_row, 2, QTableWidgetItem(str(self.min[i])))
            self.table.setItem(self.num_row, 3, QTableWidgetItem(str(self.max[i])))
            self.table.setItem(self.num_row, 4, QTableWidgetItem(self.remark[i]))

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(4, QtWidgets.QHeaderView.Stretch)
        return self.table

    def making_image(self):
        label = QLabel()
        pixmap = QPixmap(polar_plot)
        pixmap = pixmap.scaled(700, 700, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        return label

    def plotting(self):
        data = np.genfromtxt(data_polar_plot, unpack=True)
        theta = np.linspace(0, np.pi / 2, 10)
        r = np.cos(theta)
        r_data = data
        # fig = plt.figure()
        ax = plt.figure().add_subplot(111, polar=True)
        ax.set_thetamin(0)
        ax.set_thetamax(90)

        ax.scatter(theta, r_data)
        ax.scatter(theta, r)

        plt.title("Polar Plot")

        plt.gca().invert_xaxis()
        plt.gca().invert_yaxis()
        plt.savefig(polar_plot, transparent=True)