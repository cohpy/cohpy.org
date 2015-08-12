import pytest

from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from meetups.views import home_page
from meetups.pytest_fixtures import *

import pdb

def test_root_url_resolves_to_home_page():
    found = resolve('/')
    assert found.func == home_page

@pytest.mark.django_db
def test_home_page_returns_correct_html(homepage_response):    
    assert '<h3>Test meetup3</h3>' in homepage_response
    assert '<p>July 30, 2015, 6 p.m.</p>' in homepage_response
    assert '<p>Test meetup3 location</p>' in homepage_response
    assert '<p>Test meetup3 description</p>' in homepage_response
    assert '<h4>Test talk</h4>' in homepage_response
    assert '<h5>Test User</h5>' in homepage_response
    assert '<p>Test talk description</p>' in homepage_response

def test_meetups_url_resolves_to_past_meetups_page():
    found = resolve('/meetups/')
    # pdb.set_trace()
    assert found.view_name == 'index'

@pytest.mark.django_db
def test_past_meetups_page_returns_correct_html(past_meetups_page_response):
    assert '<h3>Test meetup1</h3>' in past_meetups_page_response
    assert '<p>June 1, 2015, 6 p.m.</p>' in past_meetups_page_response
    assert '<p>Test meetup1 location</p>' in past_meetups_page_response
    assert '<p>Test meetup1 description</p>' in past_meetups_page_response
    assert '<h4>Test talk</h4>' in past_meetups_page_response
    assert '<h5>Test User</h5>' in past_meetups_page_response
    assert '<p>Test talk description</p>' in past_meetups_page_response
    assert '<h3>Test meetup2</h3>' in past_meetups_page_response
    assert '<p>June 29, 2015, 6 p.m.</p>' in past_meetups_page_response
    assert '<p>Test meetup2 location</p>' in past_meetups_page_response
    assert '<p>Test meetup2 description</p>' in past_meetups_page_response

    assert '<h3>Test meetup3</h3>' not in past_meetups_page_response
    assert '<p>July 30, 2015, 6 p.m.</p>' not in past_meetups_page_response
    assert '<p>Test meetup3 location</p>' not in past_meetups_page_response
    assert '<p>Test meetup3 description</p>' not in past_meetups_page_response

