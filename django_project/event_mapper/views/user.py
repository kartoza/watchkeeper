# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'user'
__date__ = '4/27/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from django.shortcuts import render_to_response, redirect
from django.template import RequestContext, loader
from django.contrib.auth import (
    login as django_login,
    authenticate,
    logout as django_logout)
from django.contrib.sites.models import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from event_mapper.utilities.decorators import login_forbidden
from event_mapper.forms.user import UserCreationForm
from event_mapper.models.user import User
from django.contrib.messages import get_messages


@login_forbidden
def register(request):
    """Sign Up view."""
    project_name = 'Watchkeeper'
    # MAIL SENDER
    mail_sender = 'noreply@watchkeeper.org'
    if request.method == 'POST':
        form = UserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            form.save_m2m()

            current_site = get_current_site(request)
            domain = current_site.domain
            context = {
                'project_name': project_name,
                'protocol': 'http',
                'domain': domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'full_name': '%s %s' % (user.first_name, user.last_name),
                'key': user.key
            }
            email = loader.render_to_string(
                'event_mapper/user/registration_confirmation_email.html',
                context)
            subject = '%s User Registration' % project_name
            sender = '%s - No Reply <%s>' % (project_name, mail_sender)
            send_mail(
                subject, email, sender, [user.email], fail_silently=False)
            messages.success(
                request,
                ('Thank you for registering in our site! Please check your '
                 'email to confirm your registration'))
            return HttpResponseRedirect(reverse('event_mapper:register'))

    else:
        form = UserCreationForm()
    return render_to_response(
        'event_mapper/user/registration.html',
        {'form': form},
        context_instance=RequestContext(request)
    )


@login_forbidden
def confirm_registration(request, uid, key):
    """The view containing form to reset password and process it.

    :param request: A django request object.
    :type request: request

    :param uid: A unique id for a user.
    :type uid: str

    :param key: Key to confirm the user.
    :type key: str
    """
    decoded_uid = urlsafe_base64_decode(uid)
    try:
        user = User.objects.get(pk=decoded_uid)

        if not user.is_confirmed:
            if user.key == key:
                user.is_confirmed = True
                user.save(update_fields=['is_confirmed'])
                information = (
                    'Congratulations! Your account has been successfully '
                    'confirmed. Please continue to log in.')
            else:
                information = (
                    'Your link is not valid. Please make sure that you use '
                    'confirmation link we sent to your email.')
        else:
            information = ('Your account is already confirmed. Please '
                           'continue to log in.')
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        information = ('Your link is not valid. Please make sure that you use '
                       'confirmation link we sent to your email.')

    context = {
        'page_header_title': 'Registration Confirmation',
        'information': information
    }
    return render_to_response(
        'event_mapper/information.html',
        context,
        context_instance=RequestContext(request)
    )

def login(request):
    """User registration view."""
    email = ''
    error = ''
    if request.method == 'POST':
        next_url = request.POST.get('next')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)
        print user
        if user is not None:
            if user.is_active:
                django_login(request, user)
                return redirect(next_url)
        error = 'invalid email or password'
    elif request.method == 'GET':
        next_url = request.GET.get('next')
    else:
        next_url = '/'

    if not next_url:
        next_url = '/'

    return render_to_response(
        'event_mapper/login_page.html',
        {
            'email': email,
            'next': next_url,
            'error': error
        },
        context_instance=RequestContext(request))


def logout(request):
    """Log out view."""
    django_logout(request)
    return redirect('/')

