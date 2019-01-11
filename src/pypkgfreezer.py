import pkg_resources
from typing import Iterable
try:
    from pip._internal.operations import freeze
except ImportError:  # pip < 10.0
    from pip.operations import freeze


def get_pkgs() -> Iterable[list]:
    """run pip freeze and make a list of [name, version]"""
    return (line.strip().split("==") for line in freeze.freeze())


def parse_setup_file() -> Iterable[str]:
    """parse setup.py file to make requirements lists"""


def freeze_pkgs(old_lists: Iterable[str], new_lists: Iterable[list],
                add_new: bool = False) -> Iterable:
    """take old lists of requirements and insert versions
    add_new configures whether to add new pkgs inside new_lists
    that don't exist in old_lists"""


def alter_setup_file(new_lists: Iterable[str]):
    """ take new_lists and insert them to setup.py"""


def main(add_new):
    pip_output = get_pkgs()
    setup_output = parse_setup_file()
    new_pkgs = freeze_pkgs(setup_output, pip_output, add_new)
    alter_setup_file(new_pkgs)
    return new_pkgs
