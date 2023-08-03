from tkinter import filedialog as fd
from antlr4 import *
from GrammarExpressionLexer import GrammarExpressionLexer
import os

class Model:
    def __init__(self):
        self.__file = None

    def set_file(self, arq):
        if (self.__file):
            self.__file.close()
        self.__file = arq

    def open_file(self, node = None, i = None):
        if node != None:
            path = os.path.join(*node, i)
        else:
            path = fd.askopenfilename()

        if os.path.isfile(path): 
            arq = open(path, "r")
            self.set_file(arq)
            return self.__file.read()

    def save_file(self, content):
        filename = fd.asksaveasfilename()
        arq = open(filename, "w")
        arq.write(content)
        arq.close()
        arq = open(filename, "r")
        self.set_file(arq)

    def analyze_text(self, content):
        codeStream = InputStream(content)
        lexer = GrammarExpressionLexer(codeStream)
        tokens = lexer.getAllTokens()
        tokensIndex = []

        for t in tokens:
            tokensIndex.append({"line": t.line, "start": t.column, "end": t.column+(len(t.text)), "id": t.type})
        return tokensIndex
