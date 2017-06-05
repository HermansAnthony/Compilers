# Simple element represents a variable
class simpleElement:
    def __init__(self, type, address, nestingDepth, arraySize):
        self.type = type
        self.address = address
        self.nestingDepth = nestingDepth
        self.arraySize = arraySize
        if self.arraySize != 0:
            self.type['isArray'] = True
            self.type['size'] = arraySize

    def __repr__(self):
        returnValue = '(var) ' + str(self.type)
        if self.address != None: returnValue += "[address:" + str(self.address) + "]"
        return returnValue

# Simple element represents a function
class functionElement:
    def __init__(self, type, paramlist, nestingDepth, isForwardDecl):
        self.type = type
        self.parameters = paramlist
        self.nestingDepth = nestingDepth
        self.isForwardDecl = isForwardDecl

    def __repr__(self):
        returnValue = '(proc)' + str(self.type)
        if isinstance(self.parameters, list): return returnValue
        returnValue += " - parameters: "
        for key in self.parameters.keys():
            returnValue += str(key) + '[' + str(self.parameters[key]) +'] '
        return returnValue

class symbolTableLocal:
    """ Symbol table for a local scope / block"""
    def __init__(self, scopeName, parent):
        self.table = dict()
        # Name corresponding to local table
        self.scopeName = scopeName
        # Global table
        self.parent = parent

    # Return the symbol table in a readable format
    def __str__(self):
        return str(self.table)

    # Insert a key in the symbol table
    def insertSymbol(self, key, type, arraySize, currentOffset):
        if key in self.table:
            return None
        newItem = simpleElement(type, currentOffset, self.getNestingDepth(), arraySize)
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

    def getScopeName(self):
        return self.scopeName

class generalSymbolTable:
    """ Symbol table for the general program (global and local scopes)"""
    def __init__(self):
        self.globalScope = dict()
        self.localScope = list()
        self.presentScope = -1
        self.currentOffset = 1

    # Print the symbol table
    def __repr__(self):
        returnValue = "Global Scope: " + str(self.globalScope) + "\n"
        for scope in self.localScope:
            returnValue += "Local scope: " + str(scope) + "\n"
        return returnValue

    # Begin a new scope
    def createScope(self, scopeName, isFunc=False):
        if isFunc:
            # Reset current offset
            self.currentOffset = 5
        newScope = symbolTableLocal(scopeName, self)
        self.localScope.append(newScope)
        self.presentScope += 1

    # Enter the next scope
    def endScope(self):
        self.localScope.pop()
        self.presentScope -= 1

    # Insert a symbol depending on the current scope
    def insertSymbol(self, key, type, arraySize=0, params=None, isForwardDecl=False):
        # Global scope
        if len(self.localScope) == 0:
            if key in self.globalScope: return None
            newItem = None
            if params or "()" in key:
                # Function declaration
                newItem = functionElement(type, params, self.getCurrentNestingDepth(), isForwardDecl)
            else:
                # Variable declaration
                newItem = simpleElement(type, self.currentOffset, self.getCurrentNestingDepth(), arraySize)
                self.currentOffset += 1
                if arraySize:
                    self.currentOffset += (arraySize - 1)
            self.globalScope[key] = newItem
            return newItem
        # Local scopes
        newItem = self.localScope[-1].insertSymbol(key, type, arraySize, self.currentOffset)
        self.currentOffset += 1
        if arraySize:
            self.currentOffset += (arraySize-1)
        return newItem

    # Lookup a key first in the current local scope and then the surrounding scopes
    def lookupSymbol(self, key):
        currentScope = len(self.localScope)-1
        while currentScope != -1:
            if self.localScope[currentScope].lookupSymbol(key) != None:
                return self.localScope[currentScope].lookupSymbol(key)
            currentScope -= 1
        if key not in self.globalScope: return None
        return self.globalScope[key]

    # Get the current nesting depth
    def getCurrentNestingDepth(self):
        if self.presentScope == -1:
            return 0
        return self.localScope[self.presentScope].getNestingDepth()

    def resetScopeCounter(self):
        self.presentScope = -1

    def getScopeName(self):
        if self.presentScope != -1:
            return self.localScope[self.presentScope].getScopeName()
        return ""


