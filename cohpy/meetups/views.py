from django.shortcuts import render
from django.utils import timezone

from .models import Meetup

from info_blocks.views import latest_general_info, latest_dojo_info


def home_page(request):
    latest_meetups = Meetup.objects.filter(meetup_type__name='monthly').filter(date__gte=timezone.now()).order_by('date')
    return render(request, 'home.html', {
        'latest_meetups': latest_meetups,
        'general_info': latest_general_info,
        'dojo_info': latest_dojo_info,
    })

def index(request):
    meetups = Meetup.objects.filter(meetup_type__name='monthly').filter(date__lt=timezone.now()).order_by('-date')
    return render(request, 'meetups/index.html', {
        'meetups': meetups,
    })