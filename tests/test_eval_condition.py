__author__ = 'alexey-n'

import pytest_dependency
import pytest

def test_valid_condition():
    assert pytest_dependency.eval_condition("test1 or (test2   and (test3 or test4) )",
                                            {"test1":True, "test2":False, "test3":True, "test4":False})

def test_invalid_condition():
    with pytest.raises(Exception) as exception:
        pytest_dependency.eval_condition("test1 + \"a\"", {"test1":True})
    print exception.value
    assert "Eval condition error('True + \"a\"')" == str(exception.value)

