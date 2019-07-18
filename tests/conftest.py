from pytest import fixture


@fixture
def empty_filepath():
    return '/tmp/empty.txt'


@fixture
def empty_file(empty_filepath):
    open(empty_filepath, 'w').close()


