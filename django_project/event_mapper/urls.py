# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'urls'
__date__ = '3/27/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

"""URI Routing configuration for this apps."""
from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'event_mapper.views.index.index'),
    url(r'^accounts/login/$', 'event_mapper.views.user.login'),
    url(r'^accounts/logout/$', 'event_mapper.views.user.logout'),
)
