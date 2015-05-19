from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.shortcuts import render
from news.views import NewsIndex2


def index(request):
    return render(request, 'index.html')


urlpatterns = [
    # Examples:
    # url(r'^$', '_project_v1_.views.home', name='home'),
    url(r'^$', include('news.urls', namespace='news')),
    # url(r'^$', index),
    url(r'^admin/', include(admin.site.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
