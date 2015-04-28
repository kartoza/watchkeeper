from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from event_mapper.forms.user import UserCreationForm, UserChangeForm
from event_mapper.models.user import User


class MyUserAdmin(UserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'first_name', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'is_active')}),
        ('Personal info', {'fields': (
            'first_name', 'last_name', 'phone_number')}),
        ('Permissions', {'fields': ('is_admin',)}),
        ('Notification', {'fields': (
            'countries_notified', 'area_of_interest', 'notified')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'first_name', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(User, MyUserAdmin)