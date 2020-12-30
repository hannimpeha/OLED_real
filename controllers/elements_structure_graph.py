from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
import numpy as np

file = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/hannimpeha.csv'
file_png = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/hannimpeha.png'
emission_png = '/Users/hannahlee/PycharmProjects/AwesomeProject/controllers/resources/EML_graph.png'

class Elements_Structure_Graph():
    def __init__(self, window):
        self.frame = Frame(window)
        self.frame.grid(row=0, column=0, rowspan=4, sticky=NW)
        label_graph = Label(self.frame, text="Elements Structure Graph")
        label_graph.grid(row=0, column=0, padx=10, sticky=W)

        self.button = Button(self.frame, text="ReLoad", command=self.draw)
        self.button.grid(row=0, column=0, padx=10, sticky=E)
        self.fig = plt.Figure(figsize=(4.5, 4.5))
        canvas = FigureCanvasTkAgg(self.fig, master=self.frame)
        canvas.get_tk_widget().grid(row=2, column=0, padx=10, pady=10)
        self.ax = self.fig.add_subplot(111)
        self.fig.set_canvas(canvas=canvas)

        self.layer_name = ["Al", "ETL", "EML", "HTL2", "HTL1", "ITO"]
        self.material = ["Al", "ETL", "EML", "HTL2", "HTL1", "ITO"]
        self.refractive_index = ["Al.dat", "ETL.dat", "EML.dat", "HTL.dat", "HTL1.dat", "ITO.dat"]
        self.thickness = np.asarray([100, 100.5, 20, 10, 100.5, 70])
        self.unit = ["nm", "nm", "nm", "nm", "nm", "nm"]
        tps = pd.DataFrame(list(zip(self.layer_name, self.thickness)), columns =['LayerName', 'Thickness'])
        tps.pivot_table(values=["Thickness"], columns="LayerName", aggfunc='sum')
        colors = ["slateblue", "thistle", "turquoise", "olive", "skyblue", "pink"]
        # tps.div(tps.sum(1), axis=0)
        tps.set_index('LayerName').T.plot(kind='bar', stacked=True, ax=self.ax, color=colors)


        for index, rect in enumerate(self.ax.patches):
            height = rect.get_height()
            width = rect.get_width()
            x = rect.get_x()
            y = rect.get_y()

            label_text = f'{height}'
            label_x = x + width / 2
            label_y = y + height / 2
            if height > 0:
                self.ax.text(label_x, label_y, "%s %s" % (label_text, self.layer_name[index]), ha='center', va='center', fontsize=8 )

        self.ax.axes.get_xaxis().set_visible(False)
        self.ax.legend().remove()
        Emission_Layer_Graph(self.frame).__init__(self.frame)

    def draw(self):
        matplotlib.use('TkAgg')
        tps = self.write_graph().pivot_table(values=["Thickness"], columns="LayerName", aggfunc='sum')
        tps = tps.div(tps.sum(1), axis=0)
        tps.plot.bar(stacked=True, ax=self.ax)

    def write_graph(self):
        return pd.read_csv(file, header=0)

class Emission_Layer_Graph():
    def __init__(self, window):
        frame = Frame(window)
        frame.grid(row=4, column=0, rowspan=3, padx=30, sticky=NW)

        label_graph = Label(frame, text="Emission Layer Graph")
        label_graph.grid(row=0, column=0, sticky=NW)
        self.width = 450
        self.height = 250
        self.image = Image.open(emission_png).convert("RGB")
        self.copy = self.image.copy()
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = Label(frame, image=self.photo)
        self.label.bind('<Configure>', self.resize_image())
        self.label.grid(row=1, column=0)

    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = event.copy.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        event.label.config(image=photo)
        event.label.image = photo