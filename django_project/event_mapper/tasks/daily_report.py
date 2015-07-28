# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'daily_report.py'
__date__ = '7/27/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from datetime import datetime
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task(name='tasks.daily_report')
def daily_report():
    logger.info('Send daily report on %s' % datetime.now())
    # Get all events in the last 24 hours.
    # Generate a report
    # Send email to all user
