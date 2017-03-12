# Generated from Lambda.g4 by ANTLR 4.6
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\b")
        buf.write("$\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\6\2\16\n")
        buf.write("\2\r\2\16\2\17\3\3\3\3\3\3\3\3\3\3\3\3\5\3\30\n\3\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\2\2\7\2\4\6\b")
        buf.write("\n\2\2!\2\r\3\2\2\2\4\27\3\2\2\2\6\31\3\2\2\2\b\34\3\2")
        buf.write("\2\2\n!\3\2\2\2\f\16\5\4\3\2\r\f\3\2\2\2\16\17\3\2\2\2")
        buf.write("\17\r\3\2\2\2\17\20\3\2\2\2\20\3\3\2\2\2\21\30\5\n\6\2")
        buf.write("\22\23\5\6\4\2\23\24\7\3\2\2\24\25\5\4\3\2\25\30\3\2\2")
        buf.write("\2\26\30\5\b\5\2\27\21\3\2\2\2\27\22\3\2\2\2\27\26\3\2")
        buf.write("\2\2\30\5\3\2\2\2\31\32\7\4\2\2\32\33\5\n\6\2\33\7\3\2")
        buf.write("\2\2\34\35\7\5\2\2\35\36\5\4\3\2\36\37\7\6\2\2\37 \5\4")
        buf.write("\3\2 \t\3\2\2\2!\"\7\7\2\2\"\13\3\2\2\2\4\17\27")
        return buf.getvalue()


class LambdaParser ( Parser ):

    grammarFileName = "Lambda.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'.'", "'lambda'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "LETTER", "WS" ]

    RULE_expr = 0
    RULE_term = 1
    RULE_lamb = 2
    RULE_appl = 3
    RULE_var = 4

    ruleNames =  [ "expr", "term", "lamb", "appl", "var" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    LETTER=5
    WS=6

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.6")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LambdaParser.TermContext)
            else:
                return self.getTypedRuleContext(LambdaParser.TermContext,i)


        def getRuleIndex(self):
            return LambdaParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpr" ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpr" ):
                listener.exitExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpr" ):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)




    def expr(self):

        localctx = LambdaParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 10
                self.term()
                self.state = 13 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LambdaParser.T__1) | (1 << LambdaParser.T__2) | (1 << LambdaParser.LETTER))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TermContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(LambdaParser.VarContext,0)


        def lamb(self):
            return self.getTypedRuleContext(LambdaParser.LambContext,0)


        def term(self):
            return self.getTypedRuleContext(LambdaParser.TermContext,0)


        def appl(self):
            return self.getTypedRuleContext(LambdaParser.ApplContext,0)


        def getRuleIndex(self):
            return LambdaParser.RULE_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTerm" ):
                listener.enterTerm(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTerm" ):
                listener.exitTerm(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTerm" ):
                return visitor.visitTerm(self)
            else:
                return visitor.visitChildren(self)




    def term(self):

        localctx = LambdaParser.TermContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_term)
        try:
            self.state = 21
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LambdaParser.LETTER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 15
                self.var()
                pass
            elif token in [LambdaParser.T__1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 16
                self.lamb()
                self.state = 17
                self.match(LambdaParser.T__0)
                self.state = 18
                self.term()
                pass
            elif token in [LambdaParser.T__2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 20
                self.appl()
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

    class LambContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var(self):
            return self.getTypedRuleContext(LambdaParser.VarContext,0)


        def getRuleIndex(self):
            return LambdaParser.RULE_lamb

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLamb" ):
                listener.enterLamb(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLamb" ):
                listener.exitLamb(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLamb" ):
                return visitor.visitLamb(self)
            else:
                return visitor.visitChildren(self)




    def lamb(self):

        localctx = LambdaParser.LambContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_lamb)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(LambdaParser.T__1)
            self.state = 24
            self.var()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ApplContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LambdaParser.TermContext)
            else:
                return self.getTypedRuleContext(LambdaParser.TermContext,i)


        def getRuleIndex(self):
            return LambdaParser.RULE_appl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAppl" ):
                listener.enterAppl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAppl" ):
                listener.exitAppl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAppl" ):
                return visitor.visitAppl(self)
            else:
                return visitor.visitChildren(self)




    def appl(self):

        localctx = LambdaParser.ApplContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_appl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 26
            self.match(LambdaParser.T__2)
            self.state = 27
            self.term()
            self.state = 28
            self.match(LambdaParser.T__3)
            self.state = 29
            self.term()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LETTER(self):
            return self.getToken(LambdaParser.LETTER, 0)

        def getRuleIndex(self):
            return LambdaParser.RULE_var

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar" ):
                listener.enterVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar" ):
                listener.exitVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar" ):
                return visitor.visitVar(self)
            else:
                return visitor.visitChildren(self)




    def var(self):

        localctx = LambdaParser.VarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(LambdaParser.LETTER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





