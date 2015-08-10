from django.utils import timezone
import pytest

from python_resources.models import PythonResource, Category
from python_resources.pytest_fixtures import *


@pytest.mark.django_db
def test_category_creation(category):
    assert isinstance(category, Category)
    assert category.__str__() ==  'Tutorial'

@pytest.mark.django_db
def test_python_resource_creation(python_resource):
    assert isinstance(python_resource, PythonResource)
    assert python_resource.__str__() ==  'Learn Python the Hard Way'
