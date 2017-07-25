# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-23 01:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20170722_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proposal',
            name='proposal_rationale',
            field=models.FileField(help_text='this is the rationale of the proposal', upload_to='proposals/'),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='proposal_technical_support',
            field=models.FileField(help_text='this is the technical addendum of the proposal', upload_to='proposals/'),
        ),
    ]