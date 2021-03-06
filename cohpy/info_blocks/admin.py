from django.contrib import admin

from .models import GeneralInfoBlock, DojoInfoBlock


class GeneralInfoBlockAdmin(admin.ModelAdmin):
    list_display = ('info_text',)
    search_fields = ['info_text']

admin.site.register(GeneralInfoBlock, GeneralInfoBlockAdmin)


class DojoInfoBlockAdmin(admin.ModelAdmin):
    list_display = ('info_text',)
    search_fields = ['info_text']

admin.site.register(DojoInfoBlock, DojoInfoBlockAdmin)