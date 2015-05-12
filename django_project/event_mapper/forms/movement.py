# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'movement'
__date__ = '5/11/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from django.forms import models
from django import forms

from event_mapper.utilities.commons import get_verbose_name, get_help_text

from event_mapper.models.movement import Movement
from event_mapper.models.country import Country


class MovementUpdateForm(models.ModelForm):
    """A form for rating a movement."""
    class Meta:
        model = Movement
        fields = (
            'region', 'risk_level', 'movement_state', 'notes',
            'notified_immediately'
        )

    region = forms.ModelChoiceField(
        label='Region',
        queryset=Country.objects.order_by('name'),
        widget=forms.Select(
            attrs={
                'class': 'form-control'
            }
        )
    )

    risk_level = forms.ChoiceField(
        label=get_verbose_name(Movement, 'risk_level'),
        widget=forms.Select(
            attrs={'class': 'form-control'}),
        choices=Movement.RISK_LEVELS,
    )

    movement_state = forms.ChoiceField(
        label=get_verbose_name(Movement, 'movement_state'),
        widget=forms.Select(
            attrs={'class': 'form-control'}),
        choices=Movement.MOVEMENT_STATES,
    )

    notified_immediately = forms.BooleanField(
        label=get_verbose_name(Movement, 'notified_immediately'),
        help_text=get_help_text(Movement, 'notified_immediately'),
        widget=forms.CheckboxInput(
            attrs={'class': 'form-control'}),
        required=False
    )

    notes = forms.CharField(
        label=get_verbose_name(Movement, 'notes'),
        widget=forms.Textarea(
            attrs={'class': 'form-control',
                   'placeholder': get_help_text(Movement, 'notes')}),
        required=False,
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(MovementUpdateForm, self).__init__(*args, **kwargs)