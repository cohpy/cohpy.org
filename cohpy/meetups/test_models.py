from django.utils import timezone
import pytest

from meetups.pytest_fixtures import *


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
def test_meetup_creation(meetup1):
    assert isinstance(meetup1, Meetup)
    assert meetup1.__str__() ==  'Test meetup1'    

@pytest.mark.django_db
def test_meetup_safe_description(meetup1):
    assert str(type(meetup1.safe_description())) == "<class 'django.utils.safestring.SafeText'>"

@pytest.mark.django_db
def test_meetup_safe_location(meetup1):
    assert str(type(meetup1.safe_location())) == "<class 'django.utils.safestring.SafeText'>"
