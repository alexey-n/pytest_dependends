__author__ = 'alexey-n'

import pytest_dependency
from hamcrest import assert_that, equal_to


def test_new_result():
    test_results = {"test_method1": False}
    pytest_dependency.update_test_results('test_method2', False, test_results)
    assert_that(test_results['test_method2'], equal_to(False))


def test_update_result_false():
    test_results = {"test_method1": True}
    pytest_dependency.update_test_results('test_method1', False, test_results)
    assert_that(test_results['test_method1'], equal_to(False))


def test_update_result_true():
    test_results = {"test_method1": True}
    pytest_dependency.update_test_results('test_method1', True, test_results)
    assert_that(test_results['test_method1'], equal_to(True))
