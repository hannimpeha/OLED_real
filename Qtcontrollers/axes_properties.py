from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

image = 'resources/Graph.png'

class Axes_Properties(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        label = QLabel()
        label.setText("Axes Properties")
        label.setFixedSize(100, 20)
        layout.addWidget(label)

        table = self.making_table()
        image = self.making_image()
        layout.addWidget(table)
        layout.addWidget(image)
        self.setLayout(layout)

    def making_table(self):
        self.table = QTableWidget()
        self.table.setRowCount(3)
        self.table.setColumnCount(5)
        cols_element = ["Axis", 'Name', 'Min', 'Max', "Remark"]
        self.table.setHorizontalHeaderLabels(cols_element)

        self.axis = ["X-axis", "Y-axis", "Z-axis"]


        self.name = ["Angle", "Wavelength", "Intensity"]
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
