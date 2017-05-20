# Symbol table for the compiler
# Based on http://www.newagepublishers.com/samplechapter/001679.pdf
class simpleElement:
    def __init__(self, type, address, nestingDepth, arraySize):
        self.type = type
        self.address = address
        self.nestingDepth = nestingDepth
        self.arraySize = arraySize

    def __repr__(self):
        returnValue = '(var) ' + str(self.type)
        if self.address != None: returnValue += "[address:" + str(self.address) + "]"
        return returnValue

class functionElement:
    def __init__(self, type, paramlist, nestingDepth, isForwardDecl):
        self.type = type
        self.parameters = paramlist
        self.nestingDepth = nestingDepth
        self.isForwardDecl = isForwardDecl

    def __repr__(self):
        returnValue = '(proc)' + str(self.type) + " - parameters: "
        for key in self.parameters.keys():
            returnValue += str(key) + '[' + str(self.parameters[key]) +'] '
        return returnValue

class symbolTableLocal:
    """ Symbol table for a local scope / block"""
    def __init__(self, functionName, parent):
        self.table = dict()
        # Offset starts at 5 because of organizational cells
        self.currentOffset = 5
        # Current extreme stack pointer
        self.currentEP = 0
        # Maximum extreme stack pointer
        self.maxEP = 2
        # Name corresponding to local table
        self.functionName = functionName
        # Global table
        self.parent = parent

    # Return the symbol table in a readable format
    def __str__(self):
        return str(self.table)

    # Insert a key in the symbol table
    def insertSymbol(self, key, type, arraySize):
        if key in self.table: return None
        if self.parent.lookupSymbol(key):
            key = self.functionName+"()"+key
        newItem = simpleElement(type, self.currentOffset, self.getNestingDepth(), arraySize)
        self.currentOffset += 1
        if arraySize:
            self.currentOffset += (arraySize-1)
        self.table[key] = newItem
        return newItem

    # Lookup a key in the table if it is present
    def lookupSymbol(self, key):
        if key in self.table:
            return self.table[key]
        return None

    # Get the nesting depth
    def getNestingDepth(self):
        return 1 

    def resetCurrentEP(self):
        self.currentEP = 2

    # Increase the current EP
    def increaseCurrentEP(self, val):
        self.currentEP += val
        if self.currentEP > self.maxEP:
            self.maxEP = self.currentEP

    def getMaxEP(self):
        return self.maxEP

    def getFunctionName(self):
        return self.functionName

class generalSymbolTable:
    """ Symbol table for the general program (global and local scopes)"""
    def __init__(self):
        self.globalScope = dict()
        self.localScope = list()
        self.presentScope = -1
        self.currentOffset = 0

    # Print the symbol table
    def __repr__(self):
        returnValue = "Global Scope: " + str(self.globalScope) + "\n"
        for scope in self.localScope:
            returnValue += "Local scope: " + str(scope) + "\n"
        return returnValue

    # Begin a new scope
    def createScope(self, functionName):
        newScope = symbolTableLocal(functionName, self)
        self.localScope.append(newScope)
        self.presentScope += 1

    # Enter the next scope
    def nextScope(self):
        self.presentScope += 1  

    # Insert a symbol depending on the current scope
    def insertSymbol(self, key, type, arraySize=0, params=None, isForwardDecl=False):
        if self.presentScope == -1:
            if key in self.globalScope: return None
            newItem = None
            if params: 
                # Function declaration
                newItem = functionElement(type, params, 
                    self.getCurrentNestingDepth(), isForwardDecl)
            else:
                # Variable declaration
                newItem = simpleElement(type, self.currentOffset,
                    self.getCurrentNestingDepth(), arraySize)
                self.currentOffset += 1
                if arraySize:
                    self.currentOffset += (arraySize-1)
            self.globalScope[key] = newItem
            return newItem
        else:
            return self.localScope[self.presentScope].insertSymbol(key, type, arraySize)

    # Lookup a key first in the current local scope and then the surrounding scopes
    def lookupSymbol(self, key, semantic=None):
        if self.presentScope != -1:
            localItem = self.localScope[self.presentScope].lookupSymbol(key)
            if localItem != None:
                return localItem  
            if semantic and key in self.globalScope:
                semantic.identifier += "#" 
        if "#" in key:
            key = key[:-1]   
        if key not in self.globalScope: return None
        return self.globalScope[key]

    # Get the current nesting depth
    def getCurrentNestingDepth(self):
        if self.presentScope == -1:
            return 0
        return self.localScope[self.presentScope].getNestingDepth()

    def resetCurrentEP(self):
        if self.presentScope != -1:
            self.localScope[self.presentScope].resetCurrentEP(EpVal)        

    # Increase the current EP
    def increaseCurrentEP(self, val):
        if self.presentScope != -1:
            self.localScope[self.presentScope].increaseCurrentEP(EpVal)

    def getMaxEP(self):
        if self.presentScope != -1:
            return self.localScope[self.presentScope].getMaxEP()     
        return 0

    def resetScopeCounter(self):
        self.presentScope = -1

    def getFunctionName(self):
        if self.presentScope != -1:
            return self.localScope[self.presentScope].getFunctionName()     
        return ""

