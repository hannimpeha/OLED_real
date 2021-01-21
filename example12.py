import sip
from PyQt5.QtWidgets import QWidget, QPushButton, QLineEdit, QHBoxLayout, QApplication

sip.setapi('QString', 2)
sip.setapi('QVariant', 2)

from PyQt5 import QtGui, QtCore

class MyWindow(QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.pushButtonOK = QPushButton(self)
        self.pushButtonOK.setText("OK")
        self.pushButtonOK.clicked.connect(self.on_pushButtonOK_clicked)
        self.pushButtonOK.setAutoDefault(True)

        self.lineEditNumber = QLineEdit(self)
        self.lineEditNumber.returnPressed.connect(self.pushButtonOK.click)

        self.layoutHorizontal = QHBoxLayout(self)
        self.layoutHorizontal.addWidget(self.pushButtonOK)
        self.layoutHorizontal.addWidget(self.lineEditNumber)

    @QtCore.pyqtSlot()
    def on_pushButtonOK_clicked(self):
        inputNumber = self.lineEditNumber.text()
        if inputNumber.isdigit():
            info = "You selected `{0}`"

        else:
            info = "Please select a number, `{0}` isn't valid!"

        print(info.format(inputNumber))

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.show()

    sys.exit(app.exec_())