import sys
from antlr4 import *
from LambdaLexer import LambdaLexer
from LambdaParser import LambdaParser
from CustomLambdaListener import CustomListener
from CustomLambdaVisitor import CustomVisitor

def main(argv):
    input = FileStream(argv[1])
    # Initiialize Lexer/Recognizer object with the input
    lexer = LambdaLexer(input) 
    # Initialize the stream of tokens
    # populated when parser.expr() is called using the Lexer.
    stream = CommonTokenStream(lexer) 
    # Initialize the parser.
    parser = LambdaParser(stream)
    parser.addParseListener(CustomListener()) 

    # --- End of Initialization ---
   
    # Expr is the starting rule in the lambda grammar.
    # parser.expr() executes lexer -> tokenStream -> parser
    # returns a LambdaParser.ExprContext which is the root node of a tree

    # TREE HIERARCHY
    # Inner Node:
    # {RULENAME}Context(ParserRuleContext(RuleContext(RuleNode(ParseTree(SyntaxTree(Tree))))))
    #   Has parent, children
    # Leaf Node:
    # TerminalNodeImpl(TerminalNode((ParseTree(SyntaxTree(Tree))))              
    #   Has parent, symbol, payload, text (symbol.text)

    # HOW NODES ARE INSERTED
    # See LambdaParser.py:
    # parser.expr() calls parser.term() etc. according to grammar rules
    # termContext.init() will set the exprContext as its parent
    # termContext.enterRule() will set it as child of exprContext
    # .match(ttype)/.matchwildcard() for terminals will call consume() 
    # consume() will add terminalNodes and set localctx as its parent.

    # Inner nodes via tree.addChild(parseTree) 
    # Terminal nodes via tree.addTokenNode(token)

    # CONTEXT ACCESSOR METHODS
    # tree.getText() at ruleExit returns the aggregated text of all predecessor leaves.
    # tree.getChild()
    # tree.getChildren() 
    # tree.getToken() returns terminalNode if direct child
    # tree.getTokens() returns terminalNodes if direct children


    tree = parser.expr()

    # --- End of parse tree Construction ---

    print("")
    visitor = CustomVisitor()
    visitor.visit(tree)
    print("")
    
    #A way to listen to the parse tree after creation.
    #printer = CustomListener()
    #walker = ParseTreeWalker()
    #walker.walk(printer, tree)

if __name__ == '__main__':
    main(sys.argv)
