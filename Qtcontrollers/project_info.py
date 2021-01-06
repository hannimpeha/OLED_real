from datetime import datetime
import socket

from PyQt5.QtWidgets import QWidget, QGridLayout, QLabel, QApplication

class Project_Info(QGridLayout):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        #self.setLayout(layout)

        qlabel = QLabel()
        qlabel.setText(self.get_ip())
        layout.addWidget(qlabel, 0, 0)

        c_date = QLabel()
        c_date.setText(datetime.today().strftime('%Y-%m-%d'))
        layout.addWidget(c_date, 1, 0)

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