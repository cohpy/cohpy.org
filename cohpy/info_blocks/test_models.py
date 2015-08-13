from django.utils import timezone
import pytest

from info_blocks.pytest_fixtures import *


@pytest.mark.django_db
def test_general_info_creation(general_info_block1, earliest_date):
    assert isinstance(general_info_block1, GeneralInfoBlock)
    assert general_info_block1.__str__() == str(earliest_date)

@pytest.mark.django_db
def test_safe_general_info_text(general_info_block1):
    assert str(type(general_info_block1.safe_info_text())) == "<class 'django.utils.safestring.SafeText'>"

@pytest.mark.django_db
def test_dojo_info_creation(dojo_info_block1, earliest_date):
    assert isinstance(dojo_info_block1, DojoInfoBlock)
    assert dojo_info_block1.__str__() == str(earliest_date)

@pytest.mark.django_db
def test_safe_dojo_info_text(dojo_info_block1):
    assert str(type(dojo_info_block1.safe_info_text())) == "<class 'django.utils.safestring.SafeText'>"
