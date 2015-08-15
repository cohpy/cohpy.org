from django.utils import timezone
import pytest
import pdb

from .functional_helper import *

# When the pythonista navigates to the root url
#  Then they should be on the home page
#  And they should see all upcoming meetups
#  And they should see links to past meetups

def test_navigates_to_home_page(browser):
    
    browser.get('http://localhost:8000/')
    assert 'COhPy | Home' in browser.title

    header_text = browser.find_element_by_tag_name('h1').text
    assert 'COhPy' in header_text

    subheader_text = browser.find_element_by_tag_name('h2').text
    assert "The Central Ohio Python User's Group" in subheader_text

    next_meetups = browser.find_elements_by_class_name('meetup')
    assert len(next_meetups) >= 1
   
    general_info_text = browser.find_element_by_class_name('general-info').text
    assert 'About Us' in general_info_text

    dojo_info_text = browser.find_element_by_class_name('dojo-info').text
    assert 'Dojo' in dojo_info_text
