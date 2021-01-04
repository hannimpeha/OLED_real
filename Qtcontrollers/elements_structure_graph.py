import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QLabel
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import pandas as pd
import numpy as np
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

file = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/hannimpeha.csv'
foo_file = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/foo.png'
class Drawing(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('Elements_Structure_Graph')
        self.layer_name = ["Al", "ETL", "EML", "HTL2", "HTL1", "ITO"]
        self.material = ["Al", "ETL", "EML", "HTL2", "HTL1", "ITO"]
        self.refractive_index = ["Al.dat", "ETL.dat", "EML.dat", "HTL.dat", "HTL1.dat", "ITO.dat"]
        self.thickness = np.asarray([100, 100.5, 20, 10, 100.5, 70])
        self.unit = ["nm", "nm", "nm", "nm", "nm", "nm"]
        self.draw_fig()

        label = QLabel(self)
        pixmap = QPixmap(foo_file)
        pixmap = pixmap.scaled(128, 128, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)

        layout = QVBoxLayout()
        layout.addWidget(label)

    def draw_fig(self):
        self.fig = plt.Figure(figsize=(4.5, 4.5))
        self.canvas = FigureCanvas(self.fig)
        self.ax = self.fig.add_subplot(111)

        tps = pd.DataFrame(list(zip(self.layer_name, self.thickness)), columns=['LayerName', 'Thickness'])
        tps.pivot_table(values=["Thickness"], columns="LayerName", aggfunc='sum')
        colors = ["slateblue", "thistle", "turquoise", "olive", "skyblue", "pink"]
        tps.set_index('LayerName').T.plot(kind='bar', stacked=True, ax=self.ax, color=colors, width=200)

        for index, rect in enumerate(self.ax.patches):
            height = rect.get_height()
            width = rect.get_width()
            x = rect.get_x()
            y = rect.get_y()

            label_text = f'{height}'
            label_x = x + width / 2
            label_y = y + height / 2
            if height > 0:
                self.ax.text(label_x, label_y, "%s %s" % (label_text, self.layer_name[index]), ha='center', va='center',
                             fontsize=8)

        self.ax.axes.get_xaxis().set_visible(False)
        self.ax.legend().remove()

        self.fig.savefig(foo_file)

    def draw(self):
        tps = self.write_graph().pivot_table(values=["Thickness"], columns="LayerName", aggfunc='sum')
        tps = tps.div(tps.sum(1), axis=0)
        tps.plot.bar(stacked=True, ax=self.ax)

    def write_graph(self):
        return pd.read_csv(file, header=0)

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = Drawing()
#     window.show()
#     sys.exit(app.exec_())