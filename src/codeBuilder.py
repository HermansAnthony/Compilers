from astVisitor import AstVisitor
from astNode import *
import copy

class Code():
    def __init__(self):
        self.code = ""
    def newline(self, line):
        self.code += line + "\n"

# Overloaded Ast Visitor for semantic analysis and code generation.
class CodeBuilder(AstVisitor):
    def __init__(self, table):
        self.symbolTable = table
        # Intermediate code being generated
        self.code = Code()
        # Label tracker for unique labels
        self.currentLabelNo = 0

    def visitProgramNode(self, node:ProgramNode):
        # All global variable function declarations first
        for child in node.children:
            if type(child) == DeclarationNode:
                self.visit(child)
        # Implicit call for main function before function definitions
        self.code.newline("mst 0")
        self.code.newline("cup 0 main")
        # Halt the machine after executing main
        self.code.newline("hlt")
        # Generate function definitions
        for child in node.children:
            if type(child) != DeclarationNode:
                self.visit(child)        

    def visitFunctionDefinitionNode(self, node:FunctionDefinitionNode):
        self.symbolTable.nextScope() 
        # Generate procedure label
        self.code.newline(node.getID() + ":")
        # Calculate the length of the static section of the stack frame
        staticLength = 5 # 5 organizational cells after MP
        if node.parameterList:
            staticLength += len(node.parameterList.paramDecls)
        for declstat in node.functionBody:
            if type(declstat) == DeclarationNode:
                staticLength += 1
        # Set the stack pointer and the EP
        self.code.newline("ent " + str(self.symbolTable.getMaxEP()) + " " + str(staticLength))
        # Generate function body code
        for declstat in node.functionBody:
            self.visit(declstat) 
        # Implicit return statement      
        self.code.newline("retp")                

    def visitAssignmentNode(self, node:AssignmentNode):
        # Store the new value
        item = self.symbolTable.lookupSymbol(node.getID())
        nestingDiff = self.symbolTable.getCurrentNestingDepth() - item.nestingDepth
        declType = item.type
        idType = declType['idType']
        offset = item.address
        if node.dereferenceCount > 0:
            # **c = 5
            if declType['refCount'] > node.dereferenceCount:
                idType = "a"
            # Put the identifier on top of the stack
            self.visit(node.identifier)
            for i in range(node.dereferenceCount-1):
                # Take the value at the address that is on the top of the stack
                self.code.newline("ind a")
            # Generate expression
            self.visit(node.expression) 
            # Store the value at the top of the stack at the address that's on SP-1       
            self.code.newline("sto " + idType)
        else:
            # c = 5
            # Generate expression
            self.visit(node.expression) 
            # Store the expression
            if declType['refCount'] != 0:
                idType = "a"
            self.code.newline("str " + idType + " " + str(nestingDiff) + " " + str(offset))        

    def visitIfStatementNode(self, node:IfStatementNode):
        self.visit(node.condition)
        label1 = self.symbolTable.getFunctionName() + str(self.currentLabelNo)
        label2 = self.symbolTable.getFunctionName() + str(self.currentLabelNo+1)
        self.currentLabelNo += 2
        self.code.newline("fjp " + label1)
        for declStat in node.ifBody:
            self.visit(declStat)
        self.code.newline("ujp " + label2)
        self.code.newline(label1 + ":")
        for declStat in node.elseBody:
            self.visit(declStat)
        self.code.newline(label2 + ":")

    def visitIterationStatementNode(self, node:IterationStatementNode):
        if node.statementName == "While":
            # l1: e, fjp l2, body, ujp l1, l2:   
            label1 = self.symbolTable.getFunctionName() + str(self.currentLabelNo)
            label2 = self.symbolTable.getFunctionName() + str(self.currentLabelNo+1)
            self.currentLabelNo += 2  
            self.code.newline(label1 + ":")
            self.visit(node.left)
            self.code.newline("fjp " + label2)
            for declStat in node.right:
                self.visit(declStat)
            self.code.newline("ujp " + label1)
            self.code.newline(label2 + ":")

    def visitReturnNode(self, node:ReturnNode):
        if node.expressionNode:
            exprType = self.visit(node.expressionNode)
            self.code.newline("str " + exprType['idType'] + " 0 0" )
            self.code.newline("retf")
        else:
            self.code.newline("retp")

    def visitBreakNode(self, node:BreakNode):
        pass

    def visitContinueNode(self, node:ContinueNode):
        pass

    def visitDeclarationNode(self, node:DeclarationNode):
        # Generate expression
        self.visit(node.expression)
        if self.symbolTable.getCurrentNestingDepth() == 0:
            # If in global, don't store the identifier
            return
        # Store the identifier
        item = self.symbolTable.lookupSymbol(node.getID())
        offset = item.address
        nestingDiff = self.symbolTable.getCurrentNestingDepth() - item.nestingDepth
        idType = item.type['idType']
        if item.type['refCount'] != 0:
            idType = "a"
        self.code.newline("str " + idType + " " + str(nestingDiff) + " " + str(offset))

    def visitBinaryOperationNode(self, node:BinaryOperationNode):
        exprLeft = self.visit(node.left)
        self.visit(node.right)
        typeLeft = exprLeft['idType']
        if node.operator == "+":
            self.code.newline("add " + typeLeft)   
        elif node.operator == "-":
            self.code.newline("sub " + typeLeft)
        elif node.operator == "*":  
            self.code.newline("mul " + typeLeft) 
        elif node.operator == "/":  
            self.code.newline("div " + typeLeft) 
        elif node.operator == "==":  
            self.code.newline("equ " + typeLeft) 
        elif node.operator == "!=":  
            self.code.newline("neq " + typeLeft) 
        elif node.operator == "<":  
            self.code.newline("les " + typeLeft) 
        elif node.operator == ">":  
            self.code.newline("grt " + typeLeft) 
        elif node.operator == "<=":  
            self.code.newline("leq " + typeLeft) 
        elif node.operator == ">=":  
            self.code.newline("geq " + typeLeft)
        elif node.operator == "&&":  
            self.code.newline("and")
        elif node.operator == "||":  
            self.code.newline("or")
        return typeLeft
            
    def visitExpressionNode(self, node:ExpressionNode):
        exprType = None
        if node.isPostfix:
            # Get the type of the identifier
            self.visit(node.child)
            # Get the address and nesting difference of the identifier
            item = self.symbolTable.lookupSymbol(node.child.getID())
            exprType = copy.deepcopy(item.type)
            idType = exprType['idType']
            nestingDiff = self.symbolTable.getCurrentNestingDepth() - item.nestingDepth
            offset = item.address
            # load lvalue  
            self.code.newline("lod " + idType + " " + str(nestingDiff) + " " + str(offset))
            # Increment or decrement
            if node.operator == "++":
                self.code.newline("inc " + idType + "1")
            else:
                self.code.newline("dec " + idType + "1")
            # store lvalue
            self.code.newline("str " + idType + " " + str(nestingDiff) + " " + str(offset))
        return exprType

    def visitDereferenceExpressionNode(self, node:DereferenceExpressionNode):
        # int *a = *b
        # int a = ***b + 3
        # int a = *b[2] + 3
        item = self.symbolTable.lookupSymbol(node.child.getID())
        idType = "a"
        if item.type['refCount'] == node.derefCount:
            idType = item.type['idType']
        nestingDiff = self.symbolTable.getCurrentNestingDepth() - item.nestingDepth
        offset = item.address
        # Put the identifier on top of the stack
        self.visit(node.child)
        for i in range(node.derefCount-1):
            # Take the value at the address that is on the top of the stack
            self.code.newline("ind a")
        self.code.newline("ind " + idType)
        # Leave dereferenced lvalue on top of stack
        exprType = copy.deepcopy(item.type)
        exprType['refCount'] -= node.derefCount
        return exprType

    def visitReferenceExpressionNode(self, node:ReferenceExpressionNode):
        # int *a = &b + 3
        # int *a = &b[1] + 3
        # Put the global address of the identifier on the top of the stack
        item = self.symbolTable.lookupSymbol(node.child.getID())
        nestingDiff = self.symbolTable.getCurrentNestingDepth() - item.nestingDepth
        offset = item.address
        self.code.newline("lda " + str(nestingDiff) + " " + str(offset))
        # Increase the reference count of the exprType
        exprType = copy.deepcopy(item.type)
        exprType['refCount'] += 1
        return exprType  

    def visitFunctionCallNode(self, node:FunctionCallNode):
        item = self.symbolTable.lookupSymbol(node.getID()+"()")
        nestingDiff = self.symbolTable.getCurrentNestingDepth() - item.nestingDepth
        # Mark the stack
        self.code.newline("mst " + str(nestingDiff))
        # arguments
        argLength = self.visit(node.argumentExpressionListNode)
        # Call user procedure
        self.code.newline("cup " + str(argLength) + " " + node.getID())

    def visitArgumentExpressionListNode(self, node:ArgumentExpressionListNode):
        if isinstance(node.argumentExprs, list):
            for expr in node.argumentExprs:
                self.visit(expr)    
            return len(node.argumentExprs)
        self.visit(node.argumentExprs)
        return 1

    def visitParameterDeclarationNode(self, node:ParameterDeclarationNode):
        self.symbolTable.insertSymbol(node.getID(), node.getType())
        # Check if type is array to increase size     

    def visitIntegerConstantNode(self, node:IntegerConstantNode):
        self.code.newline("ldc i " + str(node.value))
        return {'idType': "i", 'refCount': 0}

    def visitFloatingConstantNode(self, node:FloatingConstantNode):
        self.code.newline("ldc r " + str(node.value))
        return {'idType': "r", 'refCount': 0}

    def visitCharacterConstantNode(self, node:CharacterConstantNode):
        self.code.newline("ldc c " + node.value)
        return {'idType': "c", 'refCount': 0}

    def visitDeclarationSpecifierNode(self, node:DeclarationSpecifierNode):
        pass   

    def visitIdentifierNode(self, node:IdentifierNode):
        # Put identifier on top of the stack
        item = self.symbolTable.lookupSymbol(node.getID())
        #for expression in node.arrayExpressionList:
        #    self.visit(expression)
        idType = item.type['idType']
        if item.type['refCount'] > 0:
            idType = "a"
        nestingDiff = self.symbolTable.getCurrentNestingDepth() - item.nestingDepth
        self.code.newline("lod " + idType + " " + str(nestingDiff) + " " + str(item.address))
        return item.type

    def getCode(self):
        return self.code.code

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

