
from lex.tokens import tokens, reserved
from errors import (
    INTEGER_OUT_OF_RANGE,
    INVALID_CHARACTER,
    REAL_OUT_OF_RANGE,
    STRING_TOO_LONG,
    error_manager,
)
from symbol_table import SymbolTable


TOKENS_WITH_ATTRIBUTE = {'integer', 'realnum', 'string', 'id'}
symbol_table = SymbolTable()


def set_token_value(t):
    if t.type not in TOKENS_WITH_ATTRIBUTE:
        t.value = None
    return t


def t_opsum(t):
    r'\+'
    return set_token_value(t)


def t_opsub(t):
    r'-'
    return set_token_value(t)


def t_opeq(t):
    r'=='
    return set_token_value(t)


def t_not(t):
    r'!'
    return set_token_value(t)


def t_logor(t):
    r'\|='
    return set_token_value(t)


def t_assig(t):
    r'='
    return set_token_value(t)


def t_parenopen(t):
    r'\('
    return set_token_value(t)


def t_parenclosed(t):
    r'\)'
    return set_token_value(t)


def t_curlopen(t):
    r'\{'
    return set_token_value(t)


def t_curlclosed(t):
    r'\}'
    return set_token_value(t)


def t_semc(t):
    r';'
    return set_token_value(t)


def t_comma(t):
    r','
    return set_token_value(t)


def t_realnum(t):
    r'\d+\.\d+'

    value = float(t.value)

    if value > 117549436.0:
        error_manager.report(REAL_OUT_OF_RANGE, t.value, t.lineno)
        return None

    t.value = value
    return t


def t_integer(t):
    r'\d+'

    value = int(t.value)

    if value > 32767:
        error_manager.report(INTEGER_OUT_OF_RANGE, t.value, t.lineno)
        return None

    t.value = value
    return t


def t_string(t):
    r'"[^"\n]*"'

    value = t.value[1:-1]

    if len(value) > 64:
        error_manager.report(STRING_TOO_LONG, t.value, t.lineno)
        return None

    t.value = value
    return t


def t_id(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'

    t.type = reserved.get(t.value, 'id')
    if t.type == 'id':
        t.value = symbol_table.lookup_or_insert(t.value)

    return set_token_value(t)


def t_comment(t):
    r'/\*[\s\S]*?\*/'
    t.lexer.lineno += t.value.count('\n')


t_ignore = ' \t\r'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    error_manager.report(INVALID_CHARACTER, t.value[0], t.lineno)
    t.lexer.skip(1)