import sys
from antlr4 import *

def main(argv):
    print ("Main program:\n")
    if len(argv) <= 3:
        print ("Specify a C program input file and a P program output file\n")
        return 0

if __name__ == '__main__':
    main(sys.argv)
