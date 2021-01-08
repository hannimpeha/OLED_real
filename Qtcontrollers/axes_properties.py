from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QComboBox, QWidget, QGridLayout, QTableWidget, QTableWidgetItem

contour_image = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/contour.png'

class Axes_Properties(QWidget):

    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        table = self.making_table()
        image = self.contour_image()
        layout.addWidget(table, 0, 0)
        layout.addWidget(image, 1, 0)
        self.setLayout(layout)

    def making_table(self):
        self.table = QTableWidget()
        self.table.setRowCount(4)
        self.table.setColumnCount(4)
        cols_element = ['Name', 'Min', 'Max']
        self.table.setHorizontalHeaderLabels(cols_element)

        self.x = ["X-axis", "Angle", "0", "90"]
        self.y = ["Y-axis", "Wavelength", "400", "700"]
        self.z = ["Z-axis", "Intensity", "0", "2.35"]
        self.tempList = [[self.x, self.y, self.z]]
        self.num_row = len(self.tempList)
        self.table.setFixedSize(610, 200)

        for i in range(len(self.x)):
            self.num_row = i
            self.table.setItem(self.num_row, 0, QTableWidgetItem(str(self.num_row)))
            self.table.setItem(self.num_row, 1, QTableWidgetItem(self.x[i]))
            self.table.setItem(self.num_row, 2, QTableWidgetItem(self.y[i]))
            self.table.setItem(self.num_row, 3, QTableWidgetItem(self.z[i]))
        return self.table

    def contour_image(self):
        label = QLabel()
        pixmap = QPixmap(contour_image)
        pixmap = pixmap.scaled(600, 600, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        return label