# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-18 17:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='extended_description',
            field=models.TextField(blank=True, help_text='expand some more if needed'),
        ),
    ]
