"""
Convert markdown file -> html -> plain text pdf
"""

from pathlib import Path

import markdown
import weasyprint

from .styles import load_css


def md_to_html(md_content: str) -> str:
    md = markdown.Markdown(
        extensions=[
            "extra",  # tables, footnotes, attribute lists, etc.
            "codehilite",  # syntax highlighted code blocks
            "toc",  # table of contents
            "nl2br",  # newlines <br>
            "sane_lists",  # better list handling
        ],
        extension_configs={
            "codehilite": {
                "guess_lang": False,  # only highlight when language is specified
                "css_class": "codehilite",
            },
            "toc": {
                "permalink": False,  # no anchor symbols in PDF (they look odd!)
            },
        },
    )
    html = md.convert(md_content)
    return html


def wrap_in_document(body: str, css: str, title="") -> str:
    """
    Wraps an HTML fragment(body) in a full HTML document.

    WeasyPrint needs a proper document to render correctly.
    CSS is injected inline in <head> so there are no external file dependencies.
    """
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{title}</title>
    <style>
    {css}
    </style>
</head>
<body>
{body}
</body>
</html>"""


def convert(input_file: Path, output_file: Path, style_file: Path | None = None) -> str:
    """
    Reads a .md file, converts it to a PDF.(.md -> html -> pdf)

    input_file:  path to the source .md file
    output_file: path to write the output .pdf
    style_file:  optional path to a .css file to override/extend default styles
    """
    md_content = input_file.read_text(encoding="utf-8")
    html_fragment = md_to_html(md_content)
    css = load_css(style_file)
    full_html = wrap_in_document(html_fragment, css, title=input_file.stem)

    result = weasyprint.HTML(string=full_html)
    result.write_pdf(output_file)
