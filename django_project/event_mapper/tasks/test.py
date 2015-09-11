# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'test'
__date__ = '9/11/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from random import randint

from django.template.loader import render_to_string


def test_generate_event_text():
    from event_mapper.models.event import Event
    events = Event.objects.all()
    event = events[randint(0, len(events))]
    report_plain = render_to_string(
        'email_templates/event_alert.txt',
        {'event': event})
    return report_plain


def test_generate_event_html():
    from event_mapper.models.event import Event
    events = Event.objects.all()
    event = events[randint(0, len(events))]
    report_html = render_to_string(
        'email_templates/event_alert.html',
        {'event': event})
    return report_html
