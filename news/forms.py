from django import forms
from django.forms import CharField

__author__ = 'Nikita'


class NewsForm(forms.Form):
    title = CharField(max_length=200)
    body = CharField(max_length=200)
