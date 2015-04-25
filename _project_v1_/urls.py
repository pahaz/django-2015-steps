from django.conf.urls import include, url
from django.contrib import admin
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


urlpatterns = [
    # Examples:
    # url(r'^$', '_project_v1_.views.home', name='home'),
    url(r'^news/', include('news.urls')),
    url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
]
