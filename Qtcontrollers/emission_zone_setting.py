from PyQt5.QtWidgets import *
import sys

class Emission_Zone_Setting(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        # rcParams['text.usetex'] = True
        # x, y, a, b, c, exp = symbols("x, y, a, b, c, exp")

        radiobutton = QRadioButton("Sheet")
        radiobutton.setChecked(True)
        radiobutton.type = ""
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 0, 0)

        radiobutton = QRadioButton("Constant")
        radiobutton.type = "x=a"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 0, 1)

        radiobutton = QRadioButton("Linear")
        radiobutton.type = "y=ax+b"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 0, 2)

        radiobutton = QRadioButton("Gaussian")
        radiobutton.type = "y = a*e^{b+x}+c"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 0, 3)

        # self.lineEntry = QLineEdit(self)
        # self.lineEntry.move(16, 16)
        # self.lineEntry.resize(200, 40)

        self.qlabel = QLabel(self)
        layout.addWidget(self.qlabel, 0, 4)


    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.qlabel.setText(radioButton.type)


app = QApplication(sys.argv)
screen = Emission_Zone_Setting()
screen.show()
sys.exit(app.exec_())