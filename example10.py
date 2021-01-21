import sys
import numpy as np

from matplotlib.backends.qt_compat import QtWidgets
from matplotlib.backends.backend_qt5agg import (FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

from matplotlib.figure import Figure
from matplotlib import animation


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self._main = QtWidgets.QWidget()
        self.setCentralWidget(self._main)
        layout = QtWidgets.QVBoxLayout(self._main)

        self.fig = Figure(figsize=(5, 3))
        self.canvas = FigureCanvas(self.fig)
        layout.addWidget(self.canvas)
        self.addToolBar(NavigationToolbar(self.canvas, self))

        self.setup()

    def setup(self):
        self.ax = self.fig.subplots()
        self.ax.set_aspect('equal')
        self.ax.grid(True, linestyle = '-', color = '0.10')
        self.ax.set_xlim([-15, 15])
        self.ax.set_ylim([-15, 15])

        self.scat = self.ax.scatter([], [],  zorder=3)
        self.scat.set_alpha(0.8)

        self.anim = animation.FuncAnimation(self.fig, self.update,
                                            frames = 720, interval = 10)


    def update(self, i):
        self.scat.set_offsets(([np.cos(np.radians(i))*7.5, np.sin(np.radians(i))*7.5],
                               [np.cos(np.radians(i/2))*9, np.sin(np.radians(i/2))*9]))



if __name__ == "__main__":
    qapp = QtWidgets.QApplication(sys.argv)
    app = ApplicationWindow()
    app.show()
    qapp.exec_()