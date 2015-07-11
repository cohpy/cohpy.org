from django.db import models
from django.utils.safestring import mark_safe


class Meetup(models.Model):
    title = models.CharField()
    description = models.TextField(blank=True)
    date = models.DateTimeField()
    location = models.CharField(max_length=200)    
    talks = models.ManyToManyField(Talk)
    
    def safe_description(self):
        '''http://stackoverflow.com/questions/2080559/disable-html-escaping-in-djangos-textfield''' 
        return mark_safe(self.description)    
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('date',)


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
    meetup = models.ForeignKey(Meetup)
    speakers = models.ManyToManyField(Speaker)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('title',)

