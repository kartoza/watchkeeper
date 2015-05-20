# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'event'
__date__ = '4/10/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from django.contrib.gis.db import models
from event_type import EventType
from perpetrator import Perpetrator
from victim import Victim
from event_mapper.models.user import User


class Event(models.Model):
    """Event model."""

    class Meta:
        """Meta Class"""
        app_label = 'event_mapper'

    INCIDENT_CODE = 1
    ADVISORY_CODE = 2

    CATEGORY_CHOICES = (
        (INCIDENT_CODE, 'Incident'),
        (ADVISORY_CODE, 'Advisory'),
    )

    category = models.IntegerField(
        choices=CATEGORY_CHOICES,
        verbose_name='Category of the event.',
        help_text='There are two event categories: Incident and Advisory'
    )

    location = models.PointField(
        verbose_name='Location',
        help_text='The location of the event in point geometry',
        srid=4326,
        null=False,
        blank=False
    )

    place_name = models.CharField(
        verbose_name='Place Name',
        help_text='The name of the event location.',
        max_length=100
    )

    date_time = models.DateTimeField(
        verbose_name='Date and Time',
        help_text='Date and time when the event happened.'
    )

    type = models.ForeignKey(
        EventType,
        verbose_name='Event Type',
        help_text='The type of the event.'
    )

    perpetrator = models.ForeignKey(
        Perpetrator,
        verbose_name='Perpetrator',
        help_text='The perpetrator of the event.'
    )

    victim = models.ForeignKey(
        Victim,
        verbose_name='Victim',
        help_text='The victim of the event.',
    )

    killed = models.IntegerField(
        verbose_name='Killed People',
        help_text='The number of killed people of the incident.',
        default=0,
        blank=True
    )

    injured = models.IntegerField(
        verbose_name='Injured People',
        help_text='The number of injured people of the incident.',
        default=0,
        blank=True
    )

    detained = models.IntegerField(
        verbose_name='Detained People',
        help_text='The number of detained people of the incident.',
        default=0,
        blank=True
    )

    source = models.TextField(
        verbose_name='Source',
        help_text='The source where the event comes from.',
        blank=True,
    )

    notes = models.TextField(
        verbose_name='Notes',
        help_text='Additional notes for the event.',
        blank=True,
        null=True
    )

    reported_by = models.ForeignKey(
        User,
        verbose_name='Event Reporter',
        help_text='The user who reports the event.'
    )

    notified_immediately = models.BooleanField(
        verbose_name='Notify Immediately',
        help_text='If True, there will be immediate notification.',
        default=False
    )

    notification_sent = models.BooleanField(
        verbose_name='Notification Sent',
        help_text='If True, a notification has been sent for this event.',
        default=False
    )

    objects = models.GeoManager()

    def __str__(self):
        return '%s of %s by %s' % (
            self.get_category_display(), self.type.name, self.perpetrator.name)

    def save(self, *args, **kwargs):
        if self.notified_immediately:
            self.notify_all_interested_users()
        else:
            self.notify_
        super(Event, self).save(*args, **kwargs)