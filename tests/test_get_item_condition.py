__author__ = 'alexey-n'

import pytest_dependency
import pytest
from . import valid_items

def test_valid_item(testdir):
    test_results = {"test1":True, "test2":True, "test3":True, "test4":True}
    items = testdir.getitems(valid_items)
    for item in items:
        index = items.index(item)
        assert valid_items.results[index] == pytest_dependency.get_item_condition(items[index], test_results)

def test_invalid_item(testdir):
    test_results = {"test1":True, "test2":True, "test3":True}
    items = testdir.getitems(valid_items)
    with pytest.raises(Exception) as exception:
        pytest_dependency.get_item_condition(items[0], test_results)
    assert "Have not resolved dependends" == str(exception.value)