from __future__ import unicode_literals, print_function, generators, division
import logging

import os
import django


__author__ = 'pahaz'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_project_v1_.settings")
django.setup()

from django.contrib.auth.models import User
from django.core.files import File

# show SQL query
l = logging.getLogger('django.db.backends')
l.setLevel(logging.DEBUG)
l.addHandler(logging.StreamHandler())

from news.models import News, Tag, Attachment

# Delete all Tags
for m in Tag.objects.all():
    m.delete()

# Delete all News
News.objects.all().delete()

for x in range(2):
    t = Tag(name="Tag-" + str(x))
    t.save()

a = News(title="New feture in some soft", body="")
a.save()

t = Attachment(name="secret.txt", file=File(open('README.md')))

a.attachment_set.add(t)
t.save()

User.objects.all().delete()

u = User(username="pahaz", email='qwe@qwe.ru')
u.set_password('qwer')
u.is_active = True
u.is_superuser = True
u.is_staff = True
u.save()
