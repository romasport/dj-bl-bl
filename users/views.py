# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, redirect
from django.contrib import auth
from forms import UserCreationForm
from django.core.context_processors import csrf
from django.shortcuts import get_object_or_404
from models import User

def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        email = request.POST.get('email', '')
        password = request.POST.get('pass', '')
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "Пользователь не найден"
            return render_to_response('users/login.html',args)
    else:
        return render_to_response('users/login.html',args)

def logout(request):
    auth.logout(request)
    return redirect('/')

def registr(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm
    if request.POST:
        new_user = UserCreationForm(request.POST)
        if new_user.is_valid():
            new_user.save()
            new_user = auth.authenticate(email=new_user.cleaned_data['email'], password=new_user.cleaned_data['password2'])
            auth.login(request, new_user)
            return redirect('/')
        else:
            args['form'] = new_user
            args['error_messages'] = 'Ошибка регистрации. Повторите попытку.'
            return render_to_response('users/registration.html',args)
    else:
        return render_to_response('users/registration.html',args)



def profile(request, username):
    args = {}
    args['username'] = auth.get_user(request).username
    args['user'] = get_object_or_404(User, username=username)
    return render_to_response('users/user.html',args)