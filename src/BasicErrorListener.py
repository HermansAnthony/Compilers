import sys
from antlr4.error.ErrorListener import ErrorListener
from Exceptions import *

# TODO maybe add more error handling (ambiguity etc)
class BasicErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        message = "Syntax error found on " + "line " + str(line) + ", position " + str(column) + ":\n" + str(msg)
        raise syntaxException(message)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        pass

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        pass

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        pass
