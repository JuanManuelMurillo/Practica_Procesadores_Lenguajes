
import ply.lex as lex
import lex.expressions as expressions
from errors import error_manager

from utils.file_reader import read_file
from utils.file_names import files
from utils.token_writer import write_tokens


def main():
    source_code = read_file(files[2])

    error_manager.clear()
    expressions.symbol_table.clear()
    lexer = lex.lex(module=expressions)
    lexer.input(source_code)

    tokens = []

    while True:
        token = lexer.token()

        if token is None:
            break

        tokens.append(token)

    write_tokens(tokens)
    expressions.symbol_table.write()


main()