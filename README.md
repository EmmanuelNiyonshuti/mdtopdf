## mdtopdf

tiny CLI tool built on WeasyPrint to convert Markdown files into styled PDF documents.

It uses:

- `markdown` to parse Markdown into HTML  
- `WeasyPrint` to render HTML into PDF  
- `Typer` for commandline arguments and options

Markdown → styled HTML → PDF.

## Install

We rely on `WeasyPrint` for HTML → PDF, which itself depends on some native system libraries.

If you run into import errors, make sure you are using **Python ≥ 3.12** and that the
required system dependencies for WeasyPrint are installed.

Then install project dependencies:
```python
uv sync
```

## Usage
### Run directly with Python:
```python
python3 -m mdtopdf.cli input.md

# results to:
input.pdf  # in the same directory.
```
# or install it in editable mode
```python
uv pip install -e .

# then run:
mdtopdf input.md

# same results:
input.pdf  # in the same directory.
```
### Options
check the available options with:

```python

python3 -m mdtopdf.cli --help

# or if you installed in editable mode
mdtopdf --help
```