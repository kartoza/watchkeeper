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
    url(r'^$', 'event_mapper.views.index.index', name='index'),

    # User related urls
    url(r'^login$', 'event_mapper.views.user.login', name='login'),
    url(r'^logout$', 'event_mapper.views.user.logout', name='logout'),
    url(r'^register$', 'event_mapper.views.user.register',
        name='register'),
    url(r'^account-confirmation/(?P<uid>[0-9A-Za-z_\-]+)/(?P<key>.+)/$',
        'event_mapper.views.user.confirm_registration',
        name='confirm_registration'),

    # Event related urls
    url(r'^add_alert', 'event_mapper.views.event.add_event', name='add_event'),
)
