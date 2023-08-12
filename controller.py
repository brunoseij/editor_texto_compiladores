class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def new(self, path):
        self.model.new(path)
        self.view.add_tab(path, self.model.get_text())
        self.highlight_text()

    def open(self, path):
        if not self.model.is_open(path):
            self.model.open(path)
            self.view.add_tab(path, self.model.get_text())
            self.highlight_text()

    def save(self):
        if self.view.tab:
            self.model.set_text(self.view.get_text())
            self.model.save()
    
    def highlight_text(self):
        if self.view.tab:
            tokens = self.model.analyze_text(self.view.get_text())
            self.view.highlight(tokens)

    def is_saved(self):
        if self.model.get_text() == self.view.get_text():
            return True
        return False

    def change_tab(self, path):
        path = self.view.get_selected_tab_filepath()
        self.model.change_tab(path)

    def handle_keypress(self, k):
        self.highlight_text()
        self.is_saved()
            

