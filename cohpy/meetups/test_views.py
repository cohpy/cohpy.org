import pytest


from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.test import Client

from meetups.views import home_page
from meetups.pytest_fixtures import *



def test_root_url_resolves_to_home_page():
    found = resolve('/')
    assert found.func == home_page

@pytest.mark.django_db
def test_home_page_returns_correct_html(meetup1, meetup2, meetup3, earliest_date, middle_date, latest_date):    
    client = Client()
    response = client.get('/').content.decode()
    print(response)
    assert '<h3>Test meetup3</h3>' in response
    assert '<p>July 30, 2015, 6 p.m.</p>' in response
    assert '<p>Test meetup3 location</p>' in response
    assert '<p>Test meetup3 description</p>' in response
    assert '<h4>Test talk</h4>' in response
    assert '<h5>Test User</h5>' in response
    assert '<p>Test talk description</p>' in response
