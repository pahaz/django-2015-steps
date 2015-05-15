from django import forms
from django.forms import CharField, ChoiceField, HiddenInput
from news.models import News

__authors__ = ('Nikita', 'pahaz')


class NewsForm(forms.Form):
    title = CharField(max_length=200)
    body = CharField(max_length=200)

    def clean_body(self):
        body = self.cleaned_data['body']
        if 'spam' in body:
            raise forms.ValidationError(u"Уберите `spam` из сообщения.")

        return body


class NewsForm1(forms.ModelForm):
    class Meta:
        model = News
        fields = ('title', 'body', )


class NewsForm2(forms.ModelForm):

    class Meta:
        model = News
        fields = ('title', 'body', 'author', )
        widgets = {'author': HiddenInput}
