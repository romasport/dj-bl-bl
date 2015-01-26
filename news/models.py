# -*- coding: utf-8 -*-
from django.db import models

class News(models.Model):
    class Meta:
        db_table = "news"

    news_title = models.CharField(max_length=200)
    news_preview = models.TextField("Текст превью для левой колонки", blank=True)
    news_text = models.TextField()
    news_date = models.DateTimeField()
    news_img = models.ImageField("Изображение", upload_to='newslimg', help_text='Картинка новости', blank=True)
    news_slug = models.SlugField('Имя для ссылки', unique = True)
    news_descreption = models.TextField(blank=True)
    news_keywords = models.TextField(help_text='Ключевые слова через запятую', blank=True)