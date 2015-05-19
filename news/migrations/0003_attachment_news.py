# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150519_1903'),
    ]

    operations = [
        migrations.AddField(
            model_name='attachment',
            name='news',
            field=models.ForeignKey(to='news.News', default=1),
            preserve_default=False,
        ),
    ]
