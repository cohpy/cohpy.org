# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meetup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('date', models.DateTimeField()),
                ('location', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='MeetupType',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=64, blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=64)),
                ('date_added', models.DateTimeField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Talk',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('speakers', models.ManyToManyField(to='meetups.Speaker')),
            ],
            options={
                'ordering': ('title',),
            },
        ),
        migrations.AddField(
            model_name='meetup',
            name='meetup_type',
            field=models.ForeignKey(
                to='meetups.MeetupType',
                related_name='meetups',
                on_delete=models.deletion.CASCADE
            ),
        ),
        migrations.AddField(
            model_name='meetup',
            name='talks',
            field=models.ManyToManyField(to='meetups.Talk'),
        ),
    ]
