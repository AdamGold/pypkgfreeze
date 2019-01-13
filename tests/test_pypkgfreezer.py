from src.pypkgfreezer import (get_pkgs, parse_setup_file,
                              freeze_pkgs, alter_setup_file)
import pytest
from src.setup_ast import SetupWrapper


def test_pip_output():
    """pip freeze should include click because this package
    requires it"""
    assert any("Click" in pkg for pkg in list(get_pkgs()))


@pytest.fixture
def wrapper():
    return SetupWrapper()


def test_setup_parse(wrapper):
    """take setup.py and get lists-install_requires,
    test_requires, setup_requires"""
    parse_setup = parse_setup_file(wrapper)
    assert isinstance(parse_setup, list)


def test_insert_versions(wrapper):
    """test that parsed lists and pip output
    make for new lists with versions"""
    parse_setup = parse_setup_file(wrapper)
    pkgs = freeze_pkgs(parse_setup, get_pkgs(), add_new=False)
    assert len(pkgs) == len(parse_setup)


def test_setup_altered(wrapper):
    """ alter setup.py with altered lists"""
    parse_setup = parse_setup_file(wrapper)
    pkgs = freeze_pkgs(parse_setup, get_pkgs(), add_new=False)
    alter_setup_file(wrapper, pkgs)
    new_parse_setup = parse_setup_file(wrapper)
    assert new_parse_setup == pkgs
