import ast
from typing import Dict


class SetupParser():
    """read ASTs from setup.py and parse them"""

    def __init__(self):
        self.pkgs = []

    def get_pkgs(self, setup_file) -> Dict[str, list]:
        """read lists of requirements from setup.py"""

    def alter_pkgs(self, new_lists):
        """alter self.pkgs with new lists"""

# ast.parse("setup(name='test', version='0.1', install_requires=['Click', 'Test'])").body[0].value.keywords[2].value.elts
