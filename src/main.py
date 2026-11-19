
import ply.lex as lex
import ply.yacc as yacc
import lex.expressions as expressions
import sin.productions as productions
from errors import error_manager

from utils.file_reader import read_file
from utils.file_names import files
from utils.token_writer import write_tokens
from utils.parse_writer import write_parse


def main():
    source_code = read_file(files[5])

    error_manager.clear()
    expressions.symbol_table.clear()
    productions.parse.clear()

    lexer = lex.lex(module=expressions)
    lexer.input(source_code)
    parser = yacc.yacc(module=productions, write_tables=False, debug=False)

    tokens = []

    def next_token():
        token = lexer.token()

        if token is not None:
            tokens.append(token)

        return token

    try:
        parser.parse(tokenfunc=next_token)
    except SyntaxError as error:
        productions.report_error(parser, error.args[0], tokens)

    write_tokens(tokens)
    expressions.symbol_table.write()
    write_parse(productions.parse)


main()