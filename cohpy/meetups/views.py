from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader


def index(request):
    return render(request, 'meetups/index.html',)