from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout

emission_image = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/EML_graph.png'

class Emission_Layer_Graph(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel()
        pixmap = QPixmap(emission_image)
        pixmap = pixmap.scaled(128, 128, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        return label