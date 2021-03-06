import pytest

from django.core.urlresolvers import resolve

from meetups.views import home_page
from meetups.pytest_fixtures import *

import pdb

def date_string(date_object):
    return date_object.strftime('%B %-d, %Y, %-I:%M')

def test_root_url_resolves_to_home_page():
    found = resolve('/')
    assert found.func == home_page

@pytest.mark.django_db
def test_menu_contains_correct_links(homepage_response):
    assert '<a href="/meetups">Past Meetups</a>' in homepage_response
    assert '<a href="http://www.pyohio.org/">PyOhio</a>' in homepage_response
    assert '<a href="https://mail.python.org/pipermail/centraloh/">Mailing List Archives</a>' in homepage_response
    assert '<a href="/resources">Resources</a>' in homepage_response
    assert '<a href="/admin">Login</a>' in homepage_response

@pytest.mark.django_db
def test_home_page_returns_correct_html(homepage_response, latest_date):    
    assert '<h3>Test meetup3</h3>' in homepage_response
    assert date_string(latest_date) in homepage_response
    assert '<p>Test meetup3 location</p>' in homepage_response
    assert '<p>Test meetup3 description</p>' in homepage_response
    assert '<h4>Test talk</h4>' in homepage_response
    assert '<h5>Test User</h5>' in homepage_response
    assert '<p>Test talk description</p>' in homepage_response

@pytest.mark.django_db
def test_no_future_meetups_returns_correct_html_on_home_page(homepage_response_without_upcoming_meetup, earliest_date, middle_date):
    assert '<h3>Test meetup2</h3>' in homepage_response_without_upcoming_meetup
    assert date_string(middle_date) in homepage_response_without_upcoming_meetup
    assert '<p>Test meetup2 location</p>' in homepage_response_without_upcoming_meetup
    assert '<p>Test meetup2 description</p>' in homepage_response_without_upcoming_meetup
    assert '<h4>Test talk</h4>' in homepage_response_without_upcoming_meetup
    assert '<h5>Test User</h5>' in homepage_response_without_upcoming_meetup
    assert '<p>Test talk description</p>' in homepage_response_without_upcoming_meetup

    assert '<h3>Test meetup1</h3>' not in homepage_response_without_upcoming_meetup
    assert date_string(earliest_date) not in homepage_response_without_upcoming_meetup
    assert '<p>Test meetup1 location</p>' not in homepage_response_without_upcoming_meetup
    assert '<p>Test meetup1 description</p>' not in homepage_response_without_upcoming_meetup

def test_meetups_url_resolves_to_past_meetups_page():
    found = resolve('/meetups/')
    assert found.view_name == 'index'

@pytest.mark.django_db
def test_past_meetups_page_returns_correct_html(past_meetups_page_response, earliest_date, middle_date, latest_date):
    assert '<h3>Test meetup1</h3>' in past_meetups_page_response
    assert date_string(earliest_date) in past_meetups_page_response
    assert '<p>Test meetup1 location</p>' in past_meetups_page_response
    assert '<p>Test meetup1 description</p>' in past_meetups_page_response
    assert '<h4>Test talk</h4>' in past_meetups_page_response
    assert '<h5>Test User</h5>' in past_meetups_page_response
    assert '<p>Test talk description</p>' in past_meetups_page_response
    assert '<h3>Test meetup2</h3>' in past_meetups_page_response
    assert date_string(middle_date) in past_meetups_page_response
    assert '<p>Test meetup2 location</p>' in past_meetups_page_response
    assert '<p>Test meetup2 description</p>' in past_meetups_page_response

    assert '<h3>Test meetup3</h3>' not in past_meetups_page_response
    assert date_string(latest_date) not in past_meetups_page_response
    assert '<p>Test meetup3 location</p>' not in past_meetups_page_response
    assert '<p>Test meetup3 description</p>' not in past_meetups_page_response
