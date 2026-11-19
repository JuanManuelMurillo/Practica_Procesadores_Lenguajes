INTEGER_OUT_OF_RANGE = 1
REAL_OUT_OF_RANGE = 2
STRING_TOO_LONG = 3
INVALID_CHARACTER = 4
UNEXPECTED_TOKEN = 5
UNEXPECTED_EOF = 6
MISSING_SEMICOLON = 7
MISSING_PARENOPEN = 8
MISSING_PARENCLOSED = 9
MISSING_CURLOPEN = 10
MISSING_CURLCLOSED = 11
MISSING_OPERAND = 12
MISSING_TYPE = 13
MISSING_ID = 14


ERROR_MESSAGES = {
    INTEGER_OUT_OF_RANGE: {
        "type": "Léxico",
        "message" : "Constante entera fuera de rango máximo (32767)",
    },
    REAL_OUT_OF_RANGE: {
        "type": "Léxico",
        "message" : "Constante real fuera de rango máximo (117549436.0)",
    }, 
    STRING_TOO_LONG: {
        "type": "Léxico",
        "message" : "Cadena mayor a 64 caracteres",
    }, 
    INVALID_CHARACTER: {
        "type": "Léxico",
        "message" : "Carácter no válido",
    },
    UNEXPECTED_TOKEN: {
        "type": "Sintáctico",
        "message" : "Token inesperado",
    },
    UNEXPECTED_EOF: {
        "type": "Sintáctico",
        "message" : "Fin de fichero inesperado",
    },
    MISSING_SEMICOLON: {
        "type": "Sintáctico",
        "message" : "Falta el punto y coma del final de la sentencia",
    },
    MISSING_PARENOPEN: {
        "type": "Sintáctico",
        "message" : "Falta el paréntesis de apertura",
    },
    MISSING_PARENCLOSED: {
        "type": "Sintáctico",
        "message" : "Falta el paréntesis de cierre",
    },
    MISSING_CURLOPEN: {
        "type": "Sintáctico",
        "message" : "Falta la llave de apertura del bloque",
    },
    MISSING_CURLCLOSED: {
        "type": "Sintáctico",
        "message" : "Falta la llave de cierre del bloque",
    },
    MISSING_OPERAND: {
        "type": "Sintáctico",
        "message" : "Falta un operando en la expresión",
    },
    MISSING_TYPE: {
        "type": "Sintáctico",
        "message" : "Falta el tipo de la variable, del parámetro o de la función",
    },
    MISSING_ID: {
        "type": "Sintáctico",
        "message" : "Falta el nombre de la variable, del parámetro o de la función",
    },
}


class ErrorManager:
    def __init__(self):
        self.errors = []

    def report(self, error_code, lexeme=None, line_number=None):
        error = ERROR_MESSAGES[error_code]

        error_message = f"Error {error['type']}"

        error_message += f": {error['message']}"

        if lexeme is not None:
            error_message += f"; lexema {lexeme!r}"

        if line_number is not None:
            error_message += f"; línea {line_number}"

        error_message += "."

        self.errors.append(error_message)
        print(error_message)
        return error_message

    def clear(self):
        self.errors.clear()


error_manager = ErrorManager()