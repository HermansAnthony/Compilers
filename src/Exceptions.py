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