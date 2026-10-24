from pathlib import Path


TEST_DIR = Path(__file__).resolve().parent.parent.parent / "test"

def read_file(filename: str) -> str:
    file_path = TEST_DIR / filename

    if not file_path.is_file():
        raise FileNotFoundError(
            f"El archivo no existe en la ruta: {file_path}"
        )

    return file_path.read_text(encoding="utf-8")