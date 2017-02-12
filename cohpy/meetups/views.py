from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta

from .models import Meetup

from info_blocks.views import latest_general_info, latest_dojo_info

# Since meetups list a start time, this is the number of hours after the
# start time to still display the meetup as a "current" and not past meetup.
HOURS_SLACK=4

def home_page(request):
    upcoming_meetups = Meetup.objects.filter(meetup_type__name='monthly').filter(date__gte=timezone.now() - timedelta(hours=HOURS_SLACK)).order_by('date')
    last_meetup = Meetup.objects.filter(meetup_type__name='monthly').latest('date')
    return render(request, 'home.html', {
        'upcoming_meetups': upcoming_meetups,
        'last_meetup': last_meetup,
        'general_info': latest_general_info,
        'dojo_info': latest_dojo_info,
    })

def index(request):
    meetups = Meetup.objects.filter(meetup_type__name='monthly').filter(date__lt=timezone.now() - timedelta(hours=HOURS_SLACK)).order_by('-date')
    return render(request, 'meetups/index.html', {
        'meetups': meetups,
    })
