from django.utils import timezone
import pytest

from info_blocks.models import GeneralInfo
from info_blocks.pytest_fixtures import *


@pytest.mark.django_db
def test_general_info_creation(general_info, get_date):
    assert isinstance(general_info, GeneralInfo)
    assert general_info.__str__() == get_date

@pytest.mark.django_db
def test_safe_info_text(general_info):
    assert str(type(general_info.safe_info_text())) == "<class 'django.utils.safestring.SafeText'>"

