import pytest

from django.core.urlresolvers import resolve

from python_resources.views import index
from python_resources.pytest_fixtures import *

import pdb

@pytest.mark.django_db
def test_resources_page_returns_correct_html(resources_page_response):
    assert 'Book, Tutorial, Video' in resources_page_response
    assert 'Learn Python the Hard Way' in resources_page_response
    assert "Python&#39;s Class Development Toolkit" in resources_page_response
    assert 'The Clean Architecture in Python' in resources_page_response
    assert 'http://learnpythonthehardway.org/' in resources_page_response
    assert 'https://www.youtube.com/watch?v=HTLu2DFOdTg' in resources_page_response
    assert 'http://pyvideo.org/video/2840/the-clean-architecture-in-python' in resources_page_response