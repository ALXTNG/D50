# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-23 18:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_auto_20170723_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='proposals',
            field=models.ManyToManyField(help_text='this is for the proposals', related_name='profile_of_proposal', to='home.Proposal'),
        ),
    ]
