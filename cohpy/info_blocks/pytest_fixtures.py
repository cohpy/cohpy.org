from django.utils import timezone
import pytest

from info_blocks.models import GeneralInfo

# For reference: https://pytest.org/latest/fixture.html#fixture
# http://www.pydanny.com/pytest-no-boilerplate-testing-2.html

@pytest.fixture
def get_date():
    return timezone.now()

@pytest.fixture
def general_info(get_date):
    kwargs = {
        'info_text': "<h1>Welcome to the Central Ohio Python User's Group</h1>\
                      <p>We really love Python and want to share it with the world!</p>",
        'date': get_date
    }
    return GeneralInfo.objects.create(**kwargs)
