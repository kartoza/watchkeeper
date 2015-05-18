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
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, loader
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.gis.geos import Polygon

from event_mapper.models.event import Event
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
            messages.error(request, error_message)
            return HttpResponseRedirect(reverse('event_mapper:add_event'))
    else:
        form = EventCreationForm(user=request.user)

    return render_to_response(
        'event_mapper/event/add_event_page.html',
        {'form': form},
        context_instance=RequestContext(request)
    )


@login_required
def event_dashboard(request):
    """Show dashboard for the events."""
    if request.method == 'GET':
        return render_to_response(
            'event_mapper/event/event_dashboard_page.html',
            context_instance=RequestContext(request)
        )
    elif request.method == 'POST':
        # POST
        pass


@csrf_exempt
def get_events(request):
    """Get events in json format."""
    if request.method == 'POST':
        bbox = json.loads(request.POST.get('bbox'))
        bbox = (bbox['sw_lng'], bbox['sw_lat'], bbox['ne_lng'], bbox['ne_lat'])
        geom = Polygon.from_bbox(bbox)
        events = Event.objects.filter(location__within=geom)

        context = {
            'events': events
        }

        events_json = loader.render_to_string(
            'event_mapper/event/events.json',
            context_instance=RequestContext(request, context))

        return HttpResponse(events_json, content_type='application/json')

