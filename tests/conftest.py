import pytest
from pages.home.navigaion_page import NavigationPage
from selenium import webdriver
from base.webdriverfactory import WebDriverFactory
from pages.home.login_page import LoginPage



@pytest.fixture(scope='class')
def one_time_setUp(request, browser):
    print("before all tests")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()
    lp = LoginPage(driver)
    lp.login('lutsiv96@mailinator.com', '123123123')

    if request.cls is not None:
            request.cls.driver = driver
    yield driver
    driver.quit()
    print("Once tearDown")

@pytest.fixture()
def setUp():

    print('running setUp')
    yield
    print("Running tearDown")



def pytest_addoption(parser):
    parser.addoption('--browser')
    parser.addoption('--osType', help='Type of operating system')

@pytest.fixture(scope='session')
def browser(request):
    return request.config.getoption('--browser')

@pytest.fixture(scope='session')
def osType(request):
    return request.config.getoption('--osType')