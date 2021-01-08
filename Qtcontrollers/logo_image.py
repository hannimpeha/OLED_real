from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout

from Qtcontrollers.execute import Execute
from Qtcontrollers.project_info import Project_Info

logo_image = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/Logo.png'

class Logo_Image(QWidget):

    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        logo_image = self.logo_image()
        layout.addWidget(logo_image, 0, 0)
        execute = Execute()
        layout.addWidget(execute, 1, 0)
        project_into = Project_Info()
        layout.addWidget(project_into, 2, 0)
        self.setLayout(layout)


    def logo_image(self):
        label = QLabel()
        pixmap = QPixmap(logo_image)
        pixmap = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        return label


