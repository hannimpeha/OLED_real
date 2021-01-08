from PyQt5.QtWidgets import QWidget, QPushButton, QProgressBar, QGridLayout
from PyQt5.QtCore import QBasicTimer


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