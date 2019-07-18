from pytest import fixture

from zev.get_filesize import get_filesize


def test_get_filesize(empty_filepath):
    assert get_filesize(empty_filepath) == 0
