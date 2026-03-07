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

*Note*: The `--open` option uses `typer.launch()` to open the generated PDF with the system's default viewer. On Linux this typically relies on `xdg-open`. Under WSL this will fail because there is no native Linux GUI environment. If that happens to you, installing `wslview` can fix it.
note that wslview comes from the wslu project, which appears to be discontinued, but the packaged version still works fine for this purpose. [wslu](https://github.com/wslutilities/wslu#installation)
```bash
sudo apt install wslu 
```

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