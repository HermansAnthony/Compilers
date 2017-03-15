grammar smallc;

primaryExpression :   Identifier | Constant | StringLiteral+

typeSpecifier
    :   ('void'
    |   'char'
    |   'short'
    |   'int'
    |   'long'
    |   'float'
    |   'double'
    ;
