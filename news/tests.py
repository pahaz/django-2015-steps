from django.core.urlresolvers import reverse
from django.test import TestCase, override_settings
from news.forms import NewsForm
from news.models import News

DEFAULT_TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
    }
]
DEFAULT_INSTALLED_APPS = [
    'django.contrib.humanize',
    'news',
]


def make_news(title="News", body="Body"):
    return News(title=title, body=body)


class TestView(TestCase):

    @override_settings(
        ROOT_URLCONF='news.urls',
        TEMPLATES=DEFAULT_TEMPLATES,
        INSTALLED_APPS=DEFAULT_INSTALLED_APPS
    )
    def test_news_index_view_has_last_one_approved_news(self):
        NEWS_INDEX_URL = reverse('news_index')
        NEW_NEWS_TITLE = "LBfLWIFBIUEBlawiubkGBlueg"

        new_news = make_news(title=NEW_NEWS_TITLE)
        new_news.approved = True
        new_news.save()

        r = self.client.get(NEWS_INDEX_URL)
        print(r.context)
        print(r.content)
        self.assertContains(r, NEW_NEWS_TITLE, status_code=200)


class TestNewsForm(TestCase):
    def test_can_not_write_body_spam(self):
        f = NewsForm({'title': 'qwe', 'body': 'spam'})
        f.is_valid()
        self.assertIn(u"Уберите `spam` из сообщения.", f.errors['body'])