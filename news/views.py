from datetime import date
from django.shortcuts import render

# Create your views here.
from news.forms import NewsForm
from news.models import News


def news_index(request):
    today_news = News.objects.filter(updated_at__gte=date.today()).all()
    form = NewsForm()
    return render(request, 'news/index.html', context={'news': today_news, 'form': form})
