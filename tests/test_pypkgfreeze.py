from pypkgfreeze.pypkgfreeze import get_pkgs, freeze_pkgs, write_to_file
import pytest


def test_pip_output():
    """pip freeze should include click because this package
    requires it"""
    assert any("Click" in pkg for pkg in list(get_pkgs()))


def test_freeze_pkgs():
    """test to see if the method
    catches the right packages and adds their version"""
    test_list = [["Test", "0.3"], ["Other", "1.2"]]
    test_text = "setup(test_requires=['Test', 'Other==1.5])"
    expect_text = 'test_requires=["Test==0.3"'
    assert expect_text in freeze_pkgs(test_text, test_list)


def test_write_to_file(tmp_path):
    """try creating a file,
    check write_to_file actually changes it"""
    p = tmp_path / "hello.txt"
    write_to_file(p, "test")
    assert p.read_text() == "test"
