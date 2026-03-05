from pathlib import Path
from typing import Annotated

import typer

from converter import convert

app = typer.Typer(
    name="md2pdf",
    help="Convert a Markdown file to a styled PDF.",
)


def _resolve_output(input_file: Path, output_file: Path | None = None) -> str:
    if output_file:
        return output_file
    return input_file.with_suffix(".pdf")


@app.command()
def main(
    input_file: Annotated[
        Path,
        typer.Argument(
            help="Path to the input Markdown file",
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
        ),
    ],
    output_file: Annotated[
        Path | None,
        typer.Option(
            "--output",
            "-o",
            help="Output PDF file path. Defaults to <input>.pdf in the same directory.",
            writable=True,
        ),
    ] = None,
    style: Annotated[
        Path | None,
        typer.Option(
            "--style",
            "-s",
            help="Path to a custom .css file. Appended after default styles, so your rules take precedence.",
            exists=True,
            file_okay=True,
            dir_okay=False,
            readable=True,
        ),
    ] = None,
    open_after: Annotated[
        bool,
        typer.Option(
            "--open",
            help="Open the generated PDF immediately after creation.",
        ),
    ] = False,
    verbose: Annotated[
        bool,
        typer.Option(
            "--verbose",
            "-v",
            help="Print details about what's happening.",
        ),
    ] = False,
):
    output_path = _resolve_output(input_file, output_file)
    if verbose:
        typer.echo(f"  Input:  {input_file}")
        typer.echo(f"  Output: {output_path}")
        typer.echo(f"  Style:  {style or 'default'}")

    try:
        convert(input_file=input_file, output_file=output_path, style_file=style)
    except FileNotFoundError as e:
        typer.secho(f"Error: {e}", fg=typer.colors.RED, err=True)
        raise typer.Exit(code=1)
    except Exception as e:
        typer.secho(f"Conversion failed: {e}", fg=typer.colors.RED, err=True)
        if verbose:
            import traceback

            traceback.print_exc()
        raise typer.Exit(code=1)

    typer.secho(f"✓ PDF written to {output_path}", fg=typer.colors.GREEN)

    if open_after:
        typer.launch(str(output_path), locate=True)
