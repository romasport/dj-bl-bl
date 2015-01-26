# -*- coding: utf-8 -*-
from django.http.response import HttpResponse, Http404
from django.shortcuts import render_to_response, redirect
from perl.models import Perl, Comments, PerlPlusMinus,PerlCommentsPlusMinus
from perl.forms import CommentForm
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

import datetime


def perls(request):
    perls_list = Perl.objects.all().order_by('-perl_date')
    paginator = Paginator(perls_list, 10)

    page = request.GET.get('page')
    try:
        perls = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        perls = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        perls = paginator.page(paginator.num_pages)

    args = {}
    args.update(csrf(request))
    args['username'] = auth.get_user(request).username
    args['perls'] = perls

    return render_to_response('perls.html', args)

def perl(request, RSlug_Title):
    comment_form = CommentForm
    args = {}
    all_comments = arr_comments = {}
    i = 0
    args.update(csrf(request))
    args['perl'] = get_object_or_404(Perl.objects,perl_slug=RSlug_Title)
    all_comments = Comments.objects.filter(comments_perl=args['perl'].id, comments_pub=True)
    for coment in all_comments:
        user_name = User.objects.get(id=coment.comments_userid).username
        arr_comments.update( {
            i : {
            'id': coment.id,
            'comments_text': coment.comments_text,
            'comments_date': coment.comments_date,
            'comments_username': user_name,
            'comments_plus': coment.comments_plus,
            'comments_minus': coment.comments_minus,
            'comments_reyting': coment.comments_plus-coment.comments_minus,
            }
        })
        i = i + 1
    args['comments'] = arr_comments
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('perl.html', args)


def last_comments(request):
    return render_to_response('last_comments.html', {'comments': Comments.objects.all()[:2]})

def plus(request):
    if request.method == 'POST':
        id = request.POST['id']
        user_id = auth.get_user(request).id
        if user_id:
            try:
                PerlPlusMinus.objects.get(perl_id=id, user_id=user_id)
                return HttpResponse("Вы уже голосовали", status=403)
            except ObjectDoesNotExist:
                try:
                    perle = Perl.objects.get(id=id)
                    perle.perl_likes += 1
                    perle.save()
                    obj = PerlPlusMinus(perl_id=id, user_id=user_id, golos=1)
                    obj.save()
                except ObjectDoesNotExist:
                    raise Http404
                return HttpResponse("ok", status=200)
        else:
            return HttpResponse("Вы не авторизованы", status=403)

def minus(request):
    if request.method == 'POST':
        id = request.POST['id']
        user_id = auth.get_user(request).id
        if user_id:
            try:
                PerlPlusMinus.objects.get(perl_id=id, user_id=user_id)
                return HttpResponse("Вы уже голосовали", status=403)
            except ObjectDoesNotExist:
                try:
                    perle = Perl.objects.get(id=id)
                    perle.perl_dontlike += 1
                    perle.save()
                    obj = PerlPlusMinus(perl_id=id, user_id=user_id, golos=-1)
                    obj.save()
                except ObjectDoesNotExist:
                    raise Http404
                return HttpResponse("ok", status=200)
        else:
            return HttpResponse("Вы не авторизованы", status=403)

def addcomment(request, RSlug_Title):
    user_id = auth.get_user(request).id
    if user_id and request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_perl = Perl.objects.get(perl_slug=RSlug_Title)
            comment.comments_userid = user_id
            comment.comments_date = datetime.datetime.now()
            form.save()
            return redirect('/%s/' % RSlug_Title)
        else:
            return redirect('/%s/' % RSlug_Title)
    else:
        redirect('/%s/' % RSlug_Title)

def comment_minus(request):
    if request.method == 'POST':
        id = request.POST['id']
        user_id = auth.get_user(request).id
        if user_id and id:
            try:
                PerlCommentsPlusMinus.objects.get(comments_id=id, user_id=user_id)
                return HttpResponse("Вы уже голосовали", status=403)
            except ObjectDoesNotExist:
                try:
                    comments = Comments.objects.get(id=id)
                    comments.comments_minus += 1
                    comments.save()
                    obj = PerlCommentsPlusMinus(comments_id=id, user_id=user_id, golos=-1)
                    obj.save()
                except ObjectDoesNotExist:
                    raise Http404
                return HttpResponse("ok", status=200)
        else:
            return HttpResponse("Вы не авторизованы", status=403)

def comment_plus(request):
    if request.method == 'POST':
        id = request.POST['id']
        user_id = auth.get_user(request).id
        if user_id and id:
            try:
                PerlCommentsPlusMinus.objects.get(comments_id=id, user_id=user_id)
                return HttpResponse("Вы уже голосовали", status=403)
            except ObjectDoesNotExist:
                try:
                    comments = Comments.objects.get(id=id)
                    comments.comments_plus += 1
                    comments.save()
                    obj = PerlCommentsPlusMinus(comments_id=id, user_id=user_id, golos=1)
                    obj.save()
                except ObjectDoesNotExist:
                    raise Http404
                return HttpResponse("ok", status=200)
        else:
            return HttpResponse("Вы не авторизованы", status=403)