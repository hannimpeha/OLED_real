from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from PIL import Image, ImageTk

# Plotting // Exportation
class Plotting_Param():
    def __init__(self, window):
        frame = Frame(window)
        frame.grid(row=0, column=2, sticky=NW, padx=10, pady=10)
        self.width = 480
        self.height = 230
        self.image = Image.open('/Users/hannahlee/PycharmProjects/AwesomeProject/controllers/resources/Logo.png').convert("RGB")
        self.copy = self.image.copy()
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = Label(frame, image=self.photo)
        self.label.bind('<Configure>', self.resize_image())
        self.label.grid(row=0, column=2, sticky=NW)

        Graph(frame).__init__(frame)

    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = event.copy.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        event.label.config(image = photo)
        event.label.image = photo


class Graph():
    def __init__(self, window):
        frame = Frame(window)
        frame.grid(row=1, column=2, pady=50)
        label_graph = Label(frame, text="Graph", font=("Arial", 13))
        label_graph.grid(row=1, column=1, sticky=NW)
        self.width = 480
        self.height = 480
        self.image = Image.open('/Users/hannahlee/PycharmProjects/AwesomeProject/controllers/resources/contour.png').convert("RGB")
        self.copy = self.image.copy()
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = Label(frame, image=self.photo)
        self.label.bind('<Configure>', self.resize_image())
        self.label.grid(row=2, column=1, rowspan=2, sticky=NW)

    def resize_image(event):
        new_width = event.width
        new_height = event.height
        image = event.copy.resize((new_width, new_height))
        photo = ImageTk.PhotoImage(image)
        event.label.config(image = photo)
        event.label.image = photo