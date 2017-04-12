# Symbol table for the compiler
# Based on http://www.newagepublishers.com/samplechapter/001679.pdf

class symbolTableLocal:
    def __init__(self):
        self.table = dict()

    def __repr__(self):
        return str(self.table)

    def insertSymbol(self, key, token):
        if key in self.table:
            print("Duplicate declaration for ", key)
        else:
            self.table[key] = token

    def lookupSymbol(self, key):
        if key in self.table:
            return self.table[key]
        print("Symbol not present in current table")
        return None

class generalSymbolTable:
    def __init__(self):
        self.globalScope = dict()
        self.localScope = list()
        self.presentScope = -1

    def __repr__(self):
        returnValue = "Global Scope: " + str(self.globalScope) + "\n"
        for scope in self.localScope:
            returnValue += "Local scope: " + str(scope) + "\n"
        return returnValue

    def beginScope(self):
        newScope = symbolTableLocal
        self.localScope.append(newScope)
        self.presentScope += 1

    def endScope(self):
        self.localScope.pop()
        self.presentScope -= 1

    def insertSymbol(self, key, token):
        if self.presentScope == -1:
            if key in self.globalScope: print("Duplicate declaration for ", key)
            self.globalScope[key] = token
        else:
            self.localScope[self.presentScope].insertSymbol(key, token)

    def lookupSymbol(self, key):
        temporaryScope = len(self.localScope)-1
        while temporaryScope != 0:
            if self.localScope[temporaryScope].lookupSymbol(key) != None:
                return self.localScope[temporaryScope].lookupSymbol(key)
            temporaryScope -= 1
        return self.globalScope[key]
