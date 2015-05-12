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
    url(r'^profile$', 'event_mapper.views.user.profile', name='profile'),
    url(r'^change_password', 'event_mapper.views.user.change_password',
        name='change_password'),

    # Event related urls
    url(r'^add_alert', 'event_mapper.views.event.add_event', name='add_event'),

    # Movement related urls
    url(r'^update_movement', 'event_mapper.views.movement.update_movement',
        name='update_movement'),
    url(r'^get_country', 'event_mapper.views.movement.get_country',
        name='get_country'),

    # Static page urls
    url(r'^contact', 'event_mapper.views.front_end.contact', name='contact'),
)
