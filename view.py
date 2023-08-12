import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import os

background_color = "#202124"

class View(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.text_list = []
        self.path = None
        self.tab = None
        self.frm_menuBar = tk.Frame(master=self)
        self.frm_menuBar.pack(fill="x", expand=False)

        self.btn_new = tk.Button(master=self.frm_menuBar, text="new", command=self.new)
        self.btn_new.pack(side="left")

        self.btn_open = tk.Button(master=self.frm_menuBar, text="open", command=self.open)
        self.btn_open.pack(side="left")

        self.btn_save = tk.Button(master=self.frm_menuBar, text="save", command=self.save)
        self.btn_save.pack(side="left")

        self.main = ttk.Notebook(master=self)
        self.main.pack(fill="both", expand=True) 

    def set_controller(self, controller):
        self.controller = controller

    def update_open_tab(self, e):
        self.tab = self.text_list[self.main.index(self.main.select())][0]
        self.path = self.text_list[self.main.index(self.main.select())][1]
        self.controller.change_tab(self.path)
        self.configure_tags()
        self.controller.highlight_text()

    def get_selected_tab_filepath(self):
        return self.path

    def set_text(self, content):
        self.tab.delete("1.0", "end")
        self.tab.insert("1.0", content)

    def get_text(self):
        return self.tab.get("1.0", "end")

    def new(self):
        path = fd.asksaveasfilename()
        if path:
            self.controller.new(path)

    def save(self):
        self.controller.save()

    def open(self):
        path = fd.askopenfilename()
        if path:
            self.controller.open(path)
    
    def highlight(self, tokens):
        for tag in self.tab.tag_names():
            self.tab.tag_remove(tag, "1.0", "end")
        for token in tokens:
            self.tab.tag_add(token["id"], f"{token['line']}.{token['start']}",f"{token['line']}.{token['end']}")

    def configure_tags(self):
        for i in range(34):
            if i >= 1 and i <= 3:
                self.tab.tag_config(f"{i}", foreground = "green")
            elif i <= 5:
                self.tab.tag_config(f"{i}", foreground = "yellow")
            elif i<=8:
                self.tab.tag_config(f"{i}", foreground = "blue")
            elif i <= 13:
                self.tab.tag_config(f"{i}", foreground = "pale turquoise")
            elif i == 14 or i>=27 and i <= 30:
                self.tab.tag_config(f"{i}", foreground = "black")
            elif i == 15:
                self.tab.tag_config(f"{i}", foreground = "orange")
            elif i <= 18:
                self.tab.tag_config(f"{i}", foreground = "pale green")
            elif i == 19 or i == 24:
                self.tab.tag_config(f"{i}", foreground = "black")
            elif i <= 26:
                self.tab.tag_config(f"{i}", foreground = "yellow")
            else:
                self.tab.tag_config(f"{i}", underline=True, underlinefg='red')

    def add_tab(self, path, content):
        text = tk.Text()
        self.text_list.append((text, path))
        text = self.text_list[len(self.text_list) - 1][0]
        self.main.add(text, text = path.split('/')[-1])
        text.insert('end', content)
        self.main.select(len(self.text_list) - 1)