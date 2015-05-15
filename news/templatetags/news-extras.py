__author__ = 'Алексей'

from django.template import Library
import datetime

from news.models import News

register = Library()


@register.filter
def lower(value):
    return value.lower()


@register.simple_tag(takes_context=True)
def current_time(context, format_string):
    return datetime.datetime.now().strftime(format_string)


@register.assignment_tag(takes_context=True)
def last_news(context, count):
    all_news = News.objects.published()
    counts_news = len(all_news)
    if counts_news - count < 0:
        return []
    return all_news[counts_news - count: counts_news]
