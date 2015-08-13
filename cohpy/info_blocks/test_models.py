from django.utils import timezone
import pytest

from info_blocks.models import GeneralInfoBlock, DojoInfoBlock
from info_blocks.pytest_fixtures import *


@pytest.mark.django_db
def test_general_info_creation(general_info_block, get_date):
    assert isinstance(general_info_block, GeneralInfoBlock)
    assert general_info_block.__str__() == str(get_date)

@pytest.mark.django_db
def test_safe_general_info_text(general_info_block):
    assert str(type(general_info_block.safe_info_text())) == "<class 'django.utils.safestring.SafeText'>"

@pytest.mark.django_db
def test_dojo_info_creation(dojo_info_block, get_date):
    assert isinstance(dojo_info_block, DojoInfoBlock)
    assert dojo_info_block.__str__() == str(get_date)

@pytest.mark.django_db
def test_safe_dojo_info_text(dojo_info_block):
    assert str(type(dojo_info_block.safe_info_text())) == "<class 'django.utils.safestring.SafeText'>"
