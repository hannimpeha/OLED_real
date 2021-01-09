from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QComboBox, QTableWidget, QTableWidgetItem, QLineEdit, \
    QPushButton, QCheckBox, QHBoxLayout

logo_image = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/Logo.png'

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
        xcombo.addItem("Emission Spectrum (3D)")
        xcombo.addItem("Pear")
        xcombo.addItem("Lemon")
        xcombo.activated[str].connect(self.onChanged)
        hlayout.addWidget(self.qlabel)
        hlayout.addWidget(xcombo)
        layout.addLayout(hlayout, 1, 0)

        hlayout = QHBoxLayout()
        self.qlabel = QLabel()
        self.qlabel.setText("X-axis: ")
        xcombo = QComboBox()
        xcombo.addItem("Angle")
        xcombo.addItem("Pear")
        xcombo.addItem("Lemon")
        xcombo.activated[str].connect(self.onChanged)
        hlayout.addWidget(self.qlabel)
        hlayout.addWidget(xcombo)
        layout.addLayout(hlayout, 2, 0)

        hlayout = QHBoxLayout()
        self.qlabel = QLabel()
        self.qlabel.setText("Y-axis: ")
        ycombo = QComboBox()
        ycombo.addItem("Wavelength")
        ycombo.addItem("Pear")
        ycombo.addItem("Lemon")
        ycombo.activated[str].connect(self.onChanged)
        hlayout.addWidget(self.qlabel)
        hlayout.addWidget(ycombo)
        layout.addLayout(hlayout, 3, 0)

        hlayout = QHBoxLayout()
        self.qlabel = QLabel()
        self.qlabel.setText("Z-axis: ")
        zcombo = QComboBox()
        zcombo.addItem("Intensity")
        zcombo.addItem("Pear")
        zcombo.addItem("Lemon")
        zcombo.activated[str].connect(self.onChanged)
        hlayout.addWidget(self.qlabel)
        hlayout.addWidget(zcombo)
        layout.addLayout(hlayout, 4, 0)

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
        self.table.setFixedSize(380, 600)

        for i in range(len(self.x)):
            self.num_row = i
            self.table.setItem(self.num_row, 0, QTableWidgetItem(self.x[i]))
            self.table.setItem(self.num_row, 1, QTableWidgetItem(self.y[i]))
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
        lineEdit.setFixedSize(100, 20)
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
        hlayout.addWidget(check_text)

        check_image = QCheckBox()
        check_image.setText("Image")
        hlayout.addWidget(check_image)

        layout.addLayout(hlayout, 2, 0)

        hlayout = QHBoxLayout()
        label = QLabel()
        label.setText("Name: ")
        hlayout.addWidget(label)

        lineEdit = QLineEdit()
        lineEdit.setFixedSize(100, 20)
        hlayout.addWidget(lineEdit)

        btn = QPushButton()
        btn.setText("Export")
        hlayout.addWidget(btn)

        layout.addLayout(hlayout, 3, 0)
        self.setLayout(layout)
