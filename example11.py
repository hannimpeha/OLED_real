from PyQt5 import QtCore, QtGui, QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.text_edit = QtWidgets.QTextEdit(
            textChanged=self.on_textChanged
        )
        self.setCentralWidget(self.text_edit)

        timer = QtCore.QTimer(
            self,
            timeout=self.on_timeout
        )
        timer.start()

    @QtCore.pyqtSlot()
    def on_textChanged(self):
        print(self.text_edit.toPlainText())

    @QtCore.pyqtSlot()
    def on_timeout(self):
        self.text_edit.blockSignals(True)
        self.text_edit.setText(QtCore.QDateTime.currentDateTime().toString())
        self.text_edit.blockSignals(False)

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())