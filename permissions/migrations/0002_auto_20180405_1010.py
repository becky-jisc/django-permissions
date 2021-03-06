# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-05 10:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='content_types',
            field=models.ManyToManyField(blank=True, related_name='content_types', to='contenttypes.ContentType', verbose_name='Content Types'),
        ),
        migrations.AlterField(
            model_name='role',
            name='global_permissions',
            field=models.ManyToManyField(blank=True, related_name='roles_globals', to='permissions.Permission', verbose_name='Global permissions'),
        ),
    ]
