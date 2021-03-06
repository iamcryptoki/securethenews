# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 00:57
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20161108_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contentpage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock()), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('quote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock()), ('source', wagtail.wagtailcore.blocks.CharBlock()), ('link', wagtail.wagtailcore.blocks.URLBlock())))))),
        ),
    ]
