# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'victim'
__date__ = '4/10/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

import os
from django.db import models
from django.conf.global_settings import MEDIA_ROOT
from django.utils.text import slugify

icon_directory = 'victim_icon'


class Victim(models.Model):
    """Victim model."""

    slug = models.SlugField(
        unique=True,
        primary_key=True
    )

    name = models.CharField(
        help_text='A name for the victim.',
        null=False,
        blank=False,
        unique=True,
        max_length=100
    )

    description = models.TextField(
        help_text='Description for the victim.',
        blank=True,
    )

    icon = models.ImageField(
        help_text='The icon for the victim.',
        upload_to=os.path.join(MEDIA_ROOT, icon_directory),
        blank=True
    )

    def save(self, *args, **kwargs):
        """Overloaded save method."""
        if not self.slug:
            self.slug = slugify(unicode(self.name))

        super(Victim, self).save(*args, **kwargs)