from django.utils import timezone
import pytest

from python_resources.models import PythonResource, Category


# For reference: https://pytest.org/latest/fixture.html#fixture
# http://www.pydanny.com/pytest-no-boilerplate-testing-2.html

@pytest.fixture
def category():
    kwargs = {
        'name': 'Tutorial',
    }
    return Category.objects.create(**kwargs)


@pytest.fixture
def python_resource(category):
    kwargs = {
        'title': 'Learn Python the Hard Way',
        'description': "An awesome way to learn Python, and it's free",
        'link': 'http://learnpythonthehardway.org/',
        'date_added': timezone.now(),
    }
    r = PythonResource.objects.create(**kwargs)
    r.categories.add(category)
    return r