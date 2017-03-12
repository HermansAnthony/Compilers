# Generated from Lambda.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LambdaParser import LambdaParser
else:
    from LambdaParser import LambdaParser

# This class defines a complete generic visitor for a parse tree produced by LambdaParser.

class LambdaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LambdaParser#expr.
    def visitExpr(self, ctx:LambdaParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaParser#term.
    def visitTerm(self, ctx:LambdaParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaParser#lamb.
    def visitLamb(self, ctx:LambdaParser.LambContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaParser#appl.
    def visitAppl(self, ctx:LambdaParser.ApplContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaParser#var.
    def visitVar(self, ctx:LambdaParser.VarContext):
        return self.visitChildren(ctx)



del LambdaParser