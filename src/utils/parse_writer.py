from pathlib import Path


def write_parse(rules, output_filename="parse.txt"):
    project_root = Path(__file__).resolve().parents[2]
    output_dir = project_root / "test" / "out"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_file = output_dir / output_filename

    with output_file.open("w", encoding="utf-8") as file:
        file.write("Ascendente")

        for rule in rules:
            file.write(f" {rule}")

        file.write("\n")

    print(f"Parse generado en: {output_file}")
