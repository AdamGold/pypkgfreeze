import click
from src.pypkgfreeze import main


@click.command()
@click.argument("add_new")
def cli():
    """run the main functionality."""
    main()
