from django import forms
from django.forms import CharField, ChoiceField, HiddenInput
from news.models import News

__author__ = 'Nikita'


class NewsForm(forms.Form):
    title = CharField(max_length=200)
    body = CharField(max_length=200)


class NewsForm1(forms.ModelForm):

    class Meta:
        model = News
        fields = ('title', 'body', )


class NewsForm2(forms.ModelForm):

    class Meta:
        model = News
        fields = ('title', 'body', 'author', )
        widgets = {'author': HiddenInput}
