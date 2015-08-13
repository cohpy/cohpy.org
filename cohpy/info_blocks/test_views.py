import pytest

from .models import GeneralInfoBlock, DojoInfoBlock

from info_blocks.views import latest_general_info, latest_dojo_info
from info_blocks.pytest_fixtures import *

import pdb


@pytest.mark.django_db
def test_latest_general_info_returns_correct_html(latest_general_info):
    assert "<h1>Welcome to the Central Ohio Python User's Group3</h1>" in latest_general_info
    

