from tkinter import *
from tkinter.ttk import *
from sympy import *
from matplotlib import rcParams

import threading

# Elements_Structure // Emission_Layer // Emission_Zone_Setting // Elements_Structure_Graph // Emission_Layer_Graph

file = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/hannimpeha.csv'
file_png = '/Users/hannahlee/PycharmProjects/penProject/controllers/resources/hannimpeha.png'
emission_png = '/Users/hannahlee/PycharmProjects/AwesomeProject/controllers/resources/EML_graph.png'
cols_element = ['L#', 'LayerName', 'Material', 'RefractiveIndex', 'Thickness', 'Unit']
cols_emission = ['L#', 'EM Materials', 'Spectrum', 'ExcitonProp', 'Q.Y', 'D.O', 'EMZone']

class Elements_Structure():

    def __init__(self, window):
        frame = Frame(window)
        frame.grid(row=0, column=1, sticky=NW, padx=20)
        label0 = Label(frame)
        label_elem = Label(label0, text="Elements Structure", font=("Arial", 13))

        self.label1 = Label(frame)
        label_measure = Label(self.label1, text="Number of Layers:")
        spin = Spinbox(self.label1, to=11, width=5)
        self.add_button = Button(self.label1, text="Add", command=self.add_row)
        self.del_button = Button(self.label1, text="Delete", command=self.delete_row)
        self.save_button = Button(self.label1, text="Save", command=self.save_row)

        self.listbox = Label(frame)
        #cols = ('L#', 'Layer Name', 'Material', 'Refractive Index', 'Thickness', 'Unit')
        self.listBox = Treeview(self.listbox, col=cols_element, show="headings")
        self.listBox.bind('<Double-1>', self.set_cell_value)

        for col in cols_element:
            self.listBox.column(col, width=85)
            self.listBox.heading(col, text=col, command=lambda _col=col: self.treeview_sort_column(self.listBox, _col, False))

        self.layer_name=["Al", "ETL", "EML", "HTL2", "HTL1", "ITO"]
        self.material = ["Al", "ETL", "EML", "HTL2", "HTL1", "ITO"]
        self.refractive_index = ["Al.dat", "ETL.dat", "EML.dat", "HTL.dat", "HTL1.dat", "ITO.dat"]
        self.thickness = [100, 100.5, 20, 10, 100.5, 70]
        self.unit = ["nm", "nm", "nm", "nm", "nm", "nm"]

        self.tempList = [[self.layer_name, self.material, self.refractive_index, self.thickness, self.unit]]
        self.num_row = len(self.tempList)

        for i in range(len(self.layer_name)):
            self.num_row = i+1
            self.listBox.insert('', i, values=(self.num_row, self.layer_name[i], self.material[i],
                                               self.refractive_index[i], self.thickness[i], self.unit[i]))

        self.tempList.sort(key=lambda e: e[1], reverse=True)

        label0.grid(row=0, column=1, sticky=NW)
        label_elem.grid(row=0, column=0, sticky=NE)
        self.label1.grid(row=0, column=1, columnspan=6, sticky=NE)
        label_measure.grid(row=0, column=1, sticky=NE)
        spin.grid(row=0, column=2, sticky=NE)
        self.listbox.grid(row=2, column=1, columnspan=7, sticky=NW, pady=5)
        self.listBox.grid(row=0, column=0)
        self.add_button.grid(row=2, column=1, sticky=NE)
        self.del_button.grid(row=2, column=2, sticky=NE)
        self.save_button.grid(row=2, column=3, sticky=NE)

        Emission_Layer(frame).__init__(frame)
        Emission_Zone_Setting(frame).__init__(frame)


    def add_row(self):
        self.num_row += 1
        # for i, (layer_name, material, refractive_index, thickness, unit) in enumerate(self.tempList, start=1):
        #     self.listBox.insert("", "end", values=(i, layer_name, material, refractive_index, thickness, unit))
        self.layer_name.append("to be named")
        self.material.append("to be named")
        self.refractive_index.append("to be named")
        self.thickness.append("to be named")
        self.unit.append("to be named")
        self.listBox.insert('', len(self.layer_name) - 1, values=(self.num_row,
                                                                  self.layer_name[len(self.layer_name) - 1],
                                                                  self.material[len(self.material) - 1],
                                                                  self.refractive_index[len(self.refractive_index) - 1],
                                                                  self.thickness[len(self.thickness) - 1],
                                                                  self.unit[len(self.unit) - 1]))
        #self.tempList.append([self.layer_name, self.material, self.refractive_index, self.thickness, self.unit])
        self.listBox.update()

    def treeview_sort_column(self, tv, col, reverse):
        l = [(tv.set(k, col), k) for k in tv.get_children('')]
        l.sort(reverse=reverse)
        for index, (val, k) in enumerate(l):
            tv.move(k, '', index)
            tv.heading(col, command=lambda: self.treeview_sort_column(tv, col, not reverse))

    def set_cell_value(self, event):
        for item in self.listBox.selection():
            item_text = self.listBox.item(item, "values")
            self.column = self.listBox.identify_column(event.x)
            self.row = self.listBox.identify_row(event.y)
        cn = int(str(self.column).replace('#', ''))
        rn = int(str(self.row).replace('I', ''))
        self.entryedit = Text(self.listBox, width=20, height=1)
        self.entryedit.place(x= cn, y= rn)

        self.okb = Button(self.listBox, text='OK', width=4, command=self.save_edit)
        self.okb.place(x= cn + 150, y= rn )

    def save_edit(self):
        self.listBox.set(self.listBox.selection(), column=self.column, value=self.entryedit.get(0.0, "end"))
        self.entryedit.destroy()
        self.okb.destroy()

    def delete_row(self):
        tuple = self.listBox.selection()
        self.listBox.delete(tuple)
        self.num_row -= 1

    def save_row(self):
        for line in self.listBox.get_children():
            with open(file, "w") as foo:
                foo.write(",".join([str(n) for n in cols_element])+"\n")
                foo.write(",".join([str(n) for n in self.listBox.item(line)['values']])+"\n")

class Emission_Layer():
    def __init__(self, window):
        frame = Frame(window)
        frame.grid(row=3, column=1, sticky=NW, pady=30)
        self.label = Label(frame, text="Emission Layer", font=("Arial",13))
        #cols = ('L#', 'EM Materials', 'Spectrum', 'Exciton Prop', 'Q.Y', 'D.O', 'EM Zone')
        self.listBox = Treeview(frame, columns=cols_emission, show='headings')

        for col in cols_emission:
            self.listBox.column(col, width=75)
            self.listBox.heading(col, text=col)
        tempList = [["none", "2pplAn_PL.dat", "1", "83", "94", "Sheet"]]
        tempList.sort(key=lambda e: e[1], reverse=True)
        for i, (em_materials, spectrum, exicton_prop, qy, do, em_zone) in enumerate(tempList, start=1):
            self.listBox.insert("", "end", values=(i, em_materials, spectrum, exicton_prop, qy, do, em_zone))
        self.label.grid(row=0, column=0, sticky=W)
        self.listBox.grid(row=1, column=0, sticky=W)


class Emission_Zone_Setting():
    def __init__(self, window):
        self.frame = Frame(window)
        self.frame.grid(row=4, column=1, sticky=NW)
        self.finished = False

        self.label0 = Label(self.frame)
        label_emission = Label(self.label0, text="Emission Zone Type",  font=("Arial", 13))
        self.v = IntVar()

        label_radio = Label(self.label0)
        radio0 = Radiobutton(label_radio, text="Sheet", variable=self.v, value=1)
        radio1 = Radiobutton(label_radio, text="Constant", variable=self.v, value=2)
        radio2 = Radiobutton(label_radio, text="Linear", variable=self.v, value=3)
        radio3 = Radiobutton(label_radio, text="Exponential", variable=self.v, value=4)
        radio4 = Radiobutton(label_radio, text="Gaussian Distribution", variable=self.v, value=5)

        label_range = Label(label_radio, text="Emit Range")
        entry = Entry(label_radio, width=5)

        label_eq = Label(self.label0, text="equation")
        self.text = Text(self.label0, width=37, height=10, wrap="none")
        #text.insert(self.choosing_expression())
        #text.insert('1.0', "y=a+bx")
        button = Button(self.label0, text="Show Equation", command=self.show_eq)

        self.label0.grid(row=0, column=0, rowspan=2, sticky=W)
        label_emission.grid(row=0, column=0, sticky=W, pady=5)
        label_radio.grid(row=1, column=0, sticky=W)
        radio0.grid(row=0, column=0, sticky=W)
        radio1.grid(row=1, column=0, sticky=W)
        radio2.grid(row=2, column=0, sticky=W)
        radio3.grid(row=3, column=0, sticky=W)
        radio4.grid(row=4, column=0, sticky=W)

        label_range.grid(row=5, column=0, sticky=W, padx=5, pady=5)
        entry.grid(row=5, column=1, sticky=E, padx=5, pady=5)

        label_eq.grid(row=0, column=1, sticky=W)
        self.text.grid(row=1, column=1, sticky=W)
        button.grid(row=2, column=1, sticky=W, pady=10)

    def choosing_expression(self):
        rcParams['text.usetex'] = True
        x, y, a, b, c, exp = symbols("x, y, a, b, c, exp")
        if self.v == "PY_VAR0":
            return Eq(x, a)
        elif self.v == "PY_VAR1":
            return Eq(y, a * x + b)
        elif self.v == "PY_VAR2":
            return Eq(y, a * exp ** (x + b) + c)

    def draw(self, win, size):
        self.win = win
        self.win.create_rectangle((0, 0, size, size), fill="white")

    def show_eq(self):
        global finished
        with threading.Lock():
            finished = False
        t = threading.Thread(target=self.count)
        t.daemon = True
        self.frame.after(1, self.check_status)
        t.start()

    def check_status(self):
        with threading.Lock():
            if not finished:
                self.frame.after(1, self.check_status)

    def count(self):
        global finished
        with threading.Lock():
            finished = True
            self.text.insert('1.0', "y=a+bx")