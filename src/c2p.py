import sys, traceback
from antlr4 import *
from BasicErrorListener import BasicErrorListener
from Exceptions import *
from CmmLexer import CmmLexer
from CmmParser import CmmParser
from astBuilder import AstBuilder
from semanticVisitor import SemanticVisitor
from codeBuilder import CodeBuilder
from SymbolTable import generalSymbolTable

def main(argv):
    #print ("Main program:\n")
    if len(argv) < 3:
        print ("Specify a C program input file and a P program output file\n")
        return 0
    input = FileStream(argv[1])

    try:
        # Initialize the lexer, tokenstream and the parser with the input
        lexer = CmmLexer(input)
        stream = CommonTokenStream(lexer)
        parser = CmmParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(BasicErrorListener())

        # Build the parse tree
        parseTree = parser.program()

        # Generate the Abstract Syntax Tree
        astBuilder = AstBuilder()
        ast = astBuilder.visit(parseTree)

        # Semantic analysis
        symbolTable = generalSymbolTable()
        semanticVisitor = SemanticVisitor(symbolTable)
        semanticVisitor.visit(ast)
        print(symbolTable)
        # Code generation
        codeBuilder = CodeBuilder(symbolTable)
        codeBuilder.visit(ast)
        
        # Write the code to the output file
        f = open(argv[2]+".p", 'w')
        f.write(codeBuilder.getCode())
        f.close()

        # Generate dot file for the AST
        filename = str(argv[1])
        outputAST = "ast_output/" + (filename.split("/")[1]).split(".")[0] + ".dot"
        ast.toDot(outputAST)

    # Catch all antlr related errors
    except antlrError as e:
        print(e)

    # Catch all semantic related errors
    except semanticException as e:
        print(e)

    # Catch the standard exceptions
    #except Exception as err:
    #    exc_traceback = sys.exc_info()[2]
    #    traceback.print_tb(exc_traceback, limit=200, file=sys.stdout)
    #    print(err)

    # Catch all errors in a clean way
    #except:
    #    print("Unexpected error: ", sys.exc_info()[0])

if __name__ == '__main__':
    main(sys.argv)
