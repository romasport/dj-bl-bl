# -*- coding: utf-8 -*-
from django.contrib import admin
from perl.models import Perl, Comments

# Register your models here.
class PerlInline(admin.StackedInline):
    model = Comments
    fields = ['comments_text', 'comments_pub']
    extra = 2

class PerlAdmin(admin.ModelAdmin):
   fields = ['perl_title', 'perl_text', 'perl_img', 'perl_date', 'perl_slug', 'perl_descreption', 'perl_keywords']
   inlines = [PerlInline]
   list_filter = ['perl_date']
   list_display = ['perl_title', 'perl_date']
   prepopulated_fields = {'perl_slug': ('perl_title', )}

class CommentAdmin(admin.ModelAdmin):
   fields = ['comments_text', 'comments_pub']
   list_display = ['comments_text', 'comments_date']

admin.site.register(Perl, PerlAdmin)

admin.site.register(Comments,CommentAdmin)