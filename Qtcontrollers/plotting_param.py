import csv
import os

import shutil
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
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
        layout.addWidget(label, 0, 0)

        hlayout = QHBoxLayout()
        self.qlabel = QLabel()
        self.qlabel.setText("Graph: ")

        combo = QComboBox()
        combo.addItems(["Mode Analysis (2D)", "Mode Analysis (3D)",
                        "Current Efficiency (2D)", "Current Efficiency (3D)",
                        "Emission Spectrum (2D)", "Emission Spectrum (3D)", "Microcavity Effect",
                        "Power Dissipation Curve (2D)", "Power Dissipation Curve (3D)",
                        "CIE 1931", "Polar Plot"])

        # combo.activated[str].connect(self.onChanged)
        combo.setFixedSize(330, 20)
        hlayout.addWidget(self.qlabel)
        hlayout.addWidget(combo)
        layout.addLayout(hlayout, 1, 0)

        hlayout = QHBoxLayout()
        self.qlabel_x = QLabel()
        self.qlabel_x.setText("X-axis: ")
        self.xcombo = QComboBox()

        self.text = str(combo.currentText())


        if (self.text == "Mode Analysis (2D)"):
            self.xcombo.addItems(["Thickness of b3p","Thickness of npb"])
        elif (self.text == "Mode Analysis (3D)"):
            self.xcombo.addItems(["Thickness of b3p","Thickness of npb"])
        elif (self.text == "Current Efficiency (2D)"):
            self.xcombo.addItems(["Thickness of b3p","Thickness of npb"])
        elif (self.text == "Current Efficiency (3D)"):
            self.xcombo.addItems(["Thickness of b3p","Thickness of npb"])
        elif (self.text == "Emission Spectrum (2D)"):
            self.xcombo.addItems(["Wavelength", "Angle"])
        elif (self.text == "Emission Spectrum (3D)"):
            self.xcombo.addItems(["Wavelength", "Angle"])
        elif (self.text == "Power Dissipation Curve (2D)"):
            self.xcombo.addItems(["In-plane Wavevector"])
        elif (self.text == "Power Dissipation Curve (3D)"):
            self.xcombo.addItems(["In-plane Wavevector"])
        elif (self.text == "Microcavity Effect"):
            self.xcombo.addItems(["Wavelength", "Angle"])
        else: # CIE 1931 // Polar Plot : None
            self.xcombo.addItems([""])

        self.xcombo.setFixedSize(330, 20)
        #xcombo.activated[str].connect(self.onChanged)
        hlayout.addWidget(self.qlabel_x)
        hlayout.addWidget(self.xcombo)
        layout.addLayout(hlayout, 2, 0)

        hlayout = QHBoxLayout()
        self.qlabel_y = QLabel()
        self.qlabel_y.setText("Y-axis: ")
        self.ycombo = QComboBox()

        if (self.text == "Mode Analysis (2D)"):
            self.ycombo.addItems(["Optical Modes", "Air Mode", "Substrate-Guided Mode",
                             "Wave-Guided Mode", "SPP Mode", "Absorption", "NR Losses"])
        elif (self.text == "Mode Analysis (3D)"):
            self.ycombo.addItems(["Thickness of b3p","Thickness of npb"])
        elif (self.text == "Current Efficiency (2D)"):
            self.ycombo.addItems(["Cd/A (photometry)", "W/mA/sr (radiometry)"])
        elif (self.text == "Current Efficiency (3D)"):
            self.ycombo.addItems(["Thickness of b3p","Thickness of npb"])
        elif (self.text == "Emission Spectrum (2D)"):
            self.ycombo.addItems(["Intensity", "Intensity (p-pol)", "Intensity (s-pol)",
                             "Intensity (h-dipole, p-pol)", "Intensity (v-dipole, p-pol)"])
        elif (self.text == "Emission Spectrum (3D)"):
            self.ycombo.addItems(["Wavelength", "Angle"])
        elif (self.text == "Power Dissipation Curve (2D)"):
            self.ycombo.addItems(["Dissipated Power", "Dissipated Power (p-pol)", "Dissipated Power (s-pol)"])
        elif (self.text == "Power Dissipation Curve (3D)"):
            self.ycombo.addItems(["Dissipated Power", "Dissipated Power (p-pol)", "Dissipated Power (s-pol)"])
        elif (self.text == "Microcavity Effect"):
            self.ycombo.addItems(["Effective Quantum Efficiency", "Purcell Factor"])
        else: # CIE 1931 // Polar Plot : None
            self.ycombo.addItems([""])

        self.ycombo.setFixedSize(330, 20)
        #ycombo.activated[str].connect(self.onChanged)
        hlayout.addWidget(self.qlabel_y)
        hlayout.addWidget(self.ycombo)
        layout.addLayout(hlayout, 3, 0)

        hlayout = QHBoxLayout()
        self.qlabel_z = QLabel()
        self.qlabel_z.setText("Z-axis: ")
        self.zcombo = QComboBox()

        if (self.text == "Mode Analysis (3D)"):
            self.zcombo.addItems(["Optical Mode", "Air Mode", "Substrate-Guided Mode",
                                  "Wave-Guided Mode", "SPP Mode", "Absorption", "NR Losses"])
        elif (self.text == "Current Efficiency (3D)"):
            self.zcombo.addItems(["Cd/A (photometry)", "W/mA/sr (radiometry)"])
        elif (self.text == "Emission Spectrum (3D)"):
            self.zcombo.addItems(["Intensity", "Intensity (p-pol)", "Intensity (s-pol)",
                             "Intensity (h-dipole, p-pol)", "Intensity (v-dipole, p-pol)",
                             "Intensity (h-dipole, s-pol)"])
        elif (self.text == "Power Dissipation Curve (3D)"):
            self.zcombo.addItems(["Dissipated Power", "Dissipated Power (p-pol)", "Dissipated Power (s-pol)"])
        else: # Mode Analysis (2D) // Current Efficiencty (2D) // Emission Spectrum (2D) //
              # Power Dissipation Curve (2D) // Microcavity Effect // CIE1 1931 // Polar Plot
            self.zcombo.addItems([""])

        self.zcombo.setFixedSize(330, 20)
        #zcombo.activated[str].connect(self.onChanged)
        hlayout.addWidget(self.qlabel_z)
        hlayout.addWidget(self.zcombo)
        layout.addLayout(hlayout, 4, 0)

        label = QLabel()
        label.setText("Fixed Parameters:")
        layout.addWidget(label, 5, 0)
        table = self.making_table()

        layout.addWidget(table, 6, 0)

        hlayout = QHBoxLayout()
        btn = QPushButton()
        btn.setText("Save")
        btn.clicked.connect(self.onButtonClickedPlot)
        hlayout.addWidget(btn)

        btn = QPushButton()
        btn.setText("Clear")
        hlayout.addWidget(btn)
        layout.addLayout(hlayout, 7, 0)

        self.setLayout(layout)

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


    def making_table(self):
        self.table = QTableWidget()
        self.table.setRowCount(10)
        self.table.setColumnCount(2)
        cols_element = ['Name', 'Measure']
        self.table.setHorizontalHeaderLabels(cols_element)

        if (self.text == "Mode Analysis (2D)"):
            another_text = str(self.xcombo.currentText())
            if (another_text=="Thickness of b3p"):
                self.x = ["Thickness of npb"]
            elif (another_text=="Thickness of npb"):
                self.x = ["Thickness of b3p"]
            self.y = [30]

        elif (self.text == "Current Efficiency (2D)"):
            another_text = str(self.xcombo.currentText())
            if (another_text=="Thickness of b3p"):
                self.x = ["Thickness of npb"]
            elif (another_text=="Thickness of npb"):
                self.x = ["Thickness of b3p"]
            self.y = [30]

        # difference between 2 and 3 #####################
        elif (self.text == "Emission Spectrum (2D)"):
            another_text = str(self.xcombo.currentText())
            if (another_text == "Thickness of b3p"):
                self.x = ["Thickness of npb", "Wavelength"]
            elif (another_text == "Thickness of npb"):
                self.x = ["Thickness of b3p", "Wavelength"]
            self.y = [30, 400]

        elif (self.text == "Emission Spectrum (3D)"):
            another_text = str(self.xcombo.currentText())
            if (another_text == "Thickness of b3p"):
                self.x = ["Thickness of npb"]
            elif (another_text == "Thickness of npb"):
                self.x = ["Thickness of b3p"]
            self.y = [30]

        elif (self.text == "Power Dissipation Curve (2D)"):
            another_text = str(self.xcombo.currentText())
            if (another_text == "Thickness of b3p"):
                self.x = ["Thickness of npb", "Wavelength"]
            elif (another_text == "Thickness of npb"):
                self.x = ["Thickness of b3p", "Wavelength"]
            self.y = [30, 400]

        elif (self.text == "Power Dissipation Curve (3D)"):
            another_text = str(self.xcombo.currentText())
            if (another_text == "Thickness of b3p"):
                self.x = ["Thickness of npb"]
            elif (another_text == "Thickness of npb"):
                self.x = ["Thickness of b3p"]
            self.y = [30]

        elif (self.text == "Microcavity Effect"):
            another_text = str(self.xcombo.currentText())
            if (another_text == "Thickness of b3p"):
                self.x = ["Thickness of npb"]
            elif (another_text == "Thickness of npb"):
                self.x = ["Thickness of b3p"]
            self.y = [30]

        else: # Mode Analysis (3D) // Current Efficiency (3D) // CIE 1931 // Polar Plot
            self.x = [""]
            self.y = [""]

        self.tempList = [[self.x, self.y]]
        self.num_row = len(self.tempList)
        self.table.setFixedSize(400, 200)

        for i in range(len(self.x)):
            self.num_row = i
            self.table.setItem(self.num_row, 0, QTableWidgetItem(self.x[i]))
            self.table.setItem(self.num_row, 1, QTableWidgetItem(str(self.y[i])))

        self.table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        return self.table


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