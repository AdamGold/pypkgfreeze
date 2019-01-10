import click
from src.pypkgfreezer import main


@click.command()
@click.argument("add_new")
def cli():
    """run the main functionality.
     add_new configures whether to add installed pkgs to setup.py
     or just insert values for the existing ones"""
    main()
