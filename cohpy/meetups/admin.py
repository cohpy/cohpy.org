from django.contrib import admin

from .models import Speaker, Talk, Meetup, MeetupType


class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'date',)
    search_fields = ['title']

admin.site.register(Meetup, MeetupAdmin)

admin.site.register(Speaker)

admin.site.register(Talk)

admin.site.register(MeetupType)