from tkinter import filedialog as fd
from antlr4 import *
from GrammarExpressionLexer import GrammarExpressionLexer

class Model:
    def __init__(self):
        self.__file = None

    def set_file(self, arq):
        self.__file = arq

    def open_file(self):
        filename = fd.askopenfilename()
        arq = open(filename, "r")
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
