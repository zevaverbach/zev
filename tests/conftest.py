from pathlib import Path

from pytest import fixture


@fixture
def empty_filepath():
    """didn't use /tmp because it makes Travis sad"""
    return 'empty.txt'


@fixture
def empty_file(empty_filepath):
    empty_file_ = Path(empty_filepath)
    empty_file_.touch()
    yield
    empty_file_.unlink()
