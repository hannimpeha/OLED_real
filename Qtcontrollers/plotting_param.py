from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QComboBox, QTableWidget, QTableWidgetItem

logo_image = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/Logo.png'

class Plotting_Param(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        logo_image = self.logo_image()
        plotting = Plotting()

        layout.addWidget(logo_image, 0, 0)
        layout.addWidget(plotting, 1, 0)
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

        self.qlabel = QLabel()
        self.qlabel.setText("Graph: ")

        xcombo = QComboBox()
        xcombo.addItem("Emission Spectrum (3D)")
        xcombo.addItem("Pear")
        xcombo.addItem("Lemon")
        xcombo.activated[str].connect(self.onChanged)
        layout.addWidget(self.qlabel, 1, 0)
        layout.addWidget(xcombo, 1, 1)


        self.qlabel = QLabel()
        self.qlabel.setText("X-axis: ")
        xcombo = QComboBox()
        xcombo.addItem("Angle")
        xcombo.addItem("Pear")
        xcombo.addItem("Lemon")
        xcombo.activated[str].connect(self.onChanged)
        layout.addWidget(self.qlabel, 2, 0)
        layout.addWidget(xcombo, 2, 1)

        self.qlabel = QLabel()
        self.qlabel.setText("Y-axis: ")
        ycombo = QComboBox()
        ycombo.addItem("Wavelength")
        ycombo.addItem("Pear")
        ycombo.addItem("Lemon")
        ycombo.activated[str].connect(self.onChanged)
        layout.addWidget(self.qlabel, 3, 0)
        layout.addWidget(ycombo, 3, 1)

        self.qlabel = QLabel()
        self.qlabel.setText("Z-axis: ")
        zcombo = QComboBox()
        zcombo.addItem("Intensity")
        zcombo.addItem("Pear")
        zcombo.addItem("Lemon")
        zcombo.activated[str].connect(self.onChanged)
        layout.addWidget(self.qlabel, 4, 0)
        layout.addWidget(zcombo, 4, 1)

        label = QLabel()
        label.setText("Fixed Parameters:")
        layout.addWidget(label, 5, 0)

        table = self.making_table()
        layout.addWidget(table, 6, 0)
        self.setLayout(layout)

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
        self.table.setFixedSize(600, 300)

        for i in range(len(self.x)):
            self.num_row = i
            self.table.setItem(self.num_row, 0, QTableWidgetItem(self.x[i]))
            self.table.setItem(self.num_row, 1, QTableWidgetItem(self.y[i]))
        return self.table
