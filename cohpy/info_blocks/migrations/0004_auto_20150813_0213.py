# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_blocks', '0003_auto_20150810_0222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dojoinfoblock',
            options={'ordering': ('date_added',)},
        ),
        migrations.AlterModelOptions(
            name='generalinfoblock',
            options={'ordering': ('date_added',)},
        ),
        migrations.RenameField(
            model_name='dojoinfoblock',
            old_name='date',
            new_name='date_added',
        ),
        migrations.RenameField(
            model_name='generalinfoblock',
            old_name='date',
            new_name='date_added',
        ),
    ]
