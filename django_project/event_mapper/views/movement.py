# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'movement'
__date__ = '5/11/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''


from django.shortcuts import render


def movement(request):
    """Landing page."""
    return render(request, 'event_mapper/movement/movement_page.html')
