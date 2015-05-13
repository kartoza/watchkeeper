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
            response = get_country_information(country_id)
            response['message'] = success_message
            return HttpResponse(json.dumps(
                response,
                ensure_ascii=False),
                content_type='application/javascript')
        else:
            errors = form.errors
            error_message = errors
            messages.error(request, error_message)
            return HttpResponseRedirect(
                reverse('event_mapper:update_movement'))
    else:
        form = MovementUpdateForm(user=request.user)

    return render_to_response(
        'event_mapper/movement/update_movement_page.html',
        {'form': form},
        context_instance=RequestContext(request)
    )


def get_country_information(country_id):
    country = Country.objects.get(pk=country_id)
    country_name = country.name
    polygon = country.polygon_geometry.coords
    polygon_extent = country.polygon_geometry.extent
    try:
        risk_level_id = country.movement.risk_level
        movement_state_id = country.movement.movement_state
        notes = country.movement.notes

        risk_level_label = Movement.get_risk_level_label(risk_level_id)
        movement_state_label = Movement.get_movement_state_label(
            movement_state_id)

        response = {
            'country_id': country_id,
            'country_name': country_name,
            'polygon': polygon,
            'risk_level_id': risk_level_id,
            'movement_state_id': movement_state_id,
            'notes': notes,
            'risk_level_label': risk_level_label,
            'movement_state_label': movement_state_label,
            'polygon_extent': polygon_extent
        }
    except Movement.DoesNotExist:
        response = {
            'country_id': country_id,
            'country_name': country_name,
            'polygon': polygon,
            'risk_level_id': 1,
            'movement_state_id': '',
            'notes': '',
            'risk_level_label': 'N/A',
            'movement_state_label': 'N/A',
            'message': 'Country does not existed.',
            'polygon_extent': polygon_extent
        }

    return response


def get_country(request):
    if request.method == 'POST':
        country_id = request.POST.get('country_id')
        response = get_country_information(country_id)
        return HttpResponse(json.dumps(
            response,
            ensure_ascii=False),
            content_type='application/javascript')
    else:
        return HttpResponse(
            json.dumps({'Nothing'}),
            content_type="application/json"
        )
