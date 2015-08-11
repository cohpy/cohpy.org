from django.shortcuts import get_object_or_404, render

# from django.http import HttpResponse
# from django.template import RequestContext, loader

from .models import Meetup


def home_page(request):
    latest_meetup = Meetup.objects.filter(meetup_type__name='monthly').latest('date')
    talks = latest_meetup.talks
    return render(request, 'home.html', {
        'latest_meetup': latest_meetup,
        'talks': talks,
    })

def index(request):
    return render(request, 'meetups/index.html',)