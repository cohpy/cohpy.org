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

@pytest.mark.django_db
def test_speaker_creation(speaker):
    assert isinstance(speaker, Speaker)
    assert speaker.__str__() ==  'Test User'

@pytest.mark.django_db
def test_talk_creation(talk):
    assert isinstance(talk, Talk)
    assert talk.__str__() ==  'Test talk'

@pytest.mark.django_db
def test_meetup_type_creation(meetup_type):
    assert isinstance(meetup_type, MeetupType)
    assert meetup_type.__str__() ==  'monthly'

@pytest.mark.django_db
def test_talk_safe_description(talk):
    assert str(type(talk.safe_description())) == "<class 'django.utils.safestring.SafeText'>"

@pytest.mark.django_db
def test_meetup_creation(meetup):
    assert isinstance(meetup, Meetup)
    assert meetup.__str__() ==  'Test meetup'    

@pytest.mark.django_db
def test_meetup_safe_description(meetup):
    assert str(type(meetup.safe_description())) == "<class 'django.utils.safestring.SafeText'>"

@pytest.mark.django_db
def test_meetup_safe_location(meetup):
    assert str(type(meetup.safe_location())) == "<class 'django.utils.safestring.SafeText'>"
