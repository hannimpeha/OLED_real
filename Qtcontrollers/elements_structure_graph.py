import math
from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats

file = 'Qtcontrollers/resources/hannimpeha.csv'
foo_file = 'Qtcontrollers/resources/foo.png'
em_figure = 'Qtcontrollers/resources/EML_graph.png'
txt_file = 'Qtcontrollers/resources/text.csv'
em_file = 'Qtcontrollers/resources/text_em.csv'

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
        graph = Emission_Layer_Graph()

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
        colors = ["slateblue", "thistle", "turquoise", "forestgreen", "skyblue", "pink", "lime", "darkturquoise", "lightgreen", "powderblue","lightsalmon"]
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

class Emission_Layer_Graph(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        tab1 = QWidget()
        tab2 = QWidget()

        label = QLabel()
        sub_layout = QVBoxLayout()
        pixmap = QPixmap(em_figure)
        pixmap = pixmap.scaled(400, 400, QtCore.Qt.KeepAspectRatio)
        label.setPixmap(pixmap)
        label.resize(pixmap.width(), pixmap.height())
        sub_layout.addWidget(label)

        tabs = QTabWidget()
        tabs.addTab(tab1, "hannimpeha1")
        tabs.addTab(tab2, "hannimpeha2")

        tabs.setLayout(sub_layout)
        layout.addWidget(tabs)

        self.setLayout(layout)

        mu = 0
        variance = 1
        sigma = math.sqrt(variance)
        x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
        plt.plot(x, stats.norm.pdf(x, mu, sigma))
        plt.suptitle("2pplAn_PL", fontsize=20)
        plt.savefig(em_figure, transparent=True)