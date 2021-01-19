from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
import pandas as pd


image = 'resources/Graph.png'
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
        button = QPushButton()
        button.setText("Plot")
        button.setFixedSize(620, 87)
        image = self.making_image()
        layout.addWidget(table)
        layout.addWidget(button)
        layout.addWidget(image)
        self.setLayout(layout)

    def making_table(self):
        self.table = QTableWidget()
        self.table.setRowCount(3)
        self.table.setColumnCount(5)
        cols_element = ["Axis", 'Name', 'Min', 'Max', "Remark"]
        self.table.setHorizontalHeaderLabels(cols_element)

        self.axis = ["X-axis", "Y-axis", "Z-axis"]

        data = pd.read_csv(plotting_option, header=None, skiprows=[0])
        data.fillna("-", inplace=True)
        data[0].astype(str).tolist()
        self.name = data[0].astype(str).tolist()


        thicknesss_of_b3p = [10, 50]
        thickness_of_npb = [10, 50]

        optical_mode = [0.1, 0.3]
        air_mode = [0.1, 0.3]
        substrate_guided_mode = [0.1, 0.3]
        wave_guided_mode = [0.1, 0.3]
        spp_mode = [0.1, 0.3]
        absorption = [0.1, 0.3]
        nr_losses = [0.1, 0.3]

        wavelength = [400, 700]
        angle = [0, 90]

        cd_a_phtometry = [11.5, 28.6]
        w_ma_sr_radiometry = [71, 217]

        intensity = [0.0, 3.0]
        intensity_p_pol = [0.0, 3.0]
        intensity_s_pol = [0.0, 3.0]
        intensity_h_dipole_p_pol = [0.0, 3.0]
        intensity_v_dipole_p_pol = [0.0, 3.0]

        in_plane_wavevector = [0.0, 1.96]

        dissipated_power = [0, 412]
        dissipated_power_p_pol = [0, 412]
        dissipated_power_s_pol = [0, 412]

        effective_quantum_efficiency = [0.77, 0.87]
        purcell_factor = [0.87, 1.67]

        # Into the Unknown
        power_function = [0, 100]
        power_coupling = [0, 100]
        none = ["-", "-"]

        text = pd.read_csv(plotting_option).columns.tolist()[0]


        self.min = ["0" , "400", "0"]
        self.max = ["90", "700", "2.35"]


        self.remark = ["-","-","-"]
        self.tempList = [[self.axis, self.name, self.min, self.max, self.remark]]
        self.num_row = len(self.tempList)
        self.table.setFixedSize(610, 110)

        for i in range(len(self.axis)):
            self.num_row = i
            self.table.setItem(self.num_row, 0, QTableWidgetItem(self.axis[i]))
            self.table.setItem(self.num_row, 1, QTableWidgetItem(self.name[i]))
            self.table.setItem(self.num_row, 2, QTableWidgetItem(self.min[i]))
            self.table.setItem(self.num_row, 3, QTableWidgetItem(self.max[i]))
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
        pixmap = QPixmap(image)
        pixmap = pixmap.scaled(610, 610, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        return label
