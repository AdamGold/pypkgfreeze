from src.pypkgfreezer import (get_pkgs, parse_setup_file,
                              freeze_pkgs, alter_setup_file)


def test_pip_output():
    """pip freeze should include click because this package
    requires it"""
    assert any("Click" in pkg for pkg in list(get_pkgs()))


def test_setup_parse():
    """take setup.py and get lists-install_requires,
    test_requires, setup_requires"""
    parse_setup = parse_setup_file()
    assert isinstance(parse_setup, list)


def test_insert_versions():
    """test that parsed lists and pip output
    make for new lists with versions"""
    parse_setup = parse_setup_file()
    pkgs = freeze_pkgs(parse_setup, get_pkgs(), add_new=False)
    assert len(pkgs) == len(parse_setup)


def test_setup_altered():
    """ alter setup.py with altered lists"""
    parse_setup = parse_setup_file()
    pkgs = freeze_pkgs(parse_setup, get_pkgs(), add_new=False)
    alter_setup_file(pkgs)
    new_parse_setup = parse_setup_file()
    assert new_parse_setup == pkgs
