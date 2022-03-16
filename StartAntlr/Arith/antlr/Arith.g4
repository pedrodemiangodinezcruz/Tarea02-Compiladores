grammar Arith;
import CommonLexer;
/** The start rule; begin parsing here. */
prog:   stat+ ; /* entry rule */

stat:   expr NEWLINE     # printExpr           
    |   ID '=' expr NEWLINE        #assign
    |   NEWLINE                    #blank
    ;

expr:   expr MUL expr   # Mul
    |   expr DIV expr  # Div
    |   expr ADD expr   # Add
    |   expr SUB expr  # Sub
    |   INT                   # INT
    |   ID                    # id
    |   '(' expr ')'         # parens
    ;

MUL: '*';
DIV: '/';
ADD: '+';
SUB: '-';