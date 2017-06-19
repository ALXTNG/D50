# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-18 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_post_extended_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='urllink',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, help_text='add image that will be displayed', max_length=500, null=True, upload_to='./'),
        ),
    ]