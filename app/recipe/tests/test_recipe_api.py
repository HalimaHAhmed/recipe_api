"""

tests for recipe api
"""


from decimal import Decimal

from django.contrib.auth import get_user_model


from django.test import TestCase

from django.urls import reverse

from rest_framework import status

from rest_framework.test import APIClient

from core.models import Recipe
from recipe.serializers import RecipeSerializer
RECIPE_URL = reverse('recipe:recipe-list')


def create_recipe(user, **params):
    """

    create and return sample recipe
    """

    defaults = {
        'title': 'sample recipe title',
        'time_minutes': 22,
        'price': Decimal('5.25'),
        'description': 'sample description',
        'link': 'http://example.com/recipe.pdf'


    }

    defaults.update(params)

    recipe = Recipe.objects.create(user=user, **defaults)
    return recipe


class PublicRecipeAPITests(TestCase):
    """

    test unauthenticated api requests
    """

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """
        test auth is required to call api
        """

        res = self.client.get(RECIPE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)
