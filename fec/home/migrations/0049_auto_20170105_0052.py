# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-05 00:52
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0048_auto_20170105_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourcepage',
            name='intro',
            field=wagtail.wagtailcore.fields.StreamField((('body', wagtail.wagtailcore.blocks.RichTextBlock()),), null=True),
        ),
    ]
