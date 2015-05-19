from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q
from django.utils.datetime_safe import datetime


class PublishedManager(models.Manager):
    def published(self):
        return self.filter(
            Q(publish_date__lte=datetime.now()) | Q(publish_date__isnull=True),
            Q(expiry_date__gte=datetime.now()) | Q(expiry_date__isnull=True),
        )


class Timable(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    publish_date = models.DateTimeField(
        "Published from",
        help_text="With Published chosen, won't be shown until this time",
        blank=True, null=True)
    expiry_date = models.DateTimeField(
        "Expires on",
        help_text="With Published chosen, won't be shown after this time",
        blank=True, null=True)

    objects = PublishedManager()

    class Meta:
        abstract = True


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class News(Timable, models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    body = models.TextField(verbose_name="Текст")
    author = models.ForeignKey(User, blank=True, null=True)  # TODO: fixit!
    tags = models.ManyToManyField(Tag, blank=True)
    approved = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        tags = ' / '.join([x.name for x in self.tags.all()])
        return "{0} // {1}".format(self.title, tags)


class Attachment(models.Model):
    news = models.ForeignKey(News)
    name = models.CharField(max_length=500)
    file = models.FileField(upload_to='attachments')

