/**
 * Grammar for our Compiler project
 */
grammar Smallc;

// Start rule
program
    : primaryExpression
    | declaration
    | statement
    | externalDefinitions
;

// Primary expression part of the grammar
primaryExpression
    : identifier
    | constant
    | '(' expression ')'
;

// Identifier part of the grammar
identifier
    : NonDigit
    | identifier NonDigit
    | identifier Digit
;

// Constant part of the grammar
constant
    : integerConstant
    | floatingConstant
    | characterConstant
;

integerConstant
    : decimalConstant
;

decimalConstant
    : NonZeroDigit
    | decimalConstant Digit
;

floatingConstant
    : decimalFloatingConstant
;

decimalFloatingConstant
    : fractionalConstant exponentPart?
    | digitSequence exponentPart
;

fractionalConstant
    : digitSequence? '.' digitSequence
    | digitSequence '.'
;

digitSequence
    : Digit
    | digitSequence Digit
;

exponentPart
    : 'e' Sign? digitSequence
    | 'E' Sign? digitSequence
;

characterConstant
    : '\'' cCharSequence '\''
;

cCharSequence
    : cChar
    | cCharSequence cChar
;

cChar
    : escapeSequence
    | '\''
    | '\n'
    | '\\'
;

escapeSequence
    : simpleEscapeSequence
;

simpleEscapeSequence
    : '\'' | '\"' | '\?' | '\\' | '\a' | '\b' | '\f' | '\n' | '\r' | '\t' | '\v'
;

// End of the constant part of the grammar
// Expression part of the grammar

expression
    : assignmentExpression
    | expression ',' assignmentExpression
;

assignmentExpression
    : conditionalExpression
    | unaryExpression AssignmentOperator assignmentExpression
;

conditionalExpression
    : logicalORexpression
;

logicalORexpression
    : logicalANDexpression
    | logicalORexpression '||' logicalANDexpression
;

logicalANDexpression
    : inclusiveORexpression
    | logicalANDexpression '&&' inclusiveORexpression
;

inclusiveORexpression
    : exclusiveORexpression
    | inclusiveORexpression '|' exclusiveORexpression
;

exclusiveORexpression
    : ANDexpression
    | exclusiveORexpression '^' ANDexpression
;

ANDexpression
    : equalityExpression
    | ANDexpression '&' equalityExpression
;

equalityExpression
    : relationalExpression
    | equalityExpression '==' relationalExpression
    | equalityExpression '!=' relationalExpression
;

relationalExpression
    : additiveExpression
    | relationalExpression '<' shiftExpression
    | relationalExpression '>' shiftExpression
    | relationalExpression '<=' shiftExpression
    | relationalExpression '>=' shiftExpression
;

shiftExpression
    :   additiveExpression
;

additiveExpression
    : multiplicativeExpression
    | additiveExpression '+' multiplicativeExpression
    | additiveExpression '-' multiplicativeExpression
;

multiplicativeExpression
    : unaryExpression
    | multiplicativeExpression '*' unaryExpression
    | multiplicativeExpression '/' unaryExpression
;

unaryExpression
    : postfixExpression
    | UnaryOperator unaryExpression
;

postfixExpression
    : primaryExpression
    | postfixExpression '[' expression ']'
    | postfixExpression '(' argumentExpressionList? ')'
;

argumentExpressionList
    : assignmentExpression
    | argumentExpressionList ',' assignmentExpression
;

// End of the expression part of the grammar

// Declaration part of the grammar
// TODO
// End of the declaration part of the grammar

// Statement part of the grammar
statement
    : compoundStatement
    | expressionStatement
    | selectionStatement
    | iterationStatement
    | jumpStatement
;

compoundStatement
    : '{' blockItemList? '}'
;

blockItemList
    : blockItem
    | blockItemList blockItem
;

blockItem
    : declaration
    | statement
;

expressionStatement
    : expression? ';'
;

selectionStatement
    : 'if' '(' expression ')' statement
    | 'if' '(' expression ')' statement 'else' statement
;

iterationStatement
    : 'while' '(' expression ')' statement
    | 'for' '(' expression? ';' expression? ';' expression? ')' statement
    | 'for' '(' declaration expression? ';' expression? ')' statement
;

jumpStatement
    : 'continue' ';'
    | 'break' ';'
    | 'return' expression? ';'
;
// End of the statement part of the grammar

// External definition part of the grammar
// TODO
// End of the external definition part of the grammar


// Terminals
NonDigit : [a-zA-Z_];
Digit : [0-9];
NonZeroDigit : [1-9];
Sign : '+' | '-';
AssignmentOperator : '=';
UnaryOperator : '&' | '*' | '+' | '-' | '!';
Char : 'char';
Int : 'int';
Float : 'float';
WS : [ \t\n\r]+ -> skip ;
