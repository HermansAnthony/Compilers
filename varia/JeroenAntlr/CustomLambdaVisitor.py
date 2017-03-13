# Generated from Lambda.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LambdaParser import LambdaParser
else:
    from LambdaParser import LambdaParser

from LambdaVisitor import LambdaVisitor

# This class defines a complete generic visitor for a parse tree produced by LambdaParser.

class CustomVisitor(LambdaVisitor):

    # Visit a parse tree produced by LambdaParser#expr.
    def visitExpr(self, ctx:LambdaParser.ExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaParser#term.
    def visitTerm(self, ctx:LambdaParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LambdaParser#lamb.
    def visitLamb(self, ctx:LambdaParser.LambContext):
        for termNode in ctx.getTokens(2):
            print(termNode.getText(), end=' ')
        t = self.visitChildren(ctx)
        print(".", end='')


    # Visit a parse tree produced by LambdaParser#appl.
    def visitAppl(self, ctx:LambdaParser.ApplContext):
        print("(", end='')        
        result = self.defaultResult()
        n = ctx.getChildCount()
        for i in range(n):
            if i == 3:
                print(" ", end='')
            childResult = ctx.getChild(i).accept(self)
            result = self.aggregateResult(result, childResult)
        print(")", end='')
        return result

    # Visit a parse tree produced by LambdaParser#var.
    def visitVar(self, ctx:LambdaParser.VarContext):
        print(ctx.getText(), end='')
        return self.visitChildren(ctx)
