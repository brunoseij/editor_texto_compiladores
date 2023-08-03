class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def open_folder(self):
        folder = self.model.open_folder()
        self.view.set_tree(folder)

    def open_file_from_folder(self, e):
        node, i = self.view.get_selected_file()
        content = self.model.open_file(node, i)
        if content:
            self.view.set_text(content)
            self.highlight_text()
    
    def open(self):
        content = self.model.open_file()
        self.view.set_text(content)
        self.highlight_text()

    def save(self):
        content = self.view.get_text()
        self.model.save_file(content)
        self.highlight_text()
    
    def highlight_text(self):
        tokens = self.model.analyze_text(self.view.get_text())
        self.view.highlight(tokens)

    def handle_keypress(self, k):
        if k.state == "Mod2":
            self.highlight_text()

