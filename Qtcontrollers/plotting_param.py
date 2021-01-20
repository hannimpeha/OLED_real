import csv
import os

import shutil
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import *

polar_plot = 'resources/polar_plot.png'
logo_image = 'resources/Logo.png'
graph = 'resources/polar_plot.png'
project_info = 'resources/project_info.csv'
result = 'resources/result.csv'
plotting_option = 'resources/plotting_option.csv'
data_polar_plot = "output/#3-2/angular_intensity/output_angular_intensity_bottom.txt"


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
        label.setFont(QFont("Arial", 15, weight=QFont.Bold))
        layout.addWidget(label, 0, 0)

        self.qlabel = QLabel()
        self.qlabel.setText("Graph: ")

        self.combo = QComboBox()
        layout.addWidget(self.combo, 1, 0)

        self.combo_x = QComboBox()
        layout.addWidget(self.combo_x, 2, 0)

        self.combo_y = QComboBox()
        layout.addWidget(self.combo_y, 3, 0)

        self.combo_z = QComboBox()
        layout.addWidget(self.combo_z, 4, 0)

        self.combo.addItem("Mode Analysis (2D)", ["Thickness of b3p", "Thickness of npb"])
        self.combo.addItem("Mode Analysis (3D)", ["Thickness of b3p", "Thickness of npb"])
        self.combo.addItem("Current Efficiency (2D)", ["Thickness of b3p", "Thickness of npb"])
        self.combo.addItem("Current Efficiency (3D)", ["Thickness of b3p", "Thickness of npb"])
        self.combo.addItem("Emission Spectrum (2D)", ["Wavelength", "Angle"])
        self.combo.addItem("Emission Spectrum (3D)", ["Wavelength", "Angle"])
        self.combo.addItem("Power Dissipation Curve (2D)", ["In-plane Wavevector"])
        self.combo.addItem("Power Dissipation Curve (3D)", ["In-plane Wavevector"])
        self.combo.addItem("Microcavity Effect", ["Wavelength", "Angle"])
        self.combo.addItem("CIE 1931")
        self.combo.addItem("Polar Plot")

        self.combo.currentIndexChanged.connect(self.indexChangedx)
        self.combo_x.currentIndexChanged.connect(self.indexChangedy)
        self.combo_y.currentIndexChanged.connect(self.indexChangedz)
        self.combo_z.currentIndexChanged.connect(self.indexChanged)

        self.indexChangedx(self.combo.currentIndex())
        self.indexChangedy(self.combo_x.currentIndex())
        self.indexChangedz(self.combo_y.currentIndex())

        label = QLabel()
        label.setText("Fixed Parameters:")
        layout.addWidget(label, 5, 0)

        self.table = QTableWidget()
        self.table.setRowCount(10)
        self.table.setColumnCount(2)
        cols_element = ['Name', 'Measure']
        self.table.setHorizontalHeaderLabels(cols_element)

        self.tempList = [[self.x, self.y]]
        self.num_row = len(self.tempList)
        self.table.setFixedSize(400, 200)

        self.table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        layout.addWidget(self.table, 6, 0)

        btn = QPushButton()
        btn.setFixedSize(410, 30)
        btn.setText("Save")
        btn.clicked.connect(self.onButtonClickedPlot)
        layout.addWidget(btn, 7, 0)

        self.setLayout(layout)

    def indexChangedx(self, index):
        self.combo_x.clear()
        data = self.combo.itemData(index)
        if data is not None:
            if self.combo.currentText() == "Mode Analysis (2D)":
                self.combo_x.addItem("Thickness of b3p", ["Optical Modes", "Air Mode",
                                                          "Substrate-Guided Mode",
                                                          "Wave-Guided Mode", "SPP Mode",
                                                          "Absorption", "NR Losses"])
                self.combo_x.addItem("Thickness of npb", ["Optical Modes", "Air Mode",
                                                          "Substrate-Guided Mode",
                                                          "Wave-Guided Mode", "SPP Mode",
                                                          "Absorption", "NR Losses"])
            elif self.combo.currentText() == "Mode Analysis (3D)":
                self.combo_x.addItem("Thickness of b3p", ["Thickness of npb"])
                self.combo_x.addItem("Thickness of npb", ["Thickness of bp3"])

            elif self.combo.currentText() == "Current Efficiency (2D)":
                self.combo_x.addItem("Thickness of b3p", ["Cd/A (photometry)", "W/mA/sr (radiometry)"])
                self.combo_x.addItem("Thickness of npb", ["Cd/A (photometry)", "W/mA/sr (radiometry)"])

            elif self.combo.currentText() == "Current Efficiency (3D)":
                self.combo_x.addItem("Thickness of b3p", ["Thickness of npb"])
                self.combo_x.addItem("Thickness of npb", ["Thickness of bp3"])

            elif self.combo.currentText() == "Emission Spectrum (2D)":
                self.combo_x.addItem("Wavelength", ["Intensity", "Intensity (p-pol)", "Intensity (s-pol)",
                                                    "Intensity (h-dipole, p-pol)", "Intensity (v-dipole, p-pol)"])
                self.combo_x.addItem("Angle", ["Intensity", "Intensity (p-pol)", "Intensity (s-pol)",
                                               "Intensity (h-dipole, p-pol)", "Intensity (v-dipole, p-pol)"])

            elif self.combo.currentText() == "Emission Spectrum (3D)":
                self.combo_x.addItem("Wavelength", ["Angle"])
                self.combo_x.addItem("Angle", ["Wavelength"])

            elif self.combo.currentText() == "Power Dissipation Curve (2D)":
                self.combo_x.addItem("In-plane Wavevector", ["Dissipated Power",
                                                             "Dissipated Power (p-pol)",
                                                             "Dissipated Power (s-pol)"])
            elif self.combo.currentText() == "Power Dissipation Curve (3D))":
                self.combo_x.addItem("In-plane Wavevector", ["Dissipated Power",
                                                             "Dissipated Power (p-pol)",
                                                             "Dissipated Power (s-pol)"])
            elif self.combo.currentText() == "Microcavity Effect":
                self.combo_x.addItem("Wavelength", ["Effective Quantum Efficiency", "Purcell Factor"])
                self.combo_x.addItem("Angle", ["Effective Quantum Efficiency", "Purcell Factor"])

            elif self.combo.currentText() == "CIE 1931":
                self.combo_x.addItems(data)
            elif self.combo.currentText() == "Polar Plot":
                self.combo_x.addItems(data)

    def indexChangedy(self, index):
        self.combo_y.clear()
        data = self.combo_x.itemData(index)
        if data is not None:
            if self.combo.currentText() == "Mode Analysis (2D)":
                self.combo_y.addItems(["Optical Modes", "Air Mode",
                                      "Substrate-Guided Mode",
                                      "Wave-Guided Mode", "SPP Mode",
                                      "Absorption", "NR Losses"])

            elif self.combo.currentText() == "Mode Analysis (3D)":
                if self.combo_x.currentText() =="Thickness of b3p":
                    self.combo_y.addItem("Thickness of npb", ["Optical Modes", "Air Mode",
                                                          "Substrate-Guided Mode",
                                                          "Wave-Guided Mode", "SPP Mode",
                                                          "Absorption", "NR Losses"])
                else:
                    self.combo_y.addItem("Thickness of b3p", ["Optical Modes", "Air Mode",
                                                              "Substrate-Guided Mode",
                                                              "Wave-Guided Mode", "SPP Mode",
                                                              "Absorption", "NR Losses"])

            elif self.combo.currentText() == "Current Efficiency (2D)":
                self.combo_y.addItems(["Cd/A (photometry)", "W/mA/sr (radiometry)"])

            elif self.combo.currentText() == "Current Efficiency (3D)":
                if self.combo_x.currentText() =="Thickness of b3p":
                    self.combo_y.addItem("Thickness of npb", ["Cd/A (photometry)",
                                                              "W/mA/sr (radiometry)"])
                else:
                    self.combo_y.addItem("Thickness of b3p", ["Cd/A (photometry)",
                                                              "W/mA/sr (radiometry)"])

            elif self.combo.currentText() == "Emission Spectrum (2D)":
                self.combo_y.addItems(["Intensity", "Intensity (p-pol)", "Intensity (s-pol)",
                                      "Intensity (h-dipole, p-pol)", "Intensity (v-dipole, p-pol)"])

            elif self.combo.currentText() == "Emission Spectrum (3D)":
                if self.combo_x.currentText() =="Wavelength":
                    self.combo_y.addItem("Angle", ["Intensity", "Intensity (p-pol)", "Intensity (s-pol)",
                                           "Intensity (h-dipole, p-pol)", "Intensity (v-dipole, p-pol)"])
                else:
                    self.combo_y.addItem("Wavelength", ["Intensity", "Intensity (p-pol)", "Intensity (s-pol)",
                                                   "Intensity (h-dipole, p-pol)", "Intensity (v-dipole, p-pol)"])


            elif self.combo.currentText() == "Power Dissipation Curve (2D)":
                self.combo_y.addItems(["Dissipated Power", "Dissipated Power (p-pol)",
                                       "Dissipated Power (s-pol)"])

            elif self.combo.currentText() == "Power Dissipation Curve (3D))":
                self.combo_y.addItem("Dissipated Power", ["Dissipated Power (p-pol)",
                                                          "Dissipated Power (s-pol)"])
                self.combo_y.addItem("Dissipated Power (p-pol)", ["Dissipated Power",
                                                          "Dissipated Power (s-pol)"])
                self.combo_y.addItem("Dissipated Power (s-pol)", ["Dissipated Power",
                                                                  "Dissipated Power (p-pol)"])
            elif self.combo.currentText() == "Microcavity Effect":
                self.combo_y.addItems(data)

            elif self.combo.currentText() == "CIE 1931":
                self.combo_y.addItems(data)

            elif self.combo.currentText() == "Polar Plot":
                self.combo_y.addItems(data)

    def indexChangedz(self, index):
        self.combo_z.clear()
        data = self.combo_y.itemData(index)
        if data is not None:
            self.combo_z.addItems(data)

    def indexChanged(self, index):
        self.x=[]
        self.y=[]

        if (self.combo.currentText() == "Mode Analysis (2D)"):
            another_text = str(self.combo_x.currentText())
            if (another_text=="Thickness of b3p"):
                self.x = ["Thickness of npb"]
            elif (another_text=="Thickness of npb"):
                self.x = ["Thickness of b3p"]
            self.y = [30]

        elif (self.combo.currentText() == "Current Efficiency (2D)"):
            another_text = str(self.combo_x.currentText())
            if (another_text=="Thickness of b3p"):
                self.x = ["Thickness of npb"]
            elif (another_text=="Thickness of npb"):
                self.x = ["Thickness of b3p"]
            self.y = [30]

        # difference between 2 and 3 #####################
        elif (self.combo.currentText() == "Emission Spectrum (2D)"):
            another_text = str(self.combo_x.currentText())
            if (another_text == "Wavelength"):
                self.x = ["Angle"]
            elif (another_text == "Angle"):
                self.x = ["Wavelength"]
            self.y = [30]

        elif (self.text == "Emission Spectrum (3D)"):
            another_text = str(self.combo_x.currentText())
            if (another_text == "Wavelength"):
                self.x = ["Angle"]
            elif (another_text == "Angle"):
                self.x = ["Wavelength"]
            self.y = [30]

        elif (self.text == "Power Dissipation Curve (3D)"):
            another_text = str(self.combo_x.currentText())
            if (another_text == "Dissipated Power"):
                self.x = ["Dissipated Power (p-pol)", "Dissipated Power (s-pol)"]
            elif (another_text == "Dissipated Power (p-pol)"):
                self.x = ["Dissipated Power", "Dissipated Power (s-pol)"]
            elif   (another_text == "Dissipated Power (s-pol)"):
                self.x = ["Dissipated Power", "Dissipated Power (p-pol)"]
            self.y = [30, 400]

        elif (self.text == "Microcavity Effect"):
            another_text = str(self.combo_x.currentText())
            if (another_text == "Wavelength"):
                self.x = ["Angle"]
            elif (another_text == "Angle"):
                self.x = ["Wavelength"]
        else:
            self.x = [""]
            self.y = [""]


    def onButtonClickedPlot(self):
        with open(plotting_option, 'w') as stream:
            writer = csv.writer(stream, lineterminator='\n')
            rowdata = [[self.text], [self.xcombo.currentText()],
                       [self.ycombo.currentText()], [self.zcombo.currentText()]]
            for item in rowdata:
                writer.writerow(item)

    def onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()


class Exportation(QWidget):
    def __init__(self):
        super().__init__()

        self.image = polar_plot
        self.path = os.getcwd()
        self.name = "2PPlAn_33PYMPM"
        # with open(project_info, "r") as pi:
        #     self.name = pi.readline()
        self.data_path = data_polar_plot

        layout = QGridLayout()
        label = QLabel()
        label.setText("Exportation")
        label.setFont(QFont("Arial", 15, weight=QFont.Bold))
        layout.addWidget(label, 0, 0)

        hlayout = QHBoxLayout()
        label = QLabel()
        label.setText("Path: ")
        hlayout.addWidget(label)

        lineEdit = QLineEdit()
        lineEdit.setText(self.path)
        lineEdit.setFixedSize(250, 20)
        hlayout.addWidget(lineEdit)

        btn = QPushButton()
        btn.setText("Browse")
        btn.clicked.connect(self.talk)
        hlayout.addWidget(btn)

        layout.addLayout(hlayout, 1, 0)

        hlayout = QHBoxLayout()
        label = QLabel()
        label.setText("Type: ")
        hlayout.addWidget(label)

        check_text = QCheckBox()
        check_text.setText("Text")
        check_text.setChecked(True)
        check_text.setStyleSheet("QCheckBox::indicator { width: 20px; height: 20px;}")
        hlayout.addWidget(check_text)

        check_image = QCheckBox()
        check_image.setText("Image")
        check_text.setChecked(True)
        check_image.setStyleSheet("QCheckBox::indicator { width: 20px; height: 20px;}")
        hlayout.addWidget(check_image)

        #hlayout.setAlignment(QtCore.Qt.AlignLeft)

        layout.addLayout(hlayout, 2, 0)

        hlayout = QHBoxLayout()
        label = QLabel()
        label.setText("Name: ")
        hlayout.addWidget(label)

        lineEdit = QLineEdit()
        lineEdit.setText(self.name)
        lineEdit.setFixedSize(250, 20)
        hlayout.addWidget(lineEdit)

        self.btn = QPushButton()
        self.btn.setText("Export")

        if(check_text.setChecked(True)):
            btn.clicked.connect(self.handleTextSave)
        elif (check_image.setChecked(True)):
            btn.clicked.connect(self.handleImageSave)

        hlayout.addWidget(self.btn)

        layout.addLayout(hlayout, 3, 0)
        self.setLayout(layout)

    def talk(self):
        self.dialog = QFileDialog()
        options = QFileDialog.DontResolveSymlinks | QFileDialog.ShowDirsOnly
        self.directory = QFileDialog.getExistingDirectory(self.dialog, "Open Folder", options=options)
        self.dialog.show()
        return self.directory

    def handleImageSave(self):
        self.name.join(".png")
        real_path = os.path.join(self.path, self.name)
        # shutil.copy(self.image, str(real_path))
        with open(self.image, "rb") as real_image:
            data = real_image.read()
        with open(real_path, "wb") as stream:
            stream.write(data)

    def handleTextSave(self):
        self.name.join(".txt")
        real_path = os.path.join(self.path, self.name)
        with open(real_path, 'w') as stream:
            stream.write(open(self.data_path, "r").read())
            stream.close()