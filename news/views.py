from django.http.response import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from news.models import News
from django.core.context_processors import csrf
from django.contrib import auth

def all(request):
    return render_to_response('all.html', {'news': News.objects.all(), 'username': auth.get_user(request).username})

def one(request, RSlug_Title):
    args = {}
    args.update(csrf(request))
    args['news'] = News.objects.get(news_slug=RSlug_Title)
    args['username'] = auth.get_user(request).username
    return render_to_response('one.html', args)