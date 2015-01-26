# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

class Perl(models.Model):
    class Meta:
        db_table = "perl"

    perl_title = models.CharField(max_length=200)
    perl_text = models.TextField()
    perl_img = models.ImageField("Изображение альбома", upload_to='perlimg', help_text='Картинка перла', blank=True)
    perl_date = models.DateTimeField()
    perl_likes = models.IntegerField(default=0)
    perl_dontlike = models.IntegerField(default=0)
    perl_slug = models.SlugField('Имя для ссылки', unique = True)
    perl_descreption = models.TextField(blank=True)
    perl_keywords = models.TextField(help_text='Ключевые слова через запятую', blank=True)

class Comments(models.Model):
    class Meta:
        db_table = "comments"

    comments_text = models.TextField(verbose_name="Текст коментария")
    comments_perl = models.ForeignKey(Perl)
    comments_userid = models.IntegerField()
    comments_pub = models.BooleanField(default=True)
    comments_date = models.DateTimeField()
    comments_plus = models.IntegerField(default=0)
    comments_minus = models.IntegerField(default=0)
    comments_pearent = models.IntegerField(default=0)

class PerlPlusMinus(models.Model):
    class Meta:
        db_table = "perlplusminus"

    perl_id = models.IntegerField()
    user_id = models.IntegerField()
    golos = models.SmallIntegerField()

class PerlCommentsPlusMinus(models.Model):
    class Meta:
        db_table = "perlcommentsplusminus"

    comments_id = models.IntegerField()
    user_id = models.IntegerField()
    golos = models.SmallIntegerField()