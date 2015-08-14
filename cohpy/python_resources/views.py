from django.shortcuts import render

from .models import PythonResource, Category


def index(request):
    python_resources = PythonResource.objects.all()
    return render(request, 'python_resources/index.html', {
        'resources': python_resources,
    })