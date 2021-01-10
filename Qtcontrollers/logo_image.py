from datetime import datetime
import socket
from PyQt5 import QtCore
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

logo_image = 'Qtcontrollers/resources/Logo.png'

class Logo_Image(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        logo_image = self.logo_image()
        layout.addWidget(logo_image, 0, 0)
        properties = Properties()
        layout.addWidget(properties, 1, 0)
        execute = Execute()
        layout.addWidget(execute, 2, 0)
        project_into = Project_Info()
        layout.addWidget(project_into, 3, 0)
        self.setLayout(layout)


    def logo_image(self):
        label = QLabel()
        pixmap = QPixmap(logo_image)
        pixmap = pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        return label


class Properties(QWidget):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        label = QLabel()
        label.setText("Properties")
        layout.addWidget(label, 0, 0)

        label = QLabel()
        label.setText("Wavelength Range (nm): ")
        layout.addWidget(label, 1, 0)

        lineEdit = QLineEdit()
        layout.addWidget(lineEdit, 1, 1)

        label = QLabel()
        label.setText("Angle Range (degree): ")
        layout.addWidget(label, 2, 0)

        lineEdit = QLineEdit()
        layout.addWidget(lineEdit, 2, 1)

        label = QLabel()
        label.setText("Calculation Types:")
        layout.addWidget(label, 3, 0)

        checkBox = QCheckBox()
        checkBox.setText("Mode Analysis")
        layout.addWidget(checkBox, 4, 0)

        checkBox = QCheckBox()
        checkBox.setText("Emission Spectrum")
        layout.addWidget(checkBox, 5, 0)

        checkBox = QCheckBox()
        checkBox.setText("Power Dissipation Curve")
        layout.addWidget(checkBox, 6, 0)

        self.setLayout(layout)


class Execute(QWidget):
    def __init__(self):
        super().__init__()

        DEFAULT_STYLE = """
        QProgressBar{
            border: 1px solid grey;
            border-radius: 5px;
            text-align: center
        }

        QProgressBar::chunk {
            background-color: lightblue;
            width: 10px;
            margin: 1px;
        }
        """

        layout = QVBoxLayout()

        label = QLabel()
        label.setText("Progress")
        label.setFixedSize(100, 20)
        layout.addWidget(label)

        self.pbar = QProgressBar()
        self.pbar.setGeometry(30, 40, 200, 40)
        self.setStyleSheet(DEFAULT_STYLE)

        self.btn = QPushButton('GPU Calc')
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        layout.addWidget(self.pbar)
        layout.addWidget(self.btn)
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
            self.btn.setText('GPU Calc')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')


class Project_Info(QWidget):
    def __init__(self):
        super().__init__()
        layout = QHBoxLayout()

        layout1 = QGridLayout()
        label = QLabel()
        label.setText("Project Info")
        layout1.addWidget(label, 0, 0)

        label_name = QLabel()
        label_name.setText("Name")
        layout1.addWidget(label_name)

        label = QLabel()
        label.setText("Designer")
        layout1.addWidget(label, 2, 0)

        label = QLabel()
        label.setText("Analyzer")
        layout1.addWidget(label, 3, 0)

        label = QLabel()
        label.setText("Creation Date")
        layout1.addWidget(label, 4, 0)

        label = QLabel()
        label.setText("Modified Date")
        layout1.addWidget(label, 5, 0)

        label = QLabel()
        label.setText("IP Address")
        layout1.addWidget(label, 6, 0)

        layout2 = QGridLayout()
        name_label = QLabel()
        name_label.setText("2PPlAn_33PYMPM")
        layout2.addWidget(name_label, 1, 0)

        label = QLabel()
        label.setText("Hannah Lee")
        layout2.addWidget(label, 2, 0)

        label = QLabel()
        label.setText("Hannah Lee")
        layout2.addWidget(label, 3, 0)

        c_date = QLabel()
        c_date.setText(datetime.today().strftime('%Y-%m-%d'))
        layout2.addWidget(c_date, 4, 0)

        c_date = QLabel()
        c_date.setText(datetime.today().strftime('%Y-%m-%d'))
        layout2.addWidget(c_date, 5, 0)

        qlabel = QLabel()
        qlabel.setText(self.get_ip())
        layout2.addWidget(qlabel, 6, 0)

        layout.addLayout(layout1)
        layout.addLayout(layout2)

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