from django.test import Client
from django.utils import timezone

from datetime import timedelta
import pytest

from meetups.models import Speaker, Talk, MeetupType, Meetup


# For reference: https://pytest.org/latest/fixture.html#fixture
# http://www.pydanny.com/pytest-no-boilerplate-testing-2.html

@pytest.fixture
def now_date():
    return timezone.now() 

@pytest.fixture
def earliest_date(now_date):
    return (now_date + timedelta(days=-40))

@pytest.fixture
def middle_date(now_date):
    return (now_date + timedelta(days=-10))

@pytest.fixture
def latest_date(now_date):
    return (now_date + timedelta(days=10))

@pytest.fixture
def speaker(earliest_date):
    kwargs = {
        'name': 'Test User',
        'date_added': earliest_date
    }
    return Speaker.objects.create(**kwargs)

@pytest.fixture
def talk(speaker):
    kwargs = {
        'title': 'Test talk',
        'description': '<p>Test talk description</p>',
    }
    t = Talk.objects.create(**kwargs)
    t.speakers.add(speaker)
    return t

@pytest.fixture
def meetup_type():
    t = MeetupType(name='monthly')
    t.save()
    return t

@pytest.fixture
def meetup1(talk, meetup_type, earliest_date):
    kwargs = {
        'title': 'Test meetup1',
        'description': '<p>Test meetup1 description</p>',
        'date': earliest_date,
        'meetup_type': meetup_type,
        'location': '<p>Test meetup1 location</p>'
    }
    m = Meetup.objects.create(**kwargs)
    m.talks.add(talk)
    return m

@pytest.fixture
def meetup2(talk, meetup_type, middle_date):
    kwargs = {
        'title': 'Test meetup2',
        'description': '<p>Test meetup2 description</p>',
        'date': middle_date,
        'meetup_type': meetup_type,
        'location': '<p>Test meetup2 location</p>'
    }
    m = Meetup.objects.create(**kwargs)
    m.talks.add(talk)
    return m

@pytest.fixture
def meetup3(talk, meetup_type, latest_date):
    kwargs = {
        'title': 'Test meetup3',
        'description': '<p>Test meetup3 description</p>',
        'date': latest_date,
        'meetup_type': meetup_type,
        'location': '<p>Test meetup3 location</p>'
    }
    m = Meetup.objects.create(**kwargs)
    m.talks.add(talk)
    return m

@pytest.fixture
def homepage_response(meetup1, meetup2, meetup3, earliest_date, middle_date, latest_date):
    client = Client()
    return client.get('/').content.decode()

@pytest.fixture
def past_meetups_page_response(meetup1, meetup2, meetup3, earliest_date, middle_date, latest_date):
    client = Client()
    return client.get('/meetups/').content.decode()
