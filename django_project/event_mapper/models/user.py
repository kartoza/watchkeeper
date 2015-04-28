# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'user'
__date__ = '4/20/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.gis.db import models
from event_mapper.models.country import Country
from event_mapper.models.user_manager import CustomUserManager


class User(AbstractBaseUser):
    """User class for event_mapper app."""

    class Meta:
        """Meta Class"""
        app_label = 'event_mapper'

    email = models.EmailField(
        verbose_name='Email',
        help_text='Your email. It will be used as your username also.',
        null=False,
        blank=False,
        unique=True
    )

    first_name = models.CharField(
        verbose_name='First Name',
        help_text='Your first name.',
        max_length=100,
        null=False,
        blank=False
    )

    last_name = models.CharField(
        verbose_name='Last Name',
        help_text='Your first name.',
        max_length=100,
        null=False,
        blank=False
    )

    phone_number = models.CharField(
        verbose_name='Your phone number.',
        help_text='It will be used for sending a notification if you want.',
        max_length=25,
        null=False,
        blank=True
    )

    notified = models.BooleanField(
        verbose_name='Notification status.',
        help_text='Set True to get sms notification.',
        null=False,
        blank=False,
        default=False
    )

    countries_notified = models.ManyToManyField(
        Country,
        verbose_name='Notified countries',
        help_text='The countries that user wants to be notified.',
    )

    is_active = models.BooleanField(
        verbose_name='Active Status',
        help_text='Whether this user is still active or not (a user could be '
                  'banned or deleted).',
        default=True)

    is_admin = models.BooleanField(
        verbose_name='Admin Status',
        help_text='Whether this user is admin or not.',
        default=False)

    area_of_interest = models.PolygonField(
        srid=4326,
        verbose_name='Area of Interest',
        help_text='Area of interest of the user.',
        default=None,
        blank=True,
        null=True
    )

    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
