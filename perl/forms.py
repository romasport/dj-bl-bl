# -*- coding: utf-8 -*-
from django.forms import ModelForm
from models import Comments
from django import forms

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']
    comments_text = forms.CharField(label='',
                                    widget=forms.Textarea(attrs={'placeholder': 'Введите текст сообщения...'}))