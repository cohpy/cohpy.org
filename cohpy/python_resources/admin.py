from django.contrib import admin

from .models import PythonResource, Category


class PythonResourceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ['categories']

admin.site.register(PythonResource, PythonResourceAdmin)

admin.site.register(Category)
