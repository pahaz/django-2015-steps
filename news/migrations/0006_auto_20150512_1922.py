# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20150512_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='expiry_date',
            field=models.DateTimeField(help_text="With Published chosen, won't be shown after this time", blank=True, verbose_name='Expires on', null=True),
        ),
        migrations.AddField(
            model_name='news',
            name='publish_date',
            field=models.DateTimeField(help_text="With Published chosen, won't be shown until this time", blank=True, verbose_name='Published from', null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='expiry_date',
            field=models.DateTimeField(help_text="With Published chosen, won't be shown after this time", blank=True, verbose_name='Expires on', null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='publish_date',
            field=models.DateTimeField(help_text="With Published chosen, won't be shown until this time", blank=True, verbose_name='Published from', null=True),
        ),
    ]
