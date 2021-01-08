from datetime import datetime
import socket
from PyQt5 import QtCore
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QGridLayout, QPushButton, QProgressBar, QVBoxLayout

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
        pixmap = pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        return label


class Execute(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()

        self.pbar = QProgressBar()
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start')
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        layout.addWidget(self.pbar, 0, 0)
        layout.addWidget(self.btn, 1, 0)
        self.setLayout(layout)

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')


class Project_Info(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()

        qlabel = QLabel()
        qlabel.setText(self.get_ip())
        layout.addWidget(qlabel)

        c_date = QLabel()
        c_date.setText(datetime.today().strftime('%Y-%m-%d'))
        layout.addWidget(c_date)

        self.setLayout(layout)

    def get_ip(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        try:
            s.connect(('10.255.255.255', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP