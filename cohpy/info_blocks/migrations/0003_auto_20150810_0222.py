# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_blocks', '0002_dojoinfo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DojoInfo',
            new_name='DojoInfoBlock',
        ),
        migrations.RenameModel(
            old_name='GeneralInfo',
            new_name='GeneralInfoBlock',
        ),
    ]
