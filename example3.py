import tkinter as tk
import tkinter.ttk as ttk

class App(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        self.entry = tk.Entry(self)
        self.button = tk.Button(self, text='Search', command=self.search)
        self.tree = ttk.Treeview(self)
        # ...
    def search(self, item=''):
        children = self.tree.get_children(item)
        for child in children:
            text = self.tree.item(child, 'text')
            if text.startswith(self.entry.get()):
                self.tree.selection_set(child)
                return True
            else:
                res = self.search(child)
                if res:
                    return True
