__author__ = 'alexey-n'

import pytest_dependency
from hamcrest import assert_that, equal_to


def test_only_method():
    test_classes = {"Class1": []}
    pytest_dependency.update_test_classes("test_method", test_classes)
    assert_that(test_classes, equal_to({"Class1": []}))


def test_class_dependency():
    test_classes = {"Class1": []}
    pytest_dependency.update_test_classes("Class2.*", test_classes)
    assert_that(test_classes, equal_to({"Class1": []}))


def test_new_class_with_method():
    test_classes = {"Class1": []}
    pytest_dependency.update_test_classes("Class2.test_method", test_classes)
    assert_that(test_classes, equal_to({"Class1": [], "Class2": ["test_method"]}))


def test_update_class_with_method():
    test_classes = {"Class1": []}
    pytest_dependency.update_test_classes("Class1.test_method", test_classes)
    assert_that(test_classes, equal_to({"Class1": ["test_method"]}))
