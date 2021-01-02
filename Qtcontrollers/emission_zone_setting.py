import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel

logo_image = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/Logo.png'

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label = QLabel(self)
        pixmap = QPixmap(logo_image)
        pixmap = pixmap.scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        self.resize(pixmap.width(), pixmap.height())

        self.setWindowTitle('QLogo_Image')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())