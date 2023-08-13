import sys
sys.path.append("./compiler")
from model import Model
from view import View
from controller import Controller
import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.tk.call('source', './yaru/yaru.tcl')
        # Set the theme with the theme_use method
        ttk.Style().theme_use('yaru')

        self.title('IDE')
        self.geometry("800x450")

        model = Model()

        view = View(self)
        view.pack(fill="both", expand=True)

        controller = Controller(model, view)
        self.bind('<<NotebookTabChanged>>',view.update_open_tab)

        view.set_controller(controller)

if __name__ == '__main__':
    app = App()
    app.mainloop()