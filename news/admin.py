# -*- coding: utf-8 -*-
from django.contrib import admin
from news.models import News

class NewsAdmin(admin.ModelAdmin):
   fields = ['news_title', 'news_preview', 'news_text', 'news_date', 'news_slug', 'news_img', 'news_descreption', 'news_keywords']
   list_filter = ['news_date']
   list_display = ['news_title', 'news_date']
   prepopulated_fields = {'news_slug': ('news_title', )}

admin.site.register(News,NewsAdmin)