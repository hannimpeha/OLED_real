from PyQt5.QtWidgets import *

class Emission_Zone_Setting(QWidget):
    def __init__(self):
        super().__init__()
        layout = QGridLayout()
        self.setLayout(layout)

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

        self.qlabel = QLabel()
        layout.addWidget(self.qlabel, 0, 4)


    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            self.qlabel.setText(radioButton.type)