import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableView, QGridLayout, QWidget, QCheckBox
from PyQt5.QtGui import QFont
from functools import partial

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.font = QFont("Helvetica", 9)
        self.setFont(self.font)
        self.showMaximized()
        grid = QGridLayout()
        self.setLayout(grid)

        positions = [(i,j) for i in range(5) for j in range(5)]
        print('\npostions: ', positions)
        wordlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y']


        for position, wordlist in zip(positions, wordlist):
            checkB =(QCheckBox(wordlist))
            checkB.setStatusTip("Crawling best singals for "+wordlist+"." ) # set Statusbar
            checkB.stateChanged.connect(partial(self.checkState, wordlist))
            grid.addWidget(checkB, *position)

        checkBoxNone = QCheckBox("None Selected")
        checkBoxNone.setChecked(True)
        checkBoxNone.stateChanged.connect(self.checkState)
        grid.addWidget(checkBoxNone, 6, 1)

        checkAll = QCheckBox("Select All")
        checkAll.setChecked(False)
        checkAll.stateChanged.connect(self.selectAll)
        grid.addWidget(checkAll, 6, 2)

        widget = QWidget()
        widget.setLayout(grid)
        self.setCentralWidget(widget)

        self.statusBar().showMessage('Ready')

    # Here are the problems.
    # Is it because I have create checkboxes with a for loop?

    def selectAll(self, state):
        if state == Qt.Checked:
            if self.sender() == MainWindow.checkAll:
                MainWindow.checkB.setChecked(True)

    def checkState(self, checktext, state):
        if state == Qt.Checked:
            print(checktext)
            if self.sender() == MainWindow.checkBoxNone:
                MainWindow.checkB.setChecked(False)
            elif self.sender() == MainWindow.checkB:
                MainWindow.checkBoxNone.setChecked(False)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    mw = MainWindow()