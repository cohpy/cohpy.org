import pytest
from selenium import webdriver


# For reference: https://pytest.org/latest/fixture.html#fixture
# http://www.pydanny.com/pytest-no-boilerplate-testing-2.html
@pytest.fixture # setup and teardown
def ff_browser(request):
    browser = webdriver.Firefox()
    browser.get('http://localhost:8000/admin')
    
    @request.addfinalizer
    def teardown():
        browser.close()
    
    return browser

def test_navigates_to_admin_login(ff_browser):
    assert 'Log in | Django site admin' in ff_browser.title
