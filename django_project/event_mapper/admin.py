from django.contrib.gis import admin
from django.contrib.auth.admin import UserAdmin
from event_mapper.forms.user import UserCreationForm, UserChangeForm
from event_mapper.models.user import User
from event_mapper.models.country import Country
from event_mapper.models.event import Event
from event_mapper.models.event_type import EventType
from event_mapper.models.perpetrator import Perpetrator
from event_mapper.models.victim import Victim


class MyUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'phone_number', 'is_admin',
                    'notified')
    list_filter = ('is_admin', 'is_active', 'countries_notified', 'notified')
    fieldsets = (
        ('Credentials', {'fields': ('email', 'password', 'is_active')}),
        ('Personal info', {'fields': (
            'first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_admin',)}),
        ('Notification', {'fields': (
            'countries_notified', 'area_of_interest', 'notified')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        ('Credentials', {'fields': (
            'email', 'password1', 'password2', 'is_active')}),
        ('Personal info', {'fields': (
            'first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_admin',)}),
        ('Notification', {'fields': (
            'countries_notified', 'area_of_interest', 'notified')}),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


class CountryAdmin(admin.GeoModelAdmin):
    pass


class EventAdmin(admin.ModelAdmin):
    list_display = (
        'category', 'place_name', 'date_time', 'type', 'perpetrator',
        'victim', 'notified_immediately', 'notification_sent', 'reported_by')
    list_filter = (
        'category', 'type', 'perpetrator', 'victim', 'notified_immediately',
        'notification_sent', 'reported_by',)
    ordering = ('date_time',)
    search_fields = ('reported_by',)


class EventTypeAdmin(admin.ModelAdmin):
    pass


class PerpetratorAdmin(admin.ModelAdmin):
    pass


class VictimAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, MyUserAdmin)
admin.site.register(Country, CountryAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(EventType, EventTypeAdmin)
admin.site.register(Perpetrator, PerpetratorAdmin)
admin.site.register(Victim, VictimAdmin)
