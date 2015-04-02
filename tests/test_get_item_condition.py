__author__ = 'alexey-n'

import pytest_dependency
import pytest
from . import valid_items


def test_valid_item(testdir):
    test_results = {"test1": True, "test2": True, "test3": True, "test4": True, "TestClass.test_c": True}
    items = testdir.getitems(valid_items)
    for item in items:
        index = items.index(item)
        assert valid_items.results[index] == pytest_dependency.get_item_condition(items[index], test_results,
                                                                                  {"TestClass": ["test_c"]})


def test_invalid_item(testdir):
    test_results = {"test1": True, "test2": True, "test3": True}
    items = testdir.getitems(valid_items)
    with pytest.raises(pytest_dependency.SyntaxError) as exception:
        pytest_dependency.get_item_condition(items[0], test_results, {})
    assert "Have not resolved dependends: test4" == str(exception.value)


def test_invalid_class(testdir):
    test_results = {"test1": True, "test2": True, "test3": True, "test4": True, "TestClass.test_c": True}
    items = testdir.getitems(valid_items)
    with pytest.raises(pytest_dependency.SyntaxError) as exception:
        pytest_dependency.get_item_condition(items[4], test_results, {})
    assert "Have not resolved class dependends: TestClass" == str(exception.value)
