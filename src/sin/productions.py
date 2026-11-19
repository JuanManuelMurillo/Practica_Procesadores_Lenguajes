from lex.tokens import tokens, reserved
from lex.expressions import symbol_table
from errors import (
    MISSING_CURLCLOSED,
    MISSING_CURLOPEN,
    MISSING_ID,
    MISSING_OPERAND,
    MISSING_PARENCLOSED,
    MISSING_PARENOPEN,
    MISSING_SEMICOLON,
    MISSING_TYPE,
    UNEXPECTED_EOF,
    UNEXPECTED_TOKEN,
    error_manager,
)


start = 'P'
parse = []


TOKEN_LEXEMES = {
    'opsum': '+',
    'opsub': '-',
    'opeq': '==',
    'not': '!',
    'logor': '|=',
    'assig': '=',
    'parenopen': '(',
    'parenclosed': ')',
    'curlopen': '{',
    'curlclosed': '}',
    'semc': ';',
    'comma': ',',
}

for word, token in reserved.items():
    TOKEN_LEXEMES[token] = word

SENTENCE_START = {'id', 'let', 'if', 'while', 'echo', 'prompt', 'ret', 'fun', 'curlclosed'}
TYPES = {'int', 'float', 'bool', 'str'}


def add_rule(rule_number):
    parse.append(rule_number)


# Programa

def p_program_block(p):
    'P : B P'
    add_rule(1)


def p_program_function(p):
    'P : F P'
    add_rule(2)


def p_program_empty(p):
    'P : '
    add_rule(3)


# Sentencias compuestas y declaración de variables

def p_block_declaration(p):
    'B : let M id T semc'
    add_rule(4)


def p_block_if(p):
    'B : if parenopen E parenclosed S'
    add_rule(5)


def p_block_while(p):
    'B : while parenopen E parenclosed curlopen C curlclosed'
    add_rule(6)


def p_block_sentence(p):
    'B : S'
    add_rule(7)


def p_declaration_marker(p):
    'M : '
    add_rule(8)


def p_type_int(p):
    'T : int'
    add_rule(9)


def p_type_float(p):
    'T : float'
    add_rule(10)


def p_type_bool(p):
    'T : bool'
    add_rule(11)


def p_type_str(p):
    'T : str'
    add_rule(12)


# Sentencias simples

def p_sentence_assig(p):
    'S : id assig E semc'
    add_rule(13)


def p_sentence_logor(p):
    'S : id logor E semc'
    add_rule(14)


def p_sentence_call(p):
    'S : id parenopen L parenclosed semc'
    add_rule(15)


def p_sentence_echo(p):
    'S : echo E semc'
    add_rule(16)


def p_sentence_prompt(p):
    'S : prompt id semc'
    add_rule(17)


def p_sentence_return(p):
    'S : ret X semc'
    add_rule(18)


def p_return_value(p):
    'X : E'
    add_rule(19)


def p_return_empty(p):
    'X : '
    add_rule(20)


def p_arguments(p):
    'L : E Q'
    add_rule(21)


def p_arguments_empty(p):
    'L : '
    add_rule(22)


def p_arguments_next(p):
    'Q : comma E Q'
    add_rule(23)


def p_arguments_end(p):
    'Q : '
    add_rule(24)


# Declaración de funciones

def p_function(p):
    'F : fun F1 F2 curlopen C curlclosed'
    add_rule(25)


def p_function_marker(p):
    'F1 : '
    add_rule(26)


def p_function_header(p):
    'F2 : F3 H parenopen A parenclosed'
    add_rule(27)


def p_function_name(p):
    'F3 : id'
    add_rule(28)


def p_return_type(p):
    'H : T'
    add_rule(29)


def p_return_type_void(p):
    'H : void'
    add_rule(30)


def p_parameters(p):
    'A : id T K'
    add_rule(31)


def p_parameters_void(p):
    'A : void'
    add_rule(32)


def p_parameters_next(p):
    'K : comma id T K'
    add_rule(33)


def p_parameters_end(p):
    'K : '
    add_rule(34)


def p_body(p):
    'C : B C'
    add_rule(35)


def p_body_empty(p):
    'C : '
    add_rule(36)


# Expresiones

def p_expression_eq(p):
    'E : E opeq R'
    add_rule(37)


def p_expression(p):
    'E : R'
    add_rule(38)


def p_additive_sum(p):
    'R : R opsum U'
    add_rule(39)


def p_additive_sub(p):
    'R : R opsub U'
    add_rule(40)


def p_additive(p):
    'R : U'
    add_rule(41)


def p_unary_not(p):
    'U : not U'
    add_rule(42)


def p_unary(p):
    'U : V'
    add_rule(43)


def p_operand_id(p):
    'V : id'
    add_rule(44)


def p_operand_paren(p):
    'V : parenopen E parenclosed'
    add_rule(45)


def p_operand_call(p):
    'V : id parenopen L parenclosed'
    add_rule(46)


def p_operand_integer(p):
    'V : integer'
    add_rule(47)


def p_operand_realnum(p):
    'V : realnum'
    add_rule(48)


def p_operand_string(p):
    'V : string'
    add_rule(49)


# Errores

def token_lexeme(t):
    if t.type == 'id':
        return symbol_table.get_lexeme(t.value)
    if t.type == 'string':
        return f'"{t.value}"'
    if t.type in ('integer', 'realnum'):
        return str(t.value)
    return TOKEN_LEXEMES[t.type]


def p_error(p):
    raise SyntaxError(p)


def accepts(parser, token_type):
    states = list(parser.statestack)

    while True:
        action = parser.action[states[-1]].get(token_type)

        if action is None:
            return False
        if action >= 0:
            return True

        production = parser.productions[-action]
        if production.len:
            del states[-production.len:]
        states.append(parser.goto[states[-1]][production.name])


def report_error(parser, token, tokens):
    expected = {
        token_type for token_type in parser.action[parser.state]
        if accepts(parser, token_type)
    }
    found = token.type if token is not None else '$end'

    previous = tokens[-2] if token is not None and len(tokens) > 1 else None
    if token is None and tokens:
        previous = tokens[-1]
    line = previous.lineno if previous is not None else 1

    if 'semc' in expected and (found in SENTENCE_START or found == '$end'):
        error_manager.report(MISSING_SEMICOLON, line_number=line)
    elif 'integer' in expected:
        error_manager.report(MISSING_OPERAND, line_number=line)
    elif 'parenclosed' in expected:
        error_manager.report(MISSING_PARENCLOSED, line_number=line)
    elif 'parenopen' in expected:
        error_manager.report(MISSING_PARENOPEN, line_number=line)
    elif 'curlopen' in expected:
        error_manager.report(MISSING_CURLOPEN, line_number=line)
    elif 'curlclosed' in expected and found in ('$end', 'fun'):
        error_manager.report(MISSING_CURLCLOSED, line_number=line)
    elif TYPES & expected and expected <= TYPES | {'void'}:
        error_manager.report(MISSING_TYPE, line_number=line)
    elif 'id' in expected and expected <= {'id', 'void'}:
        error_manager.report(MISSING_ID, line_number=line)
    elif token is None:
        error_manager.report(UNEXPECTED_EOF, line_number=line)
    else:
        error_manager.report(UNEXPECTED_TOKEN, token_lexeme(token), token.lineno)
