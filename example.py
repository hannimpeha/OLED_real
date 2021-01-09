from PyQt5 import QtGui, QtCore
from PyQt5.QtPrintSupport import QPrintDialog, QPrintPreviewDialog
from PyQt5.QtWidgets import QWidget, QPushButton, QGridLayout, QTableView, QDialog, QApplication


class Window(QWidget):
    def __init__(self, rows, columns):
        QWidget.__init__(self)
        self.table = QTableView(self)
        model =  QtGui.QStandardItemModel(rows, columns, self.table)
        for row in range(rows):
            for column in range(columns):
                item = QtGui.QStandardItem('(%d, %d)' % (row, column))
                item.setTextAlignment(QtCore.Qt.AlignCenter)
                model.setItem(row, column, item)
        self.table.setModel(model)
        self.buttonPrint = QPushButton('Print', self)
        self.buttonPrint.clicked.connect(self.handlePrint)
        self.buttonPreview = QPushButton('Preview', self)
        self.buttonPreview.clicked.connect(self.handlePreview)
        layout = QGridLayout(self)
        layout.addWidget(self.table, 0, 0, 1, 2)
        layout.addWidget(self.buttonPrint, 1, 0)
        layout.addWidget(self.buttonPreview, 1, 1)

    def handlePrint(self):
        dialog = QPrintDialog()
        if dialog.exec_() == QDialog.Accepted:
            self.handlePaintRequest(dialog.printer())

    def handlePreview(self):
        dialog = QPrintPreviewDialog()
        dialog.paintRequested.connect(self.handlePaintRequest)
        dialog.exec_()

    def handlePaintRequest(self, printer):
        document = QtGui.QTextDocument()
        cursor = QtGui.QTextCursor(document)
        model = self.table.model()
        table = cursor.insertTable(
            model.rowCount(), model.columnCount())
        for row in range(table.rows()):
            for column in range(table.columns()):
                cursor.insertText(model.item(row, column).text())
                cursor.movePosition(QtGui.QTextCursor.NextCell)
        document.print_(printer)

if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
    window = Window(25, 2)
    window.resize(300, 400)
    window.show()
    sys.exit(app.exec_())