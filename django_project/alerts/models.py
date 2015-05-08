# coding=utf-8
"""Alerts Model."""

__author__ = 'Christian Christelis <christian@kartoza.com>'
__project_name = 'watchkeeper'
__date__ = '7/05/15'
__copyright__ = 'kartoza.com'
__doc__ = ''


from django.contrib.gis.db import models

from event_mapper.models.user import User


class Alert(models.Model):
    """Class for Country."""
    date = models.DateTimeField(auto_now_add=True, blank=True)
    alert_type = models.CharField(
        choices=(('sms', 'sms'), ('email', 'email')),
        max_length=50,
        null=False,
        blank=False)
    recipient = models.ForeignKey(User)
    message_content = models.TextField()

    class Meta:
        app_label = 'alerts'

    def __unicode__(self):
        return u'%s %s' % (self.alert_type, self.recipient)

    def __str__(self):
        return str(self.__unicode__())
