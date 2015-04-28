from __future__ import unicode_literals, print_function, generators, division
import os
import logging

import django
from django.template import Context, Template
__author__ = 'pahaz'

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "_project_v1_.settings")
django.setup()

# # show SQL query
# # l = logging.getLogger('django.db.backends')
# # l.setLevel(logging.DEBUG)
# # l.addHandler(logging.StreamHandler())
#
# from news.models import News, Tag
#
# # Delete all Tags
# for m in Tag.objects.all():
#     m.delete()
#
# # Delete all News
# News.objects.all().delete()
#
# for x in range(2):
#     t = Tag(name="Tag-" + str(x))
#     t.save()
#
# t = Tag(name="Tag-hot")
# t.save()
#
# for x in range(15):
#     n = News(title="News-" + str(x), body='NoBody', author_id=1)
#     n.save()
#     n.tags = [t]
#     n.tags.add(Tag.objects.get(name="Tag-" + str(x % 2)))
#
# print([str(x) for x in News.objects.all()])
#
# t0 = Tag.objects.get(name="Tag-0")
# t1 = Tag.objects.get(name="Tag-1")
#
# print(list(t0.news_set.all()))
# print(list(t1.news_set.all()))
# print(list(t.news_set.all()))
# print(list(News.objects.filter(tags__name="Tag-0")))

class Person():
    def __init__(self):
        self.first_name = 'DJ'

p = Person()

t = Template('My name is {{name}}')
c = Context({'name': p.first_name})

print(t.render(c))