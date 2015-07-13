from django.utils import timezone
import pytest

from meetups.models import Speaker, Talk, Meetup


# For reference: https://pytest.org/latest/fixture.html#fixture
# http://www.pydanny.com/pytest-no-boilerplate-testing-2.html
@pytest.fixture # setup and teardown
def speaker():
    kwargs = {
        'name': 'Test User',
        'date_added': timezone.now()
    }
    return Speaker.objects.create(**kwargs)

@pytest.mark.django_db
def test_speaker_creation(speaker):
    s = speaker

    assert isinstance(s, Speaker)
    assert s.__str__() ==  'Test User'    

