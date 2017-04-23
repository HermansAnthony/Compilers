#!/bin/bash

#####################################################################
#  Script to a PNG image from a dot file
#  First argument is the output png image
#  Second argument is the input dot file
#####################################################################

echo "Generating png image from .dot file"
dot -Tpng -o $1 $2
