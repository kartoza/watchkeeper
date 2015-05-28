# coding=utf-8
"""Select users to be notified."""

__author__ = 'Christian Christelis <christian@kartoza.com>'
__project_name = 'watchkeeper'
__date__ = '27/05/15'
__copyright__ = 'kartoza.com'
__doc__ = ''

from celery import shared_task

from django.core.mail import send_mail

from event_mapper.models.user import User


@shared_task
def notify_priority_users(alert):
    pass