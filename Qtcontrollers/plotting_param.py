from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel

logo_image = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/Logo.png'

class Plotting_Param(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        logo_image = self.logo_image()
        layout.addWidget(logo_image, 0, 0)
        self.setLayout(layout)

    def logo_image(self):
        label = QLabel()
        pixmap = QPixmap(logo_image)
        pixmap = pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        return label
