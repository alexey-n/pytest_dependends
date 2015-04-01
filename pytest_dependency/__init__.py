__author__ = 'alexey-n'

import pytest
import re

test_results = {}

def pytest_addoption(parser):
    group = parser.getgroup("general")
    group.addoption('--no_dependends',
           action="store_true", dest="no_dependends", default=False,
           help="Disable skip test if dependends not resolved")

def pytest_configure(config):
    enable_dependends = not(config.option.no_dependends)
    setattr(pytest, "enable_dependends", enable_dependends)
    if enable_dependends:
        config.addinivalue_line("markers",
            "dependends_on(name): ...")


def pytest_report_teststatus(report):
    if pytest.enable_dependends:
        test_method = report.location[2]
        if test_method in test_results:
            test_results[test_method] &= report.passed
        else:
            test_results[test_method] = report.passed

def pytest_runtest_setup(item):
    if pytest.enable_dependends:
        condition = get_item_condition(item, test_results)
        if condition != None:
            if not(eval_condition(condition, test_results)):
                pytest.skip("Test was skipped")

def get_item_condition(item, test_results):
    markers = item.keywords.__dict__['_markers']
    if "dependends_on" in markers:
        condition = markers["dependends_on"].args[0]
        dependends = get_dependends_list(condition)
        for dependend in dependends:
            if not(dependend in test_results):
                raise Exception("Have not resolved dependends")
        return condition

def eval_condition(condition, test_results):
    dependends = get_dependends_list(condition)
    try:
        for dependend in dependends:
            condition = condition.replace(dependend, str(test_results[dependend]))
        return eval(condition)
    except:
        raise Exception("Eval condition error('" + condition + "')")

def get_dependends_list(dependends):
    dependends = dependends.replace("(", " ").replace(")", " ").replace(" or ", " ").replace(" and ", " ")
    dependends = re.sub("\\s\\s+", " ", dependends)
    dependends = re.sub("^\\s*", "", dependends)
    dependends = re.sub("\\s*$", "", dependends)
    return dependends.split(" ")

