import os


def get_filesize(path):
    """
      path: str
      returns: int
    """
    return os.stat(path).st_size
