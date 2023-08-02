import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
import os

background_color = "#202124"

class View(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.nodes = dict()
        self.frm_menuBar = tk.Frame(master=self)
        self.frm_menuBar.pack(fill="x", expand=False)

        self.btn_open = tk.Button(master=self.frm_menuBar, text="open", command=self.open_button_clicked)
        self.btn_open.pack(side="left")

        self.btn_save = tk.Button(master=self.frm_menuBar, text="save", command=self.save_button_clicked)
        self.btn_save.pack(side="left")

        self.btn_open_folder = tk.Button(master=self.frm_menuBar, text="open folder", command=self.open_folder_btn_clicked)
        self.btn_open_folder.pack(side="left")

        self.label = tk.Label(master=self, text="editor de texto", background="yellow")
        self.label.pack(fill="x")

        self.frm_main = tk.Frame(master=self, background="green")
        self.frm_main.pack(fill="both", expand=True)
    
        self.tree = ttk.Treeview(master=self.frm_main)
        self.tree.heading('#0', text='Project tree', anchor='w')
        self.tree.pack(fill="y", expand=False, side="left")

        self.txt = tk.Text(master=self.frm_main, background = background_color, fg="white")
        self.txt.pack(fill="both", expand=True)

        #self.tree.configure(yscroll=ysb.set, xscroll=xsb.set)

        self.configure_tags()
        self.tree.bind('<<TreeviewOpen>>', self.open_node)
        #self.tree.bind('<<TreeviewSelect>>', self.selecionou)
        s = ttk.Style()
        s.configure('Treeview', rowheight=40, width=1500)

    def set_controller(self, controller):
        self.controller = controller
    
    def selecionou(self, e):
        #print(self.nodes)
        #print(self.tree.focus())
        print(self.tree)

    def set_text(self, content):
        self.txt.delete("1.0", "end")
        self.txt.insert("1.0", content)

    def get_text(self):
        return self.txt.get("1.0", "end")

    def save_button_clicked(self):
        if self.controller:
            self.controller.save()

    def open_button_clicked(self):
        if self.controller:
            self.controller.open()
    
    def highlight(self, tokens):
        for tag in self.txt.tag_names():
            self.txt.tag_remove(tag, "1.0", "end")
        for token in tokens:
            self.txt.tag_add(token["id"], f"{token['line']}.{token['start']}",f"{token['line']}.{token['end']}")

    def configure_tags(self):
        for i in range(34):
            if i >= 1 and i <= 3:
                self.txt.tag_config(f"{i}", foreground = "green")
            elif i <= 5:
                self.txt.tag_config(f"{i}", foreground = "yellow")
            elif i<=8:
                self.txt.tag_config(f"{i}", foreground = "blue")
            elif i <= 13:
                self.txt.tag_config(f"{i}", foreground = "pale turquoise")
            elif i == 14 or i>=27 and i <= 30:
                self.txt.tag_config(f"{i}", foreground = "white")
            elif i == 15:
                self.txt.tag_config(f"{i}", foreground = "orange")
            elif i <= 18:
                self.txt.tag_config(f"{i}", foreground = "pale green")
            elif i == 19 or i == 24:
                self.txt.tag_config(f"{i}", foreground = "white")
            elif i <= 26:
                self.txt.tag_config(f"{i}", foreground = "yellow")
            else:
                self.txt.tag_config(f"{i}", underline=True, underlinefg='red')
    def select_all(self, e):
        self.txt.tag_add("SEL", "1.0","end")
        self.txt.tag_configure("SEL",background="#8ab4f8", foreground= "black")

    def leftclick(self, e):
        self.txt.tag_delete("SEL")

    def open_folder_btn_clicked(self):
        root = fd.askdirectory()
        self.insert_node('', root, root)

    def insert_node(self, parent, text, abspath):
        node = self.tree.insert(parent, 'end', text=text, open=False)
        if os.path.isdir(abspath):
            self.nodes[node] = abspath
            self.tree.insert(node, 'end')

    def open_node(self, event):
        node = self.tree.focus()
        abspath = self.nodes.pop(node, None)
        if abspath:
            self.tree.delete(self.tree.get_children(node))
            for p in os.listdir(abspath):
                self.insert_node(node, p, os.path.join(abspath, p))



    """
        frm_menuBar = Frame()
        frm_menuBar.pack(fill=X, expand=False)
    Button(master=frm_menuBar, text="File", command=abrir).pack(side=LEFT)
    Button(master=frm_menuBar, text="Edit").pack(side=LEFT)

    frm_textEditor = Frame(background="blue")
    frm_textEditor.pack(fill=BOTH, expand=True)



    frm_sideBar = Frame()
    frm_sideBar.pack(fill=Y ,side=LEFT)
    width = int(window.winfo_screenwidth() / 2)
    height = int(window.winfo_screenheight() / 2)

    Label(master=frm_textEditor, text="editor de texto", background="yellow").pack(fill=X)
txt = Text(master=frm_textEditor, background = "#202124")
txt.pack(fill=BOTH, expand=True)
"""