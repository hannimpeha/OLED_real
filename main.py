from controllers.elements_structure import *
from controllers.logo_image import *
from controllers.axes_properties import *
from controllers.plotting_param import *
from controllers.elements_structure_graph import *
from tkinter import filedialog, simpledialog, ttk


class Simulator():
    def __init__(self):
        self.root = Tk()
        self.root.title("JooAm Angular Luminance Spectrometer")
        self.root.iconbitmap("/Users/hannahlee/PycharmProjects/AwesomeProject/controllers/resources/pyc.ico")
        self.root.geometry('{}x{}'.format(1600, 900))
        self.root.resizable(False, False)
        self.root.update()
        self.main()

    def main(self):
        s = Style()
        s.theme_use("alt")
        s.configure("TProgressbar", thickness=30)
        s.configure("Treeview", rowheight=20)

        menubar = Menu(self.root)
        filemenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=filemenu)

        filemenu.add_command(label="New", command=self.file_new)
        filemenu.add_command(label="Open", command=self.file_open)
        filemenu.add_command(label="Save", command=self.file_save)
        filemenu.add_command(label="Export", command=self.file_export)
        filemenu.add_command(label="Exit", command=self.root.quit)
        self.root.configure(menu=menubar)

        tabControl = ttk.Notebook(self.root)
        tab1 = ttk.Frame(tabControl)
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab1, text="2PPlAn_PL")
        tabControl.add(tab2, text="Result")
        tabControl.pack(expand=1, fill="both")

        Elements_Structure(Frame(self.root)).__init__(tab1)
        Elements_Structure_Graph(Frame(self.root)).__init__(tab1)
        Logo_Image(Frame(self.root)).__init__(tab1)

        Axes_Properties(Frame(self.root)).__init__(tab2)
        Elements_Structure_Graph(Frame(self.root)).__init__(tab2)
        Plotting_Param(Frame(self.root)).__init__(tab2)

    def file_new(self):
        filename = simpledialog.askstring("file name", "Enter the file name")
        open(filename + ".luxl", "w")

    def file_open(self):
        filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("luxl files", "*.luxl"), ("all files", "*.*")))

    def file_save(self):
        filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                    filetypes=(("luxl files", "*.luxl"), ("all files", "*.*")))

    def file_export(self):
        filedialog.askdirectory()


Simulator().root.mainloop()