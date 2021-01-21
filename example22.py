import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWin(QMainWindow):
    def __init__(self):
        super().__init__()

        self.V, self.U, self.t, self.a = 0, 0, 0, 0

        centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(centralWidget)

        self.label   = QLabel("MECHANICS")

        self.calcbtn = QPushButton("SOLVE")
        self.calcbtn.clicked.connect(self.onCalcbtn)
        self.clrbtn  = QPushButton("CLEAR")
        self.clrbtn.clicked.connect(self.onClrbtn)

        self.labelResult = QLabel()

        self.spinBox1 = QDoubleSpinBox()
        self.spinBox1.setMinimum(-2.3)
        self.spinBox1.setMaximum(12)
        self.spinBox1.setValue(4.4)
        self.spinBox1.setSingleStep(0.02)
        self.spinBox1.valueChanged.connect(self.valueChanged_V)

        self.spinBox2 = QDoubleSpinBox()
        # ... see self.spinBox1
        self.spinBox2.valueChanged.connect(self.valueChanged_U)
        self.spinBox3 = QDoubleSpinBox()
        # ... see self.spinBox1
        self.spinBox3.valueChanged.connect(self.valueChanged_t)
        self.spinBox4 = QDoubleSpinBox()
        # ... see self.spinBox1
        self.spinBox4.valueChanged.connect(self.valueChanged_a)

        formlayout   = QFormLayout()
        formlayout.addRow(QLabel("V"), self.spinBox1)
        formlayout.addRow(QLabel("U"), self.spinBox2)
        formlayout.addRow(QLabel("t"), self.spinBox3)
        formlayout.addRow(QLabel("a"), self.spinBox4)
        formlayout.addRow(QLabel("Result"), self.labelResult)

        layH = QHBoxLayout()
        layH.addWidget(self.clrbtn)
        layH.addWidget(self.calcbtn)

        layout = QVBoxLayout(centralWidget)
        layout.addWidget(self.label)
        layout.addLayout(formlayout)
        layout.addLayout(layH)

    def valueChanged_V(self):
        self.V = self.spinBox1.value()
    def valueChanged_U(self):
        self.U = self.spinBox2.value()
    def valueChanged_t(self):
        self.t = self.spinBox3.value()
    def valueChanged_a(self):
        self.a = self.spinBox4.value()

    def onClrbtn(self):
        self.spinBox1.setValue(0)
        self.spinBox2.setValue(0)
        self.spinBox3.setValue(0)
        self.spinBox4.setValue(0)
        self.V, self.U, self.t, self.a = 0, 0, 0, 0
        self.labelResult.setText("")

    def onCalcbtn(self):
        formulars = "V + U + t + a = {:,.4f}".format(self.V + self.U + self.t + self.a)
        self.labelResult.setText(formulars)

      # get value of the selected combobox data
#        V = float(self.input1.text())
#        U = float(self.input2.text())
#        t = float(self.input3.text())
#        a = float(self.input4.text())
#        #conditions
#        #if u,t,a are given, use this formulars
#        V = U + a*t
#        S = U*t + (a*t**2)/2
#        t = (V - U)/a
#        #if u,a,s are given,
#        V =(U**2 + 2*a*S)**0.5
#        S = (V**2 - U**2)/2*a
#        #set the selected combobox result
#        self.lineEdit_result.setText


if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
    myapp = MyWin()
    myapp.show()
    sys.exit(app.exec_())