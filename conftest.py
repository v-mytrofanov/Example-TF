import json
import pytest
import os.path
import re
from fixture.db import DbFixture
from fixture.application import Application
from testrail_config import TestRailHelper
from data.tests_for_testrail import cases

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as filejson:
            target = json.load(filejson)
    return target


@pytest.fixture(scope="module")
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
        fixture.open_home_page()
        fixture.session.login(email=web_config["email"], password=web_config["password"])
    return fixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))['db']
    dbfixture = DbFixture(host=db_config['host'], name=db_config['name'], user=db_config['user'],
                          password=db_config['password'])
    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)
    return dbfixture


@pytest.fixture(scope="module", autouse=True)
def stop(request):
        def fin():
            fixture.destroy()
        request.addfinalizer(fin)
        return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--target", action="store", default="target.json")


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    # specify run_id in testrail
    run_id = 1
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()
    mode = 0
    if rep.when == "call":
        if rep.outcome == 'failed':
            mode = 5
        if rep.outcome == 'passed':
            mode = 1
        if rep.outcome == 'skipped':
            mode = 4
    if mode > 0:
        prog = re.compile('^[^\[]+')
        result = prog.match(item.name)
        try:
            if result:
                print(result)
        except Exception as other:
            print("Test failed because Jenkins doesn't want to work with TestRail", other)
        case_id = cases[result.group(0)]
        testR = TestRailHelper(run_id)
        testR.update_testrail(case_id, mode, " ")
        print(rep)
        print(item)
        print(case_id)


@pytest.fixture(scope="function")
def signup(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
        fixture.open_home_page()
    return fixture


@pytest.fixture(scope="function")
def signup_invite(request):
    global fixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))['web_invite']
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=web_config['baseUrl'])
        fixture.open_home_page()
    return fixture


@pytest.fixture(scope="function")
def stop_2(request):
        def fin():
            fixture.destroy()
        request.addfinalizer(fin)
        return fixture
