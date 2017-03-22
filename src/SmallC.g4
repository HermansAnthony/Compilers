/**
 *
 */
grammar Smallc;

program : 



CHAR : 'char';
INT : 'int';
FLOAT : 'float';
LETTER : [a-zA-Z] ;
WS : [ \t\n\r]+ -> skip ;
