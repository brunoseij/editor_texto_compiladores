from model import Model
from view import View
from controller import Controller
import tkinter as tk


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('IDE')
        self.geometry("800x450")

        # create a model
        model = Model()

        # create a view and place it on the root window
        view = View(self)
        view.pack(fill="both", expand=True)

        # create a controller
        controller = Controller(model, view)
        self.bind('')
        self.bind('<Control-s>', controller.handle_keypress)
        self.bind('<Control-a>', view.select_all)
        self.bind("<Button-1>", view.leftclick)
        #self.bind('')
        # set the controller to view
        view.set_controller(controller)

if __name__ == '__main__':
    app = App()
    app.mainloop()  #instancia do app