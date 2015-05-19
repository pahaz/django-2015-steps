from django.contrib import admin

from django.contrib.admin import ModelAdmin
from news.models import News, Attachment


class AttachmentInline(admin.TabularInline):
    model = Attachment


@admin.register(News)
class NewsAdmin(ModelAdmin):
    list_display = ('title', 'author', 'body')
    # list_filter = (,)
    date_hierarchy = 'updated_at'
    search_fields = ('author', 'updated_at', )
    ordering = ('updated_at', 'author', )
    inlines = [AttachmentInline]
    list_editable = ('body', )
    actions = ['approve', ]

    def approve(self, request, queryset):
        for news in queryset.filter(approved=False):
            news.approved = True
            news.save()
    approve.short_description = "В печать!"
