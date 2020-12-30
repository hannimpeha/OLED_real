from tkinter import *
from tkinter.ttk import *
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk

# Elements_Structure_Graph // Emission_Layer_Graph
root = Tk()


class Elements_Structure_Graph():
    def __init__(self, window):
        frame = Frame(window)
        frame.grid(row=0, column=0, rowspan=3, sticky=NW)
        label_graph = Label(frame, text="Elements Structure Graph")
        label_graph.grid(row=0, column=0, padx=10)

        self.graph = Label(frame)
        self.graph.grid(row=1, column=0, padx=10, pady=10)
        df = pd.read_csv("/Users/hannahlee/PycharmProjects/penProject/controllers/resources/hannimpeha.csv", header=0)
        self.fig = plt.Figure(figsize=(4.5, 4.5))

        matplotlib.use('TkAgg')
        canvas = FigureCanvasTkAgg(self.fig, master=self.graph)
        canvas.get_tk_widget().grid(row=1, column=0, padx=10, pady=10)
        self.fig.set_canvas(canvas=canvas)
        tps = df.pivot_table(values=["Thickness"], columns="LayerName", aggfunc='sum')
        tps = tps.div(tps.sum(1), axis=0)
        ax = self.fig.add_subplot(111)
        tps.plot.bar(stacked=True, ax=ax)

class Emission_Layer_Graph():
    def __init__(self, window):
        frame = Frame(window)
        frame.grid(row=2, column=0, rowspan=2, sticky=SW, padx=30, pady=50)

        label_graph = Label(frame, text="Emission Layer Graph")
        label_graph.grid(row=0, column=0, sticky=NW)
        self.width = 450
        self.height = 250
        self.image = Image.open(
            '/Users/hannahlee/PycharmProjects/AwesomeProject/controllers/resources/EML_graph.png').convert("RGB")
        self.copy = self.image.copy()
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = Label(frame, image=self.photo)
        self.label.bind('<Configure>', self.resize_image())
        self.label.grid(row=1, column=0, sticky=S)

    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = event.copy.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        event.label.config(image=photo)
        event.label.image = photo

Elements_Structure_Graph(root).__init__(root)
root.mainloop()
