"""
Test for models
"""

from decimal import Decimal

from core import models

from django.test import TestCase
from django.contrib.auth import get_user_model



class ModelTest(TestCase):
    """Tes Mdels."""

    def test_create_user_with_eamil_succefully(self):
        """Test Creatting a user with an email is succefully"""
        email = 'test@example.com'
        password = 'testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        # check if the cretad user & email are equal
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test Email is normalized for the new user"""
        sample_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM','test4@example.com']
        ]

        for email,expected in sample_emails:
            user = get_user_model().objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raises_error(self):
        """Test That createting user without email raises a valueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('','sample123')

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123',
        )

        # is_super user provided by permision mixin
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)



    def test_create_recipe(self):

        """
        testing creating a recipe is succcesfully
        """

        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123',
        )

        recipe = models.Recipe.objects.create(
            user = user,
            title='sample recipe name',
            time_minutes = 5,
            price = Decimal('5.50'),
            description = 'sample recipe'
        )


        self.assertEqual(str(recipe),recipe.title)