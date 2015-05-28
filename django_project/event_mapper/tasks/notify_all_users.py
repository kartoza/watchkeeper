# coding=utf-8
"""Select users to be notified."""

__author__ = 'Christian Christelis <christian@kartoza.com>'
__project_name = 'watchkeeper'
__date__ = '27/05/15'
__copyright__ = 'kartoza.com'
__doc__ = ''

from celery import shared_task

from django.core.mail import send_mail
from notifications.tasks.send_email import send_email_message
from notifications.tasks.send_sms import send_sms_message

from event_mapper.models.user import User


@shared_task
def notify_all_users(event):
    users = User.objects.filter(
        countries_notified__polygon_geometry__contains=event.location)
    message = event.long_message()
    for user in users:
        send_email_message(user, message)
