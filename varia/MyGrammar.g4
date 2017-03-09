// define a grammar called MyGrammar
grammar MyGrammar;
startRule   : 'hello' ID;
ID  : [a-z]+ ;
WS  : [ \t\r\n]+ -> skip ;
