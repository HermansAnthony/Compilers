import sys
from antlr4.error.ErrorListener import ErrorListener
from Exceptions import *

class BasicErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        message = "Syntax error found on " + "line " + str(line) + ":" + str(column) + "\n" + str(msg)
        raise syntaxException(message)

    def reportAmbiguity(self, recognizer, dfa, startIndex, stopIndex, exact, ambigAlts, configs):
        raise ambiguityException(startIndex, stopIndex, ambigAlts)

    def reportAttemptingFullContext(self, recognizer, dfa, startIndex, stopIndex, conflictingAlts, configs):
        raise fullContextException(startIndex, stopIndex, conflictingAlts)

    def reportContextSensitivity(self, recognizer, dfa, startIndex, stopIndex, prediction, configs):
        raise contextException(startIndex, stopIndex, prediction)
