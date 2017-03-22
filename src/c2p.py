import sys
from antlr4 import *

def main(argv):
    print ("Main program:\n")
    print("12222")
    if len(argv) <= 3:
        print ("Specify a C program input file and a P progam output file\n")
        return 0

if __name__ == '__c2p__':
    main(sys.argv)
