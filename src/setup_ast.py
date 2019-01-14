import ast


class SetupWrapper():
    """read ASTs from setup.py and parse them"""
# ast.parse("setup(name='test', version='0.1', install_requires=['Click', 'Test'])").body[0].value.keywords[2].value.elts
