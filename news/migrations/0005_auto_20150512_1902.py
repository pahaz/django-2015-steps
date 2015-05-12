# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_auto_20150512_0811'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 14, 2, 32, 393739, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='updated_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 12, 14, 2, 32, 393739, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
