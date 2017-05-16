# Symbol table for the compiler
# Based on http://www.newagepublishers.com/samplechapter/001679.pdf
from Exceptions import semanticException

class simpleElement:
    def __init__(self, type, address, nestingDepth):
        self.type = type
        self.address = address
        self.nestingDepth = nestingDepth

    def __repr__(self):
        returnValue = '(var) ' + str(self.type)
        if self.address != None: returnValue += "[address:" + str(self.address) + "]"
        return returnValue

class functionElement:
    def __init__(self, type, paramlist, nestingDepth):
        self.type = type
        self.parameters = paramlist
        self.nestingDepth = nestingDepth

    def __repr__(self):
        returnValue = '(proc)' + str(self.type) + " - parameters: "
        for key in self.parameters.keys():
            returnValue += str(key) + '[' + str(self.parameters[key]) +'] '
        return returnValue

class symbolTableLocal:
    """ Symbol table for a local scope / block"""
    def __init__(self):
        self.table = dict()
        # Offset starts at 5 because of organizational cells
        self.currentOffset = 5
        # Current extreme stack pointer
        self.currentEP = 0
        # Maximum extreme stack pointer
        self.maxEP = 2

    # Return the symbol table in a readable format
    def __str__(self):
        return str(self.table)

    # Insert a key in the symbol table
    def insertSymbol(self, key, type):
        newItem = None
        if key in self.table:
            print("Duplicate declaration for ", key)
        else:
            newItem = simpleElement(type, self.currentOffset, self.getNestingDepth())
            self.currentOffset += 1
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
    def createScope(self):
        newScope = symbolTableLocal()
        self.localScope.append(newScope)
        self.presentScope += 1

    # Enter the next scope
    def nextScope(self):
        self.presentScope += 1  

    # Insert a symbol depending on the current scope
    def insertSymbol(self, key, type, params=None):
        if self.presentScope == -1:
            if key in self.globalScope:
                msg = "Variable " + str(key) + " is already declared (" + str(self.globalScope[key]) + ")"
                raise semanticException(msg)
            newItem = None
            if params: 
                # Function declaration
                newItem = functionElement(type, params, self.getCurrentNestingDepth())
            else:
                # Variable declaration
                newItem = simpleElement(type, self.currentOffset, self.getCurrentNestingDepth())
                self.currentOffset += 1
            self.globalScope[key] = newItem
            return newItem
        else:
            return self.localScope[self.presentScope].insertSymbol(key, type)

    # Lookup a key first in the current local scope and then the surrounding scopes
    def lookupSymbol(self, key):
        if self.presentScope != -1:
            if self.localScope[self.presentScope].lookupSymbol(key) != None:
                return self.localScope[self.presentScope].lookupSymbol(key)           
        if key not in self.globalScope: 
            print("Key ", key, " not found in the symbol table")
            # TODO raise semantic error
            return None
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

