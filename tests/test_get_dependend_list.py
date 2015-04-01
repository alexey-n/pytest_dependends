__author__ = 'alexey-n'

import pytest_dependency

def test_dependend_list():
    assert ['testor1', 'testand2', 'test3'] == \
           pytest_dependency.get_dependends_list("testor1 or   (testand2 and test3)")