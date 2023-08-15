import sys
sys.path.append("./lexer")
from model import Model
from view import View
from controller import Controller
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.tk.call('source', './theme/breeze.tcl')
        ttk.Style().theme_use('breeze')

        self.geometry("1200x750")

        model = Model()

        view = View(self)
        view.pack(fill="both", expand=True)

        controller = Controller(model, view)

        view.set_controller(controller)

if __name__ == '__main__':
    app = App()
    app.mainloop()