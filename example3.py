import numpy as np
import matplotlib.pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure


class TopLevelWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.canvas = MplWidget()
        self.setCentralWidget(self.canvas)

class MplWidget(FigureCanvasQTAgg):
    def __init__(self, parent=None):
        fig = Figure()
        super(MplWidget, self).__init__(fig)
        self.setParent(parent)
        # Set default colors array
        self.defaultColors = np.array(
            [
                [0, 0.4470, 0.7410],
                [0.8500, 0.3250, 0.0980],
                [0.9290, 0.6940, 0.1250],
                [0.4660, 0.6740, 0.1880],
                [0.6350, 0.0780, 0.1840],
                [0.4940, 0.1840, 0.5560],
                [0.3010, 0.7450, 0.9330],
            ]
        )

        # Create a figure with axes

        self.ax = self.figure.add_subplot(111)

        # Form the plot and shading
        self.bottomLeftX = 0
        self.bottomLeftY = 0
        self.topRightX = 0
        self.topRightY = 0
        self.x = np.array(
            [
                self.bottomLeftX,
                self.bottomLeftX,
                self.topRightX,
                self.topRightX,
                self.bottomLeftX,
            ]
        )
        self.y = np.array(
            [
                self.bottomLeftY,
                self.topRightY,
                self.topRightY,
                self.bottomLeftY,
                self.bottomLeftY,
            ]
        )

        (self.myPlot,) = self.ax.plot(self.x, self.y, color=self.defaultColors[0, :])
        self.aspan = self.ax.axvspan(
            self.bottomLeftX, self.topRightX, color=self.defaultColors[0, :], alpha=0
        )
        self.ax.set_xlim((-100, 100))
        self.ax.set_ylim((-100, 100))

        # Set moving flag false (determines if mouse is being clicked and dragged inside plot). Set graph snap
        self.moving = False
        self.plotSnap = 5

        # Set up connectivity
        self.cid1 = self.mpl_connect("button_press_event", self.onclick)
        self.cid2 = self.mpl_connect("button_release_event", self.onrelease)
        self.cid3 = self.mpl_connect("motion_notify_event", self.onmotion)

    def setSnapBase(self, base):
        return lambda value: int(base * round(float(value) / base))

    def onclick(self, event):
        if self.plotSnap <= 0:
            self.bottomLeftX = event.xdata
            self.bottomLeftY = event.ydata
        else:
            self.calculateSnapCoordinates = self.setSnapBase(self.plotSnap)
            self.bottomLeftX = self.calculateSnapCoordinates(event.xdata)
            self.bottomLeftY = self.calculateSnapCoordinates(event.ydata)

        try:
            self.aspan.remove()
        except:
            pass

        self.moving = True

    def onrelease(self, event):
        if self.plotSnap <= 0:
            self.topRightX = event.xdata
            self.topRightY = event.ydata
        else:
            try:
                calculateSnapCoordinates = self.setSnapBase(self.plotSnap)
                self.topRightX = calculateSnapCoordinates(event.xdata)
                self.topRightY = calculateSnapCoordinates(event.ydata)
            except:
                pass

        self.x = np.array(
            [
                self.bottomLeftX,
                self.bottomLeftX,
                self.topRightX,
                self.topRightX,
                self.bottomLeftX,
            ]
        )
        self.y = np.array(
            [
                self.bottomLeftY,
                self.topRightY,
                self.topRightY,
                self.bottomLeftY,
                self.bottomLeftY,
            ]
        )

        self.myPlot.set_xdata(self.x)
        self.myPlot.set_ydata(self.y)
        # ax.fill_between(x, y, color=defaultColors[0, :], alpha=.25)
        ylimDiff = self.ax.get_ylim()[1] - self.ax.get_ylim()[0]
        self.aspan = self.ax.axvspan(
            self.bottomLeftX,
            self.topRightX,
            (self.bottomLeftY - self.ax.get_ylim()[0]) / ylimDiff,
            (self.topRightY - self.ax.get_ylim()[0]) / ylimDiff,
            color=self.defaultColors[0, :],
            alpha=0.25,
            )

        self.moving = False
        self.draw()

    def onmotion(self, event):
        if not self.moving:
            return
        if event.inaxes is None:
            return
        if event.button != 1:
            return

        if self.plotSnap <= 0:
            self.topRightX = event.xdata
            self.topRightY = event.ydata
        else:
            self.calculateSnapCoordinates = self.setSnapBase(self.plotSnap)
            self.topRightX = self.calculateSnapCoordinates(event.xdata)
            self.topRightY = self.calculateSnapCoordinates(event.ydata)

        self.x = np.array(
            [
                self.bottomLeftX,
                self.bottomLeftX,
                self.topRightX,
                self.topRightX,
                self.bottomLeftX,
            ]
        )
        self.y = np.array(
            [
                self.bottomLeftY,
                self.topRightY,
                self.topRightY,
                self.bottomLeftY,
                self.bottomLeftY,
            ]
        )
        self.myPlot.set_xdata(self.x)
        self.myPlot.set_ydata(self.y)

        self.draw()




if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = TopLevelWindow()
    w.show()

    sys.exit(app.exec_())