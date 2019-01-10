from src.pypkgfreezer import get_pkgs


def test_pip_output():
    """pip freeze should include click because this package
    requires it"""
    assert any("Click" in pkg for pkg in list(get_pkgs()))


def test_setup_parse():
    """take setup.py and get lists-install_requires,
    test_requires, setup_requires"""


def test_setup_altered():
    """ alter setup.py with altered lists"""
    pass
