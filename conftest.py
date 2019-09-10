from pytest import fixture

from selenium import webdriver


@fixture(scope='function')
def chrome_browser():
    browser = webdriver.Chrome(executable_path='/Users/admin/Downloads/chromedriver')
    return browser
