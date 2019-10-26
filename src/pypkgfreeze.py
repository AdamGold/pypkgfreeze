import re
import click
from pathlib import Path
from typing import Dict, Iterable, List

import pkg_resources

try:
    from pip._internal.operations import freeze
except ImportError:  # pip < 10.0
    from pip.operations import freeze


def get_pkgs() -> Iterable[List[str]]:
    """run pip freeze and make a list of [name, version]"""
    return (line.strip().split("==") for line in freeze.freeze())


def freeze_pkgs(text: str, new_list: Iterable[List[str]]) -> str:
    """loop through new list and replace every occurence
    of a package with its freeze version"""
    for pkg in new_list:
        try:
            name, version = pkg
        except ValueError:  # we don't have the version, let's ignore it
            continue
        # find and replace name in setup.py
        # regex https://regex101.com/r/Pqwmhx/2
        text = re.sub(
            r"[\'\"]({})\=?\=?([0-9]+\.)?([0-9]+\.)?([0-9]+)?[\'\"]".format(
                re.escape(name)
            ),
            r'"\1=={}"'.format(version),
            text,
        )

    return text


def write_to_file(path: Path, text: str):
    """write text to setup.py"""
    path.write_text(text)


@click.command()
def main():
    pip_output = get_pkgs()
    setup_path = next(Path(".").glob("setup.py"))  # get first match
    altered_setup = freeze_pkgs(setup_path.read_text(), pip_output)
    write_to_file(setup_path, altered_setup)
