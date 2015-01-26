# -*- coding: utf-8 -*-
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from models import User,Achievement,UserAchievement
from forms import UserCreationForm

class UserAchievementInline(admin.TabularInline):
    model = UserAchievement
    extra = 1

class UserAdmin(UserAdmin):
    add_form = UserCreationForm


    list_display = ('email', 'username', 'is_admin',)
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': ('date_of_birth', 'first_name', 'last_name', 'avatar')}),
        ('Permissions', {'fields': ('is_admin',)}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'date_of_birth', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    inlines = [UserAchievementInline]

class AchievementAdmin(admin.ModelAdmin):
    list_display = ('__unicode__',)

admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
admin.site.register(Achievement, AchievementAdmin)