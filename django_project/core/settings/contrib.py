# -*- coding: utf-8 -*-
from .base import *  # noqa

# Extra installed apps
INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',  # enable Raven plugin
    'rest_framework',
    'pipeline'
)


MIDDLEWARE_CLASSES += (
    'django.middleware.gzip.GZipMiddleware',
)
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.media',
)

LEAFLET_CONFIG = {
    'TILES': [
        (
            'OpenStreetMap',
            'http://{s}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png',
            ('© <a href="http://www.openstreetmap.org" '
             'target="_parent">OpenStreetMap</a> and contributors, under an '
             '<a href="http://www.openstreetmap.org/copyright" '
             'target="_parent">open license</a>')
        )]

}

# enable cached storage - requires uglify.js (node.js)
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

PIPELINE_JS = {
    'contrib': {
        'source_filenames': (
            'js/jquery-1.11.1.min.js',
            'js/bootstrap.js',
            'js/moment.min.js',
            'js/bootstrap-datetimepicker.min.js',
            'event_mapper/js/leaflet.js',
            'event_mapper/js/material.min.js',
            'event_mapper/js/ripples.min.js',
            'event_mapper/js/validate.js',
            'event_mapper/js/jquery.flot.min.js',
            'event_mapper/js/jquery.flot.time.min.js',
            'event_mapper/js/event_mapper.js',
        ),
        'output_filename': 'js/contrib.js',
    },
    'appjs': {
        'source_filenames': (
            'js/csrf-ajax.js',
            'event_mapper/css/leaflet.css',
            'event_mapper/css/material-wfont.min.css',
            'event_mapper/css/ripples.min.css',
            'event_mapper/css/bnpb-theme.css',
            'css/bootstrap-datetimepicker.min.css',
        ),
        'output_filename': 'js/appjs.js'
    }
}

PIPELINE_CSS = {
    'contrib': {
        'source_filenames': (
            'css/bootstrap.min.css',
            'css/bootstrap-datetimepicker.min.css',
        ),
        'output_filename': 'css/contrib.css',
        'extra_context': {
            'media': 'screen, projection',
        },
    }
}
