import argparse
from pathlib import Path

from pdfminer.high_level import extract_text_to_fp
from pdfminer.layout import LAParams


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert a PDF file to an HTML file using pdfminer.six."
    )
    parser.add_argument(
        "input_pdf",
        type=Path,
        help="Path to the source PDF file.",
    )
    parser.add_argument(
        "output_html",
        type=Path,
        nargs="?",
        help="Optional path to the output HTML file. If omitted, the output file is created next to the input PDF with .html extension.",
    )
    return parser.parse_args()


def convert_pdf_to_html(input_pdf: Path, output_html: Path) -> None:
    if not input_pdf.exists():
        raise FileNotFoundError(f"Input PDF does not exist: {input_pdf}")
    output_html.parent.mkdir(parents=True, exist_ok=True)

    with input_pdf.open("rb") as pdf_file, output_html.open("w", encoding="utf-8") as html_file:
        extract_text_to_fp(
            pdf_file,
            html_file,
            output_type="html",
            laparams=LAParams(),
        )


def main() -> None:
    args = parse_args()
    input_pdf = args.input_pdf
    output_html = args.output_html or input_pdf.with_suffix(".html")

    try:
        convert_pdf_to_html(input_pdf, output_html)
        print(f"Converted: {input_pdf} -> {output_html}")
    except Exception as exc:
        print(f"Error: {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
