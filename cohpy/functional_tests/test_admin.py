from .functional_helper import *


def test_navigates_to_admin_login(browser):

    browser.get('http://localhost:8000/admin')
    assert 'Log in | Django site admin' in browser.title
