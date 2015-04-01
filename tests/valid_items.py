__author__ = 'alexey-n'
import pytest

results = ["test1 or test2 and (test3 or  test4)", None, None, "TestClass.test_c", "TestClass.*"]

@pytest.mark.dependends_on("test1 or test2 and (test3 or  test4)")
def test_a():
    assert True

def test_b():
    assert True

class TestClass:
    def test_c(self):
        assert True

@pytest.mark.dependends_on("TestClass.test_c")
def test_d():
    assert True

@pytest.mark.dependends_on("TestClass.*")
def test_e():
    assert True