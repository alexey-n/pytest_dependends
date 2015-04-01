__author__ = 'alexey-n'

import pytest_dependency


def test_new_result():
    test_results = {"test_method1": False}
    pytest_dependency.update_test_results('test_method2', False, test_results)
    assert not(test_results['test_method2'])


def test_update_result_false():
    test_results = {"test_method1": True}
    pytest_dependency.update_test_results('test_method1', False, test_results)
    assert not(test_results['test_method1'])


def test_update_result_true():
    test_results = {"test_method1": True}
    pytest_dependency.update_test_results('test_method1', True, test_results)
    assert test_results['test_method1']
