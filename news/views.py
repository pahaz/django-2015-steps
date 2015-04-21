from datetime import date
from django.shortcuts import render

# Create your views here.
from django.views.generic import View, FormView
from news.forms import NewsForm, NewsForm1
from news.models import News


def news_index(request):
    if request.method == "GET":
        today_news = News.objects.filter(updated_at__gte=date.today()).all()
        form = NewsForm()
        return render(request, 'news/index.html', context={'news': today_news, 'form': form})
    elif request.method == "POST":
        today_news = News.objects.filter(updated_at__gte=date.today()).all()
        form = NewsForm(request.POST)
        if form.is_valid():
            _new = News(title=request.POST["title"], body=request.POST["body"])
            _new.save()
            form = NewsForm()
        return render(request, 'news/index.html', context={'news': today_news, 'form': form})


class NewsIndex0(View):

    def get(self, request):
        today_news = News.objects.filter(updated_at__gte=date.today()).all()
        form = NewsForm1()
        return render(request, 'news/index.html', context={'news': today_news, 'form': form})

    def post(self, request):
        today_news = News.objects.filter(updated_at__gte=date.today()).all()
        form = NewsForm(self.request.POST)
        if form.is_valid():
            _new = News(title=self.request.POST["title"], body=self.request.POST["body"])
            _new.save()
            form = NewsForm1()
        return render(self.request, 'news/index.html', context={'news': today_news, 'form': form})


class NewsIndex1(FormView):
    form_class = NewsForm1
    template_name = 'news/index.html'
    model = News
    success_url = '/news/'

    def get_context_data(self, **kwargs):
        kwargs.update(news=News.objects.filter(updated_at__gte=date.today()).all())
        return super(NewsIndex1, self).get_context_data(**kwargs)

    def form_valid(self, form):
        self.object = form.save()
        return super(NewsIndex1, self).form_valid(form)

