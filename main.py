import sys
from PyQt5.QtWidgets import QWidget, QAction, QTabWidget, QVBoxLayout, QApplication, QMenuBar, QGridLayout
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon

from tab1 import Tab1

class Real(QWidget):
    def __init__(self):
        super().__init__()
        self.making_file()
        self.making_tabs()

        layout = QVBoxLayout()
        layout.addWidget(self.menuBar)
        self.setMinimumSize(QSize(1600, 900))
        self.setWindowTitle('JooAm Angular Luminence Spectometer')

    def making_file(self):
        self.menuBar = QMenuBar()

        newAction = QAction(QIcon('new.png'), '&New', self)
        newAction.setShortcut('Ctrl+N')

        openAction = QAction(QIcon('open.png'), '&Open', self)
        openAction.setShortcut('Ctrl+O')

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')

        fileMenu = self.menuBar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)


    def making_tabs(self):
        tab1 = QWidget()
        tab2 = QWidget()

        tabs = QTabWidget()
        tabs.addTab(tab1, '2PPlAn_PL')
        tabs.addTab(tab2, 'Result')

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(tabs)

        grid = QGridLayout()
        Tab1.setLayout(tab1, grid)

        self.setLayout(self.vbox)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Real()
    window.show()
    sys.exit(app.exec_())
