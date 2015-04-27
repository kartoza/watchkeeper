# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'user'
__date__ = '4/27/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib.auth import (
    login as django_login,
    authenticate,
    logout as django_logout)


def login(request):
    """User registration view."""
    username = ''
    error = ''
    if request.method == 'POST':
        next_url = request.POST.get('next')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        print user
        if user is not None:
            if user.is_active:
                django_login(request, user)
                return redirect(next_url)
        error = 'invalid username or password'
    elif request.method == 'GET':
        next_url = request.GET.get('next')
    else:
        next_url = '/'

    if not next_url:
        next_url = '/'

    return render_to_response(
        'event_mapper/login_page.html',
        {
            'username': username,
            'next': next_url,
            'error': error
        },
        context_instance=RequestContext(request))


def logout(request):
    """Log out view."""
    django_logout(request)
    return redirect('/')


def sign_up(request):
    """Sign Up view."""
    return render_to_response(
        'event_mapper/sign_up_page.html',
        {
        },
        context_instance=RequestContext(request))

