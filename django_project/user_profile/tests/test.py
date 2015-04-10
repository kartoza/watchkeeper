# coding=utf-8
"""Docstring for this file."""
__author__ = 'ismailsunni'
__project_name = 'watchkeeper'
__filename = 'test'
__date__ = '4/10/15'
__copyright__ = 'imajimatika@gmail.com'
__doc__ = ''

from django.test import TestCase
from django.core.exceptions import ValidationError
from model_factories import OfficialFactory
from user_profile.models import Official


class OfficialTestCase(TestCase):
    """Test for Official Class."""
    def setUp(self):
        pass

    def test_create_official(self):
        """Test for Official creation."""
        official = OfficialFactory.create()
        message = 'The official is not instantiated successfully.'
        self.assertIsNotNone(official.department, message)

    # def test_validation(self):
    #     """Test for validation for the phone number."""
    #     official = Official()
    #     official.phone = 'ABCDEFGHIJKL'
    #     with self.assertRaises(ValidationError):
    #         # `full_clean` will raise a ValidationError
    #         #   if any fields fail validation
    #         if official.full_clean():
    #             official.save()
    #
    #     self.assertEqual(
    #         Official.objects.filter(phone='ABCDEFGHIJKL').count(), 0)
    #
    #     official = Official()
    #     official.phone = '+6288888888888'
    #     with self.assertRaises(ValidationError):
    #         # `full_clean` will raise a ValidationError
    #         #   if any fields fail validation
    #         if official.full_clean():
    #             official.save()
    #
    #     self.assertEqual(
    #         Official.objects.filter(phone='+6288888888888').count(), 1)
