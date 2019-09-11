import pytest
from selenium import webdriver
import json
import os.path

fixture = None
target = None


def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture(scope="session")
def config(request):
    return load_config(request.config.getoption("--target"))


@pytest.fixture
def app():
    global fixture
    # browser = request.config.getoption("--browser")
    # basepage = request.config.getoption("--basepage")
    # if fixture is None or not fixture.is_valid():
    fixture = webdriver.Chrome(executable_path='/Users/admin/Downloads/chromedriver')
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--basepage", action="store", default="production")
    parser.addoption("--target", action="store", default="target.json")

