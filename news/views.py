from datetime import date
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.
from django.views.generic import View, FormView, CreateView
from news.forms import NewsForm, NewsForm1, NewsForm2
from news.models import News


def news_index(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            _new = News(**form.cleaned_data)
            _new.save()
            return HttpResponseRedirect('/news/')

    else:
        form = NewsForm()

    today_news = News.objects.filter(updated_at__gte=date.today()).all()
    return render(request, 'news/index.html',
                  context={'news': today_news, 'form': form})


class NewsIndex0(View):
    def get(self, request):
        today_news = News.objects.filter(updated_at__gte=date.today()).all()
        form = NewsForm1()
        return render(request, 'news/index.html',
                      context={'news': today_news, 'form': form})

    def post(self, request):
        today_news = News.objects.filter(updated_at__gte=date.today()).all()
        form = NewsForm(self.request.POST)
        if form.is_valid():
            _new = News(title=self.request.POST["title"],
                        body=self.request.POST["body"])
            _new.save()
            form = NewsForm1()
        return render(self.request, 'news/index.html',
                      context={'news': today_news, 'form': form})


class NewsIndex1(FormView):
    form_class = NewsForm1
    template_name = 'news/index.html'
    model = News
    success_url = '/news/'

    def get_context_data(self, **kwargs):
        kwargs.update(
            news=News.objects.filter(updated_at__gte=date.today()).all())
        return super(NewsIndex1, self).get_context_data(**kwargs)

    def form_valid(self, form):
        form.save()
        return super(NewsIndex1, self).form_valid(form)


class NewsIndex2(CreateView):
    form_class = NewsForm2
    template_name = 'news/index.html'
    # model = News
    success_url = '/news/'

    def get_context_data(self, **kwargs):
        kwargs['news'] = News.objects.published().filter(
            updated_at__gte=date.today(), approved=True).all()
        return super(NewsIndex2, self).get_context_data(**kwargs)

    def get_initial(self):
        if self.request.user is not AnonymousUser:
            self.initial.update(author=self.request.user)
        return super(NewsIndex2, self).get_initial()
