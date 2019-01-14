import pkg_resources
import itertools
from typing import Iterable, Dict, List
from src.setup_ast import SetupWrapper
from pathlib import Path
try:
    from pip._internal.operations import freeze
except ImportError:  # pip < 10.0
    from pip.operations import freeze


def get_pkgs() -> Iterable[List[str]]:
    """run pip freeze and make a list of [name, version]"""
    return (line.strip().split("==") for line in freeze.freeze())


def parse_setup_file(wrapper: SetupWrapper) -> Dict[str, list]:
    """parse setup.py file to make requirements lists"""
    pathlib_path = next(Path('.').glob('setup.py'))  # get first match
    setup_file = pathlib_path.read_text()
    return wrapper.get_pkgs(setup_file)


def freeze_pkgs(old_lists: Dict[str, list], new_list: Iterable[List[str]],
                add_new: bool = False) -> Dict[str, list]:
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


def alter_setup_file(wrapper: SetupWrapper, new_lists: Dict[str, list]):
    """ take new_lists and insert them to setup.py"""
    return wrapper.alter_pkgs(new_lists)


def main(add_new):
    wrapper = SetupWrapper()
    pip_output = get_pkgs()
    setup_output = parse_setup_file(wrapper)
    new_pkgs = freeze_pkgs(setup_output, pip_output, add_new)
    alter_setup_file(wrapper, new_pkgs)
    return new_pkgs
