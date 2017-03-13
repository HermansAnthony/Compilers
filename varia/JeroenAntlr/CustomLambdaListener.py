from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LambdaParser import LambdaParser
else:
    from LambdaParser import LambdaParser
from LambdaListener import LambdaListener

class CustomListener(LambdaListener):     
    def enterLamb(self, ctx):
        print("Lambda", end=' ')

    def exitVar(self, ctx):
        print(ctx.getText(), end=', ')


