import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import scrolledtext
import re
import os

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

        self.searchbox = tk.Entry(master=self.frm_menuBar)
        self.searchbox.pack(side="right")
        self.searchbox.bind("<KeyRelease>", self.search)

        self.main = ttk.Notebook(master=self)
        self.main.pack(fill="both", expand=True)   
        self.main.bind('<<NotebookTabChanged>>',self.update_open_tab)

    def set_controller(self, controller):
        self.controller = controller

    def update_open_tab(self, e):
        try:
            self.tab = self.text_list[self.main.index(self.main.select())][0]
            self.path = self.text_list[self.main.index(self.main.select())][1]
            self.controller.change_tab(self.path)
            self.configure_tags()
            self.controller.highlight_text()
        except:
            self.text_list = []

    def get_selected_tab_filepath(self):
        return self.path

    def set_text(self, content):
        self.tab.delete("1.0", "end")
        self.tab.insert("1.0", content)

    def get_text(self):
        if self.tab:
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
        self.search()

    def configure_tags(self):
        self.tab.tag_config("match", background = "yellow")
        for i in range(35):
            if (i >= 1 and i <= 3) or i == 6:
                self.tab.tag_config(f"{i}", foreground = "#161884")
            elif i == 4 or i == 5: #inicio e fim
                self.tab.tag_config(f"{i}", foreground = "#E95420")
            elif i == 7 or i == 8:#read e write
                self.tab.tag_config(f"{i}", foreground = "#A79571")
            elif i >= 9 and i <= 13:#if else, while for
                self.tab.tag_config(f"{i}", foreground = "#CD6EEB")
            elif i == 14 or i == 15 or i == 25: #operadores
                self.tab.tag_config(f"{i}", foreground = "#000000")
            elif i == 16 or i == 32: #string
                self.tab.tag_config(f"{i}", foreground = "#AA262C")
            elif i >= 17 and i <= 19: #number
                self.tab.tag_config(f"{i}", foreground = "#288C60")
            elif i >= 20 and i <= 22: #variaveis . ,
                self.tab.tag_config(f"{i}", foreground = "#000000")
            elif i == 23 or i == 24 or i == 26 or i == 27: #parenteses e chaves
                self.tab.tag_config(f"{i}", foreground = "#6882FD")
            elif i >= 28 and i <= 31: # operadores matematicos
                self.tab.tag_config(f"{i}", foreground = "#000000")
            else:
                self.tab.tag_config(f"{i}", underline=True, underlinefg='red')

    def add_tab(self, path, content):
        text = scrolledtext.ScrolledText()
        text.bind('<KeyRelease>', self.controller.handle_keypress)
        text.bind('<Control-f>', self.searchbox_focus)
        self.text_list.append((text, path))
        text = self.text_list[len(self.text_list) - 1][0]
        
        self.main.add(text, text = path.split('/')[-1])
        text.insert('end', content)
        self.main.select(len(self.text_list) - 1)
            
    def searchbox_focus(self, e):
        self.searchbox.focus()

    def search(self, e=None):
        try:
            lines = self.get_text().split("\n")
        except:
            return

        searchfor = specialCharsTreatment(self.searchbox.get())

        self.tab.tag_remove("match", "1.0", "end")
        for i, line in enumerate(lines):
            for match in re.finditer(f'{searchfor}', line):
                self.tab.tag_add("match", f"{i+1}.{match.start()}",f"{i+1}.{match.end()}")

def specialCharsTreatment(s):
    specialChars = ['*', '[', ']', '(', ')', '$', '.']
    result = ''
    for c in s:
        if c in specialChars:
            result += f'[{c}]'
        else:
            result += c
    return result