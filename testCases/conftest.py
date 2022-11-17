import datetime
import os.path

import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from datetime import datetime


@pytest.fixture()
def setup(browser):
    if browser=='edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        print('launching edge browser...')

    elif browser=='firefox':
        driver = webdriver.Firefox(GeckoDriverManager().install())
        print('launching firefox browser...')
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print('launching chrome...')
    return driver

def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture()
def browser(request):
    return request.config.getoption('--browser')

########## Pytest HTML Report #######

# Hook for adding environtment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name']='nop commerce'
    config._metadata['Module Name']='login'
    config._metadata['Tester']='Saamim'

#Hook for delete /Modify environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)

#specifuing report folder location and save report with time stamp

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath=os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%Y %H-%M-%S")+".html"











