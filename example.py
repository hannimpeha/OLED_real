import sys

from PyQt5 import QtCore, QtWidgets


class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.process = QtCore.QProcess(self)
        self.process.setProgram("dirb")
        self.process.setProcessChannelMode(QtCore.QProcess.MergedChannels)

        self.lineedit = QtWidgets.QLineEdit("http://webscantest.com")
        self.button = QtWidgets.QPushButton("Start")
        self.textedit = QtWidgets.QTextEdit(readOnly=True)

        lay = QtWidgets.QGridLayout(self)
        lay.addWidget(self.lineedit, 0, 0)
        lay.addWidget(self.button, 0, 1)
        lay.addWidget(self.textedit, 1, 0, 1, 2)

        self.button.clicked.connect(self.on_clicked)
        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
        self.process.finished.connect(self.on_finished)

    @QtCore.pyqtSlot()
    def on_clicked(self):
        if self.button.text() == "Start":
            self.textedit.clear()
            self.process.setArguments([self.lineedit.text()])
            self.process.start()
            self.button.setText("Stop")
        elif self.button.text() == "Stop":
            self.process.kill()

    @QtCore.pyqtSlot()
    def on_readyReadStandardOutput(self):
        text = self.process.readAllStandardOutput().data().decode()
        self.textedit.append(text)

    @QtCore.pyqtSlot()
    def on_finished(self):
        self.button.setText("Start")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())