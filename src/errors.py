INTEGER_OUT_OF_RANGE = 1
REAL_OUT_OF_RANGE = 2
STRING_TOO_LONG = 3
INVALID_CHARACTER = 4


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
}


class ErrorManager:
    def __init__(self):
        self.errors = []

    def report(self, error_code, lexeme, line_number):
        error = ERROR_MESSAGES[error_code]

        error_message = (
            f"Error {error['type']}: {error['message']}; "
            f"lexema {lexeme!r}; línea {line_number}."
        )

        self.errors.append(error_message)
        print(error_message)
        return error_message

    def clear(self):
        self.errors.clear()


error_manager = ErrorManager()