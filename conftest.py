import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ec or fr")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption('browser_name')
    user_language = request.config.getoption("language")
    browser_name = 'chrome'
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language}) 
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
        yield browser    
    elif browser_name == "firefox":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language}) 
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
        yield browser    
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")            
    time.sleep(10)
    print("\nquit browser..")
    browser.quit()