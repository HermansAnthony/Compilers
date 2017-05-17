# All semantic related exceptions
class semanticException(Exception):
    def __init__(self, message=None):
        self.message = message

    def __str__(self):
        return "Semantic error: " + str(self.message)

# Main function is not found
class mainException(semanticException):
    def __str__(self):
        return "Error occurred: Main function not found."

# The type and the expr type mismatch
class wrongType(semanticException):
    def __init__(self, type, correctType, line):
        self.type = type
        self.correctType = correctType
        self.line = line

    def __str__(self):
        returnValue = "Mismatched type error occurred on line " + str(self.line) + ": "
        returnValue += "You declared the variable as " + str(self.type) + " while it should be " + str(self.correctType)
        return returnValue

# The return type and the type of the function don'tmatch
class wrongReturnType(semanticException):
    def __init__(self, returnType, correctType, line):
        self.returnType = returnType
        self.correctType = correctType
        self.line = line

    def __str__(self):
        returnValue = "Wrong function return type error occurred on line " + str(self.line) + ": "
        returnValue += "You returned a variable of type " + str(self.returnType) + " while it should be " + str(self.correctType)
        return returnValue

# Exception that will be throwed when you dereference too many times
def deReference(semanticException):
    def __init__(self, line):
        self.line = line

    def __str__(self):
        return "Dereference error occurred on line " + str(self.line) + ": too many dereferences in assignment"

def wrongOperation(semanticException):
    def __init__(self, operations, operand, line, secondOperand=""):
        self.operations = operations
        self.operand = operand
        self.secondOperand = secondOperand
        self.line = line

    def __str__(self):
        returnValue = "Semantic error occurred on line " + str(self.line) + ": not possible to " + str(self.operations) + " on " + str(self.operand)
        if self.secondOperand != "": returnValue += " and " + str(self.secondOperand)
        return returnValue

def incrementError(semanticExceptions):
    def __init__(self, operand, line):
        self.operand = operand
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line)+\
               ": Impossible to increment/decrement a variable of type " + str(self.operand)

def parameterError(semanticExceptions):
    def __init__(self, givenParamCount, expectedParamCount, line):
        self.currentParamCount = givenParamCount
        self.correctParamCount = expectedParamCount
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line) + ": expected " + str(self.correctParamCount)\
               + " arguments but " + str(self.currentParamCount) + " were given"

def parameterTypeError(semanticExceptions):
    def __init__(self, currentType, correctType, line):
        self.currentType = currentType
        self.correctType = correctType
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line) + ": expected argument of type " + str(self.correctType) \
               + " but received argument of type " + str(self.currentType)

# All antlr related errors
class antlrError(Exception):
    pass

class syntaxException(antlrError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return str(self.message)

class ambiguityException(antlrError):
    def __init__(self, startIndex, stopIndex, ambigAlts):
        self.startIndex = startIndex
        self.stopIndex = stopIndex
        self.alternatives = ambigAlts

    def __str__(self):
        returnValue = "Ambiguity error:\n"
        returnValue += "Input index where the decision started " + str(self.startIndex) + "\n"
        returnValue += "Input index where the ambiguity was identified " + str(self.stopIndex) + "\n"
        returnValue += "The potentially ambiguous alternatives: " + str(self.alternatives) + "\n"
        return returnValue

class fullContextException(antlrError):
    def __init__(self, startIndex, stopIndex, alts):
        self.startIndex = startIndex
        self.stopIndex = stopIndex
        self.alternatives = alts

    def __str__(self):
        returnValue = "Full context / SSL error:\n"
        returnValue += "Input index where the decision started " + str(self.startIndex) + "\n"
        returnValue += "Input index where the SLL conflict occurred " + str(self.stopIndex) + "\n"
        returnValue += "The specific conflicting alternatives: " + str(self.alternatives) + "\n"
        return returnValue

class contextException(antlrError):
    def __init__(self, startIndex, stopIndex, predict):
        self.startIndex = startIndex
        self.stopIndex = stopIndex
        self.prediction = predict

    def __str__(self):
        returnValue = "Context error:\n"
        returnValue += "Input index where the decision started " + str(self.startIndex) + "\n"
        returnValue += "Input index where the context sensitivity was finally determined " + str(self.stopIndex) + "\n"
        returnValue += "The unambiguous result of the full-context prediction: " + str(self.prediction) + "\n"
        return returnValue