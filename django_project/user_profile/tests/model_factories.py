# coding=utf-8
"""Model factories definition for models."""
__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'model_factories'
__date__ = '4/10/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

import factory
from factory import DjangoModelFactory

from user_profile.models import Official, User


class UserFactory(DjangoModelFactory):
    """Factory class for User model."""
    class Meta:
        """Meta definition."""
        model = User

    username = factory.Sequence(lambda n: 'user %s' % n)


class OfficialFactory(DjangoModelFactory):
    """Factory class for Official model."""
    class Meta:
        """Meta definition."""
        model = Official

    user = factory.SubFactory(UserFactory)
    department = factory.sequence(lambda n: 'Department %s' % n)