# coding=utf-8
"""Select users to be notified."""

__author__ = 'Christian Christelis <christian@kartoza.com>'
__project_name = 'watchkeeper'
__date__ = '27/05/15'
__copyright__ = 'kartoza.com'
__doc__ = ''

from celery import shared_task

from django.template.loader import render_to_string

from notifications.tasks.send_email import send_email_message
from notifications.tasks.send_sms import send_sms_message

from event_mapper.models.user import User
from event_mapper.models.event import Event


@shared_task
def notify_all_users(event_id):
    event = Event.objects.get(id=event_id)
    users = User.objects.filter(
        countries_notified__polygon_geometry__contains=event.location)
    text_message = render_to_string(
        'email_templates/event_alert.txt',
        {'event': event, 'category': event.get_category_display()})
    html_message = render_to_string(
        'email_templates/event_alert.html',
        {'event': event, 'category': event.get_category_display()})
    for user in users:
        send_email_message(user, text_message, html_message)
