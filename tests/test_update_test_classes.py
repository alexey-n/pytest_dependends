__author__ = 'alexey-n'

import pytest_dependency


def test_only_method():
    test_classes = {"Class1": []}
    pytest_dependency.update_test_classes("test_method", test_classes)
    assert {"Class1": []} == test_classes


def test_class_dependency():
    test_classes = {"Class1": []}
    pytest_dependency.update_test_classes("Class2.*", test_classes)
    assert {"Class1": []} == test_classes


def test_new_class_with_method():
    test_classes = {"Class1": []}
    pytest_dependency.update_test_classes("Class2.test_method", test_classes)
    assert {"Class1": [], "Class2": ["test_method"]} == test_classes


def test_update_class_with_method():
    test_classes = {"Class1": []}
    pytest_dependency.update_test_classes("Class1.test_method", test_classes)
    assert {"Class1": ["test_method"]} == test_classes
