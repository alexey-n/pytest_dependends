__author__ = 'alexey-n'

import pytest
import re


def pytest_addoption(parser):
    group = parser.getgroup("general")
    group.addoption('--no_dependends',
                    action="store_true", dest="no_dependends", default=False,
                    help="Disable skip test if dependends not resolved")


def pytest_configure(config):
    enable_dependends = not(config.option.no_dependends)
    setattr(pytest, "enable_dependends", enable_dependends)
    setattr(pytest, "test_results", {})
    setattr(pytest, "test_classes", {})
    if enable_dependends:
        config.addinivalue_line("markers", "dependends_on(name): ...")


def pytest_runtest_makereport(report):
    if pytest.enable_dependends:
        test_method = report.location[2]
        update_test_classes(test_method, pytest.test_classes)
        update_test_results(test_method, report.passed, pytest.test_results)


def update_test_classes(test_method, test_classes):
    if "." in test_method:
        (class_name, method_name) = test_method.split(".")
        if method_name != "*":
            if class_name in pytest.test_classes:
                test_classes[class_name].append(method_name)
            else:
                test_classes[class_name] = [method_name]


def update_test_results(test_method, is_passed, test_results):
    if test_method in pytest.test_results:
        test_results[test_method] &= is_passed
    else:
        test_results[test_method] = is_passed


def pytest_runtest_setup(item):
    if pytest.enable_dependends:
        condition = get_item_condition(item, pytest.test_results, pytest.test_classes)
        if condition is not None:
            if not(eval_condition(condition, pytest.test_results, pytest.test_classes)):
                pytest.skip("Test was skipped")


def get_item_condition(item, test_results, test_classes):
    markers = item.keywords.__dict__['_markers']
    if "dependends_on" in markers:
        condition = markers["dependends_on"].args[0]
        dependends = get_dependends_list(condition)
        for dependend in dependends:
            if ".*" in dependend:
                class_name = dependend.replace(".*", "")
                if not(class_name in test_classes):
                    raise Exception("Have not resolved class dependends: " + class_name)
            else:
                if not(dependend in test_results):
                    raise Exception("Have not resolved dependends: " + dependend)
        return condition


def eval_condition(condition, test_results, test_classes):
    dependends = get_dependends_list(condition)
    try:
        for dependend in dependends:
            if ".*" in dependend:
                class_name = dependend.replace(".*", "")
                class_result = True
                for method in test_classes[class_name]:
                    class_result &= test_results[class_name + "." + method]
                condition = condition.replace(dependend, str(class_result))
            else:
                condition = condition.replace(dependend, str(test_results[dependend]))
        return eval(condition)
    except:
        raise Exception("Eval condition error('" + condition + "')")


def get_dependends_list(dependends):
    dependends = dependends.replace("(", " ").replace(")", " ").replace(" or ", " ").replace(" and ", " ")
    dependends = re.sub("\\s\\s+", " ", dependends)
    dependends = re.sub("(^\\s*)|(\\s*$)", "", dependends)
    return dependends.split(" ")
