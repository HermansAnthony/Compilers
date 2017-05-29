def getType(type):
    if type == 'c': return "char"
    if type == 'i': return "integer"
    if type == 'f' or type == 'r': return "float"
    if type == 'v': return "void"
    return type

# All semantic related exceptions
class semanticException(Exception):
    pass

class wrongForloop(semanticException):
    def __init__(self, operator, line):
        self.operator = operator
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line) +":\n"\
                + "Update part of for must not be operator " + str(self.operator)
class conditionException(semanticException):
    def __init__(self, currentType, line):
        self.currentType = currentType
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line) +":\n"\
                + "Condition is of type " + getType(str(self.currentType)) + " while it should be of type bool"

class outsideLoopException(semanticException):
    def __init__(self, keyword, line):
        self.keyword = keyword
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line) +":\n"\
                + str(self.keyword) + " statement not in loop statement"

# Variable has already been declared
class declarationException(semanticException):
    def __init__(self, name, type, function, line):
        self.variableName = name
        self.isFunction = function
        self.type = type
        self.line = line

    def __str__(self):
        var = "Variable"
        if self.isFunction: var = "Function"
        return  "Semantic error occurred on line " + str(self.line) + ":\n"+ var + " "\
                + str(self.variableName) + " is already declared as " + getType(self.type)

class unknownVariable(semanticException):
    def __init__(self, name, line, isFunction=False):
        self.variableName = name
        self.line = line
        self.isFunction = isFunction

    def __str__(self):
        var = "Variable "
        if self.isFunction: var = "Function "
        return  "Semantic error occurred on line " + str(self.line) + ":\n"\
                + var + str(self.variableName) + " is not declared."

# Main function is not found
class mainException(semanticException):
    def __str__(self):
        return "Semantic error occurred:\nMain function not declared."

# Main function is not found
class mainTypeException(semanticException):
    def __init__(self, position):
        self.position = position
    def __str__(self):
        return "Semantic error occurred on line " + str(self.position) + ":\nMain function must return integer."

# The type and the expr type mismatch
class wrongType(semanticException):
    def __init__(self, type, correctType, line):
        self.type = type
        self.correctType = correctType
        self.line = line

    def __str__(self):
        returnValue = "Mismatched type error occurred on line " + str(self.line) + ":\n"
        returnValue += "You declared/defined the variable as " + str(getType(self.type)) + " while it should be " + str(getType(self.correctType))
        return returnValue

    # The type and the expr type mismatch
class wrongReturnExpression(semanticException):
    def __init__(self, type, correctType, line):
        self.type = type
        self.correctType = correctType
        self.line = line

    def __str__(self):
        returnValue = "Semantic error occurred on line " + str(self.line) + ":\n"
        returnValue += "The expression returned a value of type " + str(getType(self.type)) \
                       + " while it should be " + str(getType(self.correctType))
        return returnValue

# The return type and the type of the function don'tmatch
class wrongReturnType(semanticException):
    def __init__(self, returnType, correctType, line):
        self.returnType = returnType
        self.correctType = correctType
        self.line = line

    def __str__(self):
        returnValue = "Semantic error occurred on line " + str(self.line) + ":\n"
        returnValue += "You returned/used a variable of type " + str(getType(self.returnType)) + " while it should be " + str(getType(self.correctType))
        return returnValue

# The function is non void and has no return statement
class noReturnStatement(semanticException):
    def __init__(self, line):
        self.line = line

    def __str__(self):
        returnValue = "Warning occurred on line " + str(self.line) + ":\n"
        returnValue += "Control reaches end of non-void function"
        return returnValue

# Exception that will be throwed when you dereference too many times
class deReference(semanticException):
    def __init__(self, line):
        self.line = line

    def __str__(self):
        return "Dereference error occurred on line " + str(self.line) + ":\nToo many dereferences in assignment"

class wrongOperation(semanticException):
    def __init__(self, operations, operand, line, secondOperand=""):
        self.operations = operations
        self.operand = operand
        self.secondOperand = secondOperand
        self.line = line

    def __str__(self):
        returnValue = "Semantic error occurred on line " + str(self.line) + ":\nNot possible to " + str(self.operations) + " on " + str(getType(self.operand))
        if self.secondOperand != "": returnValue += " and " + str(getType(self.secondOperand))
        return returnValue

class incrementError(semanticException):
    def __init__(self, operand, line):
        self.operand = operand
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line)+\
               ":\n Impossible to increment/decrement a variable of type " + str(self.operand)

class parameterTypeError(semanticException):
    def __init__(self, name, currentType, correctType, line):
        self.name = name
        self.currentType = currentType
        self.correctType = correctType
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line) + ":\nExpected argument of type " + getType(str(self.correctType)) \
               + " but received argument of type " + getType(str(self.currentType)) + " for function " + str(self.name)

class conflictingArgumentLength(semanticException):
    def __init__(self, name, line):
        self.name = name
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line) + ":\n"\
                + 'Argument arraysize is different than the parameter arraysize for function ' + str(self.name)

class conflictingParameterLength(semanticException):
    def __init__(self, name, currentLength, correctLength, line):
        self.name = name
        self.currentLength = currentLength
        self.correctLength = correctLength
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line) + ":\nExpected " + str(self.correctLength) + " parameter(s) " \
               + "but received " + str(self.currentLength) + " parameter(s) for function " + str(self.name)

class conflictingArgumentLength(semanticException):
    def __init__(self, name, currentLength, correctLength, line):
        self.name = name
        self.currentLength = currentLength
        self.correctLength = correctLength
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line) + ":\nExpected " + str(
            self.correctLength) + " argument(s) " \
               + "but received " + str(self.currentLength) + " argument(s) for function " + str(self.name)

# Array related exceptions/warnings
class wrongArrayDimension(semanticException):
    def __init__(self, name, line):
        self.name = name
        self.line = line

    def __str__(self):
        return "Warning occurred on line " + str(self.line) + ":\n"\
        "Only support for 1 dimensional arrays. (parameter " + str(self.name) + ")"

class wrongArrayDefinition(semanticException):
    def __init__(self, line):
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line) + ":\n" \
                "Definition of variable with array type needs an explicit size or an initializer"

class wrongArrayIndexType(semanticException):
    def __init__(self, currentType, line):
        self.currentType = currentType
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line) + ":\n" \
                "Arrayindex has type " + getType(str(self.currentType)) + " while it should be integer"

# All printf and scanf related exceptions
class includeException(semanticException):
    def __init__(self, function, line):
        self.function = function
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line) + ":\n" \
                "You need to include <stdio.h> in order to use " + str(self.function)

class conversionWarning(semanticException):
    def __init__(self, function, line):
        self.function = function
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line) + ":\n" \
            "More '%' conversions than data arguments for function " + str(self.function)

class requiredStringConstant(semanticException):
    def __init__(self, function, line):
        self.function = function
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line) + ":\n" \
            "String constant is required as first argument for function " + str(self.function)

class wrongTypeCode(semanticException):
    def __init__(self, currentType, formatType, line):
        self.currentType = currentType
        self.formatType = formatType
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line) + ":\n" \
            "You used type code " + str(self.formatType) + " while it should be " + str(self.currentType)

class onlyBasicTypes(semanticException):
    def __init__(self, line):
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line) + ":\n" \
            + "Scanf only accepts pointers to basic type variables in the args list parameter"

class printfTypes(semanticException):
    def __init__(self, line):
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line) + ":\n" \
               + "Printf only accepts identifiers and constants as arguments"

class stringScanError(semanticException):
    def __init__(self, line):
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line) + ":\n" \
               + "Scanf only accepts char array as argument when using the %s conversion"

class builtinLibraryFunction(semanticException):
    def __init__(self, function, line):
        self.function = function
        self.line = line

    def __str__(self):
        return "Semantic error occurred on line " + str(self.line) + ":\n" \
            + "Redeclaration of builtin function " + str(self.function)

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