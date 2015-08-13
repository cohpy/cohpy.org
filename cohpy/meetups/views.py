from django.shortcuts import get_object_or_404, render

from .models import Meetup
from info_blocks.views import *
import pdb


def home_page(request):
    latest_meetup = Meetup.objects.filter(meetup_type__name='monthly').latest('date')
    talks = latest_meetup.talks
    return render(request, 'home.html', {
        'latest_meetup': latest_meetup,
        'general_info': latest_general_info,
        'dojo_info': latest_dojo_info,
    })

def index(request):
    meetups = Meetup.objects.order_by('-date')[1:]
    return render(request, 'meetups/index.html', {
        'meetups': meetups,
    })