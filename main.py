import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QAction, QTabWidget, QVBoxLayout, QApplication
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        menuBar = self.menuBar()

        newAction = QAction(QIcon('new.png'), '&New', self)
        newAction.setShortcut('Ctrl+N')

        openAction = QAction(QIcon('open.png'), '&Open', self)
        openAction.setShortcut('Ctrl+O')

        exitAction = QAction(QIcon('exit.png'), '&Exit', self)
        exitAction.setShortcut('Ctrl+Q')

        fileMenu = menuBar.addMenu('&File')
        fileMenu.addAction(newAction)
        fileMenu.addAction(openAction)
        fileMenu.addAction(exitAction)

class MainVBox(QWidget):
    def __init__(self):
        super().__init__()
        tab1 = QWidget()
        tab2 = QWidget()

        tabs = QTabWidget()
        tabs.addTab(tab1, '2PPlAn_PL')
        tabs.addTab(tab2, 'Result')

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)

class Real(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(MainWindow())
        layout.addWidget(MainVBox())
        self.setLayout(layout)
        self.setMinimumSize(QSize(1600, 900))
        self.setWindowTitle('JooAm Angular Luminence Spectometer')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Real()
    window.show()
    sys.exit(app.exec_())
