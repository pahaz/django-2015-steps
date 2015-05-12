from django.contrib import admin

from django.contrib.admin import ModelAdmin
from news.models import News


@admin.register(News)
class NewsAdmin(ModelAdmin):
    list_display = ('title', 'author', )
    # list_filter = (,)
    search_fields = ('author', 'updated_at', )
    ordering = ('updated_at', 'author', )

    actions = ['approve', ]

    def approve(self, request, queryset):
        for news in queryset.filter(approved=False):
            news.approved = True
            news.save()
    approve.short_description = "В печать!"
