__author__ = 'alexey-n'

import pytest_dependency
import pytest


def test_valid_condition():
    assert pytest_dependency.eval_condition("test1 or (test2   and (test3 or test4) )",
                                            {"test1": True, "test2": False, "test3": True, "test4": False}, {})


def test_valid_condition_with_class_true():
    assert pytest_dependency.eval_condition("TestClass.*",
                                            {"test1": True, "TestClass.test5": True, "TestClass.test6": True},
                                            {"TestClass": ["test5", "test6"]})


def test_valid_condition_with_class_false():
    assert not(pytest_dependency.eval_condition("TestClass.*",
                                                {"test1": True, "TestClass.test5": True, "TestClass.test6": False},
                                                {"TestClass": ["test5", "test6"]}))


def test_valid_condition_with_class():
    assert pytest_dependency.eval_condition("TestClass.test5",
                                            {"test1": True, "TestClass.test5": True, "TestClass.test6": False},
                                            {"TestClass": ["test5", "test6"]})


def test_invalid_condition():
    with pytest.raises(Exception) as exception:
        pytest_dependency.eval_condition("test1 + \"a\"", {"test1": True}, {})
    print exception.value
    assert "Eval condition error('True + \"a\"')" == str(exception.value)
