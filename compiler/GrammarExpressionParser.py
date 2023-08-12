# Generated from GrammarExpression.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,206,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,1,0,1,0,4,0,39,8,0,11,0,
        12,0,40,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,
        1,2,1,2,1,2,3,2,60,8,2,1,3,1,3,1,3,1,3,1,3,5,3,67,8,3,10,3,12,3,
        70,9,3,1,4,4,4,73,8,4,11,4,12,4,74,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,
        5,3,5,85,8,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,7,1,7,
        3,7,100,8,7,1,7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,8,3,8,
        114,8,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,1,9,
        1,9,1,9,1,9,1,9,1,9,3,9,135,8,9,1,9,1,9,1,10,1,10,1,10,1,10,1,10,
        1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,10,1,11,
        1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,13,1,13,1,13,1,14,1,14,1,14,1,14,
        1,14,1,14,3,14,185,8,14,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,
        1,16,3,16,196,8,16,1,17,1,17,1,17,1,17,1,17,1,17,3,17,204,8,17,1,
        17,0,0,18,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,0,2,1,
        0,27,28,1,0,29,30,204,0,36,1,0,0,0,2,47,1,0,0,0,4,59,1,0,0,0,6,61,
        1,0,0,0,8,72,1,0,0,0,10,84,1,0,0,0,12,86,1,0,0,0,14,93,1,0,0,0,16,
        104,1,0,0,0,18,117,1,0,0,0,20,138,1,0,0,0,22,155,1,0,0,0,24,166,
        1,0,0,0,26,175,1,0,0,0,28,184,1,0,0,0,30,186,1,0,0,0,32,195,1,0,
        0,0,34,203,1,0,0,0,36,38,5,4,0,0,37,39,3,2,1,0,38,37,1,0,0,0,39,
        40,1,0,0,0,40,38,1,0,0,0,40,41,1,0,0,0,41,42,1,0,0,0,42,43,3,8,4,
        0,43,44,5,5,0,0,44,45,5,21,0,0,45,46,6,0,-1,0,46,1,1,0,0,0,47,48,
        3,4,2,0,48,49,6,1,-1,0,49,50,3,6,3,0,50,51,5,21,0,0,51,52,6,1,-1,
        0,52,3,1,0,0,0,53,54,5,1,0,0,54,60,6,2,-1,0,55,56,5,2,0,0,56,60,
        6,2,-1,0,57,58,5,3,0,0,58,60,6,2,-1,0,59,53,1,0,0,0,59,55,1,0,0,
        0,59,57,1,0,0,0,60,5,1,0,0,0,61,62,5,19,0,0,62,68,6,3,-1,0,63,64,
        5,20,0,0,64,65,5,19,0,0,65,67,6,3,-1,0,66,63,1,0,0,0,67,70,1,0,0,
        0,68,66,1,0,0,0,68,69,1,0,0,0,69,7,1,0,0,0,70,68,1,0,0,0,71,73,3,
        10,5,0,72,71,1,0,0,0,73,74,1,0,0,0,74,72,1,0,0,0,74,75,1,0,0,0,75,
        9,1,0,0,0,76,85,3,12,6,0,77,85,3,14,7,0,78,79,3,16,8,0,79,80,5,21,
        0,0,80,85,1,0,0,0,81,85,3,18,9,0,82,85,3,20,10,0,83,85,3,22,11,0,
        84,76,1,0,0,0,84,77,1,0,0,0,84,78,1,0,0,0,84,81,1,0,0,0,84,82,1,
        0,0,0,84,83,1,0,0,0,85,11,1,0,0,0,86,87,5,7,0,0,87,88,5,22,0,0,88,
        89,5,19,0,0,89,90,6,6,-1,0,90,91,5,23,0,0,91,92,5,21,0,0,92,13,1,
        0,0,0,93,94,5,8,0,0,94,99,5,22,0,0,95,96,5,15,0,0,96,100,6,7,-1,
        0,97,98,5,19,0,0,98,100,6,7,-1,0,99,95,1,0,0,0,99,97,1,0,0,0,100,
        101,1,0,0,0,101,102,5,23,0,0,102,103,5,21,0,0,103,15,1,0,0,0,104,
        105,5,19,0,0,105,106,6,8,-1,0,106,107,6,8,-1,0,107,113,5,24,0,0,
        108,109,3,26,13,0,109,110,6,8,-1,0,110,114,1,0,0,0,111,112,5,15,
        0,0,112,114,6,8,-1,0,113,108,1,0,0,0,113,111,1,0,0,0,114,115,1,0,
        0,0,115,116,6,8,-1,0,116,17,1,0,0,0,117,118,5,9,0,0,118,119,6,9,
        -1,0,119,120,5,22,0,0,120,121,3,24,12,0,121,122,5,23,0,0,122,123,
        5,10,0,0,123,124,5,25,0,0,124,125,3,8,4,0,125,126,6,9,-1,0,126,134,
        5,26,0,0,127,128,5,11,0,0,128,129,6,9,-1,0,129,130,5,25,0,0,130,
        131,3,8,4,0,131,132,5,26,0,0,132,133,6,9,-1,0,133,135,1,0,0,0,134,
        127,1,0,0,0,134,135,1,0,0,0,135,136,1,0,0,0,136,137,6,9,-1,0,137,
        19,1,0,0,0,138,139,5,12,0,0,139,140,6,10,-1,0,140,141,5,22,0,0,141,
        142,3,16,8,0,142,143,6,10,-1,0,143,144,5,21,0,0,144,145,3,24,12,
        0,145,146,6,10,-1,0,146,147,5,21,0,0,147,148,3,16,8,0,148,149,6,
        10,-1,0,149,150,5,23,0,0,150,151,5,25,0,0,151,152,3,8,4,0,152,153,
        5,26,0,0,153,154,6,10,-1,0,154,21,1,0,0,0,155,156,5,13,0,0,156,157,
        6,11,-1,0,157,158,5,22,0,0,158,159,3,24,12,0,159,160,5,23,0,0,160,
        161,5,25,0,0,161,162,3,8,4,0,162,163,6,11,-1,0,163,164,5,26,0,0,
        164,165,6,11,-1,0,165,23,1,0,0,0,166,167,6,12,-1,0,167,168,3,26,
        13,0,168,169,6,12,-1,0,169,170,5,14,0,0,170,171,6,12,-1,0,171,172,
        6,12,-1,0,172,173,3,26,13,0,173,174,6,12,-1,0,174,25,1,0,0,0,175,
        176,3,30,15,0,176,177,3,28,14,0,177,27,1,0,0,0,178,179,7,0,0,0,179,
        180,6,14,-1,0,180,181,3,30,15,0,181,182,3,28,14,0,182,185,1,0,0,
        0,183,185,1,0,0,0,184,178,1,0,0,0,184,183,1,0,0,0,185,29,1,0,0,0,
        186,187,3,34,17,0,187,188,3,32,16,0,188,31,1,0,0,0,189,190,7,1,0,
        0,190,191,6,16,-1,0,191,192,3,34,17,0,192,193,3,32,16,0,193,196,
        1,0,0,0,194,196,1,0,0,0,195,189,1,0,0,0,195,194,1,0,0,0,196,33,1,
        0,0,0,197,198,5,16,0,0,198,204,6,17,-1,0,199,200,5,19,0,0,200,204,
        6,17,-1,0,201,202,5,22,0,0,202,204,6,17,-1,0,203,197,1,0,0,0,203,
        199,1,0,0,0,203,201,1,0,0,0,204,35,1,0,0,0,11,40,59,68,74,84,99,
        113,134,184,195,203
    ]

class GrammarExpressionParser ( Parser ):

    grammarFileName = "GrammarExpression.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'integer'", "'real'", "'string'", "'programa'", 
                     "'fimprog'", "'declare'", "'leia'", "'escreva'", "'se'", 
                     "'entao'", "'senao'", "'para'", "'enquanto'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "','", "'.'", "'('", "')'", "':='", "'{'", 
                     "'}'", "'+'", "'-'", "'*'", "'/'", "'\"'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "PROGRAM", "ENDPROG", "DECLARE", "READ", "WRITE", 
                      "IF", "THEN", "ELSE", "FOR", "WHILE", "RELOP", "TEXT", 
                      "NUM", "INT", "REAL", "ID", "COMMA", "DOT", "LPARENTHESIS", 
                      "RPARENTHESIS", "ASSIGN", "LCURLY", "RCURLY", "PLUS", 
                      "MINUS", "MULT", "DIV", "DQUOTE", "WS", "Unknown" ]

    RULE_programa = 0
    RULE_declara = 1
    RULE_type = 2
    RULE_varlist = 3
    RULE_bloco = 4
    RULE_cmd = 5
    RULE_cmdleitura = 6
    RULE_cmdescrita = 7
    RULE_cmdexpr = 8
    RULE_cmdif = 9
    RULE_cmdfor = 10
    RULE_cmdwhile = 11
    RULE_relexpr = 12
    RULE_expr = 13
    RULE_exprl = 14
    RULE_termo = 15
    RULE_termol = 16
    RULE_fator = 17

    ruleNames =  [ "programa", "declara", "type", "varlist", "bloco", "cmd", 
                   "cmdleitura", "cmdescrita", "cmdexpr", "cmdif", "cmdfor", 
                   "cmdwhile", "relexpr", "expr", "exprl", "termo", "termol", 
                   "fator" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    PROGRAM=4
    ENDPROG=5
    DECLARE=6
    READ=7
    WRITE=8
    IF=9
    THEN=10
    ELSE=11
    FOR=12
    WHILE=13
    RELOP=14
    TEXT=15
    NUM=16
    INT=17
    REAL=18
    ID=19
    COMMA=20
    DOT=21
    LPARENTHESIS=22
    RPARENTHESIS=23
    ASSIGN=24
    LCURLY=25
    RCURLY=26
    PLUS=27
    MINUS=28
    MULT=29
    DIV=30
    DQUOTE=31
    WS=32
    Unknown=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(GrammarExpressionParser.PROGRAM, 0)

        def bloco(self):
            return self.getTypedRuleContext(GrammarExpressionParser.BlocoContext,0)


        def ENDPROG(self):
            return self.getToken(GrammarExpressionParser.ENDPROG, 0)

        def DOT(self):
            return self.getToken(GrammarExpressionParser.DOT, 0)

        def declara(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarExpressionParser.DeclaraContext)
            else:
                return self.getTypedRuleContext(GrammarExpressionParser.DeclaraContext,i)


        def getRuleIndex(self):
            return GrammarExpressionParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

    def programa(self):

        localctx = GrammarExpressionParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 36
            self.match(GrammarExpressionParser.PROGRAM)
            self.state = 38 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 37
                self.declara()
                self.state = 40 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 14) != 0)):
                    break

            self.state = 42
            self.bloco()
            self.state = 43
            self.match(GrammarExpressionParser.ENDPROG)
            self.state = 44
            self.match(GrammarExpressionParser.DOT)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def type_(self):
            return self.getTypedRuleContext(GrammarExpressionParser.TypeContext,0)


        def varlist(self):
            return self.getTypedRuleContext(GrammarExpressionParser.VarlistContext,0)


        def DOT(self):
            return self.getToken(GrammarExpressionParser.DOT, 0)

        def getRuleIndex(self):
            return GrammarExpressionParser.RULE_declara

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclara" ):
                listener.enterDeclara(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclara" ):
                listener.exitDeclara(self)




    def declara(self):

        localctx = GrammarExpressionParser.DeclaraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declara)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.type_()

            self.state = 49
            self.varlist()
            self.state = 50
            self.match(GrammarExpressionParser.DOT)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return GrammarExpressionParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterType" ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitType" ):
                listener.exitType(self)




    def type_(self):

        localctx = GrammarExpressionParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_type)
        try:
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(GrammarExpressionParser.T__0)

                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(GrammarExpressionParser.T__1)

                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 3)
                self.state = 57
                self.match(GrammarExpressionParser.T__2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarlistContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarExpressionParser.ID)
            else:
                return self.getToken(GrammarExpressionParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarExpressionParser.COMMA)
            else:
                return self.getToken(GrammarExpressionParser.COMMA, i)

        def getRuleIndex(self):
            return GrammarExpressionParser.RULE_varlist

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVarlist" ):
                listener.enterVarlist(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVarlist" ):
                listener.exitVarlist(self)




    def varlist(self):

        localctx = GrammarExpressionParser.VarlistContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_varlist)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(GrammarExpressionParser.ID)

            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==20:
                self.state = 63
                self.match(GrammarExpressionParser.COMMA)
                self.state = 64
                self.match(GrammarExpressionParser.ID)

                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlocoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmd(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarExpressionParser.CmdContext)
            else:
                return self.getTypedRuleContext(GrammarExpressionParser.CmdContext,i)


        def getRuleIndex(self):
            return GrammarExpressionParser.RULE_bloco

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloco" ):
                listener.enterBloco(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloco" ):
                listener.exitBloco(self)




    def bloco(self):

        localctx = GrammarExpressionParser.BlocoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_bloco)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 71
                self.cmd()
                self.state = 74 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 537472) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cmdleitura(self):
            return self.getTypedRuleContext(GrammarExpressionParser.CmdleituraContext,0)


        def cmdescrita(self):
            return self.getTypedRuleContext(GrammarExpressionParser.CmdescritaContext,0)


        def cmdexpr(self):
            return self.getTypedRuleContext(GrammarExpressionParser.CmdexprContext,0)


        def DOT(self):
            return self.getToken(GrammarExpressionParser.DOT, 0)

        def cmdif(self):
            return self.getTypedRuleContext(GrammarExpressionParser.CmdifContext,0)


        def cmdfor(self):
            return self.getTypedRuleContext(GrammarExpressionParser.CmdforContext,0)


        def cmdwhile(self):
            return self.getTypedRuleContext(GrammarExpressionParser.CmdwhileContext,0)


        def getRuleIndex(self):
            return GrammarExpressionParser.RULE_cmd

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmd" ):
                listener.enterCmd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmd" ):
                listener.exitCmd(self)




    def cmd(self):

        localctx = GrammarExpressionParser.CmdContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_cmd)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 76
                self.cmdleitura()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 77
                self.cmdescrita()
                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 3)
                self.state = 78
                self.cmdexpr()
                self.state = 79
                self.match(GrammarExpressionParser.DOT)
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 81
                self.cmdif()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 5)
                self.state = 82
                self.cmdfor()
                pass
            elif token in [13]:
                self.enterOuterAlt(localctx, 6)
                self.state = 83
                self.cmdwhile()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdleituraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def READ(self):
            return self.getToken(GrammarExpressionParser.READ, 0)

        def LPARENTHESIS(self):
            return self.getToken(GrammarExpressionParser.LPARENTHESIS, 0)

        def ID(self):
            return self.getToken(GrammarExpressionParser.ID, 0)

        def RPARENTHESIS(self):
            return self.getToken(GrammarExpressionParser.RPARENTHESIS, 0)

        def DOT(self):
            return self.getToken(GrammarExpressionParser.DOT, 0)

        def getRuleIndex(self):
            return GrammarExpressionParser.RULE_cmdleitura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdleitura" ):
                listener.enterCmdleitura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdleitura" ):
                listener.exitCmdleitura(self)




    def cmdleitura(self):

        localctx = GrammarExpressionParser.CmdleituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_cmdleitura)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(GrammarExpressionParser.READ)
            self.state = 87
            self.match(GrammarExpressionParser.LPARENTHESIS)
            self.state = 88
            self.match(GrammarExpressionParser.ID)

            self.state = 90
            self.match(GrammarExpressionParser.RPARENTHESIS)
            self.state = 91
            self.match(GrammarExpressionParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdescritaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE(self):
            return self.getToken(GrammarExpressionParser.WRITE, 0)

        def LPARENTHESIS(self):
            return self.getToken(GrammarExpressionParser.LPARENTHESIS, 0)

        def RPARENTHESIS(self):
            return self.getToken(GrammarExpressionParser.RPARENTHESIS, 0)

        def DOT(self):
            return self.getToken(GrammarExpressionParser.DOT, 0)

        def TEXT(self):
            return self.getToken(GrammarExpressionParser.TEXT, 0)

        def ID(self):
            return self.getToken(GrammarExpressionParser.ID, 0)

        def getRuleIndex(self):
            return GrammarExpressionParser.RULE_cmdescrita

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdescrita" ):
                listener.enterCmdescrita(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdescrita" ):
                listener.exitCmdescrita(self)




    def cmdescrita(self):

        localctx = GrammarExpressionParser.CmdescritaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_cmdescrita)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.match(GrammarExpressionParser.WRITE)
            self.state = 94
            self.match(GrammarExpressionParser.LPARENTHESIS)
            self.state = 99
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [15]:
                self.state = 95
                self.match(GrammarExpressionParser.TEXT)

                pass
            elif token in [19]:
                self.state = 97
                self.match(GrammarExpressionParser.ID)

                pass
            else:
                raise NoViableAltException(self)

            self.state = 101
            self.match(GrammarExpressionParser.RPARENTHESIS)
            self.state = 102
            self.match(GrammarExpressionParser.DOT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(GrammarExpressionParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(GrammarExpressionParser.ASSIGN, 0)

        def expr(self):
            return self.getTypedRuleContext(GrammarExpressionParser.ExprContext,0)


        def TEXT(self):
            return self.getToken(GrammarExpressionParser.TEXT, 0)

        def getRuleIndex(self):
            return GrammarExpressionParser.RULE_cmdexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdexpr" ):
                listener.enterCmdexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdexpr" ):
                listener.exitCmdexpr(self)




    def cmdexpr(self):

        localctx = GrammarExpressionParser.CmdexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_cmdexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(GrammarExpressionParser.ID)


            self.state = 107
            self.match(GrammarExpressionParser.ASSIGN)
            self.state = 113
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16, 19, 22]:
                self.state = 108
                self.expr()

                pass
            elif token in [15]:
                self.state = 111
                self.match(GrammarExpressionParser.TEXT)

                pass
            else:
                raise NoViableAltException(self)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdifContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(GrammarExpressionParser.IF, 0)

        def LPARENTHESIS(self):
            return self.getToken(GrammarExpressionParser.LPARENTHESIS, 0)

        def relexpr(self):
            return self.getTypedRuleContext(GrammarExpressionParser.RelexprContext,0)


        def RPARENTHESIS(self):
            return self.getToken(GrammarExpressionParser.RPARENTHESIS, 0)

        def THEN(self):
            return self.getToken(GrammarExpressionParser.THEN, 0)

        def LCURLY(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarExpressionParser.LCURLY)
            else:
                return self.getToken(GrammarExpressionParser.LCURLY, i)

        def bloco(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarExpressionParser.BlocoContext)
            else:
                return self.getTypedRuleContext(GrammarExpressionParser.BlocoContext,i)


        def RCURLY(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarExpressionParser.RCURLY)
            else:
                return self.getToken(GrammarExpressionParser.RCURLY, i)

        def ELSE(self):
            return self.getToken(GrammarExpressionParser.ELSE, 0)

        def getRuleIndex(self):
            return GrammarExpressionParser.RULE_cmdif

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdif" ):
                listener.enterCmdif(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdif" ):
                listener.exitCmdif(self)




    def cmdif(self):

        localctx = GrammarExpressionParser.CmdifContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_cmdif)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 117
            self.match(GrammarExpressionParser.IF)

            self.state = 119
            self.match(GrammarExpressionParser.LPARENTHESIS)
            self.state = 120
            self.relexpr()
            self.state = 121
            self.match(GrammarExpressionParser.RPARENTHESIS)
            self.state = 122
            self.match(GrammarExpressionParser.THEN)
            self.state = 123
            self.match(GrammarExpressionParser.LCURLY)
            self.state = 124
            self.bloco()

            self.state = 126
            self.match(GrammarExpressionParser.RCURLY)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==11:
                self.state = 127
                self.match(GrammarExpressionParser.ELSE)

                self.state = 129
                self.match(GrammarExpressionParser.LCURLY)
                self.state = 130
                self.bloco()
                self.state = 131
                self.match(GrammarExpressionParser.RCURLY)




        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdforContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(GrammarExpressionParser.FOR, 0)

        def LPARENTHESIS(self):
            return self.getToken(GrammarExpressionParser.LPARENTHESIS, 0)

        def cmdexpr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarExpressionParser.CmdexprContext)
            else:
                return self.getTypedRuleContext(GrammarExpressionParser.CmdexprContext,i)


        def DOT(self, i:int=None):
            if i is None:
                return self.getTokens(GrammarExpressionParser.DOT)
            else:
                return self.getToken(GrammarExpressionParser.DOT, i)

        def relexpr(self):
            return self.getTypedRuleContext(GrammarExpressionParser.RelexprContext,0)


        def RPARENTHESIS(self):
            return self.getToken(GrammarExpressionParser.RPARENTHESIS, 0)

        def LCURLY(self):
            return self.getToken(GrammarExpressionParser.LCURLY, 0)

        def bloco(self):
            return self.getTypedRuleContext(GrammarExpressionParser.BlocoContext,0)


        def RCURLY(self):
            return self.getToken(GrammarExpressionParser.RCURLY, 0)

        def getRuleIndex(self):
            return GrammarExpressionParser.RULE_cmdfor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdfor" ):
                listener.enterCmdfor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdfor" ):
                listener.exitCmdfor(self)




    def cmdfor(self):

        localctx = GrammarExpressionParser.CmdforContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_cmdfor)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(GrammarExpressionParser.FOR)

            self.state = 140
            self.match(GrammarExpressionParser.LPARENTHESIS)
            self.state = 141
            self.cmdexpr()

            self.state = 143
            self.match(GrammarExpressionParser.DOT)
            self.state = 144
            self.relexpr()

            self.state = 146
            self.match(GrammarExpressionParser.DOT)
            self.state = 147
            self.cmdexpr()

            self.state = 149
            self.match(GrammarExpressionParser.RPARENTHESIS)
            self.state = 150
            self.match(GrammarExpressionParser.LCURLY)
            self.state = 151
            self.bloco()
            self.state = 152
            self.match(GrammarExpressionParser.RCURLY)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CmdwhileContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(GrammarExpressionParser.WHILE, 0)

        def LPARENTHESIS(self):
            return self.getToken(GrammarExpressionParser.LPARENTHESIS, 0)

        def relexpr(self):
            return self.getTypedRuleContext(GrammarExpressionParser.RelexprContext,0)


        def RPARENTHESIS(self):
            return self.getToken(GrammarExpressionParser.RPARENTHESIS, 0)

        def LCURLY(self):
            return self.getToken(GrammarExpressionParser.LCURLY, 0)

        def bloco(self):
            return self.getTypedRuleContext(GrammarExpressionParser.BlocoContext,0)


        def RCURLY(self):
            return self.getToken(GrammarExpressionParser.RCURLY, 0)

        def getRuleIndex(self):
            return GrammarExpressionParser.RULE_cmdwhile

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCmdwhile" ):
                listener.enterCmdwhile(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCmdwhile" ):
                listener.exitCmdwhile(self)




    def cmdwhile(self):

        localctx = GrammarExpressionParser.CmdwhileContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_cmdwhile)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(GrammarExpressionParser.WHILE)

            self.state = 157
            self.match(GrammarExpressionParser.LPARENTHESIS)
            self.state = 158
            self.relexpr()
            self.state = 159
            self.match(GrammarExpressionParser.RPARENTHESIS)
            self.state = 160
            self.match(GrammarExpressionParser.LCURLY)
            self.state = 161
            self.bloco()

            self.state = 163
            self.match(GrammarExpressionParser.RCURLY)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelexprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(GrammarExpressionParser.ExprContext)
            else:
                return self.getTypedRuleContext(GrammarExpressionParser.ExprContext,i)


        def RELOP(self):
            return self.getToken(GrammarExpressionParser.RELOP, 0)

        def getRuleIndex(self):
            return GrammarExpressionParser.RULE_relexpr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelexpr" ):
                listener.enterRelexpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelexpr" ):
                listener.exitRelexpr(self)




    def relexpr(self):

        localctx = GrammarExpressionParser.RelexprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_relexpr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            self.expr()

            self.state = 169
            self.match(GrammarExpressionParser.RELOP)


            self.state = 172
            self.expr()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo(self):
            return self.getTypedRuleContext(GrammarExpressionParser.TermoContext,0)


        def exprl(self):
            return self.getTypedRuleContext(GrammarExpressionParser.ExprlContext,0)


        def getRuleIndex(self):
            return GrammarExpressionParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)




    def expr(self):

        localctx = GrammarExpressionParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.termo()
            self.state = 176
            self.exprl()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprlContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termo(self):
            return self.getTypedRuleContext(GrammarExpressionParser.TermoContext,0)


        def exprl(self):
            return self.getTypedRuleContext(GrammarExpressionParser.ExprlContext,0)


        def PLUS(self):
            return self.getToken(GrammarExpressionParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(GrammarExpressionParser.MINUS, 0)

        def getRuleIndex(self):
            return GrammarExpressionParser.RULE_exprl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExprl" ):
                listener.enterExprl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExprl" ):
                listener.exitExprl(self)




    def exprl(self):

        localctx = GrammarExpressionParser.ExprlContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_exprl)
        self._la = 0 # Token type
        try:
            self.state = 184
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [27, 28]:
                self.enterOuterAlt(localctx, 1)
                self.state = 178
                _la = self._input.LA(1)
                if not(_la==27 or _la==28):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()

                self.state = 180
                self.termo()
                self.state = 181
                self.exprl()
                pass
            elif token in [14, 21, 23]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator(self):
            return self.getTypedRuleContext(GrammarExpressionParser.FatorContext,0)


        def termol(self):
            return self.getTypedRuleContext(GrammarExpressionParser.TermolContext,0)


        def getRuleIndex(self):
            return GrammarExpressionParser.RULE_termo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermo" ):
                listener.enterTermo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermo" ):
                listener.exitTermo(self)




    def termo(self):

        localctx = GrammarExpressionParser.TermoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_termo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.fator()
            self.state = 187
            self.termol()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TermolContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fator(self):
            return self.getTypedRuleContext(GrammarExpressionParser.FatorContext,0)


        def termol(self):
            return self.getTypedRuleContext(GrammarExpressionParser.TermolContext,0)


        def MULT(self):
            return self.getToken(GrammarExpressionParser.MULT, 0)

        def DIV(self):
            return self.getToken(GrammarExpressionParser.DIV, 0)

        def getRuleIndex(self):
            return GrammarExpressionParser.RULE_termol

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermol" ):
                listener.enterTermol(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermol" ):
                listener.exitTermol(self)




    def termol(self):

        localctx = GrammarExpressionParser.TermolContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_termol)
        self._la = 0 # Token type
        try:
            self.state = 195
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [29, 30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 189
                _la = self._input.LA(1)
                if not(_la==29 or _la==30):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()

                self.state = 191
                self.fator()
                self.state = 192
                self.termol()
                pass
            elif token in [14, 21, 23, 27, 28]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self):
            return self.getToken(GrammarExpressionParser.NUM, 0)

        def ID(self):
            return self.getToken(GrammarExpressionParser.ID, 0)

        def LPARENTHESIS(self):
            return self.getToken(GrammarExpressionParser.LPARENTHESIS, 0)

        def getRuleIndex(self):
            return GrammarExpressionParser.RULE_fator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFator" ):
                listener.enterFator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFator" ):
                listener.exitFator(self)




    def fator(self):

        localctx = GrammarExpressionParser.FatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_fator)
        try:
            self.state = 203
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [16]:
                self.enterOuterAlt(localctx, 1)
                self.state = 197
                self.match(GrammarExpressionParser.NUM)

                pass
            elif token in [19]:
                self.enterOuterAlt(localctx, 2)
                self.state = 199
                self.match(GrammarExpressionParser.ID)

                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 3)
                self.state = 201
                self.match(GrammarExpressionParser.LPARENTHESIS)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





