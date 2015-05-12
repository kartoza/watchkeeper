# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'movement'
__date__ = '5/11/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

import json

from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext
from event_mapper.forms.movement import MovementUpdateForm

from event_mapper.models.country import Country
from event_mapper.models.movement import Movement


def update_movement(request):
    """Update movement."""
    if request.method == 'POST':
        form = MovementUpdateForm(request.POST, user=request.user)
        if form.is_valid():
            movement = form.update()
            country_id = movement.country.id
            success_message = 'You have successfully update new movement.'
            messages.success(request, success_message)
            return HttpResponse()
            # return HttpResponseRedirect(
            #     reverse('event_mapper:update_movement'))
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


def get_country(request):
    if request.method == 'POST':
        country_id = request.POST.get('country_id')
        country = Country.objects.get(pk=country_id)
        polygon = country.polygon_geometry
        try:
            risk_level = country.movement.risk_level
            movement_state = country.movement.movement_state
            notes = country.movement.notes

            response = {
                'risk_level': risk_level,
                'movement_state': movement_state,
                # 'polygon': polygon,
                'notes': notes
            }
        except Movement.DoesNotExist:
            response = {
                'risk_level': 1,
                'movement_state': 1,
                # 'polygon': polygon,
                'notes': ''
            }

        return HttpResponse(json.dumps(
            response,
            ensure_ascii=False),
            content_type='application/javascript')
    else:
        return HttpResponse(
            json.dumps({'Nothing'}),
            content_type="application/json"
        )