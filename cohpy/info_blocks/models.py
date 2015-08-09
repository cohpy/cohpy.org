from django.db import models
from django.utils.safestring import mark_safe


class GeneralInfo(models.Model):
    info_text = models.TextField()
    date = models.DateTimeField()
    
    def safe_info_text(self):
        '''http://stackoverflow.com/questions/2080559/disable-html-escaping-in-djangos-textfield'''
        return mark_safe(self.info_text)
    
    def __str__(self):
        return self.date

    class Meta:
        ordering = ('date',)
        