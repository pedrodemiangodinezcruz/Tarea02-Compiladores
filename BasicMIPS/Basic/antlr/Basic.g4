grammar Basic;
import CommonLexer;
/** The start rule; begin parsing here. */
prog:   stat+ ; /* entry rule */

stat:   ifstat                     # if
    |   ifelsestat                 # ifelse
    |   expr NEWLINE               # printExpr
    |   ID '=' INT NEWLINE         # assign            
    |   ID '=' expr NEWLINE        # reassign
    |   NEWLINE                    # blank
    ;

ifstat: WHEN '(' boolExpr '):' NEWLINE ('\t' stat);

ifelsestat: IF '(' boolExpr '):' NEWLINE ('\t' stat) ELSE ':' NEWLINE ('\t' stat);

expr:   expr MUL expr   # Mul
    |   expr DIV expr  # Div
    |   expr ADD expr   # Add
    |   expr SUB expr  # Sub
    |   INT                   # INT
    |   ID                    # id
    |   '(' expr ')'         # parens
    ;

boolExpr:   boolExpr AND boolExpr   # And
        |   boolExpr OR boolExpr    # Or
        |   NOT boolExpr        # Not
        |   expr GT expr    # GreaterThan
        |   expr LT expr    # LessThan
        |   expr EQ expr    # IsEqual
        |   TRUE            # True
        |   FALSE           # False
    ;

MUL: '*';
DIV: '/';
ADD: '+';
SUB: '-';

IF  :   'if' ;
WHEN :  'when' ;
ELSE:   'else' ;
AND: '&&';
OR:'||';
NOT:'!';
EQ: '==';
GT: '>';
LT: '<';
TRUE: 'true';
FALSE: 'false';