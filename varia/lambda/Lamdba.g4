// define a grammar called Lambda
grammar Lambda;
startRule   : 'lambda' ID;
ID  : [a-z]+ ;
WS  : [ \t\r\n]+ -> skip ;
