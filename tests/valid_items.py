__author__ = 'alexey-n'
import pytest

results = ["test1 or test2 and (test3 or  test4)", None]

@pytest.mark.dependends_on("test1 or test2 and (test3 or  test4)")
def test_a():
    assert True

def test_b():
    assert True