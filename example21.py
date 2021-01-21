import sys
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLabel, QMessageBox,QSizePolicy, QLayoutItem,QFrame,QHBoxLayout, QGridLayout, QVBoxLayout
from PyQt5.QtCore import QCoreApplication,QSize,QFileInfo
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from functools import partial
from PyQt5.QtCore import pyqtSlot
import sip

class ClickableWidget(QWidget):
    clicked = pyqtSignal(int)
    def  __init__(self, n=5, parent=None):
        QWidget.__init__(self, parent)
        self.hlayout = QVBoxLayout(self)
        for i in range(n):
            label = QLabel("btn {}".format(i), self)
            label.setProperty("index", i)
            self.hlayout.addWidget(label)
            label.installEventFilter(self)

    def eventFilter(self, obj, event):
        if isinstance(obj, QLabel) and event.type() == QEvent.MouseButtonPress:
            i = obj.property("index")
            self.clicked.emit(i)
        return QWidget.eventFilter(self, obj, event)

class DynamicWidget(QWidget):
    def  __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.hlayout = QVBoxLayout(self)

    def changeWidget(self, n):
        def clearLayout(layout):
            item = layout.takeAt(0)
            while item:
                w = item.widget()
                if w:
                    w.deleteLater()
                lay = item.layout()
                if lay:
                    clearLayout(item.layout())
                item = layout.takeAt(0)

        clearLayout(self.hlayout)
        for i in range(n):
            label = QLabel("btn {}".format(i), self)
            self.hlayout.addWidget(label)


class Screen(QWidget):
    def __init__(self):
        super(Screen, self).__init__()
        self.layout = QHBoxLayout(self)
        c = ClickableWidget(6, self)
        d = DynamicWidget(self)
        c.clicked.connect(d.changeWidget)
        self.layout.addWidget(c)
        self.layout.addWidget(d)

app = QApplication(sys.argv)
Gui = Screen()
sys.exit(app.exec_())