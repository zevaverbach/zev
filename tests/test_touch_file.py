import os

from zev.touch_file import touch_file
from zev.get_filesize import get_filesize



def test_touch_file(empty_filepath):
    touch_file(empty_filepath)
    assert os.path.exists(empty_filepath)
    assert get_filesize(empty_filepath) == 0
