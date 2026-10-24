
from pathlib import Path


def write_tokens(tokens, output_filename="tokens.txt"):
    project_root = Path(__file__).resolve().parents[2]
    output_dir = project_root / "test" / "out"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / output_filename

    with output_file.open("w", encoding="utf-8") as file:
        for token in tokens:
            if token.value is not None and token.value != "":
                line = f"< {token.type} , {token.value} >"
            else:
                line = f"< {token.type} , >"

            file.write(f"{line}\n")

    print(f"Tokens generados en: {output_file}")