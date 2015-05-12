# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    replaces = [('news', '0001_initial'), ('news', '0002_auto_20150414_1914'), ('news', '0003_auto_20150421_1823'), ('news', '0004_auto_20150512_0811'), ('news', '0005_auto_20150512_1902'), ('news', '0006_auto_20150512_1922'), ('news', '0007_auto_20150512_1933')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL)),
                ('body', models.TextField(default='Empty =/')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2015, 4, 14, 14, 14, 2, 830592, tzinfo=utc), auto_now_add=True)),
                ('updated_at', models.DateTimeField(default=datetime.datetime(2015, 4, 14, 14, 14, 8, 312446, tzinfo=utc), auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(to='news.Tag'),
        ),
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.AddField(
            model_name='news',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='news',
            name='body',
            field=models.TextField(verbose_name='Текст'),
        ),
        migrations.AlterField(
            model_name='news',
            name='tags',
            field=models.ManyToManyField(blank=True, to='news.Tag'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AddField(
            model_name='news',
            name='expiry_date',
            field=models.DateTimeField(blank=True, help_text="With Published chosen, won't be shown after this time", null=True, verbose_name='Expires on'),
        ),
        migrations.AddField(
            model_name='news',
            name='publish_date',
            field=models.DateTimeField(blank=True, help_text="With Published chosen, won't be shown until this time", null=True, verbose_name='Published from'),
        ),
    ]
