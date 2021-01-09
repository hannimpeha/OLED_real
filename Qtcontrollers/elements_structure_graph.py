import sys

from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QVBoxLayout, QLabel, QGridLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

file = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/hannimpeha.csv'
foo_file = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/foo.png'
emission_image = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/EML_graph.png'
txt_file = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/text.csv'

class Elements_Structure_Graph(QWidget):
    def __init__(self):
        super().__init__()

        df = pd.read_csv(txt_file, header=None)
        self.layer_name = df[1]
        self.material = df[2]
        self.refractive_index = df[3]
        self.thickness = np.asarray(df[4])
        self.unit = df[5]
        self.draw_fig()
        graph = self.emission_layer_graph()

        label = QLabel()
        pixmap = QPixmap(foo_file)
        pixmap = pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)

        layout = QGridLayout()
        layout.addWidget(label, 0, 0)
        layout.addWidget(graph, 1, 0)

        self.setLayout(layout)

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

        self.fig.savefig(foo_file, transparent=True)

    def draw(self):
        tps = self.write_graph().pivot_table(values=["Thickness"], columns="LayerName", aggfunc='sum')
        tps = tps.div(tps.sum(1), axis=0)
        tps.plot.bar(stacked=True, ax=self.ax)

    def write_graph(self):
        return pd.read_csv(file, header=0)

    def emission_layer_graph(self):
        label = QLabel()
        pixmap = QPixmap(emission_image)
        pixmap = pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        return label