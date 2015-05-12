# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'movement'
__date__ = '5/11/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from event_mapper.forms.movement import MovementUpdateForm


def update_movement(request):
    """Update movement."""
    if request.method == 'POST':
        form = MovementUpdateForm(request.POST, user=request.user)
        if form.is_valid():
            movement = form.save()
            success_message = 'You have successfully added new event.'
            messages.success(request, success_message)
            return HttpResponseRedirect(
                reverse('event_mapper:update_movement'))
        else:
            errors = form.errors
            error_message = errors
            messages.success(request, error_message)
            return HttpResponseRedirect(
                reverse('event_mapper:update_movement'))
    else:
        form = MovementUpdateForm(user=request.user)

    return render_to_response(
        'event_mapper/movement/update_movement_page.html',
        {'form': form},
        context_instance=RequestContext(request)
    )
