"""
CSS styles for PDF rendering.

- DEFAULT_CSS is always loaded
- load_css(custom_path) appends custom CSS after default, so it naturally overrides via cascade
- WeasyPrint uses @page for margins/size — those live here too
"""

from pathlib import Path

DEFAULT_CSS = """
/* ── Page layout (WeasyPrint specific) ── */
@page {
    size: A4;
    margin: 20mm 20mm 20mm 20mm;
}

/* ── Base typography ── */
body {
    font-family: 'Georgia', 'Times New Roman', serif;
    font-size: 11pt;
    line-height: 1.7;
    color: #1a1a1a;
    max-width: 100%;
}

/* ── Headings ── */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Helvetica Neue', 'Arial', sans-serif;
    font-weight: 700;
    color: #111;
    margin-top: 1.4em;
    margin-bottom: 0.4em;
    line-height: 1.3;
    page-break-after: avoid;
}

h1 { font-size: 22pt; border-bottom: 2px solid #e0e0e0; padding-bottom: 6px; }
h2 { font-size: 17pt; border-bottom: 1px solid #e0e0e0; padding-bottom: 4px; }
h3 { font-size: 14pt; }
h4 { font-size: 12pt; }
h5 { font-size: 11pt; font-style: italic; }
h6 { font-size: 10pt; font-style: italic; color: #555; }

/* ── Paragraphs & spacing ── */
p {
    margin: 0 0 1em 0;
    orphans: 3;
    widows: 3;
}

/* ── Links ── */
a {
    color: #2563eb;
    text-decoration: underline;
}

/* ── Inline code ── */
code {
    font-family: 'Courier New', 'Courier', monospace;
    font-size: 9.5pt;
    background-color: #f4f4f4;
    border: 1px solid #ddd;
    border-radius: 3px;
    padding: 1px 4px;
}

/* ── Code blocks ── */
pre {
    background-color: #f6f8fa;
    border: 1px solid #d1d5db;
    border-left: 4px solid #2563eb;
    border-radius: 4px;
    padding: 12px 16px;
    font-size: 9pt;
    line-height: 1.5;
    overflow-x: auto;
    page-break-inside: avoid;
    margin: 1em 0;
}

pre code {
    background: none;
    border: none;
    padding: 0;
    font-size: inherit;
}

/* ── Tables ── */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.2em 0;
    font-size: 10pt;
    page-break-inside: avoid;
}

thead {
    background-color: #2563eb;
    color: white;
}

thead th {
    padding: 8px 12px;
    text-align: left;
    font-weight: 600;
}

tbody tr:nth-child(even) {
    background-color: #f1f5f9;
}

tbody tr:nth-child(odd) {
    background-color: #ffffff;
}

td, th {
    border: 1px solid #d1d5db;
    padding: 7px 12px;
    vertical-align: top;
}

/* ── Blockquotes ── */
blockquote {
    margin: 1em 0;
    padding: 10px 16px;
    border-left: 4px solid #2563eb;
    background-color: #eff6ff;
    color: #374151;
    font-style: italic;
    page-break-inside: avoid;
}

blockquote p {
    margin: 0;
}

/* ── Lists ── */
ul, ol {
    margin: 0.5em 0 1em 0;
    padding-left: 1.6em;
}

li {
    margin-bottom: 0.3em;
    line-height: 1.6;
}

li > ul, li > ol {
    margin-top: 0.3em;
    margin-bottom: 0.3em;
}

/* ── Images ── */
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 1em auto;
    page-break-inside: avoid;
}

/* ── Horizontal rule ── */
hr {
    border: none;
    border-top: 2px solid #e0e0e0;
    margin: 2em 0;
}

/* ── Syntax highlighting (codehilite) ── */
.codehilite {
    background: #f6f8fa;
    border: 1px solid #d1d5db;
    border-left: 4px solid #2563eb;
    border-radius: 4px;
    padding: 12px 16px;
    margin: 1em 0;
    overflow-x: auto;
}

.codehilite pre {
    border: none;
    padding: 0;
    margin: 0;
    background: none;
}

/* ── Table of contents ── */
.toc {
    background-color: #f8fafc;
    border: 1px solid #e2e8f0;
    border-radius: 4px;
    padding: 12px 20px;
    margin-bottom: 2em;
    font-size: 10pt;
}

.toc ul {
    list-style: none;
    padding-left: 1em;
}

.toc > ul {
    padding-left: 0;
}

.toc a {
    color: #374151;
    text-decoration: none;
}

/* ── Footnotes ── */
.footnote {
    font-size: 9pt;
    color: #6b7280;
    border-top: 1px solid #e0e0e0;
    margin-top: 2em;
    padding-top: 0.5em;
}
"""


def load_css(custom_path: Path | None = None) -> str:
    """
    Always returns DEFAULT_CSS as the base.
    If a custom CSS file path is provided, its contents are appended after
    so custom rules override defaults naturally via CSS cascade.
    """
    if custom_path is None:
        return DEFAULT_CSS

    if not custom_path.exists():
        raise FileNotFoundError(f"CSS file not found: {custom_path}")

    if not custom_path.suffix == ".css":
        raise ValueError(f"Expected a .css file, got: {custom_path.name}")

    custom_css = custom_path.read_text(encoding="utf-8")
    return f"{DEFAULT_CSS}\n\n/* ── Custom overrides ── */\n{custom_css}"
