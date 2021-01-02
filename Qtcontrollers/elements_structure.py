from PyQt5.QtWidgets import *
import sys

class Elements_Structure(QWidget):
    def __init__(self):
        super().__init__()
        real_table = self.make_table()
        vbox = QVBoxLayout()
        vbox.addWidget(real_table)
        self.setLayout(vbox)
        self.setWindowTitle('Elements_Structure')
        self.setGeometry(300, 300, 300, 200)

    def make_table(self):
        self.table = QTableWidget()
        self.table.setRowCount(6)
        self.table.setColumnCount(6)
        cols_element = ['L#', 'LayerName', 'Material', 'RefractiveIndex', 'Thickness', 'Unit']
        self.table.setHorizontalHeaderLabels(cols_element)

        self.layer_name = ["Al", "ETL", "EML", "HTL2", "HTL1", "ITO"]
        self.material = ["Al", "ETL", "EML", "HTL2", "HTL1", "ITO"]
        self.refractive_index = ["Al.dat", "ETL.dat", "EML.dat", "HTL.dat", "HTL1.dat", "ITO.dat"]
        self.thickness = [100, 100.5, 20, 10, 100.5, 70]
        self.unit = ["nm", "nm", "nm", "nm", "nm", "nm"]
        self.tempList = [[self.layer_name, self.material, self.refractive_index, self.thickness, self.unit]]
        self.num_row = len(self.tempList)

        for i in range(len(self.layer_name)):
            self.num_row = i+1
            self.table.setItem(self.num_row, 0, QTableWidgetItem(str(self.num_row)))
            self.table.setItem(self.num_row, 1, QTableWidgetItem(self.layer_name[i]))
            self.table.setItem(self.num_row, 2, QTableWidgetItem(self.material[i]))
            self.table.setItem(self.num_row, 3, QTableWidgetItem(self.refractive_index[i]))
            self.table.setItem(self.num_row, 4, QTableWidgetItem(str(self.thickness[i])))
            self.table.setItem(self.num_row, 5, QTableWidgetItem(self.unit[i]))
        return self.table

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Elements_Structure()
    window.show()
    sys.exit(app.exec_())