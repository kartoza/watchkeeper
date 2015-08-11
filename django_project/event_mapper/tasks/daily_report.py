# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'daily_report.py'
__date__ = '7/27/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from datetime import datetime, timedelta
from celery import shared_task
from celery.utils.log import get_task_logger
from notifications.tasks.send_email import send_email_message
from notifications.tasks.send_sms import send_sms_message
from event_mapper.models.event import Event
from event_mapper.models.event import User
from event_mapper.models.movement import Movement

logger = get_task_logger(__name__)


@shared_task(name='tasks.daily_report')
def daily_report():
    logger.info('Send daily report on %s' % datetime.now())
    # Get all events in the last 24 hours.
    # All times are in UTC
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=1)
    events = Event.objects.filter(
        date_time__gt=start_time, date_time__lt=end_time)
    # Generate a report for event
    report = 'Daily Reports\n\n'
    report += 'Event Report\n'
    report += 'List of all events that happened from %s to %s:\n' % (
        start_time.strftime('%H:%M:%S, %A %d %B %Y'),
        end_time.strftime('%H:%M:%S, %A %d %B %Y'))
    if len(events) > 0:
        i = 1
        for event in events:
            event_report = event.long_message()
            event_report = '%s. %s\n' % (i, event_report)
            report += event_report
            i += 1
    else:
        report += 'No event found in these period.\n'

    report += '\n\n'

    # Generate a report for movement
    movements = Movement.objects.filter(
        last_updated_time__gt=start_time,last_updated_time__lt=end_time)
    report += 'Movement Update Report'
    report += 'List of all movement that updated from %s to %s:\n' % (
        start_time.strftime('%H:%M:%S, %A %d %B %Y'),
        end_time.strftime('%H:%M:%S, %A %d %B %Y'))
    if len(movements) > 0:
        i = 1
        for movement in movements:
            movement_report = movement.report()
            movement_report = '%s. %s\n' % (i, movement_report)
            report += movement_report
            i += 1
    else:
        report += 'No movement updated found in these period.\n'

    logger.info(report)

    # Do not send email notification if no events or movement updates
    if len(events) == 0 and len(movements) == 0:
        return

    # Send email to all user
    users = User.objects.all()
    for user in users:
        logger.info('send email to %s' % user.get_full_name())
        send_email_message(user, report)
