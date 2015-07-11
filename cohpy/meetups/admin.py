from django.contrib import admin

from meetups.models import Speaker, Talk, Meetup


class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'date',)
    search_fields = ['title']

admin.site.register(Meetup, MeetupAdmin)