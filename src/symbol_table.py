from pathlib import Path


class SymbolTable:
    def __init__(self, table_number=0):

        self.table_number = table_number
        self._positions = {}
        self._lexemes = []

    def lookup_or_insert(self, lexeme):

        if lexeme not in self._positions:
            self._positions[lexeme] = len(self._lexemes)
            self._lexemes.append(lexeme)

        return self._positions[lexeme]

    def get_lexeme(self, position):
        return self._lexemes[position]

    def lexemes(self):
        return tuple(self._lexemes)

    def clear(self):
        self._positions.clear()
        self._lexemes.clear()

    def to_text(self):
        lines = [f"#{self.table_number}:"]
        lines.extend(f"* '{lexeme}'" for lexeme in self._lexemes)
        return "\n".join(lines) + "\n"

    def write(self):
        project_root = Path(__file__).resolve().parents[1]
        output_path = project_root / "test" / "out" / "symbol_table.txt"

        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(self.to_text(), encoding="utf-8")
        return output_path