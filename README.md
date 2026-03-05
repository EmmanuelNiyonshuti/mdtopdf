## mdtopdf

tiny CLI tool built on WeasyPrint to convert Markdown files into styled PDF documents.

It uses:

- `markdown` to parse Markdown into HTML  
- `WeasyPrint` to render HTML into PDF  
- `Typer` for commandline arguments and options

Markdown → styled HTML → PDF.

## Install

`WeasyPrint` relies on native system libraries and works best with stable Python versions.

You have to make sure you have **Python ≥ 3.12** installed.

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