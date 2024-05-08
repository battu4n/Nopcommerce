import pytest
from selenium import webdriver


@pytest.fixture
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("launching chromebrowser")
    elif browser == 'firefox':
        driver = webdriver.Firefox()
        print("launching firefox browser")
    else:
        driver = webdriver.Chrome()
        print("launching chromebrowser")

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")  # parser method we call as hook


# to geenrate pytest HTML report
# it is hook for adding environment info to HTML report
"""def pytest_configure(config):
    config._metadata['Proect Name']='nop Commerce'
    config._metadata['Module Name']='Customers'
    config._metadata['Tester Name'] = 'Narendra'"""


# it is hook to delete/modify environment info into html report
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("pluggins", None)


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")
