from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import render
from news.views import news_index, NewsIndex0, NewsIndex1, NewsIndex2


urlpatterns = [
    # url(r'^$', news_index),
    # url(r'^$', NewsIndex0.as_view()),
    # url(r'^$', NewsIndex1.as_view()),
    url(r'^$', NewsIndex2.as_view(), name="news_index"),
]
