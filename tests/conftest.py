import os

from pytest import fixture


@fixture
def empty_filepath():
    """didn't use /tmp because it makes Travis sad"""
    return 'empty.txt'


@fixture
def empty_file(empty_filepath):
    open(empty_filepath, 'w').close()
    # this is instead of yield statement to make this work with Python 2
    request.addfinalizer(lambda _: os.remove(empty_filepath))
