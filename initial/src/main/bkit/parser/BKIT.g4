grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
def emit(self):
    tk = self.type
    result = super().emit()
    if tk == self.UNCLOSE_STRING:       
        raise UncloseString(result.text)
    elif tk == self.ILLEGAL_ESCAPE:
        raise IllegalEscape(result.text)
    elif tk == self.ERROR_CHAR:
        raise ErrorToken(result.text)
    else:
        return result;
}

options {
	language = Python3;
}

// DANG VU SI DAN - 2020017

// ================================================================== PARSER ==================================================================

program: glob_var_decl_part func_decl_part EOF;

// GLOBAL VARIABLE DECLARATION PART
glob_var_decl_part: var_decl_list?;

var_decl_list: var_decl var_decl_list | var_decl;

var_decl: VAR COLON var_list SEMI;

var_list: var COMMA var_list | var;

var: scalar_var | compo_var;

scalar_var: ID (ASSIGN literal)?;

compo_var: ID dimensions (ASSIGN array_lit)?;

// FUNCTION DECLARATION PART
func_decl_part: func_decl_list?;

func_decl_list: func_decl func_decl_list | func_decl;

func_decl: FUNCTION COLON ID func_param? func_body;

func_param: PARAMETER COLON param_list;

param_list: param COMMA param_list | param;

param: ID | ID dimensions;

func_body: BODY COLON stmt_list ENDBODY DOT;

stmt_list: var_decl_stmt_list? other_stmt_list?;

var_decl_stmt_list:
	var_decl_stmt var_decl_stmt_list
	| var_decl_stmt;

other_stmt_list: other_stmt other_stmt_list | other_stmt;

other_stmt:
	assign_stmt
	| if_stmt
	| for_stmt
	| while_stmt
	| do_while_stmt
	| break_stmt
	| continue_stmt
	| call_stmt
	| return_stmt;

var_decl_stmt: VAR COLON var_list SEMI;

assign_stmt: (ID | index_exp) ASSIGN exp SEMI;

if_stmt:
	IF exp THEN stmt_list else_if_list? (ELSE stmt_list)? ENDIF DOT;

else_if_list: else_if else_if_list | else_if;

else_if: ELSEIF exp THEN stmt_list;

for_stmt:
	FOR LB ID ASSIGN exp COMMA exp COMMA exp RB DO stmt_list ENDFOR DOT;

while_stmt: WHILE exp DO stmt_list ENDWHILE DOT;

do_while_stmt: DO stmt_list WHILE exp ENDDO DOT;

break_stmt: BREAK SEMI;

continue_stmt: CONTINUE SEMI;

call_stmt: ID LB exp_list? RB SEMI;

return_stmt: RETURN exp? SEMI;

exp:
	exp1 (
		EQ_I
		| NEQ_I
		| LT_I
		| GT_I
		| LTE_I
		| GTE_I
		| NEQ_F
		| LT_F
		| GT_F
		| LTE_F
		| GTE_F
	) exp1
	| exp1;

exp1: exp1 (AND | OR) exp2 | exp2;

exp2: exp2 (ADD_I | ADD_F | SUB_I | SUB_F) exp3 | exp3;

exp3: exp3 (MUL_I | MUL_F | DIV_I | DIV_F | MOD_I) exp4 | exp4;

exp4: NOT exp4 | exp5;

exp5: (SUB_I | SUB_F) exp5 | index_exp | func_call_exp;

index_exp: (ID|func_call) index_operator;

index_operator: LS exp RS | LS exp RS index_operator;

func_call_exp: func_call | operand;

operand: literal | ID | LB exp RB;

func_call: ID LB exp_list? RB;

exp_list: exp COMMA exp_list | exp;

// HELPER RULES
literal:
	DEC_INT_LIT
	| HEX_INT_LIT
	| OCT_INT_LIT
	| FLT_LIT
	| BOOL_LIT
	| STR_LIT
	| array_lit;

dimensions: dimension dimensions | dimension;

dimension: LS (DEC_INT_LIT | HEX_INT_LIT | OCT_INT_LIT) RS;

array_lit: LC array_element_list RC;

array_element_list: array_element COMMA array_element_list | array_element;

array_element: literal;

// ================================================================== LEXER ==================================================================

// FRAGMENTS
fragment DEGIT: [0-9];
fragment DEGIT_NO_ZERO: [1-9];
fragment OCT_DEGIT: [0-7];
fragment OCT_DEGIT_NO_ZERO: [1-7];
fragment HEX_CHAR: [A-F];
fragment HEX_PREFIX: ('0X' | '0x');
fragment OCT_PREFIX: ('0O' | '0o');
fragment FLT_INT_PART: ('0' | [1-9] [0-9]*);
fragment FLT_DEC_PART: '.' [0-9]*;
fragment FLT_EXP_PART: ('e' | 'E') ('+' | '-')? (
		'0'
		| [1-9][0-9]*
	);
fragment ESCAPE_CHAR: '\\' [bfrnt'\\];
fragment DOUBLE_QUOTE_CHAR: '\'"';

DEC_INT_LIT: ('0' | DEGIT_NO_ZERO DEGIT*);
HEX_INT_LIT:
	HEX_PREFIX (DEGIT_NO_ZERO | HEX_CHAR) (DEGIT | HEX_CHAR)*;
OCT_INT_LIT: OCT_PREFIX OCT_DEGIT OCT_DEGIT_NO_ZERO*;
FLT_LIT:
	FLT_INT_PART (FLT_DEC_PART FLT_EXP_PART? | FLT_EXP_PART);
BOOL_LIT: (TRUE | FALSE);
STR_LIT:
	'"' (DOUBLE_QUOTE_CHAR | ESCAPE_CHAR | ~["\\\n\r])* '"' {self.text = self.text[1:-1]};

// KEYWORDS
BODY: 'Body';
BREAK: 'Break';
CONTINUE: 'Continue';
DO: 'Do';
ELSE: 'Else';
ELSEIF: 'ElseIf';
ENDBODY: 'EndBody';
ENDIF: 'EndIf';
ENDFOR: 'EndFor';
ENDWHILE: 'EndWhile';
FOR: 'For';
FUNCTION: 'Function';
IF: 'If';
PARAMETER: 'Parameter';
RETURN: 'Return';
THEN: 'Then';
VAR: 'Var';
WHILE: 'While';
fragment TRUE: 'True';
fragment FALSE: 'False';
ENDDO: 'EndDo';

// OPERATOR
ADD_I: '+';
SUB_I: '-';
MUL_I: '*';
DIV_I: '\\';
MOD_I: '%';
ADD_F: '+.';
SUB_F: '-.';
MUL_F: '*.';
DIV_F: '\\.';
EQ_I: '==';
NEQ_I: '!=';
LT_I: '<';
GT_I: '>';
LTE_I: '<=';
GTE_I: '>=';
NEQ_F: '=/=';
LT_F: '<.';
GT_F: '>.';
LTE_F: '<=.';
GTE_F: '>=.';
NOT: '!';
AND: '&&';
OR: '||';
ASSIGN: '=';

// SEPARATORS
LS: '[';
RS: ']';
LB: '(';
RB: ')';
LC: '{';
RC: '}';
SEMI: ';';
COLON: ':';
COMMA: ',';
DOT: '.';

// IDENTIFIERS
ID: [a-z][_a-zA-Z0-9]*;

// COMMENTS
COMMENT: ('**' .*? '**') -> skip;
// WHITE SPACE
WS: [ \t\r\n]+ -> skip;
ILLEGAL_ESCAPE:
	'"' (DOUBLE_QUOTE_CHAR | ESCAPE_CHAR | ~["\\\n\r])* '\\' ~[bfrnt'\\] {
    raise IllegalEscape(self.text[1:])
};
UNCLOSE_STRING:
	'"' (DOUBLE_QUOTE_CHAR | ESCAPE_CHAR | ~["\\\n\r])* {
	raise UncloseString(self.text[1:])
};
ERROR_CHAR:
	. {
	raise ErrorToken(self.text);
};