import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Treeview demo')
        self.geometry('620x200')

        self.tree = self.create_tree_widget()

    def create_tree_widget(self):
        columns = ('name')
        tree = ttk.Treeview(self, columns=columns, show='headings')

        tree.heading('name', text='Nombre')
        tree.grid(row=0, column=0, sticky=tk.NSEW)
        tree.insert('', tk.END, values=('John'))
        tree.insert('', tk.END, values=('Jane'))
        tree.insert('', 0, values=('Alice'))

        return tree


if __name__ == '__main__':
    app = App()
    app.mainloop()