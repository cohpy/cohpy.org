from django.utils import timezone

from .functional_helper import *

# When the pythonista navigates to the meetups url
#  Then they should be on the past meetups page
#  And they should see past meetups

def test_navigates_to_resources_page(browser):
    
    browser.get('http://localhost:8000/resources')
    assert 'COhPy | Resources' in browser.title

    header_text = browser.find_element_by_tag_name('h1').text
    assert 'COhPy' in header_text

    subheader_text = browser.find_element_by_tag_name('h3').text
    assert "The Central Ohio Python User's Group: Resources" in subheader_text

    # there is a section that contains the last meetup
    resource_rows = browser.find_elements_by_css_selector('table tbody tr')
    assert len(resource_rows) > 4