# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info_blocks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DojoInfo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('info_text', models.TextField()),
                ('date', models.DateTimeField()),
            ],
            options={
                'ordering': ('date',),
            },
        ),
    ]
