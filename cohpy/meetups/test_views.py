from django.core.urlresolvers import resolve

import pytest

from meetups.views import home_page


def test_root_url_resolves_to_home_page():
    found = resolve('/')
    assert found.func == home_page
