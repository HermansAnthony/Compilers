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
        # Label tracker for breaknodes
        self.breakNodes = list()
        # Label tracker for continue nodes
        self.continueNodes = list()

    def visitProgramNode(self, node:ProgramNode):
        # All global variable declarations first
        for child in node.children:
            if type(child) == DeclarationNode:
                self.visit(child)

        # Implicit call for main function before function definitions
        self.code.newline("mst 0")
        self.code.newline("cup 0 mainFunc")
        # Halt the machine after executing main
        self.code.newline("hlt")

        # Generate function definitions
        # for child in node.children:
        #     if type(child) != DeclarationNode:
        #         self.visit(child)

    def visitFunctionDefinitionNode(self, node:FunctionDefinitionNode):
        self.currentLabelNo = 0
        # Generate procedure label
        self.code.newline(node.getID() + "Func:")
        # Calculate the length of the static section of the stack frame
        staticLength = 5 # 5 organizational cells after MP
        if node.parameterList:
            staticLength += self.visit(node.parameterList)
        for declStat in node.functionBody:
            if type(declStat) == DeclarationNode:
                exprList = declStat.identifier.arrayExpressionList
                idSize = 1
                if len(exprList) >= 1:
                    idSize = int(exprList[0].value)
                staticLength += idSize
            if type(declStat) == IfStatementNode or type(declStat) == IterationStatementNode:
                staticLength += self.getStaticLength(declStat)

        # Set the stack pointer and the EP
        # self.code.newline("ent " + str(self.symbolTable.getMaxEP()) + " " + str(staticLength))
        self.code.newline("ssp " + str(staticLength))

        # Generate function body code
        # TODO
        # for declStat in node.functionBody:
        #     self.visit(declStat)
        # # Implicit return statement
        # self.code.newline("retp")

    def visitParameterListNode(self, node:ParameterListNode):
        paramDataSize = 0
        for paramDecl in node.paramDecls:
            paramDataSize += self.visit(paramDecl)
        return paramDataSize        

    def visitParameterDeclarationNode(self, node:ParameterDeclarationNode):
        identifier = node.declarator
        exprList = identifier.arrayExpressionList
        if len(exprList) == 1:
            # Return the size of the array
            return int(exprList[0].value)
        # All basic types have size 1
        return 1

    def visitAssignmentNode(self, node:AssignmentNode):
        # Store the new value
        item = self.symbolTable.lookupSymbol(node.getID())
        nestingDiff = self.symbolTable.getCurrentNestingDepth() - item.nestingDepth
        declType = item.type
        idType = declType['idType']
        offset = item.address
        if node.dereferenceCount > 0:
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
            if declType['refCount'] != 0:
                idType = "a"
            if item.arraySize == 0:
                # Generate expression
                self.visit(node.expression) 
                self.code.newline("str " + idType + " " + str(nestingDiff) + " " + str(offset))    
                return
            arrayExpr = node.identifier.arrayExpressionList
            nestingDiff = self.symbolTable.getCurrentNestingDepth() - item.nestingDepth
            # Put the global address on the top of the stack
            self.code.newline("lda " + str(nestingDiff) + " " + str(offset))
            # Put index on the top of the stack            
            self.visit(arrayExpr[0])
            # Check if the expr is within bounds
            self.code.newline("chk 0 " + str(item.arraySize))
            # Calculate the global indexed address
            self.code.newline("ixa 1")   
            # Generate expression
            self.visit(node.expression) 
            # Store the value at the top of the stack at the global index address      
            self.code.newline("sto " + idType) 

    def visitIfStatementNode(self, node:IfStatementNode):
        self.visit(node.condition)
        label1 = self.symbolTable.getScopeName() + str(self.currentLabelNo)
        label2 = self.symbolTable.getScopeName() + str(self.currentLabelNo+1)
        self.currentLabelNo += 2
        self.code.newline("fjp " + label1)
        print("If labels", [label1, label2])
        return [label1, label2]


    def visitIterationStatementNode(self, node:IterationStatementNode):
        if node.statementName == "While":
            # l1: e, fjp l2, body, ujp l1, l2:   
            label1 = self.symbolTable.getScopeName() + str(self.currentLabelNo)
            label2 = self.symbolTable.getScopeName() + str(self.currentLabelNo+1)
            self.continueNodes.append(label1)
            self.breakNodes.append(label2)
            self.currentLabelNo += 2  
            self.code.newline(label1 + ":")
            self.visit(node.left)
            self.code.newline("fjp " + label2)
            return [label1, label2]

        if node.statementName == "For":
            # l1: e, fjp l2, body, ujp l1, l2:
            label1 = self.symbolTable.getScopeName() + str(self.currentLabelNo)
            label2 = self.symbolTable.getScopeName() + str(self.currentLabelNo+1)
            label3 = self.symbolTable.getScopeName() + str(self.currentLabelNo+2)
            self.continueNodes.append(label3)
            self.breakNodes.append(label2)
            self.currentLabelNo += 3
            # Visit initialization
            if node.left: self.visit(node.left)

            # Visit condition
            self.code.newline(label1 + ":")
            if node.middle1:
                self.visit(node.middle1)
                self.code.newline("fjp " + label2)
            return [label1, label2, label3]


            # # Visit updation
            # if node.middle2: self.visit(node.middle2)

    def visitReturnNode(self, node:ReturnNode):
        # Return a value
        if node.expressionNode:
            exprType = self.visit(node.expressionNode)
            self.code.newline("str " + exprType['idType'] + " 0 0" )
            self.code.newline("retf")
        else:
            # Return no results
            self.code.newline("retp")

    def visitBreakNode(self, node:BreakNode):
        print("Got break labels:",self.breakNodes)
        label = self.breakNodes[-1]
        self.code.newline("ujp " + label)

    def visitContinueNode(self, node:ContinueNode):
        label = self.continueNodes[-1]
        self.code.newline("ujp " + label)

    def visitDeclarationNode(self, node:DeclarationNode):
        item = self.symbolTable.lookupSymbol(node.getID())
        offset = item.address 
        curNestingDepth = self.symbolTable.getCurrentNestingDepth()
        nestingDiff = curNestingDepth - item.nestingDepth
        idType = item.type['idType']
        if item.type['refCount'] != 0:
            idType = "a"
        postFix = ""
        if idType == "r":
            postFix = ".0"
        idExprList = node.identifier.arrayExpressionList
        if not node.expression:
            # Implicit initialization
            if len(idExprList) > 0:
                # Array declaration
                for i in range(int(idExprList[0].value)):
                    self.code.newline("ldc " + idType + " 0" + postFix)
                    if curNestingDepth != 0:
                        self.code.newline("str " + idType + " " 
                            + str(nestingDiff) + " " + str(offset))
                    offset += 1
            else:
                # Variable declaration
                self.code.newline("ldc " + idType + " 0" + postFix)    
                if curNestingDepth != 0:       
                    self.code.newline("str " + idType + " " +
                        str(nestingDiff) + " " + str(offset))
            return
        # Explicit initialization
        if type(node.expression) == InitializerListNode:
            # Array with initializer list
            initExprList = node.expression.expressions[:int(idExprList[0].value)]
            for expr in initExprList:
                self.visit(expr)
                if curNestingDepth != 0:
                    self.code.newline("str " + idType + " " 
                        + str(nestingDiff) + " " + str(offset))
                offset += 1 
            for i in range(int(idExprList[0].value) - len(initExprList)):
                # Initialize the rest as 0
                self.code.newline("ldc " + idType + " 0" + postFix)
                if curNestingDepth != 0:
                    self.code.newline("str " + idType + " " 
                        + str(nestingDiff) + " " + str(offset))
                offset += 1  
            return
        # Variable with initializer
        self.visit(node.expression)
        if curNestingDepth == 0:
            return
        # Store the identifier
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
        return exprLeft
            
    def visitExpressionNode(self, node:ExpressionNode):
        exprType = None
        if node.isPostfix:
            # Put the identifier on the top of the stack 2 times
            self.visit(node.child)
            self.visit(node.child)
            # Get the address and nesting difference of the identifier
            item = self.symbolTable.lookupSymbol(node.child.getID())
            exprType = copy.deepcopy(item.type)
            idType = exprType['idType']
            nestingDiff = self.symbolTable.getCurrentNestingDepth() - item.nestingDepth
            offset = item.address
            # Increment or decrement
            if node.operator == "++":
                self.code.newline("inc " + idType + " 1")
            else:
                self.code.newline("dec " + idType + " 1")
            # store the first identifier
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

    # The scanf and printf are generated at the function call node

    def visitStdioNode(self, node:StdioNode):
        pass

    def visitFunctionCallNode(self, node:FunctionCallNode):
        # Printf related code generation
        if node.getID() == "printf":
            args = node.argumentExpressionListNode.argumentExprs
            stringLit = str(args[0].value)
            argsIndex = 1
            printCount = 0
            for index, char in enumerate(stringLit):
                if index != 0 and stringLit[index-1] == "%": continue
                if index != 0 and stringLit[index-1] == "\\" and char == "n": continue # Newline related if statement
                if index == 0 or index == len(stringLit)-2: continue
                if char == "%" and index+1 < len(stringLit):
                    nextChar = stringLit[index+1]
                    item = None
                    idType = None
                    nestingDiff = None
                    offset = None
                    if nextChar == "%":
                        self.toAscii(char, stringLit[index + 1])
                        printCount += 1
                        continue
                    # Identifier related printf variables
                    if type(args[argsIndex]) == IdentifierNode:
                        self.visit(args[argsIndex])
                        item = self.symbolTable.lookupSymbol(args[argsIndex].getID())
                        idType = item.type['idType']
                        self.code.newline("out " + idType)
                    if type(args[argsIndex]) == StringConstantNode:
                        tempIndex = 0
                        prevChar = None
                        for i in args[argsIndex].value:
                            tempIndex+=1
                            nextChar = None
                            if tempIndex < len(args[argsIndex].value) - 1: nextChar = args[argsIndex].value[tempIndex]
                            if i == '"' or i == "\0" or (prevChar == "\\" and i == "n"): continue
                            self.toAscii(i, nextChar)
                            prevChar = i
                        argsIndex+=1
                        continue

                    # Constant related printf variables
                    if type(args[argsIndex]) != IdentifierNode:
                        # TODO check if this works (aka constants in printf function)
                        idType = args[argsIndex].getType()
                        self.code.newline("ldc " + idType + " " + args[argsIndex].value)
                        self.code.newline("out " + idType)
                        argsIndex+=1
                        continue
                    argsIndex += 1
                    printCount += 1
                    continue
                if index != len(stringLit)-1:
                    self.toAscii(char, stringLit[index+1])
                    printCount += 1
            # Put the amount of characters printed on top of the stack
            self.code.newline("ldc i " + str(printCount))
            return

        # Scanf related code generation
        if node.getID() == "scanf":
            # TODO test the scanf function thoroughly
            args = node.argumentExpressionListNode.argumentExprs
            stringLit = str(args[0].value)
            print("Input ", stringLit)
            argsIndex = 1
            inCount = 0
            for index, char in enumerate(stringLit):
                print("Index:", index, " with char ", char,"|")
                if char == '"': continue
                if index != 0 and stringLit[index-1] == "%": continue
                if char == "%" and index+1 < len(stringLit):
                    nextChar = stringLit[index+1]
                    if nextChar == "%":
                        self.code.newline("ldc c %")
                        self.code.newline("out c")
                        inCount += 1
                        continue
                    argExpr = args[argsIndex]
                    print("Hello it is me",type(argExpr))
                    idType = None
                    # Scanf function with char array as argument
                    if type(argExpr) == IdentifierNode:
                        item = self.symbolTable.lookupSymbol(argExpr.getID())
                        idType = item.type['idType']
                        nestingDiff = self.symbolTable.getCurrentNestingDepth() - item.nestingDepth
                        offset = item.address
                        if nextChar == "s" and item.type['size'] > 0:
                            # Argument is an array
                            # TODO what if given string goes out of char array bounds?
                            for i in range(item.type['size']):
                                # Put the index address on top of the stack
                                self.code.newline("ldc " + str(idType) + " " + str(offset))
                                # Store the read value
                                self.code.newline("in " + idType)
                                self.code.newline("str " + idType + " " + str(nestingDiff) + " " + str(offset))
                                offset += 1
                                inCount += 1
                            argsIndex += 1
                            continue

                    # Standard scanf function with &a as argument
                    if type(argExpr) == ReferenceExpressionNode:
                        item = self.symbolTable.lookupSymbol(argExpr.getID())
                        idType = item.type['idType']
                        nestingDiff = self.symbolTable.getCurrentNestingDepth() - item.nestingDepth
                        offset = item.address
                        print(item)

                    # Put the address on top of the stack
                    self.visit(args[argsIndex])
                    # Store the read value
                    self.code.newline("in " + idType)
                    self.code.newline("sto " + idType)
                    inCount += 1
                    argsIndex += 1     
                    continue

                if index != len(stringLit)-1:
                    if stringLit[index-1] == "\\" and char == "n": continue
                    self.toAscii(char, stringLit[index+1])
                    inCount += 1

            # Put the amount of characters read on top of the stack
            self.code.newline("ldc i " + str(inCount))
            return

        # Just regular function calls (Not printf and not scanf)
        item = self.symbolTable.lookupSymbol(node.getID()+"()")
        nestingDiff = self.symbolTable.getCurrentNestingDepth() - item.nestingDepth
        # Mark the stack
        self.code.newline("mst " + str(nestingDiff))
        # arguments
        argLength=0
        # Check if there are arguments provided
        if node.argumentExpressionListNode != None:
            argLength = self.visit(node.argumentExpressionListNode)
        # Call user procedure
        self.code.newline("cup " + str(argLength) + " " + node.getID()+"Func")
        return item.type

    def visitArgumentExpressionListNode(self, node:ArgumentExpressionListNode):
        argExprs = node.argumentExprs
        if not isinstance(argExprs, list):
            argExprs = [argExprs]
        argSize = 0
        for index, expr in enumerate(argExprs):
            if type(expr) == IdentifierNode:
                item = self.symbolTable.lookupSymbol(expr.getID())
                if item.arraySize:
                    # Pass array by value
                    nestingDiff = (self.symbolTable.getCurrentNestingDepth() 
                        - item.nestingDepth)
                    offset = item.address
                    # Put the global address of the array on the stack           
                    self.code.newline("lda " + str(nestingDiff) + " " + str(offset))
                    # Copy the array on the stack
                    self.code.newline("movs " + str(item.arraySize)) 
                    argSize += item.arraySize
                    continue
            self.visit(expr)
            argSize += 1    
        return argSize

    def visitIntegerConstantNode(self, node:IntegerConstantNode):
        self.code.newline("ldc i " + str(node.value))
        return {'idType': "i", 'refCount': 0}

    def visitFloatingConstantNode(self, node:FloatingConstantNode):
        self.code.newline("ldc r " + str(node.value))
        return {'idType': "r", 'refCount': 0}

    def visitCharacterConstantNode(self, node:CharacterConstantNode):
        self.code.newline("ldc c " + node.value)
        return {'idType': "c", 'refCount': 0}

    def visitStringConstantNode(self, node:StringConstantNode):
        # String constant only for printf and scanf
        return {'idType': "c", 'refCount': 0, 'isArray': True}

    def visitDeclarationSpecifierNode(self, node:DeclarationSpecifierNode):
        pass   

    def visitIdentifierNode(self, node:IdentifierNode):
        # Put identifier on top of the stack
        item = self.symbolTable.lookupSymbol(node.getID())
        idType = item.type['idType']
        if item.type['refCount'] > 0:
            idType = "a"
        arrayExpr = node.arrayExpressionList
        if len(arrayExpr) > 0:
            nestingDiff = self.symbolTable.getCurrentNestingDepth() - item.nestingDepth
            offset = item.address
            # Put the global address on the top of the stack
            self.code.newline("lda " + str(nestingDiff) + " " + str(offset))
            # Put index on the top of the stack            
            self.visit(arrayExpr[0])
            # Check if the expr is within bounds
            self.code.newline("chk 0 " + str(item.arraySize))
            # Calculate the global indexed address
            self.code.newline("ixa 1")
            # Put its value on the top of the stack
            self.code.newline("ind " + idType)
            return item.type
        nestingDiff = self.symbolTable.getCurrentNestingDepth() - item.nestingDepth
        self.code.newline("lod " + idType + " " + str(nestingDiff) + " " + str(item.address))
        return item.type

    def visitForwardFunctionDeclarationNode(self, node:ForwardFunctionDeclarationNode):
        return

#====[Helper methods]====
    def getCode(self):
        return self.code.code

    def toAscii(self, char, nextChar):
        asciiValue = ord(char)
        if char == "\\" and nextChar == "n":
            asciiValue = 10
        self.code.newline("ldc c " + str(asciiValue))
        self.code.newline("out c")
        return

    def implicitReturn(self):
        # Implicit return statement
        self.code.newline("retp")

    # Get the static length of the statements through recursion
    def getStaticLength(self, node):
        length = 0
        if type(node) == IfStatementNode:
            if node.ifBody:
                for stat in node.ifBody:
                    if type(stat) == DeclarationNode:
                        exprList = stat.identifier.arrayExpressionList
                        idSize = 1
                        if len(exprList) == 1:
                            idSize = int(exprList[0].value)
                        length += idSize
                    if type(stat) == IfStatementNode or type(stat) == IterationStatementNode:
                        print("Recursion")
                        length += self.getStaticLength(stat)
            if node.elseBody:
                for stat in node.elseBody:
                    if type(stat) == DeclarationNode:
                        exprList = stat.identifier.arrayExpressionList
                        idSize = 1
                        if len(exprList) == 1:
                            idSize = int(exprList[0].value)
                        length += idSize
                    if type(stat) == IfStatementNode or type(stat) == IterationStatementNode:
                        length + self.getStaticLength(stat)
        if type(node) == IterationStatementNode:
            if node.statementName == "For":
                if type(node.left) == DeclarationNode:
                    exprList = node.left.identifier.arrayExpressionList
                    idSize = 1
                    if len(exprList) == 1:
                        idSize = int(exprList[0].value)
                    length += idSize
            for stat in node.right:
                if type(stat) == DeclarationNode:
                    exprList = stat.identifier.arrayExpressionList
                    idSize = 1
                    if len(exprList) == 1:
                        idSize = int(exprList[0].value)
                    length += idSize
                if type(stat) == IfStatementNode or type(stat) == IterationStatementNode:
                    length += self.getStaticLength(stat)
        return length

    def visitUpdation(self, node, label3):
        self.code.newline(label3 + ":")
        if node!=None: self.visit(node)

    def endLoop(self, label1, label2):
        self.code.newline("ujp " + label1)
        self.code.newline(label2 + ":")
        self.continueNodes = self.continueNodes[:-1]
        self.breakNodes = self.breakNodes[:-1]

    def endIf(self, label1, label2):
        self.code.newline("ujp " + label2)
        self.code.newline(label1 + ":")

    def endElse(self, label1, label2):
        self.code.newline(label2 + ":")
