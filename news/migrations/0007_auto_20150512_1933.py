# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_auto_20150512_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='expiry_date',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='publish_date',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='updated_at',
        ),
    ]
