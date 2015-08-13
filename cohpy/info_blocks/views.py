from .models import GeneralInfoBlock, DojoInfoBlock

from django.utils.safestring import mark_safe

def latest_general_info():
    return mark_safe(GeneralInfoBlock.objects.latest('date_added').safe_info_text())

def latest_dojo_info():
    return mark_safe(DojoInfoBlock.objects.latest('date_added').safe_info_text())