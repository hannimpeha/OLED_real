from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QComboBox, QTableWidget, QTableWidgetItem, QLineEdit, \
    QPushButton, QCheckBox, QHBoxLayout, QAbstractItemView
import numpy as np
import matplotlib.pyplot as plt

logo_image = 'Qtcontrollers/resources/Logo.png'
data_path = "output/#3-2/CIE/output_CIE_bottom.txt"
data_path2 = "output/#3-2/angular_intensity/output_angular_intensity_bottom.txt"
graph = 'Qtcontrollers/resources/Graph.png'


class Plotting_Param(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        logo_image = self.logo_image()
        plotting = Plotting()
        exportation = Exportation()

        layout.addWidget(logo_image, 0, 0)
        layout.addWidget(plotting, 1, 0)
        layout.addWidget(exportation, 2, 0)
        self.setLayout(layout)

    def logo_image(self):
        label = QLabel()
        pixmap = QPixmap(logo_image)
        pixmap = pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        return label


class Plotting(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        label = QLabel()
        label.setText("Plotting")
        layout.addWidget(label, 0, 0)

        hlayout = QHBoxLayout()
        self.qlabel = QLabel()
        self.qlabel.setText("Graph: ")

        xcombo = QComboBox()
        xcombo.addItems(["Emission Spectrum (3D)", "Pear", "Lemon", "Apple"])
        #xcombo.activated[str].connect(self.onChanged)
        xcombo.setFixedSize(330, 20)
        hlayout.addWidget(self.qlabel)
        hlayout.addWidget(xcombo)
        layout.addLayout(hlayout, 1, 0)

        hlayout = QHBoxLayout()
        self.qlabel_x = QLabel()
        self.qlabel_x.setText("X-axis: ")
        xcombo = QComboBox()
        xcombo.addItems(["Angle", "Pear", "Lemon", "Apple"])
        xcombo.setFixedSize(330, 20)
        #xcombo.activated[str].connect(self.onChanged)
        hlayout.addWidget(self.qlabel_x)
        hlayout.addWidget(xcombo)
        layout.addLayout(hlayout, 2, 0)

        hlayout = QHBoxLayout()
        self.qlabel_y = QLabel()
        self.qlabel_y.setText("Y-axis: ")
        ycombo = QComboBox()
        ycombo.addItems(["Wavelength","Pear", "Lemon", "Apple"])
        ycombo.setFixedSize(330, 20)
        #ycombo.activated[str].connect(self.onChanged)
        hlayout.addWidget(self.qlabel_y)
        hlayout.addWidget(ycombo)
        layout.addLayout(hlayout, 3, 0)

        hlayout = QHBoxLayout()
        self.qlabel_z = QLabel()
        self.qlabel_z.setText("Z-axis: ")
        zcombo = QComboBox()
        zcombo.addItems(["Intensity", "Pear", "Lemon", "Apple"])
        zcombo.setFixedSize(330, 20)
        #zcombo.activated[str].connect(self.onChanged)
        hlayout.addWidget(self.qlabel_z)
        hlayout.addWidget(zcombo)
        layout.addLayout(hlayout, 4, 0)

        label = QLabel()
        label.setText("Fixed Parameters:")
        layout.addWidget(label, 5, 0)
        table = self.making_table()

        layout.addWidget(table, 6, 0)

        hlayout = QHBoxLayout()
        btn = QPushButton()
        btn.setText("Plot")
        btn.clicked.connect(self.onButtonClickedPlot)
        hlayout.addWidget(btn)

        btn = QPushButton()
        btn.setText("Clear")
        hlayout.addWidget(btn)
        layout.addLayout(hlayout, 7, 0)

        self.setLayout(layout)

    def onButtonClickedPlot(self):
        # data = np.loadtxt(data_path, unpack=True)
        # index = np.array(range(0, 100, 10))
        # # labels = ('x', 'y', 'z')
        # dic = {k: v for k, v in (zip(index, np.transpose(data)))}
        #
        # x_dic = {k: v[0] for k, v in dic.items()}
        # y_dic = {k: v[1] for k, v in dic.items()}
        # z_dic = {k: v[2] for k, v in dic.items()}
        #
        # ds = [x_dic, y_dic, z_dic]
        # d = {}
        # for k in x_dic.keys():
        #     d[k] = tuple(d[k] for d in ds)
        #
        # sds = MultiSpectralDistributions(d)
        # plot = plot_chromaticity_diagram_CIE1931()
        # write_image(plot, graph)

        data = np.genfromtxt(data_path2, unpack=True)
        theta = np.linspace(0, np.pi / 2, 10)
        r = np.cos(theta)
        r_data = data
        fig = plt.figure()
        ax = fig.add_subplot(111, polar=True)
        ax.set_thetamin(0)
        ax.set_thetamax(90)

        ax.scatter(theta, r)
        ax.scatter(theta, r_data)

        fig.savefig(graph, transparent=True)


    def onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()


    def making_table(self):
        self.table = QTableWidget()
        self.table.setRowCount(16)
        self.table.setColumnCount(2)
        cols_element = ['1', '2']
        self.table.setHorizontalHeaderLabels(cols_element)

        self.x = ["Thickness of B3PYMPM", "Thickness of TAPC"]
        self.y = ["50", "50"]
        self.tempList = [[self.x, self.y]]
        self.num_row = len(self.tempList)
        self.table.setFixedSize(380, 180)

        for i in range(len(self.x)):
            self.num_row = i
            self.table.setItem(self.num_row, 0, QTableWidgetItem(self.x[i]))
            self.table.setItem(self.num_row, 1, QTableWidgetItem(self.y[i]))

        self.table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        return self.table


class Exportation(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()

        label = QLabel()
        label.setText("Exportation")
        layout.addWidget(label, 0, 0)

        hlayout = QHBoxLayout()
        label = QLabel()
        label.setText("Path: ")
        hlayout.addWidget(label)

        lineEdit = QLineEdit()
        lineEdit.setFixedSize(200, 20)
        hlayout.addWidget(lineEdit)

        btn = QPushButton()
        btn.setText("Browse")
        hlayout.addWidget(btn)

        layout.addLayout(hlayout, 1, 0)

        hlayout = QHBoxLayout()
        label = QLabel()
        label.setText("Type: ")
        hlayout.addWidget(label)

        check_text = QCheckBox()
        check_text.setText("Text")
        check_text.setChecked(False)
        check_text.setStyleSheet("QCheckBox::indicator { width: 20px; height: 20px;}")
        hlayout.addWidget(check_text)

        check_image = QCheckBox()
        check_image.setText("Image")
        check_text.setChecked(False)
        check_image.setStyleSheet("QCheckBox::indicator { width: 20px; height: 20px;}")
        hlayout.addWidget(check_image)

        #hlayout.setAlignment(QtCore.Qt.AlignLeft)

        layout.addLayout(hlayout, 2, 0)

        hlayout = QHBoxLayout()
        label = QLabel()
        label.setText("Name: ")
        hlayout.addWidget(label)

        lineEdit = QLineEdit()
        lineEdit.setFixedSize(200, 20)
        hlayout.addWidget(lineEdit)

        btn = QPushButton()
        btn.setText("Export")
        hlayout.addWidget(btn)

        layout.addLayout(hlayout, 3, 0)
        self.setLayout(layout)
