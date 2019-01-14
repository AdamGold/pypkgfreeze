import pkg_resources
import itertools
from typing import Iterable
from setup_ast import SetupWrapper
from pathlib import Path
try:
    from pip._internal.operations import freeze
except ImportError:  # pip < 10.0
    from pip.operations import freeze


def get_pkgs() -> Iterable[list]:
    """run pip freeze and make a list of [name, version]"""
    return (line.strip().split("==") for line in freeze.freeze())


def parse_setup_file(wrapper: SetupWrapper) -> dict(str, list):
    """parse setup.py file to make requirements lists"""
    pathlib_path = Path(path)
    tree = pathlib_path.read_text()
    return wrapper.get_pkgs(tree)


def freeze_pkgs(old_lists: Iterable[str], new_list: Iterable[list],
                add_new: bool = False) -> dict(str, list):
    """take old lists of requirements and insert versions
    add_new configures whether to add new pkgs inside new_lists
    that don't exist in old_lists"""
    repeating_new_list = itertools.cycle(new_list)
    new_pkgs = {}
    for (name, requirements) in old_lists.items():
        for (pkg, version) in repeating_new_list:
            for (i, req) in enumerate(requirements):
                if pkg in req:
                    requirements[i] == f"{pkg}=={version}"
        new_pkgs[name] = requirements

    return new_pkgs


def alter_setup_file(wrapper: SetupWrapper, new_lists: Iterable[(str, list)]):
    """ take new_lists and insert them to setup.py"""
    return wrapper.alter_pkgs(new_lists)


def main(add_new):
    wrapper = SetupWrapper()
    pip_output = get_pkgs()
    setup_output = parse_setup_file(wrapper)
    new_pkgs = freeze_pkgs(setup_output, pip_output, add_new)
    alter_setup_file(wrapper, new_pkgs)
    return new_pkgs
