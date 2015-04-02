__author__ = 'alexey-n'

import pytest_dependency
from hamcrest import assert_that, equal_to


def test_dependend_list():
    dependends_list = "testor1 or   (testand2 and test3)"
    expected_value = ["testor1", "testand2", "test3"]
    actual_value = pytest_dependency.get_dependends_list(dependends_list)
    assert_that(actual_value, equal_to(expected_value))
