from .functional_helper import *

# When the pythonista navigates to the root url
#  Then they should be on the home page
#  And they should see all upcoming meetups
#  And they should see links to past meetups

def test_navigates_to_home_page(browser):
    browser.get('http://localhost:8000/')
    assert 'COhPy | Home' in browser.title