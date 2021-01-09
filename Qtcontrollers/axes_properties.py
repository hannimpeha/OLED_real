from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget, QTableWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout

contour_image = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/contour.png'

class Axes_Properties(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel()
        label.setText("Axes Properties")
        label.setFixedSize(100, 20)
        layout.addWidget(label)

        table = self.making_table()
        image = self.contour_image()
        layout.addWidget(table)
        layout.addWidget(image)
        self.setLayout(layout)

    def making_table(self):
        self.table = QTableWidget()
        self.table.setRowCount(3)
        self.table.setColumnCount(4)
        cols_element = ["Axis", 'Name', 'Min', 'Max']
        self.table.setHorizontalHeaderLabels(cols_element)

        self.axis = ["X-axis", "Y-axis", "Z-axis"]
        self.name = ["Angle", "Wavelength", "Intensity"]
        self.min = ["0" , "400", "0"]
        self.max = ["90", "700", "2.35"]
        self.tempList = [[self.axis, self.name, self.min, self.max]]
        self.num_row = len(self.tempList)
        self.table.setFixedSize(610, 200)

        for i in range(len(self.axis)):
            self.num_row = i
            self.table.setItem(self.num_row, 0, QTableWidgetItem(self.axis[i]))
            self.table.setItem(self.num_row, 1, QTableWidgetItem(self.name[i]))
            self.table.setItem(self.num_row, 2, QTableWidgetItem(self.min[i]))
            self.table.setItem(self.num_row, 3, QTableWidgetItem(self.max[i]))
        self.table.horizontalHeader().setStretchLastSection(True)
        return self.table

    def contour_image(self):
        label = QLabel()
        pixmap = QPixmap(contour_image)
        pixmap = pixmap.scaled(600, 600, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        return label