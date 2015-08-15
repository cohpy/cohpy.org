# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0002_auto_20150810_2329'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetup',
            name='posted_to_meetup',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='meetup',
            name='talks',
            field=models.ManyToManyField(to='meetups.Talk', blank=True),
        ),
    ]
