from tkinter import *
from tkinter import filedialog
from tkinter.ttk import *
from os import *


file = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/hannimpeha.csv'
file_png = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/hannimpeha.png'
emission_png = '/Users/hannahlee/PycharmProjects/AwesomeProject/controllers/resources/EML_graph.png'
cols_element = ['L#', 'LayerName', 'Material', 'RefractiveIndex', 'Thickness', 'Unit']
# Axes_Properties // Graph // Elements_Structure_Graph // Emission_Layer_Graph
class Axes_Properties():
    def __init__(self, window):
        frame = Frame(window)
        frame.grid(row=0, column=1, sticky=NW, padx=20)

        self.label = Label(frame, text="Axes Properties", font=("Arial", 13))
        cols = ('Axis', 'Name', 'Min', 'Max')
        self.listBox = Treeview(frame, col=cols, show="headings")
        for col in cols:
            self.listBox.column(col, width=120)
            self.listBox.heading(col, text=col)

        tempList = [["X-Axis", "Al", "-", "-"], ["Y-Axis", "EML", "-", "-"], ["Z-Axis", "EFL", "-", "-"]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (axis, name, min, max) in enumerate(tempList, start=1):
            self.listBox.insert("", "end", values=(axis, name, min, max))

        self.label.grid(row=0, column=1, sticky=NW)
        self.listBox.grid(row=1, column=1, sticky=NW)

        Plotting(frame).__init__(frame)
        Exportation(frame).__init__(frame)
        # Elements_Structure_Graph(frame).__init__(frame)
        # Emission_Layer_Graph(frame).__init__(frame)


class Plotting():
    def __init__(self, window):
        frame = Frame(window)
        frame.grid(row=2, column=1, sticky=NW, pady=20)

        label0 = Label(frame, text="Plotting",font=("Arial",13))

        label1 = Label(frame)
        label_graph = Label(label1, text="Graph:")
        emission = StringVar(label1)
        emission.set("Emission Spectrum 3D")
        option_g = OptionMenu(label1, emission)
        label_x = Label(label1, text="X-axis:")
        angle = StringVar(label1)
        angle.set("Angle")
        option_x = OptionMenu(label1, angle)
        label_y = Label(label1, text="Y-axis:")
        wave = StringVar(label1)
        wave.set("Wavelength")
        option_y = OptionMenu(label1, wave)
        label_z = Label(label1, text="Z-axis:")
        intensity = StringVar(label1)
        intensity.set("Intensity")
        option_z = OptionMenu(label1, intensity)

        label2 = Label(frame)
        label_fixed = Label(label2, text="Fixed Parameters")
        scrol = Scrollbar(label2)

        cols = ("1", "2", "3")
        listBox = Treeview(label2, col=cols, show="headings", yscrollcommand=scrol.set)
        for col in cols:
            listBox.column(col, width=150)
            listBox.heading(col, text=col)
        tempList = [["Thickness of B3PYMPM", "50"],
                    ["Thickness of TAPC", "50"]]

        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (param, measure) in enumerate(tempList, start=1):
            listBox.insert("", "end", values=(i, param, measure))

        label0.grid(row=0, sticky=NW)

        label1.grid(row=2, sticky=NW, pady=30)
        label_graph.grid(row=0, column=0, sticky=NW)
        option_g.grid(row=0, column=1, sticky=NW)
        label_x.grid(row=2, column=0, sticky=NW)
        option_x.grid(row=2, column=1, sticky=E)
        label_y.grid(row=3, column=0, sticky=NW)
        option_y.grid(row=3, column=1,sticky=E)
        label_z.grid(row=4, column=0, sticky=NW)
        option_z.grid(row=4, column=1,sticky=E)

        label2.grid(row=1, sticky=NW)
        label_fixed.grid(row=0, sticky=NW)
        scrol.grid(row=1, sticky=NW)
        listBox.grid(row=1, sticky=NW)

        option_g.config(width=20)
        option_x.config(width=20)
        option_y.config(width=20)
        option_z.config(width=20)
        scrol.config(command=listBox.yview)


class Exportation():
    def __init__(self, window):
        frame = Frame(window)
        frame.grid(row=3, column=1, sticky=NW)

        label0 = Label(frame, text="Exportation", font=("Arial",13))

        label1 = Label(frame)
        pathlabel = Label(label1, text="Path:")
        fileEntry = Entry(label1, textvariable=path.dirname(__file__))
        browse_button = Button(label1, text="Browse", command=self.browse)

        label2 = Label(frame)
        typelabel = Label(label2, text="Type:")
        check_button_text = Checkbutton(label2, text="text")
        check_button_image = Checkbutton(label2, text="image")

        label3 = Label(frame)
        namelabel = Label(label3, text="Name:")
        entry = Entry(label3)
        button = Button(label3, text="Export", command=self.getFileName)

        label0.grid(row=0, column=0, sticky=NW)
        label1.grid(row=1, column=0, sticky=NW)
        pathlabel.grid(row=0, column=0, sticky=NW)
        fileEntry.grid(row=0, column=1, sticky=NW)
        browse_button.grid(row=0, column=2, sticky=NW)

        label2.grid(row=2, column=0, sticky=NW)
        typelabel.grid(row=0, column=0, sticky=NW)
        check_button_text.grid(row=0, column=1, sticky=NW)
        check_button_image.grid(row=0, column=2, sticky=NW)

        label3.grid(row=3, column=0, sticky=NW)
        namelabel.grid(row=0, column=0, sticky=NW)
        entry.grid(row=0, column=1, sticky=NW)
        button.grid(row=0, column=2, sticky=E)

    def browse(self):
        filedialog.askdirectory()

    def getFileName(self):
        print("Hello World")

# class Elements_Structure_Graph():
#     def __init__(self, window):
#         frame = Frame(window)
#         frame.grid(row=0, column=0, rowspan=3, sticky=NW)
#         label_graph = Label(frame, text="Elements Structure Graph")
#         label_graph.grid(row=0, column=0, padx=10, sticky=W)
#
#         self.width = 450
#         self.height = 480
#         self.image = Image.open(file_png).convert("RGB")
#         self.copy = self.image.copy()
#         self.photo = ImageTk.PhotoImage(self.image)
#         self.label = Label(frame, image=self.photo)
#         self.label.bind('<Configure>', self.resize_image())
#         self.label.grid(row=1, column=0)
#
#     def resize_image(event):
#         new_width = event.width
#         new_height = event.height
#         image = event.copy.resize((new_width, new_height))
#         photo = ImageTk.PhotoImage(image)
#         event.label.config(image=photo)
#         event.label.image = photo
#
# class Emission_Layer_Graph():
#     def __init__(self, window):
#         frame = Frame(window)
#         frame.grid(row=2, column=0, rowspan=2, padx=30, sticky=S)
#
#         label_graph = Label(frame, text="Emission Layer Graph")
#         label_graph.grid(row=0, column=0, sticky=NW)
#         self.width = 450
#         self.height = 250
#         self.image = Image.open(emission_png).convert("RGB")
#         self.copy = self.image.copy()
#         self.photo = ImageTk.PhotoImage(self.image)
#         self.label = Label(frame, image=self.photo)
#         self.label.bind('<Configure>', self.resize_image())
#         self.label.grid(row=1, column=0)
#
#     def resize_image(event):
#         new_width = event.width
#         new_height = event.height
#         image = event.copy.resize((new_width, new_height))
#         photo = ImageTk.PhotoImage(image)
#         event.label.config(image=photo)
#         event.label.image = photo