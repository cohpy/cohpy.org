import pytest

from info_blocks.pytest_fixtures import *


@pytest.mark.django_db
def test_latest_general_info_returns_correct_html(latest_general_info_block):
    assert "<h1>Welcome to the Central Ohio Python User's Group3</h1>" in latest_general_info_block
    assert "<h1>Welcome to the Central Ohio Python User's Group1</h1>" not in latest_general_info_block
    assert "<h1>Welcome to the Central Ohio Python User's Group2</h1>" not in latest_general_info_block

@pytest.mark.django_db
def test_latest_dojo_info_returns_correct_html(latest_dojo_info_block):
    assert "<h1>Friday Night Dojo3</h1>" in latest_dojo_info_block
    assert "<h1>Friday Night Dojo1</h1>" not in latest_dojo_info_block
    assert "<h1>Friday Night Dojo2</h1>" not in latest_dojo_info_block

