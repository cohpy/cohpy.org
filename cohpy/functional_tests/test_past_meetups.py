from django.utils import timezone
import pytest

from .functional_helper import *

# When the pythonista navigates to the meetups url
#  Then they should be on the past meetups page
#  And they should see past meetups

def test_navigates_to_past_meetups_page(browser):
    
    browser.get('http://localhost:8000/meetups')
    assert 'COhPy | Past Meetups' in browser.title

    header_text = browser.find_element_by_tag_name('h1').text
    assert 'COhPy' in header_text

    subheader_text = browser.find_element_by_tag_name('h3').text
    assert "The Central Ohio Python User's Group: Past Meetups" in subheader_text

    # there is a section that contains the last meetup
    past_meetups = browser.find_elements_by_class_name('meetup')
    assert len(past_meetups) > 3
    for meetup in past_meetups:
        assert 'Monthly Meeting' in meetup.text
