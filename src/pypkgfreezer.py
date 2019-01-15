import itertools
from pathlib import Path
from typing import Dict, Iterable, List

import pkg_resources
import re

from src.setup_ast import SetupParser

try:
    from pip._internal.operations import freeze
except ImportError:  # pip < 10.0
    from pip.operations import freeze


def get_pkgs() -> Iterable[List[str]]:
    """run pip freeze and make a list of [name, version]"""
    return (line.strip().split("==") for line in freeze.freeze())


def freeze_pkgs(path: Path, new_list: Iterable[List[str]]) -> str:
    """loop through new list and replace every occurence
    of a package with its freeze version"""
    setup_file_text = path.read_text()
    for (name, version) in new_list:
        # find and replace name in setup.py
        # regex https://regex101.com/r/Pqwmhx/1
        setup_file_text = re.sub(r"[\'\"]({})[\'\"]".format(name),
                                 r"\1=={}".format(version), setup_file_text)
    return setup_file_text


def alter_setup_file(wrapper: SetupParser, new_lists: Dict[str, list]):
    """ take new_lists and insert them to setup.py"""
    return wrapper.alter_pkgs(new_lists)


def write_to_setup(path, text: str):
    """write text to setup.py"""


def main():
    pip_output = get_pkgs()
    setup_path = next(Path('.').glob('setup.py'))  # get first match
    altered_setup = freeze_pkgs(setup_path, pip_output)
    print(altered_setup)
    write_to_setup(setup_path, altered_setup)


if __name__ == "__main__":
    main()
