from django.contrib import admin

from .models import GeneralInfo


class GeneralInfoAdmin(admin.ModelAdmin):
    list_display = ('date',)
    search_fields = ['info_text']

admin.site.register(GeneralInfo, GeneralInfoAdmin)