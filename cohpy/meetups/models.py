from django.db import models
from django.utils.safestring import mark_safe


class Speaker(models.Model):
    name = models.CharField(max_length=64)
    date_added = models.DateTimeField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Talk(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    speakers = models.ManyToManyField(Speaker)

    def safe_description(self):
        '''http://stackoverflow.com/questions/2080559/disable-html-escaping-in-djangos-textfield''' 
        return mark_safe(self.description)

    def comma_separated_speakers(self):
        speaker_list = []
        speakers = Speaker.objects.filter(talk__pk=self.id)
        for speaker in speakers:
            speaker_list.append(speaker.name)
        return ', '.join(speaker_list)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)


class MeetupType(models.Model):
    name = models.CharField(max_length=64, default='monthly')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Meetup(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    location = models.TextField(blank=True)    
    talks = models.ManyToManyField(Talk, blank=True)
    meetup_type = models.ForeignKey(
        MeetupType,
        related_name='meetups',
        on_delete=models.CASCADE,
    )
    posted_to_meetup = models.BooleanField(default=False)
    
    def safe_description(self):
        return mark_safe(self.description)

    def safe_location(self):
        return mark_safe(self.location)  
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('date',)

