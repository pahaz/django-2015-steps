from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import render
from news.views import news_index


urlpatterns = [
    url(r'^$', news_index),
]
