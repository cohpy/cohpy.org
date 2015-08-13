from django.utils import timezone

import pytest

from info_blocks.models import GeneralInfoBlock, DojoInfoBlock

# For reference: https://pytest.org/latest/fixture.html#fixture
# http://www.pydanny.com/pytest-no-boilerplate-testing-2.html

@pytest.fixture
def earliest_date():
    return '2015-06-01 18:00'

@pytest.fixture
def middle_date():
    return '2015-06-29 18:00'

@pytest.fixture
def latest_date():
    return '2015-07-30 18:00'

@pytest.fixture
def general_info_block1(earliest_date):
    kwargs = {
        'info_text': "<h1>Welcome to the Central Ohio Python User's Group1</h1>\
                      <p>We really love Python and want to share it with the world!</p>",
        'date_added': earliest_date
    }
    return GeneralInfoBlock.objects.create(**kwargs)

@pytest.fixture
def dojo_info_block1(earliest_date):
    kwargs = {
        'info_text': "<h1>Friday Night Dojo1</h1>\
                      <p>Come hang out with us and work on your Python projects!</p>",
        'date_added': earliest_date
    }
    return DojoInfoBlock.objects.create(**kwargs)

@pytest.fixture
def general_info_block2(middle_date):
    kwargs = {
        'info_text': "<h1>Welcome to the Central Ohio Python User's Group2</h1>\
                      <p>We really love Python and want to share it with the world!</p>",
        'date_added': middle_date
    }
    return GeneralInfoBlock.objects.create(**kwargs)

@pytest.fixture
def dojo_info_block2(middle_date):
    kwargs = {
        'info_text': "<h1>Friday Night Dojo2</h1>\
                      <p>Come hang out with us and work on your Python projects!</p>",
        'date_added': middle_date
    }
    return DojoInfoBlock.objects.create(**kwargs)

@pytest.fixture
def general_info_block3(latest_date):
    kwargs = {
        'info_text': "<h1>Welcome to the Central Ohio Python User's Group3</h1>\
                      <p>We really love Python and want to share it with the world!</p>",
        'date_added': latest_date
    }
    return GeneralInfoBlock.objects.create(**kwargs)

@pytest.fixture
def dojo_info_block3(latest_date):
    kwargs = {
        'info_text': "<h1>Friday Night Dojo3</h1>\
                      <p>Come hang out with us and work on your Python projects!</p>",
        'date_added': latest_date
    }
    return DojoInfoBlock.objects.create(**kwargs)
