__author__ = 'alexey-n'

import pytest_dependency
import pytest
from hamcrest import assert_that, equal_to


def test_valid_condition():
    actual_value = pytest_dependency.eval_condition("test1 or (test2   and (test3 or test4) )",
                                                    {"test1": True, "test2": False, "test3": True, "test4": False}, {})
    assert_that(actual_value, equal_to(True))


def test_valid_condition_with_class_true():
    actual_value = pytest_dependency.eval_condition("TestClass.*",
                                                    {"test1": True, "TestClass.test5": True, "TestClass.test6": True},
                                                    {"TestClass": ["test5", "test6"]})
    assert_that(actual_value, equal_to(True))


def test_valid_condition_with_class_false():
    actual_value = pytest_dependency.eval_condition("TestClass.*",
                                                    {"test1": True, "TestClass.test5": True, "TestClass.test6": False},
                                                    {"TestClass": ["test5", "test6"]})
    assert_that(actual_value, equal_to(False))


def test_valid_condition_with_class():
    actual_value = pytest_dependency.eval_condition("TestClass.test5",
                                                    {"test1": True, "TestClass.test5": True, "TestClass.test6": False},
                                                    {"TestClass": ["test5", "test6"]})
    assert_that(actual_value, equal_to(True))


def test_invalid_condition():
    with pytest.raises(pytest_dependency.EvalError) as exception:
        pytest_dependency.eval_condition("test1 + \"a\"", {"test1": True}, {})
    assert_that(str(exception.value), equal_to("Eval condition error('True + \"a\"')"))
