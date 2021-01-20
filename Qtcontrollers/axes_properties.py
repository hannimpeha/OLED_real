from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data_polar_plot = "output/#3-2/angular_intensity/output_angular_intensity_bottom.txt"
polar_plot = 'resources/polar_plot.png'
plotting_option = 'resources/plotting_option.csv'

class Axes_Properties(QWidget):

    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        image = self.making_image()
        layout.addWidget(image)
        button_plot = QPushButton()
        button_plot.setText("Plot")
        button_plot.setFixedSize(700, 80)
        button_plot.clicked.connect(self.making_image)
        layout.addWidget(button_plot)
        self.setLayout(layout)

    def making_image(self):
        label = QLabel()
        pixmap = QPixmap(polar_plot)
        pixmap = pixmap.scaled(730, 730, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        return label

    def plotting(self):
        data = np.genfromtxt(data_polar_plot, unpack=True)
        theta = np.linspace(0, np.pi / 2, 10)
        r = np.cos(theta)
        r_data = data
        # fig = plt.figure()
        ax = plt.figure().add_subplot(111, polar=True)
        ax.set_thetamin(0)
        ax.set_thetamax(90)

        ax.scatter(theta, r_data)
        ax.scatter(theta, r)

        plt.title("Polar Plot")

        plt.gca().invert_xaxis()
        plt.gca().invert_yaxis()
        plt.savefig(polar_plot, transparent=True)