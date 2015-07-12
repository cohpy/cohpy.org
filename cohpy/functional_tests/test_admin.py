import pytest
from selenium import webdriver


# For reference: https://pytest.org/latest/fixture.html#fixture
@pytest.fixture # setup and teardown
def ff_browser(request):
    browser = webdriver.Firefox()
    browser.get('http://localhost:8000/admin')
    def fin():
        print ('Closing FireFox browser.')
        browser.close()
    request.addfinalizer(fin)
    return browser

def test_navigates_to_admin_login(ff_browser):
    assert 'Log in | Django site admin' in ff_browser.title

