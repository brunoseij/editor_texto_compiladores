//TODO: expressions inside for loops and if statements aren't supposed to evaluated?
//TODO: explicitly negative numbers or expressions may not supported
//TODO: exprl and termol may contain empty productions
//TODO: may not need the expression with the variables' value

grammar GrammarExpression;

/**
 * programa
 *     declara+
 *     commands
 * fimprog.
 */
programa     : PROGRAM declara+ bloco ENDPROG DOT {}
             ;

/**
 * type varlist.
 * int a, b, c.
 */
declara      : type {} varlist DOT {}
             ;

/**
 * (integer | real | string)
 */
type         : 'integer' {}
             | 'real' {}
             | 'string' {}
             ;

/**
 * ID (, ID)*
 * a, b, c.
 */
varlist      : ID {}
               (
                   COMMA
                   ID {}
               )*
             ; 

bloco        : (cmd)+
             ;

cmd          : cmdleitura | cmdescrita | cmdexpr DOT | cmdif | cmdfor | cmdwhile
             ;

/**
 * leia(ID).
 */
cmdleitura   : READ LPARENTHESIS
               ID {}
               RPARENTHESIS DOT
             ;

/**
 * escreva(ID | TEXT).
 */
cmdescrita   : WRITE LPARENTHESIS
               (
                   TEXT {}
                   |
                   ID {}
               ) RPARENTHESIS DOT
             ;

/**
 * ID := (expr | TEXT).
 * a := 1 + 2.
 * a := "string".
 */
cmdexpr      : ID {}
               {} 
               ASSIGN
               (
                   expr {}
                   |
                   TEXT {}
               )
               {}
             ;

/**
 * se (relexpr) entao {
 *     bloco  
 * } (senao {
 *     bloco  
 * })?
 */
cmdif        : IF {} LPARENTHESIS relexpr RPARENTHESIS THEN LCURLY bloco {} RCURLY
               (
                   ELSE {} LCURLY bloco RCURLY {}
               )?
               {}
             ;

/**
 * para (cmdexpr. relexpr. cmdexpr) {
 *     bloco  
 * }
 */
cmdfor       : FOR {} LPARENTHESIS cmdexpr {} DOT relexpr {} DOT cmdexpr {} RPARENTHESIS LCURLY bloco RCURLY {}
             ;

/**
 * enquanto (relexpr) {
 *     bloco  
 * }
 */
cmdwhile     : WHILE {} LPARENTHESIS relexpr RPARENTHESIS LCURLY bloco {} RCURLY
               {}
             ;

/**
 * expr RELOP expr
 */
relexpr      : {}
               expr {}
               RELOP {}
               {}
               expr {}
             ;

/**
 * a := 1 + 2 - 3 * 4 / 5 * (6 + 7)
 */
expr         : termo exprl
             ;

exprl        : (PLUS | MINUS) {}
               termo exprl |
             ;

termo        : fator termol
             ;

termol       : (MULT | DIV) {} fator termol |
             ;

fator        : NUM {}
               |
               ID {}
               | LPARENTHESIS {}
             ;

PROGRAM      : 'programa'
             ;

ENDPROG      : 'fimprog'
             ;

DECLARE      : 'declare'
             ;

READ         : 'leia'
             ;

WRITE        : 'escreva'
             ;

IF           : 'se'
             ;

THEN         : 'entao'
             ;

ELSE         : 'senao'
             ;

FOR          : 'para'
             ;

WHILE        : 'enquanto'
             ;

RELOP        : '<' | '>' | '<=' | '>=' | '!=' | '=='
             ;

TEXT         : DQUOTE ([0-9] | [a-z] | [A-Z] | ' ' | '\t' | '\'')* DQUOTE
             ;

NUM          : INT | REAL 
             ;

INT          : [0-9]+
             ;

REAL         : [0-9]+ COMMA [0-9]+
             ;

ID           : ([a-z] | [A-Z]) ([a-z] | [A-Z] | [0-9])*
             ;

COMMA        : ','
             ;

DOT          : '.'
             ;

LPARENTHESIS : '('
             ;

RPARENTHESIS : ')'
             ;

ASSIGN       : ':='  
             ;  

LCURLY       : '{'  
             ;  

RCURLY       : '}'  
             ;  

PLUS         : '+'  
             ;  

MINUS        : '-'
             ;

MULT         : '*'
             ;

DIV          : '/'
             ;

DQUOTE       : '"'
             ;

WS           : (' ' | '\t' | '\n' | '\r')+ -> skip
             ;  

Unknown      : .+?
             ;