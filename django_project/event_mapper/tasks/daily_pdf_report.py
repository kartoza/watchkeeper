# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'daily_pdf_report'
__date__ = '8/3/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''


import os
from datetime import datetime, timedelta
from celery import shared_task
from celery.utils.log import get_task_logger
from rst2pdf.createpdf import RstToPdf
from django.conf.global_settings import MEDIA_ROOT
import hashlib

logger = get_task_logger(__name__)

from event_mapper.models.event import Event
from event_mapper.models.movement import Movement

reports_directory = os.path.abspath(os.path.join(
    MEDIA_ROOT,
    os.path.pardir,
    'reports'))


def generate_rst_report(start_time, end_time):
    """Return an rst report for event and movement.

    :param start_time: Starting time.
    :param end_time: End time.

    :returns: RST report.
    :rtype: str
    """
    title = 'IMMAP Daily Report\n'
    report = title + '=' * len(title) + '\n'
    report += 'Period %s - %s\n\n' % (
        start_time.strftime('%H:%M:%S, %A %d %B %Y'),
        end_time.strftime('%H:%M:%S, %A %d %B %Y'))
    event_subtitle = 'Event Report\n'
    report += event_subtitle + '-' * len(event_subtitle) + '\n'
    report += 'List of all report in this period of time:\n\n'
    events = Event.objects.filter(
        date_time__gt=start_time, date_time__lt=end_time)
    if len(events) > 0:
        i = 1
        for event in events:
            event_report = event.long_message()
            event_report = '%s. %s\n' % (i, event_report)
            report += event_report
            i += 1
    else:
        report += 'There is no event in this period.\n'

    report += '\n\n'

    movement_subtitle = 'Movement Update Report\n'
    report += movement_subtitle + '-' * len(movement_subtitle) + '\n'
    report += 'List of all movement update in this period of time:\n\n'
    movements = Movement.objects.filter(
        last_updated_time__gt=start_time,
        last_updated_time__lt=end_time)
    if len(movements) > 0:
        i = 1
        for movement in movements:
            movement_report = movement.report()
            movement_report = '%s. %s\n' % (i, movement_report)
            report += movement_report
            i += 1
    else:
        report += 'There is no movement update in this period.\n'

    return report


def test_report():
    """Test for generate_rst_report."""
    from datetime import datetime, timedelta
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=30)
    rst_report = generate_rst_report(start_time, end_time)
    return rst_report


def generate_report(start_time, end_time):
    """Return an rst report for event and movement.

    :param start_time: Starting time.
    :param end_time: End time.

    """
    rst_report = generate_rst_report(start_time, end_time)
    sha = hashlib.sha1('%s' % datetime.utcnow()).hexdigest()[:6]
    filename = end_time.strftime('IMMAP_Report_%Y%m%d') + sha + '.pdf'
    file_path = os.path.join(reports_directory, filename)
    if not os.path.exists(reports_directory):
        logger.info('Reports directory not exists')
        os.makedirs(reports_directory)
    else:
        logger.info('Reports directory exists')
    pdf = RstToPdf()
    pdf.createPdf(text=rst_report, output=file_path)
    logger.info('Report is created as %s' % filename)


@shared_task(name='tasks.daily_pdf_report')
def daily_pdf_report():
    logger.info('Generate daily pdf report on %s' % datetime.now())
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=1)

    generate_report(start_time, end_time)
