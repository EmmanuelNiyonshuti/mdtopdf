## mdtopdf

tiny CLI tool built on WeasyPrint to convert Markdown files into styled PDF documents.

It uses:

- `markdown` to parse Markdown into HTML  
- `WeasyPrint` to render HTML into PDF  
- `Typer` for commandline arguments and options

Markdown → styled HTML → PDF.


## Usage

### Run:

```python
python main.py input.md

# results to:
input.pdf

in the same directory.
```
### Options
check the available options with:

```python

python3 main.py --help
```