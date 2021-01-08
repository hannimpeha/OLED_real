from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QComboBox, QWidget, QGridLayout


contour_image = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/contour.png'

class Axes_Properties(QWidget):

    def __init__(self):
        super().__init__()
        layout = QGridLayout()



        self.qlabel = QLabel()
        self.qlabel.setText("X-axis")
        xcombo = QComboBox()
        xcombo.addItem("Apple")
        xcombo.addItem("Pear")
        xcombo.addItem("Lemon")
        xcombo.activated[str].connect(self.onChanged)
        layout.addWidget(self.qlabel, 0, 0)
        layout.addWidget(xcombo, 1, 0)

        self.qlabel = QLabel()
        self.qlabel.setText("Y-axis")
        ycombo = QComboBox()
        ycombo.addItem("Apple")
        ycombo.addItem("Pear")
        ycombo.addItem("Lemon")
        ycombo.activated[str].connect(self.onChanged)
        layout.addWidget(self.qlabel, 2, 0)
        layout.addWidget(ycombo, 3, 0)

        self.qlabel = QLabel()
        self.qlabel.setText("Z-axis")
        zcombo = QComboBox()
        zcombo.addItem("Apple")
        zcombo.addItem("Pear")
        zcombo.addItem("Lemon")
        zcombo.activated[str].connect(self.onChanged)
        layout.addWidget(self.qlabel, 4, 0)
        layout.addWidget(zcombo, 5, 0)

        image = self.contour_image()
        layout.addWidget(image, 6, 0)

        self.setLayout(layout)

    def onChanged(self, text):
        self.qlabel.setText(text)
        self.qlabel.adjustSize()


    def contour_image(self):
        label = QLabel()
        pixmap = QPixmap(contour_image)
        pixmap = pixmap.scaled(800, 800, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        return label