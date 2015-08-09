from django.utils import timezone
import pytest

from meetups.models import Speaker, Talk, MeetupType, Meetup


# For reference: https://pytest.org/latest/fixture.html#fixture
# http://www.pydanny.com/pytest-no-boilerplate-testing-2.html

@pytest.fixture
def speaker():
    kwargs = {
        'name': 'Test User',
        'date_added': timezone.now()
    }
    return Speaker.objects.create(**kwargs)

@pytest.fixture
def talk(speaker):
    kwargs = {
        'title': 'Test talk',
        'description': 'Test talk description',
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
def meetup(talk, meetup_type):
    kwargs = {
        'title': 'Test meetup',
        'description': '<p>Test meetup description</p>',
        'date': timezone.now(),
        'meetup_type': meetup_type,
        'location': '<p>Test meetup location</p>'
    }
    m = Meetup.objects.create(**kwargs)
    m.talks.add(talk)
    return m