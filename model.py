import sys
from tkinter import filedialog as fd
from antlr4 import *
sys.path.append("./compiler")
from GrammarExpressionLexer import GrammarExpressionLexer
import os

class Model:
    def __init__(self):
        self.file = None
        self.open_files = {}

    def set_file(self, arq):
        self.file = arq

    def change_tab(self, path):
        self.set_file(self.open_files[path])

    def open(self, path):
        new_file = File(path)
        self.open_files[path] = new_file
        self.file = new_file
    
    def new(self, path):
        open(path, "w").close()
        new_file = File(path)
        self.open_files[path] = new_file
        self.file = new_file

    def save(self):
        self.file.save_file()

    def set_text(self, content):
        self.file.set_text(content)

    def get_text(self):
        return self.file.get_text()

    def is_open(self, path):
        if path in self.open_files:
            return True
        return False

    def analyze_text(self, content):
        codeStream = InputStream(content)
        lexer = GrammarExpressionLexer(codeStream)
        tokens = lexer.getAllTokens()
        tokensIndex = []

        for t in tokens:
            tokensIndex.append({"line": t.line, "start": t.column, "end": t.column+(len(t.text)), "id": t.type})
        return tokensIndex

class File:
    def __init__(self, path):
        self.path = path
        self.file = open(self.path, "r")
        self.txt = self.file.read()

    def get_text(self):
        return self.txt

    def set_text(self, newText):
        self.txt = newText
    
    def save_file(self):
        self.file = open(self.path, "w")
        self.file.write(self.txt)
        self.file.close()
        self.file = open(self.path, "r")