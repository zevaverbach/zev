import os

from zev import __all__


def test_helpers_available():
    num_modules = len([
        i for i in os.listdir('zev') 
        if i.endswith('.py')
        if not i.startswith('__')
    ])
    assert num_modules == len(__all__)
