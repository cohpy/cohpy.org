from django.test import Client
from django.utils import timezone
import pytest

from python_resources.models import PythonResource, Category


# For reference: https://pytest.org/latest/fixture.html#fixture
# http://www.pydanny.com/pytest-no-boilerplate-testing-2.html

@pytest.fixture
def category1():
    kwargs = {
        'name': 'Tutorial',
    }
    return Category.objects.create(**kwargs)

@pytest.fixture
def category2():
    kwargs = {
        'name': 'Book',
    }
    return Category.objects.create(**kwargs)

@pytest.fixture
def category3():
    kwargs = {
        'name': 'Video',
    }
    return Category.objects.create(**kwargs)


@pytest.fixture
def python_resource1(category1, category2, category3):
    kwargs = {
        'title': 'Learn Python the Hard Way',
        'description': "An awesome way to learn Python, and it's free",
        'link': 'http://learnpythonthehardway.org/',
        'date_added': timezone.now(),
    }
    r = PythonResource.objects.create(**kwargs)
    r.categories.add(category1)
    r.categories.add(category2)
    r.categories.add(category3)
    return r

@pytest.fixture
def python_resource2(category3):
    kwargs = {
        'title': "Python's Class Development Toolkit",
        'description': "A talk by Raymond Hettinger, Published on Mar 20, 2013.",
        'link': 'https://www.youtube.com/watch?v=HTLu2DFOdTg',
        'date_added': timezone.now(),
    }
    r = PythonResource.objects.create(**kwargs)
    r.categories.add(category3)
    return r

@pytest.fixture
def python_resource3(category3):
    kwargs = {
        'title': 'The Clean Architecture in Python',
        'description': "Come learn about how “Clean Architecture” applies in Python,",
        'link': 'http://pyvideo.org/video/2840/the-clean-architecture-in-python',
        'date_added': timezone.now(),
    }
    r = PythonResource.objects.create(**kwargs)
    r.categories.add(category3)
    return r

@pytest.fixture
def resources_page_response(python_resource1, python_resource2, python_resource3):
    client = Client()
    return client.get('/resources/').content.decode()
