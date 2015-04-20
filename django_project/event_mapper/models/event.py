# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'event'
__date__ = '4/10/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from django.db import models
from django.contrib.gis.db import models
from event_type import EventType
from perpetrator import Perpetrator
from victim import Victim
from django.contrib.auth.models import User


class Event(models.Model):
    """Event model."""
    slug = models.SlugField(
        unique=True,
        primary_key=True
    )

    name = models.CharField(
        help_text='A name for the event.',
        null=False,
        blank=False,
        unique=True,
        max_length=100
    )

    description = models.TextField(
        help_text='Description for the event.',
        blank=True,
    )

    type = models.ForeignKey(
        EventType,
        help_text='The type of the event.'
    )

    perpetrator = models.ForeignKey(
        Perpetrator,
        help_text='The perpetrator of the event.'
    )

    victim = models.ForeignKey(
        Victim,
        help_text='The victim of the event.'
    )

    date_time = models.DateTimeField(
        verbose_name=u'Date Time (UTC)',
        help_text='Date and time when the event happened.'
    )

    source = models.TextField(
        help_text='The source where the event comes from.',
        blank=True,
    )

    notes = models.TextField(
        help_text='Additional notes for the event',
        blank=True,
        null=True
    )

    reported_by = models.ForeignKey(
        User,
        help_text='The user who reports the event.'
    )

    point_geometry = models.PointField(srid=4326, null=False, blank=False)

