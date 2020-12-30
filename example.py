# import ctypes
#
# hannimpeha = ctypes.CDLL("./testlib.so")
#
# hannimpeha.main()
#

# from oct2py import octave
#
# octave.addpath('/Users/hannahlee/PycharmProjects/AwesomeProject/library')
# octave.eval("OLED_main")

from tkinter import ttk
import tkinter as tk


blow = [("january", "2013"),("february", "2014"),("march", "2015"),("april",
"2016"),("may", "2017")]

def append_select():
    cur_id = tree.focus()

    data = e1_sub.get()  # if none is provided the default should 2018
    if not data:
        data = 2018

    if cur_id:
        month = tree.item(cur_id)['values'][0]
        tree2.insert("", tk.END, values=(month, data))


root = tk.Tk()
root.geometry("500x500")

tree = ttk.Treeview(columns=("columns1", "columns"), show="headings",
selectmode="browse")
tree.heading("#1", text="Month")
tree.heading("#2", text="Year")

for n in blow:
    tree.insert("", tk.END, values=(n))

tree.pack()

e1_sub = tk.StringVar()
e1 = tk.Entry(root, textvariable=e1_sub)
e1.pack()

b1 = tk.Button(text="append", command=append_select)
b1.pack()

tree2 = ttk.Treeview(columns=("Month", "Year"), show="headings")
tree2.heading("#1", text="First name")
tree2.heading("#2", text="Surname")
tree2.pack()

root.mainloop()