# Generated from Lambda.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LambdaParser import LambdaParser
else:
    from LambdaParser import LambdaParser

# This class defines a complete listener for a parse tree produced by LambdaParser.
class LambdaListener(ParseTreeListener):

    # Enter a parse tree produced by LambdaParser#expr.
    def enterExpr(self, ctx:LambdaParser.ExprContext):
        pass

    # Exit a parse tree produced by LambdaParser#expr.
    def exitExpr(self, ctx:LambdaParser.ExprContext):
        pass


    # Enter a parse tree produced by LambdaParser#term.
    def enterTerm(self, ctx:LambdaParser.TermContext):
        pass

    # Exit a parse tree produced by LambdaParser#term.
    def exitTerm(self, ctx:LambdaParser.TermContext):
        pass


    # Enter a parse tree produced by LambdaParser#lamb.
    def enterLamb(self, ctx:LambdaParser.LambContext):
        pass

    # Exit a parse tree produced by LambdaParser#lamb.
    def exitLamb(self, ctx:LambdaParser.LambContext):
        pass


    # Enter a parse tree produced by LambdaParser#appl.
    def enterAppl(self, ctx:LambdaParser.ApplContext):
        pass

    # Exit a parse tree produced by LambdaParser#appl.
    def exitAppl(self, ctx:LambdaParser.ApplContext):
        pass


    # Enter a parse tree produced by LambdaParser#var.
    def enterVar(self, ctx:LambdaParser.VarContext):
        pass

    # Exit a parse tree produced by LambdaParser#var.
    def exitVar(self, ctx:LambdaParser.VarContext):
        pass


