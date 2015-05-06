# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'country'
__date__ = '4/20/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from django.contrib.gis.db import models


class Country(models.Model):
    """Class for Country."""

    class Meta:
        """Meta Class"""
        app_label = 'event_mapper'
        verbose_name_plural = "Countries"

    name = models.CharField(
        verbose_name='Country\'s name',
        help_text='The name of the country.',
        max_length=50,
        null=False,
        blank=False
    )

    polygon_geometry = models.PolygonField(srid=4326)

    objects = models.GeoManager()

    def __str__(self):
        return self.name
