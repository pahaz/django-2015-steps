from django.contrib.auth.models import User
from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    body = models.TextField(verbose_name="Текст")
    author = models.ForeignKey(User, blank=True, null=True)  # TODO: fixit!
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField(Tag, blank=True)
    approved = models.BooleanField(default=False, blank=False)

    class Meta:
        verbose_name = "Статья"
        verbose_name_plural = "Статьи"

    def __str__(self):
        tags = ' / '.join([x.name for x in self.tags.all()])
        return "{0} // {1}".format(self.title, tags)
