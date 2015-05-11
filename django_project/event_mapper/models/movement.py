# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'movement'
__date__ = '5/11/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from django.contrib.gis.db import models

from event_mapper.models.user import User
from event_mapper.models.rating import Rating


class Movement(models.Model):
    """Movement model."""

    class Meta:
        """Meta class."""
        app_label = 'event_mapper'

    name = models.CharField(
        verbose_name='Movement Name',
        help_text='The name of the movement.',
        max_length=100
    )

    region = models.PolygonField(
        verbose_name='Region',
        help_text='The location of the event in polygon geometry',
        srid=4326,
        null=False,
        blank=False
    )

    rating = models.ForeignKey(
        Rating,
        verbose_name='Rating',
        help_text='The rating of the movement.'
    )

    notes = models.TextField(
        verbose_name='Notes',
        help_text='Notes for the movement.',
        blank=True,
        null=True
    )

    notified_immediately = models.BooleanField(
        verbose_name='Notified Immediately',
        help_text='If True, there will be immediate notification.',
        default=False
    )

    notification_sent = models.BooleanField(
        verbose_name='Notification Sent',
        help_text='If True, a notification has been sent for this event.',
        default=False
    )

    last_updater = models.ForeignKey(
        User,
        verbose_name='Last Updater',
        help_text='The last user who update the movement.'
    )

    objects = models.GeoManager()

    def __str__(self):
        return self.name