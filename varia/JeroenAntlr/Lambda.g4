/**
 *
 */
grammar Lambda;

expr:   (term)+ ;

term
    :   var | lamb'.'term | appl
    ;

lamb 
    :   'lambda'var
    ;

appl
    : '('term')' term
    ;
var
    :   LETTER
    ;

LETTER  : [a-zA-Z] ;

WS  :   [ \t\n\r]+ -> skip ;
