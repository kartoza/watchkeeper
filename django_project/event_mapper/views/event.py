# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'event'
__date__ = '5/4/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''


from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext

from event_mapper.forms.event import EventCreationForm


@login_required
def add_event(request):
    """Add event views."""
    if request.method == 'POST':
        form = EventCreationForm(request.POST, user=request.user)
        if form.is_valid():
            event = form.save()
            success_message = 'You have successfully added new event.'
            messages.success(request, success_message)
            return HttpResponseRedirect(reverse('event_mapper:add_event'))
        else:
            errors = form.errors
            error_message = errors
            messages.success(request, error_message)
            return HttpResponseRedirect(reverse('event_mapper:add_event'))
    else:
        form = EventCreationForm(user=request.user)

    return render_to_response(
        'event_mapper/event/add_event_page.html',
        {'form': form},
        context_instance=RequestContext(request)
    )
