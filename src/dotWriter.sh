#!/bin/bash

#####################################################################
#  Script to build the lexer, parser, visitor and listener with ANTLR
#  First argument is the output png image
#  Second argument is the input dot file
#####################################################################

echo "Generating png image from .dot file"
dot -Tpng -o $1 $2
