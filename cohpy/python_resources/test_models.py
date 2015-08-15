from django.utils import timezone
import pytest

from python_resources.models import PythonResource, Category
from python_resources.pytest_fixtures import *


@pytest.mark.django_db
def test_category_creation(category1):
    assert isinstance(category1, Category)
    assert category1.__str__() ==  'Tutorial'

@pytest.mark.django_db
def test_python_resource_creation(python_resource1):
    assert isinstance(python_resource1, PythonResource)
    assert python_resource1.__str__() ==  'Learn Python the Hard Way'
    assert python_resource1.comma_separated_categories() == 'Book, Tutorial, Video'
