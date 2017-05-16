from astVisitor import AstVisitor
from astNode import *
import copy

class Code():
    code = ""
    maxOffset = 0

    def newline(self, line):
        code += line + "\n"

    def newblock(self, other)
        self.code += other.code

# Overloaded Ast Visitor for semantic analysis and code generation.
class CodeBuilder(AstVisitor):
    def __init__(self, table):
        self.symbolTable = table
        # Intermediate code being generated
        self.code = Code()
        # Function body intermediate code
        self.functionBodyCode = None

    def visitDeclarationNode(self, node:DeclarationNode):
        declType = node.getType()
        item = self.symbolTable.insertSymbol(node.getID(), declType)
        # Generate expression and compare types
        exprType = self.visit(node.expression)
        if exprType['idType'] != declType['idType'] or 
            exprType['refCount'] != declType['refCount']:   
            # Semantic error: declType and exprType don't match
            # TODO use an actual error
            print("Semantic error in declaration"
            return
        # Store as address if it is a pointer
        idType = declType['idType']
        if declType['refCount'] != 0:
            idType = "a"
        code.newline("str " + idType + "0"

    def visitBinaryOperationNode(self, node:BinaryOperationNode):
        # address + float X
        # address + char  X
        # char + anything X
        # int + float     X
        # Only int + int and int+address
        # float + float
        # char + char
        # address + address
        exprTypeLeft = self.visit(node.left)
        exprTypeRight = self.visit(node.right)
        typeLeft = exprTypeLeft['idType']
        typeRight = exprTypeRight['idType']
        # Currently add, minus, mul, div only
        if node.operator != "+" and node.operator != "-"
            and node.operator != "*" and node.operator != "/":
            return
        if exprTypeRight['refCount'] > 0 or
            exprTypeLeft['refCount'] > 0:
            # TODO use an actual error
            print("Semantic Error: cannot add/subtract/mul or div an address") 
            return
        if typeLeft == typeRight:
            if node.operator == "+":
                code.newline("add " + typeLeft)   
            else if node.operator == "-":
                code.newline("sub " + typeLeft)
            else if node.operator == "*":  
                code.newline("mul " + typeLeft) 
            else if node.operator == "/":  
                code.newline("div " + typeLeft) 
        else:
            # TODO use an actual error
            print("Semantic Error: cannot add " + typeLeft + " and " + typeRight)
            return
        return typeLeft
            
    def visitExpressionNode(self, node:ExpressionNode):
        exprType = None
        if self.isPostfix():
            # Id++ or Id-- works for all types except for char
            # Get the type of the identifier
            exprType = self.visit(node.child)
            idType = exprType['idType']
            if exprType['refCount'] > 0:
                idType = "a"
            if idType == "c":
                # TODO use an actual error
                print("Semantic Error: cannot increment/decrement character")
                return
            # Get the address and nesting difference of the identifier
            item = self.symbolTable.lookupSymbol(node.child.getID())
            offset = item.address
            nestingDiff = symboltable.getCurrentNestingDepth() - item.nestingdepth
            # load lvalue  
            code.newline("lod " + idType + " " + nestingDiff + " " + offset)
            # Increment or decrement
            if node.operator == "++":
                code.newline("inc " + idType + "1")
            else:
                code.newline("dec " + idType + "1")
            # store lvalue
            code.newline("str " + idType + " " + nestingDiff + " " + offset")
        return exprType

    def visitDereferenceExpressionNode(self, node:DereferenceExpressionNode):
        # Rule: Star+ expression
        # int *a = *b
        # int a = ***b + 3
        # int a = *b[2] + 3
        item = self.symbolTable.lookupSymbol(node.child.getID())
        if item.type['refCount'] < node.derefCount:
            # TODO Raise too many dereferences error
            print("Too many dereferences")
            return 
        idType = "a"
        if item.type['refCount'] == node.derefCount:
            idType = item.type['idType']
        offset = item.address
        code.newline("ldc a " + offset)
        for i in range(node.derefCount-1):
            code.newline("ind a")
        code.newline("ind " + idType)
        # Leave dereferenced lvalue on top of stack
        exprType = copy.deepcopy(item.type)
        exprType['refCount'] -= node.derefCount
        return exprType

    def visitReferenceExpressionNode(self, node:ReferenceExpressionNode):
        # int *a = &b + 3
        # int *a = &b[1] + 3
        item = self.symbolTable.lookupSymbol(node.child.getID())
        code.newline("ldc a " + item.address)
        exprType = copy.deepcopy(item.type)
        exprType['refCount'] += 1
        return exprType  

    def visitFunctionCallNode(self, node:FunctionCallNode):
        self.visit(node.identifier)
        self.visit(node.argumentExpressionListNode)  

    def visitFunctionDefinitionNode(self, node:FunctionDefinitionNode):
        # Insert function into symbol table
        parameters = dict()
        if node.parameterList:
            parameters = node.parameterList.getParams()
        functionName = node.getID()
        self.symbolTable.insertSymbol(functionName+"()", 
            node.declarationSpecifier.getType(), parameters)

        self.symbolTable.beginScope()
        # Generate procedure label
        code.newline(functionName + ":")
        
        # Calculate the length of the static section of the stack frame
        # 5 organizational cells after MP
        staticLength = 5    
        for paramDecl in node.parameterList.paramDecls:
            self.visit(paramDecl)
            staticLength += 1
        for declstat in self.functionBody:
            if type(declstat) == DeclarationNode:
                staticLength += 1
        # Calculate the value of the extreme stack pointer
        functionBodyCode = Code()
        for declstat in self.functionBody:
            self.visit(declstat)
        maxOffset = functionBodyCode.maxOffset
        
        # Set the stack pointer and EP
        code.newline("ent " + maxOffset + " " + staticLength)

        code.newblock(functionBodyCode)
        self.symbolTable.endScope() 

    def visitParameterDeclarationNode(self, node:ParameterDeclarationNode):
        self.symbolTable.insertSymbol(node.getID(), node.getType())
        # Check if type is array to increase size        

    def visitIdentifierNode(self, node:IdentifierNode):
        idType = {'idType': idType, 'refCount': 0}
        for expression in node.arrayExpressionList:
            self.visit(expression)




    def visitForwardFunctionDeclarationNode(self, node:ForwardFunctionDeclarationNode):
        # Ignore forward function declarations for now
        parameters = dict()
        if node.parameterList:
            parameters = node.parameterList.getParams()
        self.symbolTable.insertSymbol(node.getID()+"()", node.declarationSpecifier.getType(), parameters)
        if node.declarationSpecifier:
            self.visit(node.declarationSpecifier)
        self.visit(node.identifier)
        if parameterList:
            self.visit(node.parameterList)

