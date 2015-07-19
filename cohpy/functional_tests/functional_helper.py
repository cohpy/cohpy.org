import environ
import os
import pytest
from selenium import webdriver


BROWSER = os.environ.get('BROWSER')

# For reference: https://pytest.org/latest/fixture.html#fixture
# http://www.pydanny.com/pytest-no-boilerplate-testing-2.html
@pytest.fixture # setup and teardown
def browser(request):
    if BROWSER == 'HEADLESS':
        browser = webdriver.PhantomJS()
    else:
        browser = webdriver.Firefox()
    browser.implicitly_wait(10)
    
    @request.addfinalizer
    def teardown():
        browser.close()
    
    return browser