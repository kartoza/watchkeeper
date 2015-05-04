# coding=utf-8
"""Docstring for this file."""
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.crypto import get_random_string
from event_mapper.models.user import User
from event_mapper.models.country import Country
from event_mapper.utilities.commons import get_verbose_name

__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'user'
__date__ = '4/28/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number',
                  'notified', 'countries_notified')

    email = forms.EmailField(
        label=get_verbose_name(User, 'email'),
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'john@doe.com'})
        )

    first_name = forms.CharField(
        label=get_verbose_name(User, 'first_name'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'John'})
    )

    last_name = forms.CharField(
        label=get_verbose_name(User, 'last_name'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Doe'})
    )

    phone_number = forms.CharField(
        label=get_verbose_name(User, 'phone_number'),
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': '+6281234567890'})
    )

    notified = forms.BooleanField(
        label=get_verbose_name(User, 'notified'),
        widget=forms.CheckboxInput(
            attrs={'class': 'form-control'})
    )

    countries_notified = forms.ModelMultipleChoiceField(
        label=get_verbose_name(User, 'countries_notified'),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        queryset=Country.objects,
    )

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your s3cr3T password'})
    )

    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your s3cr3T password'})
    )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.key = get_random_string()
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name',
                  'phone_number', 'notified', 'countries_notified',
                  'is_active', 'is_admin')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class LoginForm(forms.Form):
    """Form for user to log in."""
    class Meta:
        """Meta of the form."""
        fields = ['email', 'password']

    email = forms.EmailField(
        label=get_verbose_name(User, 'email'),
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'john@doe.com'})
    )
    password = forms.CharField(
        label=get_verbose_name(User, 'password'),
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Your s3cr3T password'})
    )

