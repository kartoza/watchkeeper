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
from django.contrib.auth.decorators import login_required

from event_mapper.forms.movement import MovementUpdateForm
from event_mapper.models.country import Country
from event_mapper.models.movement import Movement


@login_required
def update_movement(request):
    """Update movement."""
    if request.method == 'POST':
        form = MovementUpdateForm(request.POST, user=request.user)
        if form.is_valid():
            movement = form.update()
            country_id = movement.country.id
            success_message = (
                'You have successfully update new movement for %s.' %
                movement.country.name)
            response = get_country_information(country_id)
            response['success_message'] = success_message
            response['success'] = True
            return HttpResponse(json.dumps(
                response,
                ensure_ascii=False),
                content_type='application/javascript')
        else:
            error_message = form.errors
            response = {'error_message': error_message, 'success': False}
            return HttpResponse(json.dumps(
                response,
                ensure_ascii=False),
                content_type='application/javascript')
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
    polygon = country.polygon_geometry.geojson
    polygon_extent = country.polygon_geometry.extent
    try:
        risk_level_id = country.movement.risk_level
        movement_state_id = country.movement.movement_state
        notes = country.movement.notes
        notified_immediately = country.movement.notified_immediately

        risk_level_label = Movement.get_risk_level_label(risk_level_id)
        movement_state_label = Movement.get_movement_state_label(
            movement_state_id)

    except Movement.DoesNotExist:
        risk_level_id = Movement.INSIGNIFICANT_CODE
        movement_state_id = Movement.NORMAL_CODE
        notes = ''

        risk_level_label = Movement.get_risk_level_label(risk_level_id)
        movement_state_label = Movement.get_movement_state_label(
            movement_state_id)
        notified_immediately = False

    response = {
        'country_id': country_id,
        'country_name': country_name,
        'polygon': polygon,
        'risk_level_id': risk_level_id,
        'movement_state_id': movement_state_id,
        'notes': notes,
        'risk_level_label': risk_level_label,
        'movement_state_label': movement_state_label,
        'polygon_extent': polygon_extent,
        'notified_immediately': notified_immediately
    }

    return response


@login_required
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
