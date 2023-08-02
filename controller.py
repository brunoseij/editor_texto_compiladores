class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def open_folder(self):
        folder = self.model.open_folder()
        self.view.set_tree(folder)
    
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
        print(k)
        print(k.state)
        if k.state == "Mod2":
            self.highlight_text()

