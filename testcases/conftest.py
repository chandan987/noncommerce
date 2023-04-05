from selenium import webdriver
import pytest
from selenium.webdriver.edge.service import Service

@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome("C:\\drivers\\chrome\\chromedriver.exe")
        print("Launching Chrome Browser")

    elif browser == 'Edge':
        driver = webdriver.Edge("C:\\drivers\\msedgedriver.exe")
        print("Launching Edge Browser")

    else:
        driver = webdriver.Chrome("C:\\drivers\\chrome\\chromedriver.exe")
        print("Launching Edge Browser")

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

