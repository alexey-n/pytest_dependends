__author__ = 'alexey-n'

import pytest_dependency
import pytest
from . import valid_items
from hamcrest import assert_that, equal_to


def test_valid_item(testdir):
    test_results = {"test1": True, "test2": True, "test3": True, "test4": True, "TestClass.test_c": True}
    expected_values = ["test1 or test2 and (test3 or  test4)", None, None, "TestClass.test_c", "TestClass.*"]
    items = testdir.getitems(valid_items)
    actual_values = []
    for item in items:
        actual_values.append(pytest_dependency.get_item_condition(item, test_results,
                                                                  {"TestClass": ["test_c"]}))
    assert_that(actual_values, equal_to(expected_values))


def test_invalid_item(testdir):
    test_results = {"test1": True, "test2": True, "test3": True}
    items = testdir.getitems(valid_items)
    with pytest.raises(SyntaxError) as exception:
        pytest_dependency.get_item_condition(items[0], test_results, {})
    assert_that(str(exception.value), equal_to("Have not resolved dependends: test4"))


def test_invalid_class(testdir):
    test_results = {"test1": True, "test2": True, "test3": True, "test4": True, "TestClass.test_c": True}
    items = testdir.getitems(valid_items)
    with pytest.raises(SyntaxError) as exception:
        pytest_dependency.get_item_condition(items[4], test_results, {})
    assert_that(str(exception.value), equal_to("Have not resolved class dependends: TestClass"))
