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
        driver = webdriver.PhantomJS()
    else:
        driver = webdriver.Firefox()

    driver.get('http://localhost:8000/admin')
    
    @request.addfinalizer
    def teardown():
        driver.close()
    
    return driver

def test_navigates_to_admin_login(browser):
    assert 'Log in | Django site admin' in browser.title
