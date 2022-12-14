from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QComboBox, QApplication


class myWindow(QWidget):
    def __init__(self, parent=None):
        super(myWindow, self).__init__(parent)

        self.comboBox = QComboBox(self)
        self.comboBox.addItems([str(x) for x in range(3)])
        self.comboBox.currentIndexChanged.connect(self.on_comboBox_currentIndexChanged)

        slotLambda = lambda: self.on_comboBox_currentIndexChanged_lambda("some_value")
        self.comboBox.currentIndexChanged.connect(slotLambda)

    @QtCore.pyqtSlot(int)
    def on_comboBox_currentIndexChanged(self, value):
        print(value)

    @QtCore.pyqtSlot(str)
    def on_comboBox_currentIndexChanged_lambda(self, string):
        print(string)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setApplicationName('myWindow')

    main = myWindow()
    main.show()

    sys.exit(app.exec_())